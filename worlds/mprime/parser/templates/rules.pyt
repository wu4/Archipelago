from BaseClasses import MultiWorld, CollectionState
from typing import Callable

ConnectionDict = tuple[str, Callable[[CollectionState], bool]]
NodePair = tuple[str, tuple[ConnectionDict, ...]]

def add_exits_to_world(world: MultiWorld, player: int, regions: tuple[NodePair, ...]):
    for region_name, exits in regions:
        region = world.get_region(region_name, player)
        for connecting_region_name, rule in exits:
            region.connect(world.get_region(connecting_region_name, player), None, rule)

def set_rules(multiworld: MultiWorld, player: int):
    templates = {
    {%- for template_name, requirements in templates.items() %}
        "{{template_name}}": {{requirements}},
    {%- endfor %}
    }
    dock_requirements = {
    {%- for dock_type, requirements in dock_requirements.items() %}
    {%- if requirements is not none %}
        "{{dock_type}}": {{requirements}},
    {%- endif %}
    {%- endfor %}
    }
    add_exits_to_world(multiworld, player, (
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