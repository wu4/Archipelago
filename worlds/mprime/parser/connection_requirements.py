from __future__ import annotations

from . import Types as DataTypes
from .parser_utils import trick_name_gen, intersperse

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .json_parsing import RandovaniaData

def parse_connection_requirements(data: RandovaniaData, req: DataTypes.RequirementData, exclude_compile = False) -> str:
    """
    Parses the requirements for a connection. Returns the appropriate logic as
    an AST string, extracting static values (e.g. ones that rely on player
    options) outside of the resulting code.
    """
    head: DataTypes.RequirementData
    if req["type"] == "and" or req["type"] == "or":
        head = req
    else:
        # funny hack for singletons. watch this backfire spectacularly
        head = {
            "type": "and",
            "data": {
                "comment": None,
                "items": [req]
            }
        }

    if len(head["data"]["items"]) == 0:
        if not exclude_compile and head["type"] == "and":
            return "None"
        else:
            return f"lambda _:{head['type'] == 'and'}"

    total = render_requirements(data, head["type"] == "and", *head["data"]["items"])

    if exclude_compile:
        return total
    else:
        return f"lambda s:{total}"

def render_resource_requirement(data: RandovaniaData, req: DataTypes.Resource) -> str:
    req_data = req["data"]

    if req_data["type"] == "items":
        item_name = data.items_short_to_long[req_data['name']]
        if item_name == "Missile":
            return f"l_hm(s, p, {req_data['amount']})"
        else:
            if req_data["amount"] == 1:
                return f"s.has('{item_name}', p)"
            else:
                return f"s.count('{item_name}',p)>={req_data['amount']}"

    elif req_data["type"] == "damage":
        return f"l_csd(s,p,{req_data['amount']},'{req_data['name']}')"

    elif req_data["type"] == "events":
        return f"s.has('{data.events_short_to_long[req_data['name']]}',p)"

    elif req_data["type"] == "misc":
        return f"l_hmisc(s,p,'{req_data['name']}')"

    elif req_data["type"] == "tricks":
        trick_name = trick_name_gen(data.tricks_short_to_long[req_data['name']])
        ret_str = f"o.{trick_name}.value>={req_data['amount']}"
        return ret_str

    else:
        raise ValueError(f"unknown resource requirement: {req_data}")
    
def render_requirement(data: RandovaniaData, req: DataTypes.RequirementData) -> str:
    if req["type"] == "and" or req["type"] == "or":
        return render_requirements(data, req["type"] == "and", *req["data"]["items"])

    elif req["type"] == "template":
        return f"t['{req['data']}'](s)"

    elif req["type"] == "resource":
        req_data = req["data"]

        if req_data["negate"]:
            return f"not {render_resource_requirement(data, req)}"
        else:
            return render_resource_requirement(data, req)

    raise ValueError(f"unknown requirement type: {req['type']}")
    
def render_requirements(data: RandovaniaData, is_and: bool, *reqs: DataTypes.RequirementData) -> str:
    if len(reqs) == 0:
        return f"{is_and}"
    elif len(reqs) == 1:
        return render_requirement(data, reqs[0])
    else:
        return '(' + ' '.join(intersperse(
            'and' if is_and else 'or',
            map(lambda x: render_requirement(data, x), reqs)
        )) + ')'