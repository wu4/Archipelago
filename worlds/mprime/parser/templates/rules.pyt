from BaseClasses import MultiWorld, CollectionState
from worlds.AutoWorld import World
from typing import Callable

ConnectionRule = Callable[[CollectionState], bool]

ConnectionTuple = tuple[str, ConnectionRule]
RegionRules = tuple[str, tuple[ConnectionTuple, ...]]

def add_exits_to_world(world: MultiWorld, player: int, regions: tuple[RegionRules, ...]):
    for region_name, exits in regions:
        region = world.get_region(region_name, player)
        for connecting_region_name, rule in exits:
            region.connect(world.get_region(connecting_region_name, player), None, rule)

ConnectionDict = dict[str, ConnectionRule]

def set_rules(self: World):
    print("rules start!")
    multiworld = self.multiworld
    p = self.player
    o = self.options
    from . import logic as l

    t: ConnectionDict = {
    {%- for template_name, requirements in data.templates.items() %}
        "{{template_name}}": {{requirements}},
    {%- endfor %}
    }

    add_exits_to_world(multiworld, p, (
    {%- for node_from, nodes in data.rules.items() -%}
        (
        "{{tuplefmt(node_from)}}", (
        {%- for node_to, rule in nodes.items() -%}
            ("{{tuplefmt(node_to)}}", {{rule}}),
        {%- endfor -%}
        )
        ),
    {%- endfor -%}
    ))
    print("rules end!")