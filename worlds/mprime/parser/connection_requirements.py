from __future__ import annotations

from . import Types as DataTypes
from .util import trick_name_gen, partition, intersperse
from enum import Enum
from .writing_ast import And, Not, Or, Constant, Name, Lambda, Call, LogicCall, StateHas, StateCountGtE, quoted_str

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

# def logic_as_str(logics: Iterable[str], is_and: bool) -> str:
#     li = list(logics)
#     if len(li) == 0:
#         return f"Constant({is_and})"
#     elif len(li) == 1:
#         return str(li[0])
#     else:
#         return f"{'a' if is_and else 'o'}(" + ','.join(map(str, li)) + ')'

ReqTuple = tuple[int, DataTypes.RequirementData]
Req = DataTypes.RequirementData
def staticness_partition3(
    iterable: Iterable[DataTypes.RequirementData]
) -> tuple[list[Req],
           list[Req],
           list[Req]]:
    statics: list[Req] = []
    semi_statics: list[Req] = []
    dynamics: list[Req] = []
    for item in iterable:
        staticness = get_staticness(item)
        if staticness == Staticness.DYNAMIC:
            dynamics.append(item)
        elif staticness == Staticness.SEMISTATIC:
            semi_statics.append(item)
        else:
            statics.append(item)
    return statics, semi_statics, dynamics

def staticness_partition3_enumerated(
    iterable: Iterable[DataTypes.RequirementData]
) -> tuple[list[ReqTuple],
           list[ReqTuple],
           list[ReqTuple]]:
    statics: list[ReqTuple] = []
    semi_statics: list[ReqTuple] = []
    dynamics: list[ReqTuple] = []
    for item in enumerate(iterable):
        staticness = get_staticness(item[1])
        if staticness == Staticness.DYNAMIC:
            dynamics.append(item)
        elif staticness == Staticness.SEMISTATIC:
            semi_statics.append(item)
        else:
            statics.append(item)
    return statics, semi_statics, dynamics

