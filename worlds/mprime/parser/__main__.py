from __future__ import annotations
from jinja2 import Environment as J2Environment, FileSystemLoader as J2FSLoader

from .parser_utils import trick_name_gen, relative_to_file, absolute_location_tuple_format
from .json_parsing import RandovaniaData
from ..logic import generation_exports as logic_exports

import re
link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\\n")

if __name__ == "__main__":
    data = RandovaniaData(relative_to_file(__file__, "data/randovania_data/json_data/header.json"))

    methods={
        "tuplefmt": absolute_location_tuple_format,
        "trick_name_gen": trick_name_gen,
        "parse_trick_desc": parse_trick_desc,

        "logic_imports": "from ..logic import " + ",".join((f"{func.__name__} as {shortname}" for shortname, func in logic_exports.items())),
    }

    env = J2Environment(loader=J2FSLoader(relative_to_file(__file__, "templates")))

    templates = ["options","regions","rules"]
    for template_name in templates:
        template = env.get_template(f"{template_name}.pyt")
        rendered = template.render(data=data, methods=methods)
        with open(relative_to_file(__file__, f"../generated/{template_name}.py"), "w") as f:
            f.write(rendered)

    builder: list[str] = []
    builder.append(f"damage_resistances={data.damage_resistances}")
    builder.append(f"items={data.items}")
    builder.append(f"locations={[absolute_location_tuple_format(node_from) for node_from in data.rules.keys() if data.node_info[node_from].pickup]}")
    builder.append("from . import " + ",".join(templates))
    with open(relative_to_file(__file__, "../generated/__init__.py"), "w") as f:
        f.write("\n".join(builder))
