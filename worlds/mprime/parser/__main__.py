from __future__ import annotations

import json
from typing import cast, Callable, TYPE_CHECKING, TypeVar
from inflection import underscore

import Types as DataTypes
if TYPE_CHECKING:
    import worlds.mprime.parser.Types as DataTypes

def absolute_location_format(location: DataTypes.AbsoluteLocation) -> str:
    return absolute_node_format(location["node"], location["area"], location["region"])

def absolute_node_format(node_name: str, area_name: str, region_name: str) -> str:
    return f"{node_name} ({area_name}, {region_name})"

def intersperse(val, sequence):
    first = True
    for item in sequence:
        if not first:
            yield val
        yield item
        first = False

V = TypeVar("V")
V2 = TypeVar("V2")

def map_dict(func: Callable[[V], V2], dictionary: dict[str, V]) -> dict[str, V2]:
    return dict((k, func(v)) for (k, v) in dictionary.items())

HEADER_FILENAME: str = "data/randovania_data/json_data/header.json"

VALIDATE: bool = False

def relative_to_script(script_path: str, rel_path: str) -> str:
    import os.path
    return os.path.join(os.path.dirname(os.path.abspath(script_path)), rel_path)

def _get_header() -> DataTypes.Header:
    with open(relative_to_script(__file__, HEADER_FILENAME), "r") as f:
        return json.load(f)

header = _get_header()

def trick_name_gen(trick_name: str):
    trick_name = underscore(f"{trick_name.replace(' ', '')}")
    if trick_name == "combat/scan_dash":
        return "scan_dash"
    elif trick_name == "spinnerswithout_boost":
        return "spinners_without_boost"
    elif trick_name == "single_room_outof_bounds":
        return "single_room_oob"
    else:
        return trick_name

items_short_to_long: dict[str, str] = {
    short_name: item["long_name"]
    for short_name, item in header["resource_database"]["items"].items()
    if not short_name in ["LockedPB", "LockedMissile", "Unknown1", "Unknown2", "HealthRefill"]
}

items: list[str] = list(items_short_to_long.values())

events_short_to_long: dict[str, str] = {
  short_name: event["long_name"]
  for short_name, event in header["resource_database"]["events"].items()
}
            
tricks_short_to_long = {
    short: trick["long_name"]
    for short, trick in header["resource_database"]["tricks"].items()
}


class ConnectionRequirement:
    parent: Optional[ConnectionRequirement]
    static_requirements: Optional[ConnectionRequirement]
    tainted_with_statics: bool
    requirement_data: DataTypes.RequirementData

    def __init__(self, req: DataTypes.RequirementData, parent: Optional[ConnectionRequirement] = None):
        self.parent = parent
        self.tainted_with_statics = False
        self.static_requirements = None
        self.requirement_data = req

class TemplateRequirement(ConnectionRequirement):
    requirement_data: DataTypes.Template

    def __init__(self, req: DataTypes.Template):
        super().__init__(req)
        
    def __str__(self) -> str:
        return f"templates['{self.requirement_data['data']}'](state)"

def logic_as_str(logics: Iterable[str], is_and: bool) -> str:
    return '(' + ' '.join(intersperse(
        'and' if is_and else 'or',
        map(str, logics)
    )) + ')'

ExtractedRequirements = tuple[list[ConnectionRequirement], list["AndOrRequirement"], list[ConnectionRequirement]]

