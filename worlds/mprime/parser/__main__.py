from __future__ import annotations

import json
from typing import cast, Callable, TYPE_CHECKING, TypeVar
from inflection import underscore

import Types as DataTypes

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

# from ..Utils import map_dict, region_format, get_underscored, relative_to_script

# from . import Types as DataTypes


if TYPE_CHECKING:
    from ..Logic import MetroidPrimeLogic

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

def parse_resource_requirement(res: DataTypes.ResourceData) -> str:
    if res["type"] == "items":
        item_name = items_short_to_long[res['name']]
        if item_name == "Missile":
            return f"logic.metroid_prime_has_missiles(player, {res['amount']})"
        else:
            if res["amount"] == 1:
                return f"logic.has('{item_name}', player)"
            else:
                return f"logic.count('{item_name}', player) >= {res['amount']}"

    elif res["type"] == "damage":
        return f"logic.metroid_prime_can_sustain_damage(player, {res['amount']}, '{res['name']}')"

    elif res["type"] == "events":
        return f"logic.has('{events_short_to_long[res['name']]}', player)"

    elif res["type"] == "misc":
        return f"logic.metroid_prime_has_misc(player, '{res['name']}')"

    elif res["type"] == "tricks":
        return f"logic.multiworld.{trick_name_gen(tricks_short_to_long[res['name']])}[player].value >= {res['amount']}"
    
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
        return f"templates['{requirement['data']}'](logic)"

    else:
        raise ValueError(f"unknown connection requrement: {requirement}")

def parse_connection_data(requirement: DataTypes.RequirementData) -> str:
    if requirement["type"] == "and" and len(requirement["data"]["items"]) == 0:
        return "None"
    if requirement["type"] == "or" and len(requirement["data"]["items"]) == 0:
        return "lambda _: False"
    if requirement["type"] == "template":
        return f"templates['{requirement['data']}']"
    return f"lambda logic: {parse_connection_data_helper(requirement)}"

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

with open("../Extracted.py", "w") as f:
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