class RequirementRenderer:
    data: RandovaniaData

    def __init__(self, data: RandovaniaData) -> None:
        self.data = data
        
    def render_dynamic_resource_requirement(self, req: DataTypes.Resource) -> str:
        data = req["data"]

        if data["type"] == "items":
            item_name = self.data.items_short_to_long[data['name']]
            if item_name == "Missile":
                return LogicCall("has_missiles", Constant(str(data["amount"])))
                return f"l_hm({data['amount']})"
                return f"logic.has_missiles(state, player, {data['amount']})"
            else:
                if data["amount"] == 1:
                    return StateHas(item_name)
                    return f"s_has('{item_name}')"
                    return f"state.has('{item_name}', player)"
                else:
                    return StateCountGtE(item_name, data["amount"])
                    return f"s_gte('{item_name}', {data['amount']})"
                    return f"state.count('{item_name}', player) >= {data['amount']}"

        elif data["type"] == "damage":
            return LogicCall("can_sustain_damage", Constant(str(data['amount'])), Constant(quoted_str(data['name'])))
            return f"l_csd({data['amount']},'{data['name']}')"
            return f"logic.can_sustain_damage(state, player, {data['amount']}, '{data['name']}')"

        elif data["type"] == "events":
            return StateHas(self.data.events_short_to_long[data["name"]])
            return f"s_has('{self.data.events_short_to_long[data['name']]}')"
            return f"state.has('{events_short_to_long[data['name']]}', player)"

        elif data["type"] == "misc":
            return LogicCall("has_misc", Constant(quoted_str(data["name"])))
            return f"l_hmisc('{data['name']}')"
            return f"logic.has_misc(state, player, '{data['name']}')"

        else:
            raise ValueError(f"unknown resource requirement: {data}")
        
    def render_dynamic_requirement(self, req: DataTypes.RequirementData) -> str:
        if req["type"] == "and" or req["type"] == "or":
            return self.render_dynamic_requirements(req["type"] == "and", *req["data"]["items"])

        elif req["type"] == "template":
            return f"t['{req['data']}']"

        elif req["type"] == "resource":
            data = req["data"]

            if data["negate"]:
                return Not(self.render_dynamic_resource_requirement(req))
            else:
                return self.render_dynamic_resource_requirement(req)

        raise ValueError(f"unknown requirement type: {req['type']}")
        
    def render_dynamic_requirements(self, is_and: bool, *reqs: DataTypes.RequirementData) -> str:
        if len(reqs) == 0:
            return Constant(str(is_and))
        elif len(reqs) == 1:
            return self.render_dynamic_requirement(reqs[0])
        else:
            logic_func = And if is_and else Or
            return logic_func(*map(self.render_dynamic_requirement, reqs))
    
    def render_static_requirement(self, req: DataTypes.RequirementData) -> str:
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
        
    def navigate_to(self, navigation_key: NavigationKey) -> DataTypes.RequirementData:
        a = self.head

        for k in navigation_key:
            if a["type"] != "and" and a["type"] != "or":
                raise IndexError("trying to navigate through non and/or requirement")

            a = a["data"]["items"][k]

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
    
    # def get_parent(self, navigation_key: NavigationKey) -> tuple[NavigationKey, DataTypes.Logic]:
    #     nav = navigation_key[:-1]
    #     a = cast(DataTypes.Logic, self.navigate_to(nav))
    #     return (nav, a)

    # def isolate_statics(self, req: Optional[DataTypes.Logic] = None, navigation_key: NavigationKey = ()) -> list[tuple[NavigationKey, str]]:
    #     if req == None:
    #         req = self.head

    #     total_statics: list[tuple[NavigationKey, str]] = []
    #     
    #     for i, item in enumerate(req["data"]["items"]):
    #         staticness = get_staticness(item)
    #         if staticness == Staticness.DYNAMIC:
    #             continue
    #         # if not static.tainted_with_statics:
    #         #     continue

    #         if (item["type"] == "and" or item["type"] == "or") and staticness != Staticness.STATIC:
    #             nav = (*navigation_key, i)
    #             total_statics.extend(self.isolate_statics(item, nav))
    #         else:
    #             # purely static element found. locate nearest parent and save it

    #             nav = (*navigation_key, i)
    #             parent_nav, _ = self.get_parent(nav)
    #             total_statics.append((parent_nav, self.renderer.render_static_requirement(item)))

    #     return total_statics
    
    def deep_and_search(
        self,
        req: DataTypes.Logic,
        used: set[NavigationKey],
        navigation_key: NavigationKey
    ) -> list[tuple[NavigationKey, DataTypes.RequirementData]]:
        ret = []
        for i, sub_req in enumerate(req["data"]["items"]):
            nav = (*navigation_key, i)
            if nav in used: continue
            staticness = get_staticness(sub_req)
            if staticness == Staticness.STATIC:
                # print(nav, sub_req)
                used.add(nav)
                ret.append((nav, sub_req))
            elif sub_req["type"] == "and":
                if staticness != Staticness.DYNAMIC:
                    ret.extend(self.deep_and_search(sub_req, used, nav))
        
        return ret

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
        staticness = get_staticness(self.head)
        if staticness == "static":
            fully_static_logic = self.renderer.render_static_requirements(self.head["type"] == "and", *self.head["data"]["items"])
            return f"(lambda _:True) if {fully_static_logic} else (lambda _:False)"
        elif staticness == "dynamic":
            fully_dynamic_logic = self.renderer.render_dynamic_requirements(self.head["type"] == "and", *self.head["data"]["items"])
            return f"{fully_dynamic_logic}"
            
        # static_entry_points = self.isolate_statics()

        total = self.parse_through([], used = set())
        # eval(Lambda(args=arguments(args=[arg(arg='state')]), body=BoolOp(op=And(), values=[Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Power Beam'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='logic', ctx=Load()), attr='has_missiles', ctx=Load()), args=[Name(id='state', ctx=Load()), Name(id='player', ctx=Load()), Constant(value=5)], keywords=[]), Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Charge Beam'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Attribute(value=Name(id='state', ctx=Load()), attr='has', ctx=Load()), args=[Constant(value='Super Missile'), Name(id='player', ctx=Load())], keywords=[]), Call(func=Subscript(value=Name(id='templates', ctx=Load()), slice=Constant(value='Can Use Arm Cannon'), ctx=Load()), args=[Name(id='state', ctx=Load())], keywords=[])]))

        # from ast import BoolOp, And, Constant, Or, Name, Load, Attribute, Call, Subscript, Expression, arguments, arg, Lambda
        # return f"eval(compile({total}, '<generated>', 'eval'))"
        if total == "":
            if not exclude_compile and self.head["type"] == "and":
                return "None"
            else:
                return Lambda(["_"], Constant(str(self.head["type"] == "and")))
        if exclude_compile:
            return total
        else:
            return f"e({total})"