class AndOrRequirement(ConnectionRequirement):
    requirement_data: DataTypes.Logic

    is_and: bool
    children: list[ConnectionRequirement]
    tainted_children: list[ConnectionRequirement]
    
    def __init__(self, req: DataTypes.Logic):
        super().__init__(req)

        self.is_and = req["type"] == "and"
        self.children = list(map(create_connection_requirement, req["data"]["items"]))

        self.tainted_children = list(filter(lambda x: x.tainted_with_statics, self.children))

        self.tainted_with_statics = len(self.tainted_children) > 0

    def __str__(self) -> str:
        return logic_as_str(map(str, self.children), self.is_and)
        # if self.tainted_with_statics:
        #     raise ValueError(f"trying to stringify an and/or that is not fully dynamic: {self.requirement_data}")

    # # AND
    # if (REQUIREMENTS):
    #     def NESTED_DATA
    #     
    #     # if more statics
    #     if (NESTED_REQUIREMENTS):
    #         ...
    #     else:
    #         ...
    #     # otherwise
    #     return NESTED_DATA
    # else:
    #     return upper_level_or_false

    # # OR
    # if (REQUIREMENTS):
    #     return upper_level_or_true
    # else:
    #     def NESTED_DATA
    #     
    #     # if more statics
    #     if (NESTED_REQUIREMENTS):
    #         ...
    #     else:
    #         ...
    #     # otherwise
    #     return NESTED_DATA
        
    def extract(self) -> ExtractedRequirements:
        if not self.tainted_with_statics:
            return ([], [], self.children)
    
        else:
            this_level_static_requirements = []
            nested_statics = []
            non_statics = []
            for child in self.children:
                if child.tainted_with_statics:
                    if not isinstance(child, AndOrRequirement):
                        this_level_static_requirements.append(child)
                    else:
                        nested_statics.append(child)
                else:
                    non_statics.append(child)

            return (this_level_static_requirements, nested_statics, non_statics)
    
    def staticness(self) -> Literal["static", "partial", "dynamic"]:
        if not self.tainted_with_statics:
            return "dynamic"
        _, nested_statics, non_statics = self.extract()

        if len(non_statics) > 0 or any(map(lambda x: x.staticness() == "partial", nested_statics)):
            return "partial"
        else:
            return "static"

from typing import Iterable, TypeVar
A = TypeVar("A")
def partition(pred: Callable[[A], bool], iterable: Iterable[A]) -> tuple[list[A], list[A]]:
    trues: list[A] = []
    falses: list[A] = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses

NavigationKey = tuple[int, ...]
from typing import Optional

import re

regexes: list[tuple[re.Pattern, str]] = [
    (re.compile(r"arguments\("), "ags("),
    (re.compile(r"arg\("), "a("),
    (re.compile(r"And\("), "A("),
    (re.compile(r"Attribute\("), "At("),
    (re.compile(r"BoolOp\("), "BO("),
    (re.compile(r"Call\("), "C("),
    (re.compile(r"Constant\("), "Co("),
    (re.compile(r"Expression\("), "E("),
    (re.compile(r"Lambda\("), "L("),
    (re.compile(r"Load\("), "Lo("),
    (re.compile(r"Name\("), "N("),
    (re.compile(r"Or\("), "O("),
    (re.compile(r"Subscript\("), "S("),
]
shorten_names: list[tuple[bool, str, str]] = [
    ("Attribute", "A"),
    ("BoolOp", "B"),
    ("Call", "C"),
    ("Compare", "Cm"),
    ("Constant", "Cn"),
    ("Expression", "E"),
    ("GtE", "G"),
    ("Lambda", "L"),
    ("Name", "N"),
    ("Subscript", "S"),
    ("UnaryOp", "U"),
    ("arg", "a")
]

regexes: list[tuple[re.Pattern, str]] = [
    (re.compile(f"{long_name}\\("), f"{short_name}(")
        for long_name, short_name in shorten_names
]
     

def shorten_ast(ast_str: str) -> str:
    return ast_str
    accum_str = ast_str
    for reg, to in regexes:
        accum_str = reg.sub(to, accum_str)
    return accum_str

