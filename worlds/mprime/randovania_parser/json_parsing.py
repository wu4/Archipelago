from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import orjson

from .types.header import Header, DockWeaknessEntry
from .types.region import Region, Node
from .types.requirement import Requirement, Logic

from .connection_requirements import parse_connection_requirements
from .parser_utils import relative_to_file, LocationTuple, as_location_tuple


def is_event_skippable(event_name: str) -> bool:
    return event_name in ["Observatory Activated", "Control Tower Fight"]

def load_header(header_filename: str) -> Header:
    with open(header_filename, "r") as f:
        return orjson.loads(f.read())

def load_region_json(header_filename: str, region_filename: str) -> Region:
    with open(relative_to_file(header_filename, region_filename), 'rt') as f:
        json_data = orjson.loads(f.read())
    return json_data

def get_dock_requirements(dock: DockWeaknessEntry) -> Requirement:
    lock = dock["lock"]
    if lock is None:
        return dock["requirement"]
    else:
        return {
            "type": "and",
            "data": {
                "comment": None,
                "items": [dock["requirement"], lock["requirement"]]
            }
        }

ConnectionsDict = dict[LocationTuple, Requirement]
NestedConnectionsDict = dict[LocationTuple, ConnectionsDict]

@dataclass
class NodeInfo:
    pickup: bool
    items_every_room: bool
    unskippable_event: bool
    heal: bool

    event_name: Optional[str]

    def __init__(self, data: RandovaniaData, node: Node) -> None:
        self.pickup = False
        self.items_every_room = False
        self.unskippable_event = False
        self.heal = False

        self.event_name = None

        if node["node_type"] == "pickup":
            self.pickup = True

            if "items_every_room" in node["layers"]:
                self.items_every_room = True

        if node["heal"]:
            self.heal = True

        if node["node_type"] == "event":
            self.event_name = data.events_short_to_long[node["event_name"]]
            if not is_event_skippable(self.event_name):
                self.unskippable_event = True

    def is_important(self) -> bool:
        return self.pickup or self.unskippable_event or self.heal

def same_region_and_area(loc: LocationTuple, loc2: LocationTuple) -> bool:
    return (loc[1], loc[2]) == (loc2[1], loc2[2])

class ConnectionData:
    incoming: NestedConnectionsDict
    outgoing: NestedConnectionsDict

    def __init__(self) -> None:
        self.incoming = {}
        self.outgoing = {}

    def add(self, from_key: LocationTuple, to_key: LocationTuple, rule: Requirement):
        self.outgoing.setdefault(from_key, {})[to_key] = rule
        self.incoming.setdefault(to_key, {})[from_key] = rule

    def pop(self, from_key: LocationTuple, to_key: LocationTuple):
        ret = self.outgoing[from_key].pop(to_key)
        # del self.incoming[to_key][from_key]
        if len(self.outgoing[from_key]) == 0:
            del self.outgoing[from_key]
            # del self.incoming[to_key]
        return ret

class RandovaniaData:
    header: Header
    regions: dict[str, Region]

    items_short_to_long: dict[str, str]
    items: list[str]
    events_short_to_long: dict[str, str]
    tricks_short_to_long: dict[str, str]
    dock_requirements: dict[str, Requirement]
    template_lines: list[str]
    damage_resistances: dict[str, dict[str, float]]

    connections: ConnectionData

    rules: dict[LocationTuple, dict[LocationTuple, str]]

    node_info: dict[LocationTuple, NodeInfo]

    def __init__(self, header_filename: str) -> None:
        self.header = load_header(header_filename)
        self.regions = {}
        for region_filename in self.header["regions"]:
            if region_filename in ["Frigate Orpheon.json"]: continue
            region = load_region_json(header_filename, region_filename)
            self.regions[region["name"]] = region

        self.dock_requirements = {
            dock_type: get_dock_requirements(item)
            for docks in self.header["dock_weakness_database"]["types"].values()
            for dock_type, item in docks["items"].items()
        }

        self.events_short_to_long = {
          short_name: event["long_name"]
          for short_name, event in self.header["resource_database"]["events"].items()
        }

        self.init_nodes_and_connections()
        self.init_items()
        self.init_tricks()

        self.combine_bilinear_paths()

        self.rules = {}
        for from_loc, to_locs in self.connections.outgoing.items():
            d: dict[LocationTuple, str] = {}
            is_empty: bool = True
            for to_loc, rule_data in to_locs.items():
                rule = parse_connection_requirements(self, rule_data)

                if rule == False: continue

                if rule == True:
                    is_empty = False
                    d[to_loc] = "None"
                else:
                    is_empty = False
                    d[to_loc] = rule
            if not is_empty:
                self.rules[from_loc] = d

        self.templates = {
            template_name: parse_connection_requirements(self, reqs)
            for template_name, reqs in self.header["resource_database"]["requirement_template"].items()
        }

        self.damage_resistances = {
            item["name"]: {i["name"]: i["multiplier"] for i in item["reductions"]}
            for item in self.header["resource_database"]["damage_reductions"]
        }

    def get_node(self, loc: LocationTuple) -> Node:
        return self.regions[loc[2]]["areas"][loc[1]]["nodes"][loc[0]]

    def combine_bilinear_paths(self):
        from itertools import pairwise
        from .connection_chains import get_unnecessary_connection_chains

        for (from_loc, to_loc), inbetween_locs in get_unnecessary_connection_chains(self, self.node_info).items():
            inbetween_locs.insert(0, from_loc)
            inbetween_locs.append(to_loc)

            forward_reqs: list[Requirement] = []
            backward_reqs: list[Requirement] = []
            for loc, next_loc in pairwise(inbetween_locs):
                forward_reqs.append(self.connections.pop(loc, next_loc))
                backward_reqs.append(self.connections.pop(next_loc, loc))

            forward_req: Logic = {
                "type": "and",
                "data": {
                    "comment": None,
                    "items": forward_reqs
                }
            }

            backward_req: Logic = {
                "type": "and",
                "data": {
                    "comment": None,
                    "items": backward_reqs
                }
            }

            self.connections.add(from_loc, to_loc, forward_req)
            self.connections.add(to_loc, from_loc, backward_req)

            inbetween_locs.pop(0)
            inbetween_locs.pop()

            for rem in inbetween_locs:
                del self.node_info[rem]

    def init_nodes_and_connections(self):
        self.connections = ConnectionData()

        self.node_info = {}

        for region_name, region in self.regions.items():
            for area_name, area in region["areas"].items():
                for node_name, node in area["nodes"].items():
                    from_key = (node_name, area_name, region_name)
                    self.node_info[from_key] = NodeInfo(self, node)

                    for to_node_name, rule in node["connections"].items():
                        to_key = (to_node_name, area_name, region_name)
                        self.connections.add(from_key, to_key, rule)

                    if node["node_type"] == "dock":
                        rule = self.dock_requirements[node["default_dock_weakness"]]
                        if rule is not None:
                            to_key = as_location_tuple(node["default_connection"])
                            self.connections.add(from_key, to_key, rule)

    def init_items(self):
        self.items_short_to_long = {
            short_name: item["long_name"]
            for short_name, item in self.header["resource_database"]["items"].items()
            if not short_name in ["LockedPB", "LockedMissile", "Unknown1", "Unknown2", "HealthRefill"]
        }

        self.items = list(self.items_short_to_long.values())

    def init_tricks(self):
        self.tricks_short_to_long = {
            short: trick["long_name"]
            for short, trick in self.header["resource_database"]["tricks"].items()
        }