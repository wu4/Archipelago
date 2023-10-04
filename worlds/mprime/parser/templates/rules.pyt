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
    multiworld = self.multiworld
    player = self.player
    options = self.options
    from . import logic

    # from ast import BoolOp as BO, And as A, Constant as Co, Or as O, Name as N, Load as Lo, Attribute as At, Call as C, Subscript as S, Expression as E, arguments as ags, arg as a, Lambda as L
    from ast import And, Or, Not, Load
    from typing import Any
    {%- for name in ["BoolOp", "UnaryOp", "Constant", "Name", "Attribute", "Call", "Subscript", "Expression", "arg", "Lambda", "Compare", "GtE"] %}
    from ast import {{name}} as {{name}}_
    def {{name}}(*args, **kwargs): return {{name}}_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    {%- endfor %}
    from ast import arguments as arguments_
    def arguments(*args, **kwargs): return arguments_(*args, **kwargs, kwonlyargs=[], kw_defaults=[], defaults=[])
        
    def e(b):
        import astvalidate
        # import ast
        # print(ast.dump(b, False))
        token = Expression(Lambda(arguments([], [arg('state')]), b), )
        # astvalidate.validate(token)
        nonlocal options
        nonlocal player
        nonlocal templates
        nonlocal logic
        # print(locals())
        return eval(compile(token, '<generated>', 'eval'), locals())

    templates: ConnectionDict = {
    {%- for template_name, requirements in templates.items() %}
        "{{template_name}}": {{requirements}},
    {%- endfor %}
    }
    dock_requirements: ConnectionDict = {
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