class AndOrParser:
    head: AndOrRequirement

    def __init__(self, andor: AndOrRequirement) -> None:
        self.head = andor
        
    def navigate_to(self, navigation_key: NavigationKey) -> ConnectionRequirement:
        a = self.head

        for k in navigation_key:
            if k == -1: continue

            a = a.children[k] # type: ignore

        return a
       
    # def find_parent_or(self, navigation_key: NavigationKey) -> tuple[NavigationKey, AndOrRequirement]:
    #     depth = len(navigation_key)

    #     for i in range(1, depth-1):
    #         nav = navigation_key[:-i]
    #         a = cast(AndOrRequirement, self.navigate_to(nav))
    #         if not a.is_and:
    #             return (nav, a)
    #     
    #     return ((), self.head)
    
    def get_parent(self, navigation_key: NavigationKey) -> tuple[NavigationKey, AndOrRequirement]:
        nav = navigation_key[:-1]
        a = cast(AndOrRequirement, self.navigate_to(nav))
        return (nav, a)

    def isolate_statics(self, andor: Optional[AndOrRequirement] = None, navigation_key: NavigationKey = ()) -> list[tuple[NavigationKey, str]]:
        if andor == None:
            andor = self.head

        total_statics = []
        
        for i, static in enumerate(andor.children):
            if not static.tainted_with_statics:
                continue

            if isinstance(static, AndOrRequirement) and static.staticness() != "static":
                nav = (*navigation_key, i)
                total_statics.extend(self.isolate_statics(static, nav))
            else:
                # purely static element found. locate nearest parent and save it

                nav = (*navigation_key, i)
                parent_nav, _ = self.get_parent(nav)
                total_statics.append((parent_nav, str(static)))

        return total_statics
    
    def parse_through( self,
                       static_entry_points: list[tuple[NavigationKey, str]],
                       andor: Optional[AndOrRequirement] = None,
                       navigation_key: NavigationKey = () ):
                       
        if andor == None:
            andor = self.head

        import ast

        current_statics = list(map(lambda x: x[1], filter(lambda x: x[0] == navigation_key, static_entry_points)))
        statics, non_statics = partition(lambda x: x[1].tainted_with_statics, enumerate(andor.children))

        
        values_string_builder: list[str] = []
            
        has_current_statics = len(current_statics) > 0
        has_non_statics = len(non_statics) > 0

        if has_non_statics:
            # from ast import BoolOp as BO, And as A, Constant as C, Or as O, Name as N, Load as L, Attribute as At, Call as C, Subscript as S, Expression as E, arguments as ags, arg as a, Lambda as L
            non_static_logic = shorten_ast(ast.dump(ast.parse(logic_as_str(map(lambda x: str(x[1]), non_statics), andor.is_and), '<string>', 'eval').body, False))
            if has_current_statics:
                fully_static_logic = logic_as_str(current_statics, andor.is_and)
                if andor.is_and:
                    values_string_builder.append(f"{non_static_logic} if {fully_static_logic} else Constant(False)")
                else:
                    values_string_builder.append(f"Constant(True) if {fully_static_logic} else {non_static_logic}")
            else:
                values_string_builder.append(non_static_logic)

        for i, static in statics:
            if isinstance(static, AndOrRequirement):
                if static.staticness() != "static":
                    nav = (*navigation_key, i)
                    values_string_builder.append(self.parse_through(static_entry_points, static, nav))
        
        values = ', '.join(values_string_builder)

        if len(values_string_builder) > 1:
            return f"BoolOp({'And' if andor.is_and else 'Or'}(), [{values}])"
        else:
            return values

    def parse(self):
        staticness = self.head.staticness()
        if staticness == "static":
            fully_static_logic = logic_as_str(map(str, self.head.children), self.head.is_and)
            return f"(lambda _: True) if {fully_static_logic} else (lambda _: False)"
        elif staticness == "dynamic":
            fully_dynamic_logic = logic_as_str(map(str, self.head.children), self.head.is_and)
            return f"lambda state: {fully_dynamic_logic}"
            
        static_entry_points = self.isolate_statics()

        total = self.parse_through(static_entry_points)
        # eval(Lambda(args=arguments(args=[arg(arg='state')]), body=BoolOp(op=And(), values=[Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Power Beam'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='logic', ctx=Load()), attr='has_missiles', ctx=Load()), args=[Name(id='state', ctx=Load()), Name(id='player', ctx=Load()), Constant(value=5)], keywords=[]), Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Charge Beam'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Super Missile'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Subscript(value=Name(id='templates', ctx=Load()), slice=Constant(value='Can Use Arm Cannon'), ctx=Load()), args=[Name(id='state', ctx=Load())], keywords=[])]))

        from ast import BoolOp, And, Constant, Or, Name, Load, Attribute, Call, Subscript, Expression, arguments, arg, Lambda
        return f"eval(compile({token}, '<generated>', 'eval'))"
        return f"e({total})"

