from __future__ import annotations
from dataclasses import dataclass
from typing import TYPE_CHECKING, cast, Optional, Literal
import orjson

from .connection_requirements import parse_connection_requirements
from .util import relative_to_file, absolute_node_format, absolute_location_format

if TYPE_CHECKING:
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

def parse_dock_requirements(data: RandovaniaData, dock: DataTypes.DockWeaknessEntry) -> Optional[str]:
    lock = dock["lock"]
    if lock is None:
        return parse_connection_requirements(data, dock["requirement"], True)
    else:
        return parse_connection_requirements(data, {
            "type": "and",
            "data": {
                "comment": None,
                "items": [dock["requirement"], lock["requirement"]]
            }
        }, True)

@dataclass
class RegionInfo:
    has_location: Optional[Literal["pickup", "event", "items_every_room"]]
    event_name: Optional[str]
    event_skippable: Optional[bool]
    connections: list[tuple[str, str]]
    dock_connection: Optional[tuple[str, str]]
    
    def __init__(self, data: RandovaniaData, node: DataTypes.Node, area_name: str, region_name: str) -> None:
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
                self.event_name = data.events_short_to_long[node["event_name"]]
                self.event_skippable = is_event_skippable(self.event_name)

        if node["node_type"] == "dock":
            rule = data.dock_requirements[node["default_dock_weakness"]]
            if rule is not None:
                self.dock_connection = (absolute_location_format(node["default_connection"]), f"e(dock_requirements['{node['default_dock_weakness']}'])")
        
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
            (absolute_node_format(node_connection_name, area_name, region_name), parse_connection_requirements(data, requirements))
            for node_connection_name, requirements in node["connections"].items()
        ]

class RandovaniaData:
    header: DataTypes.Header
    regions: list[DataTypes.Region]

    items_short_to_long: dict[str, str]
    items: list[str]
    events_short_to_long: dict[str, str]
    tricks_short_to_long: dict[str, str]
    dock_requirements: dict[str, Optional[str]]
    rules: list[tuple[str, RegionInfo]]
    template_lines: list[str]
    damage_resistances: dict[str, dict[str, float]]
    
    def __init__(self, header_filename: str) -> None:
        self.header = load_header(header_filename)
        self.regions = [
            load_region_json(header_filename, region_filename)
            for region_filename in self.header["regions"]
            if region_filename not in ["Frigate Orpheon.json"]
        ]

        self.items_short_to_long = {
            short_name: item["long_name"]
            for short_name, item in self.header["resource_database"]["items"].items()
            if not short_name in ["LockedPB", "LockedMissile", "Unknown1", "Unknown2", "HealthRefill"]
        }

        self.items = list(self.items_short_to_long.values())

        self.events_short_to_long = {
          short_name: event["long_name"]
          for short_name, event in self.header["resource_database"]["events"].items()
        }

        self.tricks_short_to_long = {
            short: trick["long_name"]
            for short, trick in self.header["resource_database"]["tricks"].items()
        }

        self.dock_requirements = {
            dock_type: parse_dock_requirements(self, item)
            for docks in self.header["dock_weakness_database"]["types"].values()
            for dock_type, item in docks["items"].items()
        }

        self.rules = [
            (absolute_node_format(node_name, area_name, region["name"]), RegionInfo(self, node, area_name, region["name"]))
            for region in self.regions
            for area_name, area in region["areas"].items()
            for node_name, node in area["nodes"].items()
        ]
        
        def deep_search_template_calls(req: DataTypes.RequirementData) -> set[str]:
            accum: set[str] = set()
            if req["type"] == "and" or req["type"] == "or":
                for names_set in map(deep_search_template_calls, req["data"]["items"]):
                    accum.update(names_set)
            elif req["type"] == "template":
                accum.add(req["data"])
            return accum

        template_requirements = list(self.header["resource_database"]["requirement_template"].values())
        
        template_dependencies: dict[str, set[str]] = {
            template_name: deep_search_template_calls(req)
            for template_name, req in self.header["resource_database"]["requirement_template"].items()
        }

        template_builder: list[list[tuple[str, str]]] = []

        reqs: set[str] = set()
        reqs.update(self.header["resource_database"]["requirement_template"].keys())
            
        header_templates = self.header["resource_database"]["requirement_template"]

        passn = 0
        while len(reqs) > 0:
            passn += 1
            tmp: list[tuple[str, str]] = []
            queue_remove: set[str] = set()
            for template_name in reqs:
                if not template_dependencies[template_name].isdisjoint(reqs): continue
                tmp.append((template_name, parse_connection_requirements(self, header_templates[template_name], True)))
                queue_remove.add(template_name)
                
            template_builder.append(tmp)

            reqs.difference_update(queue_remove)
            
        def build_templates(template_tpl: tuple[int, list[tuple[str, str]]]) -> str:
            (i, templates) = template_tpl
            string_builder = []
            if i == 0:
                string_builder.append("t={")
            else:
                string_builder.append("t.update({")

            for template_name, template in templates:
                string_builder.append(f"'{template_name}': {template},")

            if i == 0:
                string_builder.append("}")
            else:
                string_builder.append("})")
            
            return ''.join(string_builder)

        self.template_lines = list(map(build_templates, enumerate(template_builder)))

        self.damage_resistances = {
            item["name"]: {i["name"]: i["multiplier"] for i in item["reductions"]}
            for item in self.header["resource_database"]["damage_reductions"]
        }