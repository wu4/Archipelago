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

    {{ast_imports}}
    
    t: ConnectionDict
    {%- for line in template_lines %}
    {{line}}
    {%- endfor %}

    dock_requirements: ConnectionDict = {
    {%- for dock_type, requirements in dock_requirements.items() %}
    {%- if requirements is not none %}
        "{{dock_type}}": {{requirements}},
    {%- endif %}
    {%- endfor %}
    }

    from ast import Expression
    {{e_def}}
    add_exits_to_world(multiworld, p, (
    {%- for node_from, node_rules in rules %}
        {%- if node_rules.has_location != "items_every_room" %}
            (
            "{{node_from}}", (
            {%- for node_to, rule in node_rules.connections %}
                ("{{node_to}}", {{rule}}),
            {%- endfor %}
            {%- if node_rules.dock_connection is not none %}
                ("{{node_rules.dock_connection[0]}}", {{node_rules.dock_connection[1]}}),
            {%- endif %}
            )
            ),
        {%- endif %}
    {%- endfor %}
    ))
    print("rules end!")