# class AndOrBuilder:
#     indent_level: int
#     def_level: int
#     all_and: bool
#     current_state: Literal["and", "or", "start"]
#     string_builder: list[str]
#     
#     def __init__(self) -> None:
#         self.indent_level = 1
#         self.def_level = 0
#         self.all_and = True
#         self.current_state = "start"
#         self.string_builder = []
# 
#     def indented(self, string: str, ind = 0) -> str:
#         return f"{'    ' * (self.indent_level + ind)}{string}"
# 
#     def add_to_builder(self, string: str):
#         self.string_builder.append(self.indented(string, 0))
#         
#     def parse(self, req: AndOrRequirement):
#         previous_state = self.current_state
#         this_level_statics, nested_statics, non_statics = req.extract()
#         
#         add_to_builder = self.add_to_builder
#         
#         if previous_state == "start":
#             add_to_builder("logic_total = []")
# 
#         def add_block():
#             increase_def_level = False
#             if len(non_statics) > 0:
#                 logic_accum = []
#                 if self.def_level > 0:
#                     logic_accum.append(f"level_{self.def_level - 1}(state)")
#                 logic_accum.extend(map(str, non_statics))
#                 logic = ' '.join(intersperse(
#                     previous_state if previous_state != "start" else ("and" if req.is_and else "or"),
#                     logic_accum
#                 ))
#                 add_to_builder(f"level_{self.def_level} = lambda state: {logic}")
# 
#                 increase_def_level = True
#                 
#             if len(nested_statics) > 0:
#                 self.current_state = "and" if req.is_and else "or"
#                 for nested in nested_statics:
#                     # self.indent_level += 1
#                     if increase_def_level: self.def_level += 1
#                     self.parse(nested)
#                     if increase_def_level: self.def_level -= 1
#                     # self.indent_level -= 1
#                 self.current_state = previous_state
#             else:
#                 add_to_builder(f"return level_{self.def_level}")
# 
#         if len(this_level_statics) > 0:
#             statics_requirement = ' '.join(["(",
#                 *intersperse(
#                     'and' if req.is_and else 'or',
#                     map(str, this_level_statics)
#                 )
#             ,")"])
# 
#             add_to_builder(f"if {statics_requirement}:")
#             self.indent_level += 1
#             
#         if req.is_and:
#             add_block()
# 
#             if len(this_level_statics) > 0:
#                 self.indent_level -= 1
#                 add_to_builder("else:")
#                 self.indent_level += 1
# 
#                 if self.def_level == 0 or self.all_and:
#                     add_to_builder(f"return no_entry")
#                 else:
#                     add_to_builder(f"return level_{self.def_level-1}")
#                 
#                 self.indent_level -= 1
# 
#         else:
#             self.all_and = False
# 
#             if len(this_level_statics) > 0:
#                 if self.def_level == 0:
#                     add_to_builder(f"return lambda _: True")
#                 else:
#                     add_to_builder(f"return level_{self.def_level-1}")
# 
#                 self.indent_level -= 1
#                 add_to_builder("else:")
#                 self.indent_level += 1
# 
#             add_block()
#             if len(this_level_statics) > 0:
#                 self.indent_level -= 1
# 
#         if previous_state == "start":
#             add_to_builder(f"if len(logic_total) == 0:")
#             self.indent_level += 1
#             add_to_builder(f"return lambda _: False")
#             self.indent_level -= 1
#             add_to_builder(f"elif len(logic_total) == 1:")
#             self.indent_level += 1
#             add_to_builder(f"return logic_total[0]")
#             self.indent_level -= 1
#             add_to_builder(f"else:")
#             self.indent_level += 1
#             add_to_builder(f"return lambda state: {'all' if req.is_and else 'any'}(lambda x: x(state), logic_total)")
#         return self.string_builder

        
class ResourceRequirement(ConnectionRequirement):
    negate: bool
    requirement_data: DataTypes.Resource
    
    def __init__(self, req: DataTypes.Resource):
        super().__init__(req)
        
        data = req["data"]

        self.negate = data["negate"]

        if data["type"] == "tricks":
            self.tainted_with_statics = True
    
    def __str__(self) -> str:
        if self.negate:
            return f"not {self.str_helper()}"
        else:
            return self.str_helper()
        
    def str_helper(self) -> str:
        data = self.requirement_data["data"]

        if data["type"] == "items":
            item_name = items_short_to_long[data['name']]
            if item_name == "Missile":
                return f"logic.has_missiles(state, player, {data['amount']})"
            else:
                if data["amount"] == 1:
                    return f"state.has('{item_name}', player)"
                else:
                    return f"state.count('{item_name}', player) >= {data['amount']}"

        elif data["type"] == "damage":
            return f"logic.can_sustain_damage(state, player, {data['amount']}, '{data['name']}')"

        elif data["type"] == "events":
            return f"state.has('{events_short_to_long[data['name']]}', player)"

        elif data["type"] == "misc":
            return f"logic.has_misc(state, player, '{data['name']}')"

        elif data["type"] == "tricks":
            return f"options.{trick_name_gen(tricks_short_to_long[data['name']])}.value >= {data['amount']}"

        else:
            raise ValueError(f"unknown resource requirement: {data}")


