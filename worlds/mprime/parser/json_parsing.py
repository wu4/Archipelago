from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import orjson

from .connection_requirements import parse_connection_requirements
from .util import relative_to_file

from . import Types as DataTypes


def is_event_skippable(event_name: str) -> bool:
    return event_name in ["Observatory Activated", "Control Tower Fight"]

VALIDATE = False

def load_header(header_filename: str) -> DataTypes.Header:
    with open(header_filename, "r") as f:
        return orjson.loads(f.read())

def load_region_json(header_filename: str, region_filename: str) -> DataTypes.Region:
    with open(relative_to_file(header_filename, region_filename), 'rt') as f:
        json_data = orjson.loads(f.read())
    if VALIDATE:
        from . import Schema
        Schema.Region.validate(json_data)
    return json_data

def get_dock_requirements(dock: DataTypes.DockWeaknessEntry) -> DataTypes.RequirementData:
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
        
from .util import LocationTuple, absolute_location_tuple_format, as_location_tuple

ConnectionsDict = dict[LocationTuple, DataTypes.RequirementData]
NestedConnectionsDict = dict[LocationTuple, ConnectionsDict]

@dataclass
class NodeInfo:
    pickup: bool
    items_every_room: bool
    unskippable_event: bool
    heal: bool

    event_name: Optional[str]
    
    def __init__(self, data: RandovaniaData, node: DataTypes.Node) -> None:
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

    def add(self, from_key: LocationTuple, to_key: LocationTuple, rule: DataTypes.RequirementData):
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
    header: DataTypes.Header
    regions: dict[str, DataTypes.Region]

    items_short_to_long: dict[str, str]
    items: list[str]
    events_short_to_long: dict[str, str]
    tricks_short_to_long: dict[str, str]
    dock_requirements: dict[str, DataTypes.RequirementData]
    template_lines: list[str]
    damage_resistances: dict[str, dict[str, float]]

    connections: ConnectionData

    rules: dict[LocationTuple, dict[LocationTuple, str]]
    
    node_info: dict[LocationTuple, NodeInfo]

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

    def init_items_and_tricks(self):
        self.items_short_to_long = {
            short_name: item["long_name"]
            for short_name, item in self.header["resource_database"]["items"].items()
            if not short_name in ["LockedPB", "LockedMissile", "Unknown1", "Unknown2", "HealthRefill"]
        }

        self.items = list(self.items_short_to_long.values())

        self.tricks_short_to_long = {
            short: trick["long_name"]
            for short, trick in self.header["resource_database"]["tricks"].items()
        }
    
    def get_node(self, loc: LocationTuple) -> DataTypes.Node:
        return self.regions[loc[2]]["areas"][loc[1]]["nodes"][loc[0]]

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

        self.init_items_and_tricks()

        self.combine_bilinear_paths()

        self.rules = {
            from_loc: {
                to_loc: parse_connection_requirements(self, rule)
                for to_loc, rule in to_locs.items()
            }
            for from_loc, to_locs in self.connections.outgoing.items()
        }
        
        # def deep_search_template_calls(req: DataTypes.RequirementData) -> set[str]:
        #     accum: set[str] = set()
        #     if req["type"] == "and" or req["type"] == "or":
        #         for names_set in map(deep_search_template_calls, req["data"]["items"]):
        #             accum.update(names_set)
        #     elif req["type"] == "template":
        #         accum.add(req["data"])
        #     return accum

        # template_requirements = list(self.header["resource_database"]["requirement_template"].values())
        # 
        # template_dependencies: dict[str, set[str]] = {
        #     template_name: deep_search_template_calls(req)
        #     for template_name, req in self.header["resource_database"]["requirement_template"].items()
        # }

        # template_builder: list[list[tuple[str, str]]] = []

        # reqs: set[str] = set()
        # reqs.update(self.header["resource_database"]["requirement_template"].keys())

        #     
        header_templates = self.header["resource_database"]["requirement_template"]

        # passn = 0
        # while len(reqs) > 0:
        #     passn += 1
        #     tmp: list[tuple[str, str]] = []
        #     queue_remove: set[str] = set()
        #     for template_name in reqs:
        #         if not template_dependencies[template_name].isdisjoint(reqs): continue
        #         tmp.append((template_name, parse_connection_requirements(self, header_templates[template_name], True)))
        #         queue_remove.add(template_name)
        #         
        #     template_builder.append(tmp)

        #     reqs.difference_update(queue_remove)
        #     
        # def build_templates(template_tpl: tuple[int, list[tuple[str, str]]]) -> str:
        #     (i, templates) = template_tpl
        #     string_builder = []
        #     if i == 0:
        #         string_builder.append("t={")                
        #     else:
        #         string_builder.append("t.update({")

        #     for template_name, template in templates:
        #         string_builder.append(f"'{template_name}': {template},")

        #     if i == 0:
        #         string_builder.append("}")
        #     else:
        #         string_builder.append("})")
        #     
        #     return ''.join(string_builder)

        # self.template_lines = list(map(build_templates, enumerate(template_builder)))
        self.templates = {
            template_name: parse_connection_requirements(self, reqs)
            for template_name, reqs in header_templates.items()
        }

        self.damage_resistances = {
            item["name"]: {i["name"]: i["multiplier"] for i in item["reductions"]}
            for item in self.header["resource_database"]["damage_reductions"]
        }

    def combine_bilinear_paths(self):
        from itertools import pairwise
        from .node_visitor import get_unnecessary_connection_chains
        
        for (from_loc, to_loc), inbetween_locs in get_unnecessary_connection_chains(self, self.node_info).items():
            inbetween_locs.insert(0, from_loc)
            inbetween_locs.append(to_loc)
            
            forward_reqs: list[DataTypes.RequirementData] = []
            backward_reqs: list[DataTypes.RequirementData] = []
            for loc, next_loc in pairwise(inbetween_locs):
                forward_reqs.append(self.connections.pop(loc, next_loc))
                backward_reqs.append(self.connections.pop(next_loc, loc))

            forward_req: DataTypes.Logic = {
                "type": "and",
                "data": {
                    "comment": None,
                    "items": forward_reqs
                }
            }
            backward_req: DataTypes.Logic = {
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