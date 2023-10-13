from __future__ import annotations
from jinja2 import Environment as J2Environment, FileSystemLoader as J2FSLoader

from .parser_utils import LocationTuple, trick_name_gen, relative_to_file, absolute_location_tuple_format
from .json_parsing import RandovaniaData
from ..logic import generation_exports as logic_generation_exports

import re
link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\\n")

from typing import TypeVar
V = TypeVar("V")
def as_str_dict(d: dict[LocationTuple, V]) -> dict[str, V]:
    return {
        absolute_location_tuple_format(k): v
        for k, v in d.items()
    }

if __name__ == "__main__":
    data = RandovaniaData(relative_to_file(__file__, "randovania_data/json_data/header.json"))

    tricks=data.header["resource_database"]["tricks"].items()

    template_metadata={
        "options": {
            "tricks": tricks,
            "trick_descs": {
                trick_name: parse_trick_desc(trick_data["description"])
                for trick_name, trick_data in tricks
            },
            "underscored_trick_names": {
                trick_name: trick_name_gen(trick_data["long_name"])
                for trick_name, trick_data in tricks
            }
        },
        "rules": {
            "rules": {
                absolute_location_tuple_format(k): {
                    absolute_location_tuple_format(kk): vv
                    for kk, vv in v.items()
                } for k, v in data.rules.items()
            }.items(),
            "templates": data.templates.items(),
            "logic_imports": (
                "from ..logic import " +
                ",".join((
                    f"{func.__name__} as {shortname}"
                    for shortname, func in logic_generation_exports.items()
                ))
            )
        },
        "regions": {
            "node_infos": {
                absolute_location_tuple_format(node_from): info
                for node_from, info in data.node_info.items()
            }.items()
        }
    }

    env = J2Environment(loader=J2FSLoader(relative_to_file(__file__, "templates")))

    templates = ["options","regions","rules"]
    for template_name in templates:
        template = env.get_template(f"{template_name}.pyt")
        rendered = template.render(**template_metadata[template_name])
        with open(relative_to_file(__file__, f"../generated/{template_name}.py"), "w") as f:
            f.write(rendered)

    builder: list[str] = []
    builder.append(f"damage_resistances={data.damage_resistances}")
    builder.append(f"items={data.items}")
    builder.append(f"locations={[absolute_location_tuple_format(node_from) for node_from in data.rules.keys() if data.node_info[node_from].pickup]}")
    builder.append("from . import " + ",".join(templates))
    with open(relative_to_file(__file__, "../generated/__init__.py"), "w") as f:
        f.write("\n".join(builder))