def create_connection_requirement(data: DataTypes.RequirementData) -> ConnectionRequirement:
    if data["type"] == "and" or data["type"] == "or":
        return AndOrRequirement(data)

    elif data["type"] == "resource":
        return ResourceRequirement(data)

    elif data["type"] == "template":
        return TemplateRequirement(data)

    else:
        raise ValueError(f"unknown connection requrement: {data}")


def parse_resource_requirement(res: DataTypes.ResourceData) -> str:
    if res["type"] == "items":
        item_name = items_short_to_long[res['name']]
        if item_name == "Missile":
            return f"logic.has_missiles(state, player, {res['amount']})"
        else:
            if res["amount"] == 1:
                return f"state.has('{item_name}', player)"
            else:
                return f"state.count('{item_name}', player) >= {res['amount']}"

    elif res["type"] == "damage":
        return f"logic.can_sustain_damage(state, player, {res['amount']}, '{res['name']}')"

    elif res["type"] == "events":
        return f"state.has('{events_short_to_long[res['name']]}', player)"

    elif res["type"] == "misc":
        return f"logic.has_misc(state, player, '{res['name']}')"

    elif res["type"] == "tricks":
        return f"options.{trick_name_gen(tricks_short_to_long[res['name']])}.value >= {res['amount']}"
    
    else:
        raise ValueError(f"unknown resource requirement: {res}")

def parse_connection_data_helper(requirement: DataTypes.RequirementData) -> str:
    if requirement["type"] == "and" or requirement["type"] == "or":
        return ' '.join(["(",
            *intersperse(
                # and / or
                requirement['type'],
                map(parse_connection_data_helper, requirement["data"]["items"])
            )
        ,")"])

    elif requirement["type"] == "resource":
        logic = parse_resource_requirement(requirement["data"])
            
        if requirement["data"]["negate"]:
            return f"not {logic}"
        else:
            return logic

    elif requirement["type"] == "template":
        return f"templates['{requirement['data']}'](state)"

    else:
        raise ValueError(f"unknown connection requrement: {requirement}")

def parse_connection_data(requirement: DataTypes.RequirementData) -> str:
    if requirement["type"] == "and" and len(requirement["data"]["items"]) == 0:
        return "None"
    if requirement["type"] == "or" and len(requirement["data"]["items"]) == 0:
        return "lambda _: False"
    if requirement["type"] == "template":
        return f"templates['{requirement['data']}']"
    
    if requirement["type"] == "and" or requirement["type"] == "or":
        conn = cast(AndOrRequirement, create_connection_requirement(requirement))
        parser = AndOrParser(conn)
        return parser.parse()
    return f"lambda state: {parse_connection_data_helper(requirement)}"

def parse_dock_requirements(dock: DataTypes.DockWeaknessEntry) -> Optional[str]:
    req = parse_connection_data(dock["requirement"])
    if req == "lambda _: False":
        return None
    lock = dock["lock"]
    if lock is None:
        return req
    else:
        lock_req = parse_connection_data(lock["requirement"])
        if lock_req == "lambda _: False":
            return None
        elif req == "None":
            return lock_req
        elif lock_req == "None":
            return req
        else:
            return f"({req}) and ({lock_req})"

dock_requirements: dict[str, Optional[str]] = {
    dock_type: parse_dock_requirements(item)
    for docks in header["dock_weakness_database"]["types"].values()
    for dock_type, item in docks["items"].items()
}

