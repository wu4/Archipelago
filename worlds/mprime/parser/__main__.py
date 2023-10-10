from __future__ import annotations

from .util import trick_name_gen, relative_to_file
from typing import TYPE_CHECKING

from ..logic import generation_exports as logic_exports


if TYPE_CHECKING:
    import worlds.mprime.parser.Types as DataTypes

VALIDATE: bool = False

import re
link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\n")

from jinja2 import Environment as J2Environment, FileSystemLoader as J2FSLoader
from .connection_requirements import parse_connection_requirements
from .json_parsing import NodeInfo, RandovaniaData
from .util import absolute_location_tuple_format

def generate():
    data = RandovaniaData(relative_to_file(__file__, "data/randovania_data/json_data/header.json"))

    env = J2Environment(loader=J2FSLoader(relative_to_file(__file__, "templates")))
    options_template = env.get_template("options.pyt")
    regions_template = env.get_template("regions.pyt")
    rules_template = env.get_template("rules.pyt")

    funcdefs = []
    for shortname, func in logic_exports.items():
        import inspect
        (spec, _, _, _, _, _, annos) = inspect.getfullargspec(func)
        
        func_args = ','.join(f"{x}:{annos[x].__name__}" for x in spec[2:])
        args_as_consts = ','.join(f"Constant({x})" for x in spec[2:])

        funcdefs.append(f"def {shortname}({func_args}): return Call(Attribute(Name('logic',Load()),'{func.__name__}',Load()),[Name('state',Load()),Constant(player),{args_as_consts}],[])")

    builder: list[str] = []
    builder.append("# pyright: reportGeneralTypeIssues=false")
    builder.append(f"damage_resistances={data.damage_resistances}")
    builder.append(f"items={data.items}")
    builder.append(options_template.render(tricks=data.header["resource_database"]["tricks"].items(), trick_name_gen=trick_name_gen, parse_trick_desc=parse_trick_desc))
    builder.append(regions_template.render(tuplefmt=absolute_location_tuple_format, data=data))
    builder.append(rules_template.render(tuplefmt=absolute_location_tuple_format, data=data))
    with open(relative_to_file(__file__, "../generated.py"), "w") as f:
        f.write("\n".join(builder))

generate()