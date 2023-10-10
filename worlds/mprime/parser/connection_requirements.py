from __future__ import annotations

from . import Types as DataTypes
from .util import trick_name_gen, partition, intersperse
from enum import Enum

from typing import Optional, TYPE_CHECKING, cast, Iterable, Callable
if TYPE_CHECKING:
    from .json_parsing import RandovaniaData

def parse_connection_requirements(data: RandovaniaData, req: DataTypes.RequirementData, exclude_compile = False) -> str:
    """
    Parses the requirements for a connection. Returns the appropriate logic as
    an AST string, extracting static values (e.g. ones that rely on player
    options) outside of the resulting code.
    """
    a = RequirementParser(data, req)
    return a.parse(exclude_compile)

class RequirementRenderer:
    data: RandovaniaData

    def __init__(self, data: RandovaniaData) -> None:
        self.data = data
        
    def render_dynamic_resource_requirement(self, req: DataTypes.Resource) -> str:
        data = req["data"]

        if data["type"] == "items":
            item_name = self.data.items_short_to_long[data['name']]
            if item_name == "Missile":
                return f"l.has_missiles(s, p, {data['amount']})"
            else:
                if data["amount"] == 1:
                    return f"s.has('{item_name}', p)"
                else:
                    return f"s.count('{item_name}',p)>={data['amount']}"

        elif data["type"] == "damage":
            return f"l.can_sustain_damage(s,p,{data['amount']},'{data['name']}')"

        elif data["type"] == "events":
            return f"s.has('{self.data.events_short_to_long[data['name']]}',p)"

        elif data["type"] == "misc":
            return f"l.has_misc(s,p,'{data['name']}')"

        elif data["type"] == "tricks":
            trick_name = trick_name_gen(self.data.tricks_short_to_long[data['name']])
            ret_str = f"o.{trick_name}.value>={data['amount']}"
            return ret_str

        else:
            raise ValueError(f"unknown resource requirement: {data}")
        
    def render_dynamic_requirement(self, req: DataTypes.RequirementData) -> str:
        if req["type"] == "and" or req["type"] == "or":
            return self.render_dynamic_requirements(req["type"] == "and", *req["data"]["items"])

        elif req["type"] == "template":
            return f"t['{req['data']}'](s)"

        elif req["type"] == "resource":
            data = req["data"]

            if data["negate"]:
                return f"not {self.render_dynamic_resource_requirement(req)}"
            else:
                return self.render_dynamic_resource_requirement(req)

        raise ValueError(f"unknown requirement type: {req['type']}")
        
    def render_dynamic_requirements(self, is_and: bool, *reqs: DataTypes.RequirementData) -> str:
        if len(reqs) == 0:
            return f"{is_and}"
        elif len(reqs) == 1:
            return self.render_dynamic_requirement(reqs[0])
        else:
            return '(' + ' '.join(intersperse(
                'and' if is_and else 'or',
                map(self.render_dynamic_requirement, reqs)
            )) + ')'
            return logic_func(*map(self.render_dynamic_requirement, reqs))
    
    def render_static_requirement(self, req: DataTypes.RequirementData) -> str:
        raise DeprecationWarning
        if req["type"] == "and" or req["type"] == "or":
            return self.render_static_requirements(req["type"] == "and", *(req["data"]["items"]))
        elif req["type"] == "resource":
            if req["data"]["type"] == "tricks":
                trick_name = trick_name_gen(self.data.tricks_short_to_long[req['data']['name']])
                ret_str = f"o.{trick_name}.value>={req['data']['amount']}"

                if req["data"]["negate"]:
                    return f"not {ret_str}"
                else:
                    return ret_str
            raise ValueError(f"trying to render a non-static resource as static ({req['data']})")
        elif req["type"] == "template":
            raise ValueError("trying to render a template as static")

        raise ValueError(f"unknown static resource requirement type {req['type']}")
        
    def render_static_requirements(self, is_and: bool, *reqs: DataTypes.RequirementData) -> str:
        raise DeprecationWarning
        if len(reqs) == 0:
            return Constant(str(is_and))
        elif len(reqs) == 1:
            return self.render_static_requirement(reqs[0])
        else:
            # a = list(map(self.render_static_requirement, reqs))
            # if len(a[0]) == 1:
            #     print(a)
            return "(" + " ".join(
                intersperse(
                    "and" if is_and else "or",
                    map(self.render_static_requirement, reqs)
                )
            ) + ")"

class Staticness(Enum):
    DYNAMIC = 0
    SEMISTATIC = 1
    STATIC = 2

def get_staticness(req: DataTypes.RequirementData) -> Staticness:
    if req["type"] == "and" or req["type"] == "or":
        if len(req["data"]["items"]) == 0:
            return Staticness.STATIC
        first = -1
        for item in req["data"]["items"]:
            if first == -1:
                first = get_staticness(item)
                continue
            if first != get_staticness(item):
                return Staticness.SEMISTATIC
        return cast(Staticness, first)
    elif req["type"] == "resource":
        if req["data"]["type"] == "tricks": #or req["data"]["type"] == "misc":
            return Staticness.STATIC
        else:
            return Staticness.DYNAMIC
    elif req["type"] == "template":
        return Staticness.DYNAMIC

    raise ValueError(f"unknown data type {req['type']}")

