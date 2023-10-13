if __name__ == "__main__":
    import jinja2

    from .parser_utils import relative_to_file
    from .tricks import trick_name_gen, parse_trick_desc
    from .location import location_tuple_format
    from .json_parsing import RandovaniaData
    from ..logic import generation_exports as logic_generation_exports

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
                location_tuple_format(k): {
                    location_tuple_format(kk): vv
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
                location_tuple_format(node_from): info
                for node_from, info in data.node_info.items()
            }.items()
        }
    }

    env = jinja2.Environment(
        loader=jinja2.FileSystemLoader(
            relative_to_file(__file__, "templates")
        )
    )

    template_names = ["options", "regions", "rules"]
    for template_name in template_names:
        template = env.get_template(f"{template_name}.jinja2")
        rendered = template.render(**template_metadata[template_name])
        with open(relative_to_file(__file__, f"../generated/{template_name}.py"), "w") as f:
            f.write(rendered)

    builder: list[str] = [
        f"damage_resistances={data.damage_resistances}",
        f"items={data.items}",
        f"""locations={[
            location_tuple_format(node_from)
            for node_from in data.rules.keys()
            if data.node_info[node_from].pickup
        ]}""",
        "from . import " + ",".join(template_names),
    ]
    with open(relative_to_file(__file__, "../generated/__init__.py"), "w") as f:
        f.write("\n".join(builder))
