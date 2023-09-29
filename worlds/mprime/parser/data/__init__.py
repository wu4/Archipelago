from __future__ import annotations

import json
from typing import cast, Callable, Protocol, TYPE_CHECKING

from BaseClasses import MultiWorld

from Options import Range, AssembleOptions
from ..Utils import map_dict, region_format, get_underscored, relative_to_script

from . import Types as DataTypes

if TYPE_CHECKING:
    from ..Logic import MetroidPrimeLogic

CheckFunc = Callable[["MetroidPrimeLogic"], bool]
CheckFuncFactory = Callable[[int], CheckFunc]

ParsedArea = dict[str, "Node"]
ParsedRegion = dict[str, ParsedArea]


HEADER_FILENAME: str = "randovania_data/json_data/header.json"

class Node:
    connections: dict[str, CheckFuncFactory]
    layers: list[str]

    def __init__(self, node: DataTypes.Node) -> None:
        self.layers = node["layers"]

        self.connections = dict((k, _parse_connection_data(v)) for (k, v) in node["connections"].items())


class DockNode(Node):
    default_connection_rule: CheckFuncFactory
    default_connection: DataTypes.AbsoluteLocation

    def __init__(self, node: DataTypes.DockNode) -> None:
        super().__init__(node)
        rule = dock_category_requirements.get(node["default_dock_weakness"])
        if rule is None:
            rule = dock_requirements.get(node["default_dock_weakness"])
            if rule is None:
                raise ValueError(f"unknown dock type {node['default_dock_weakness']}")
        self.default_connection_rule = rule
        self.default_connection = node["default_connection"]


class PickupNode(Node):
    id: int
    progression: bool

    def __init__(self, node: DataTypes.PickupNode) -> None:
        super().__init__(node)
        self.id = node["pickup_index"]
        self.progression = node["location_category"] == "major"


class EventNode(Node):
    event_name: str

    def __init__(self, node: DataTypes.EventNode) -> None:
        super().__init__(node)
        self.event_name = node["event_name"]

###########
# PARSING #
###########


def _parse_node(node: DataTypes.Node) -> Node:
    new_node: Node

    if node["node_type"] == "dock":
        new_node = DockNode(node)
    elif node["node_type"] == "pickup":
        new_node = PickupNode(node)
    elif node["node_type"] == "event":
        new_node = EventNode(node)
    elif node["node_type"] == "generic":
        new_node = Node(node)
    else:
        raise ValueError(f"unknown node type {node['node_type']}")

    return new_node


def _parse_area(area: DataTypes.Area) -> ParsedArea:
    return map_dict(_parse_node, area["nodes"])


def _parse_region(region: DataTypes.Region) -> ParsedRegion:
    return map_dict(_parse_area, region["areas"])


def _parse_connection_data(connection_data: DataTypes.RequirementData) -> CheckFuncFactory:
    if connection_data["type"] == "and" or connection_data["type"] == "or":
        if len(connection_data["data"]["items"]) == 0:
            return lambda _: lambda _: True
        logic_func = all if connection_data["type"] == "and" else any
        funcs = list(map(_parse_connection_data, connection_data["data"]["items"]))
        return lambda player: lambda logic: logic_func(map(lambda f: f(player)(logic), funcs))

    if connection_data["type"] == "template":
        # since some templates contain other templates, we have to dynamically call them
        return lambda player: lambda logic: templates[connection_data["data"]](player)(logic)

    if connection_data["type"] == "resource":
        data = connection_data["data"]
        # if data["type"] == "tricks":
        #       print("trick:", data["name"])
        # elif data["type"] == "misc":
        #       print("misc:", data["name"])
        return lambda player: lambda logic: data["negate"] != logic.metroid_prime_has_resource(player, data)

    raise IndexError("Unknown connection data type {}".format(connection_data["type"]))


########
# INIT #
########

VALIDATE: bool = False

def _get_header() -> DataTypes.Header:
    with open(relative_to_script(__file__, HEADER_FILENAME), "r") as f:
        return json.load(f)

header = _get_header()

damage_resistances: dict[str, dict[str, float]] = {
    item["name"]: {i["name"]: i["multiplier"] for i in item["reductions"]}
    for item in header["resource_database"]["damage_reductions"]
}

templates: dict[str, CheckFuncFactory] = {
    template_name: _parse_connection_data(template)
    for template_name, template in header["resource_database"]["requirement_template"].items()
}

options = cast(dict[str, AssembleOptions], {
    get_underscored(f"metroid_prime_{trick_name}"): type(
        trick_name, (Range,), {
            "display_name": trick_data["long_name"],
            "__doc__": trick_data["description"],
            "range_start": 0,
            "range_end": 5,
            "default": 0
        }
    ) for trick_name, trick_data in header["resource_database"]["tricks"].items()
})

dock_requirements: dict[str, CheckFuncFactory] = {}
dock_category_requirements: dict[str, CheckFuncFactory] = {}

for dock_category, docks in header["dock_weakness_database"]["types"].items():
    parsed_docks: list[CheckFuncFactory] = []

    for (name, item) in docks["items"].items():
        parsed = _parse_connection_data(item["requirement"])
        parsed_docks.append(parsed)
        dock_requirements[name] = parsed

    dock_category_requirements[dock_category] = lambda player: lambda logic: any(map(lambda x: x(player)(logic), parsed_docks))

def _load_region_json(region_filename):
    with open(relative_to_script(__file__, f"randovania_data/json_data/{region_filename}"), 'rt') as f:
        json_data = json.load(f)
        if VALIDATE:
            from . import Schema
            Schema.Region.validate(json_data)
    return json_data

regions: dict[str, ParsedRegion] = {
    json_data["name"]: _parse_region(json_data)
    for json_data in map(_load_region_json, header["regions"])
}