from typing import TypeVar, Any
A = TypeVar("A")
def only_second(t: tuple[Any, A]) -> A:
    return t[1]

NavigationKey = tuple[int, ...]
class RequirementParser:
    head: DataTypes.Logic
    data: RandovaniaData
    renderer: RequirementRenderer

    def __init__(self, data: RandovaniaData, req: DataTypes.RequirementData) -> None:
        self.data = data
        if req["type"] == "and" or req["type"] == "or":
            self.head = req
        else:
            # funny hack for singletons. watch this backfire spectacularly
            self.head = {
                "type": "and",
                "data": {
                    "comment": None,
                    "items": [req]
                }
            }
        self.renderer = RequirementRenderer(data)

    def parse_through( self,
                       static_entry_points: list[tuple[NavigationKey, str]],
                       req: Optional[DataTypes.Logic] = None,
                       top_level: bool = True,
                       used: set[NavigationKey] = set(),
                       navigation_key: NavigationKey = () ):
                       
        if req == None:
            req = self.head

        # current_statics = list(map(lambda x: x[1], filter(lambda x: x[0] == navigation_key, static_entry_points)))
        has_current_statics = False
        current_statics: list[Req] = []
        statics, semi_statics, dynamics = staticness_partition3_enumerated(req["data"]["items"])

        def filter_used(ns: list[ReqTuple]) -> list[ReqTuple]:
            return list(filter(lambda x: (*navigation_key, x[0]) not in used, ns))

        statics =      filter_used(statics)
        semi_statics = filter_used(semi_statics)
        dynamics =     filter_used(dynamics)

        if req["type"] == "and":
            for i, static in statics:
                used.add((i,))
                current_statics.append(static) #= self.renderer.render_static_requirements(req["type"] == "and", *statics)
        
            for i, semi in semi_statics:
                nav = (*navigation_key, i)
                if nav in used: continue
                if semi["type"] == "and":
                    extracted_datas = self.deep_and_search(semi, used, nav)
                    current_statics.extend(map(lambda x: x[1], extracted_datas))
            # if not (semi["type"] == "and" or semi["type"] == "or"): continue
            # sub_statics, _, _ = staticness_partition3(semi["data"]["items"])
            # current_statics.extend(sub_statics)
            # probe_statics(req["data"]["items"])
        
        has_current_statics = len(current_statics) > 0
        values_string_builder: list[str] = []
            
        if len(dynamics) > 0:
            # from ast import BoolOp as BO, And as A, Constant as C, Or as O, Name as N, Load as L, Attribute as At, Call as C, Subscript as S, Expression as E, arguments as ags, arg as a, Lambda as L
            # non_static_logic = shorten_ast(ast.dump(ast.parse(logic_as_str(map(lambda x: str(x[1]), non_statics), andor.is_and), '<string>', 'eval').body, False))
            dynamic_logic = self.renderer.render_dynamic_requirements(req["type"] == "and", *map(only_second, dynamics))
            if has_current_statics:
                static_logic = self.renderer.render_static_requirements(req["type"] == "and", *current_statics)
                if req["type"] == "and":
                    values_string_builder.append(f"{dynamic_logic} if {static_logic} else {Constant(quoted_str('False'))}")
                else:
                    values_string_builder.append(f"{Constant(quoted_str('True'))} if {static_logic} else {dynamic_logic}")
            else:
                # print('appending dynamic logic only')
                # print(dynamic_logic)
                values_string_builder.append(dynamic_logic)

        for i, semi in semi_statics:
            if semi["type"] == "and" or semi["type"] == "or":
                nav = (*navigation_key, i)
                values_string_builder.append(self.parse_through(static_entry_points, semi, False, used, nav))
        
        # values = ', '.join(values_string_builder)

        if len(values_string_builder) > 1:
            logic_func = And if req["type"] == "and" else Or
            return logic_func(*values_string_builder)
        elif len(values_string_builder) == 1:
            return values_string_builder[0]
        else:
            return ""

    def parse(self, exclude_compile = False):
        if len(self.head["data"]["items"]) == 0:
            if not exclude_compile and self.head["type"] == "and":
                return "None"
            else:
                return f"lambda _:{self.head['type'] == 'and'}"

        total = self.renderer.render_dynamic_requirements(self.head["type"] == "and", *self.head["data"]["items"])

        if exclude_compile:
            return total
        else:
            return f"lambda s:{total}"
        if staticness == "static":
            fully_static_logic = self.renderer.render_static_requirements(self.head["type"] == "and", *self.head["data"]["items"])
            return f"(lambda _:True) if {fully_static_logic} else (lambda _:False)"
        elif staticness == "dynamic":
            fully_dynamic_logic = self.renderer.render_dynamic_requirements(self.head["type"] == "and", *self.head["data"]["items"])
            return f"{fully_dynamic_logic}"
            
        # static_entry_points = self.isolate_statics()

        total = self.parse_through([], used = set())

        # from ast import BoolOp, And, Constant, Or, Name, Load, Attribute, Call, Subscript, Expression, arguments, arg, Lambda
        # return f"eval(compile({total}, '<generated>', 'eval'))"