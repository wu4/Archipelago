from __future__ import annotations

from .types.requirement import Requirement, Resource
from .parser_utils import trick_name_gen, intersperse

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .json_parsing import RandovaniaData

def parse_connection_requirements(data: RandovaniaData, req: Requirement) -> str | bool:
    """
    Parses the requirements for a connection. Returns the appropriate logic as
    an AST string, extracting static values (e.g. ones that rely on player
    options) outside of the resulting code.
    """
    flattened = _flatten_requirements(data, req)
    if type(flattened) == bool:
        return flattened
    else:
        rendered = _render_requirement(data, flattened)

        return f"lambda s:{rendered}"

def req_eq(left: Requirement, right: Requirement) -> bool:
    if (left["type"] == "and" and right["type"] == "and") or (left["type"] == "or" and right["type"] == "or"):
        try:
            return all(map(
                lambda reqs: req_eq(*reqs),
                zip(left["data"]["items"], right["data"]["items"],
                    strict=True) # raises ValueError if items are of different length
            ))
        except ValueError:
            return False
    else:
        return left["type"] == right["type"] and left["data"] == right["data"]

def is_req_in(req: Requirement, st: list[Requirement]) -> bool:
    """Test if a Requirement is inside of a list. Ignores comments."""
    return any(map(lambda x: req_eq(req, x), st))

from typing import Optional
def _flatten_requirements( data: RandovaniaData,
                           req: Requirement,
                           seen: Optional[list[Requirement]] = None
                         ) -> Requirement | bool:

    # return req

    if not (req["type"] == "and" or req["type"] == "or"):
        return req


    is_or = req["type"] == "or"
    items = req["data"]["items"]

    non_bool_items: list[Requirement] = []
    if seen is None:
        seen = []
    unique_items = []

    for item in items:
        if is_req_in(item, seen):
            continue
        seen.append(item)
        unique_items.append(item)
    
    for item in unique_items:
        if req["type"] == "and" and item["type"] != "or":
            flattened = _flatten_requirements(data, item, seen)
        else:
            flattened = _flatten_requirements(data, item, seen.copy())
        if type(flattened) == bool:
            # True  and (logic) == (logic)
            # False and (logic) == False
            # True  or  (logic) == True
            # False or  (logic) == (logic)

            if flattened == is_or:
                return is_or
        else:
            non_bool_items.append(flattened)

    if len(non_bool_items) == 0:
        return req["type"] == "and"
    elif len(non_bool_items) == 1:
        return non_bool_items[0]
    else:
        return {
            "type": "or" if is_or else "and",
            "data": {
                "comment": None,
                "items": non_bool_items
            }
        }


def _render_resource_requirement(data: RandovaniaData, req: Resource) -> str:
    req_data = req["data"]

    if req_data["type"] == "items":
        item_name = data.items_short_to_long[req_data['name']]
        if item_name == "Missile":
            return f"l_hm(s, p, {req_data['amount']})"
        else:
            if req_data["amount"] == 1:
                return f"s.has('{item_name}',p)"
            else:
                return f"s.has('{item_name}',p,{req_data['amount']})"

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
    
def _render_requirement(data: RandovaniaData, req: Requirement) -> str:
    if ( req["type"] == "and"
      or req["type"] == "or"):      return _render_requirements(data, req["type"] == "and", *req["data"]["items"])
    elif req["type"] == "template": return f"t['{req['data']}'](s)"
    elif req["type"] == "resource": return ('not ' if req['data']['negate'] else '') + _render_resource_requirement(data, req)

    raise ValueError(f"unknown requirement type: {req['type']}")
    
def _render_requirements(data: RandovaniaData, is_and: bool, *reqs: Requirement) -> str:
    if len(reqs) == 0:
        return f"{is_and}"
    elif len(reqs) == 1:
        return _render_requirement(data, reqs[0])
    else:
        return '(' + ' '.join(intersperse(
            'and' if is_and else 'or',
            map(lambda x: _render_requirement(data, x), reqs)
        )) + ')'