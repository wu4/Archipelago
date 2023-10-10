from BaseClasses import MultiWorld, CollectionState
from worlds.AutoWorld import World
from typing import Callable, Optional, cast

ConnectionRule = Callable[[CollectionState], bool]
ConnectionTuple = tuple[str, Optional[ConnectionRule]]
RegionRules = tuple[str, tuple[ConnectionTuple, ...]]

def add_exits_to_world(world: MultiWorld, player: int, regions: tuple[RegionRules, ...]):
    for region_name, exits in regions:
        region = world.get_region(region_name, player)
        for connecting_region_name, rule in exits:
            region.connect(world.get_region(connecting_region_name, player), None, rule)

def set_rules(self: World):
    from ..options import MetroidPrimeOptions
    {{methods["logic_imports"]}}
    p = self.player
    o = cast(MetroidPrimeOptions, self.options)

    t: dict[str, ConnectionRule] = {
    {%- for template_name, requirements in data.templates.items() %}
        "{{template_name}}": {{requirements}},
    {%- endfor %}
    }

    add_exits_to_world(self.multiworld, p, (
    {%- for node_from, nodes in data.rules.items() -%}
        ("{{methods["tuplefmt"](node_from)}}", (
            {%- for node_to, rule in nodes.items() -%}
                ("{{methods["tuplefmt"](node_to)}}", {{rule}}),
            {%- endfor -%})
        ),
    {%- endfor -%}
    ))