# for dock_category, docks in header["dock_weakness_database"]["types"].items():
#     parsed_docks: list[str] = []
# 
#     for (name, item) in docks["items"].items():
#         parsed = parse_connection_data(item["requirement"])
#         parsed_docks.append(parsed)
#         dock_requirements[name] = parsed
# 
#     dock_category_requirements[dock_category] = ' '.join(intersperse("and", parsed_docks))

from typing import Optional, Literal
from dataclasses import dataclass

def is_event_skippable(event_name: str) -> bool:
    return event_name in ["Observatory Activated", "Control Tower Fight"]

@dataclass
class RegionInfo:
    has_location: Optional[Literal["pickup", "event", "items_every_room"]]
    event_name: Optional[str]
    event_skippable: Optional[bool]
    connections: list[tuple[str, str]]
    dock_connection: Optional[tuple[str, str]]
    
    def __init__(self, node: DataTypes.Node, area_name: str, region_name: str) -> None:
        self.has_location = None
        self.event_name = None
        self.event_skippable = None
        self.dock_connection = None

        if node["node_type"] == "pickup" or node["node_type"] == "event":
            if "default" in node["layers"]:
                self.has_location = node["node_type"]
            elif "items_every_room" in node["layers"]:
                self.has_location = "items_every_room"

            if node["node_type"] == "event":
                self.event_name = events_short_to_long[node["event_name"]]
                self.event_skippable = is_event_skippable(self.event_name)

        if node["node_type"] == "dock":
            rule = dock_requirements[node["default_dock_weakness"]]
            if rule is not None:
                self.dock_connection = (absolute_location_format(node["default_connection"]), f"dock_requirements['{node['default_dock_weakness']}']")
        
        if False:
            for node_connection_name, requirements in node["connections"].items():
                conn = create_connection_requirement(requirements)
                if isinstance(conn, AndOrRequirement) and node_connection_name == "Pickup (Wavebuster)":
                    # builder = AndOrBuilder()
                    # a = builder.parse(conn)
                    # print('\n'.join(a))
                    a = AndOrParser(conn)
                    a.parse()
        
        self.connections = [
            (absolute_node_format(node_connection_name, area_name, region_name), parse_connection_data(requirements))
            for node_connection_name, requirements in node["connections"].items()
        ]

def load_region_json(region_filename) -> tuple[str, DataTypes.Region]:
    with open(relative_to_script(__file__, f"data/randovania_data/json_data/{region_filename}"), 'rt') as f:
        json_data = json.load(f)
        if VALIDATE:
            from . import Schema
            Schema.Region.validate(json_data)
    return (json_data["name"], json_data)

import re
link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\n")

with open("../generated.py", "w") as f:
    from jinja2 import Environment as J2Environment, FileSystemLoader as J2FSLoader

    env = J2Environment(loader=J2FSLoader(relative_to_script(__file__, "templates")))
    options_template = env.get_template("options.pyt")
    regions_template = env.get_template("regions.pyt")
    rules_template = env.get_template("rules.pyt")

    rules = [
        (absolute_node_format(node_name, area_name, region_name), RegionInfo(node, area_name, region_name))
        for region_name, region in map(load_region_json, filter(lambda x: x != "Frigate Orpheon.json", header["regions"]))
        for area_name, area in region["areas"].items()
        for node_name, node in area["nodes"].items()
    ]

    templates: dict[str, str] = {
        template_name: parse_connection_data(template)
        for template_name, template in header["resource_database"]["requirement_template"].items()
    }

    damage_resistances: dict[str, dict[str, float]] = {
        item["name"]: {i["name"]: i["multiplier"] for i in item["reductions"]}
        for item in header["resource_database"]["damage_reductions"]
    }

    builder: list[str] = []
    builder.append("# pyright: reportGeneralTypeIssues=false")
    builder.append(f"damage_resistances={damage_resistances}")
    # builder.append(f"locations={[node_from for node_from, node_rules in rules if node_rules.has_location == 'pickup']}")
    builder.append(f"items={items}")
    builder.append(options_template.render(tricks=header["resource_database"]["tricks"].items(), trick_name_gen=trick_name_gen, parse_trick_desc=parse_trick_desc))
    builder.append(regions_template.render(rules=rules))
    builder.append(rules_template.render(rules=rules, templates=templates, dock_requirements=dock_requirements))
    f.write("\n".join(builder))