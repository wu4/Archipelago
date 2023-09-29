from typing import TypedDict, Union, Literal, Optional, TypeAlias


class Vector3(TypedDict):
    x: float
    y: float
    z: float


DockType: TypeAlias = Literal[
    "door",
    "teleporter",
    "Teleporter",
    "morph_ball",
    "Missile Blast Shield",
    "Morph Ball Door",
    "Normal Door",
    "Ice Door",
    "Wave Door",
    "Plasma Door",
    "other",
    "Open Passage",
    "Closed Passage",
    "Permanently Locked",
    "Circular Door",
    "Square Door",
]


class Template(TypedDict):
    type: Literal["template"]
    data: str


class LogicData(TypedDict):
    comment: Optional[str]
    items: list["RequirementData"]


class Logic(TypedDict):
    type: Literal["and", "or"]
    data: LogicData


class ResourceData(TypedDict):
    type: Literal["items", "tricks", "damage", "events", "misc"]
    name: str
    amount: int
    negate: bool


class Resource(TypedDict):
    type: Literal["resource"]
    data: ResourceData


RequirementData: TypeAlias = Union[Template, Logic, Resource]


class EventNode(TypedDict):
    node_type: Literal["event"]

    heal: Literal[False]
    coordinates: Optional[Vector3]
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: Literal[False]
    connections: dict[str, RequirementData]

    event_name: str


class GenericNode(TypedDict):
    node_type: Literal["generic"]

    heal: bool
    coordinates: None
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: bool
    connections: dict[str, RequirementData]


class PickupNode(TypedDict):
    node_type: Literal["pickup"]

    heal: bool
    coordinates: None
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: Literal[False]
    connections: dict[str, RequirementData]

    pickup_index: int
    location_category: Literal["major", "minor"]


class AbsoluteLocation(TypedDict):
    region: str
    area: str
    node: str


class DockNode(TypedDict):
    node_type: Literal["dock"]

    heal: bool
    coordinates: Optional[Vector3]
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: bool
    connections: dict[str, RequirementData]

    dock_type: DockType
    default_connection: AbsoluteLocation
    default_dock_weakness: DockType
    exclude_from_dock_rando: bool
    incompatible_dock_weaknesses: list
    override_default_open_requirement: None
    override_default_lock_requirement: None


Node: TypeAlias = Union[PickupNode, GenericNode, EventNode, DockNode]


class Area(TypedDict):
    default_node: str
    extra: Optional[dict]
    nodes: dict[str, Node]

class Region(TypedDict):
    name: str
    areas: dict[str, Area]


class ItemDataExtra(TypedDict):
    item_id: int

class ItemData(TypedDict):
    long_name: str
    max_capacity: int
    extra: ItemDataExtra

class EventData(TypedDict):
    long_name: str
    extra: dict
    
class TrickData(TypedDict):
    long_name: str
    description: str
    extra: dict
    
class DamageData(TypedDict):
    long_name: str
    extra: dict
    
class VersionData(TypedDict):
    long_name: str
    extra: dict

class MiscData(TypedDict):
    long_name: str
    extra: dict
    
class DamageReductionEntry(TypedDict):
    name: str
    multiplier: float

class DamageReductionData(TypedDict):
    name: str
    reductions: list[DamageReductionEntry]

class ResourceDatabase(TypedDict):
    items: dict[str, ItemData]
    events: dict[str, EventData]
    tricks: dict[str, TrickData]
    damage: dict[str, DamageData]
    versions: dict[str, VersionData]
    misc: dict[str, MiscData]
    requirement_template: dict[str, RequirementData]
    damage_reductions: list[DamageReductionData]
    energy_tank_item_index: str
    
    
class DockWeaknessExtra(TypedDict):
    shieldType: str
    
class DockWeaknessLock(TypedDict):
    lock_type: str
    requirement: RequirementData

class DockWeaknessEntry(TypedDict):
    requirement: RequirementData
    lock: Optional[DockWeaknessLock]
    extra: DockWeaknessExtra

class DockWeaknessCategory(TypedDict):
    name: str
    extra: dict
    items: dict[str, DockWeaknessEntry]

class DockWeaknessDatabase(TypedDict):
    types: dict[str, DockWeaknessCategory]
    default_weakness: dict
    dock_rando: dict

class Header(TypedDict):
    schema_version: int
    game: str
    resource_database: ResourceDatabase
    layers: list[str]
    starting_location: AbsoluteLocation
    initial_states: dict[str, list]
    minimal_logic: dict
    victory_condition: RequirementData
    dock_weakness_database: DockWeaknessDatabase
    used_trick_levels: dict[str, list[int]]
    regions: list[str]