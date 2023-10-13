from typing import TypedDict, Literal, Optional, TypeAlias
from .shared import AbsoluteLocation, Vector3
from .requirement import Requirement

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



class EventNode(TypedDict):
    node_type: Literal["event"]

    heal: Literal[False]
    coordinates: Optional[Vector3]
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: Literal[False]
    connections: dict[str, Requirement]

    event_name: str


class GenericNode(TypedDict):
    node_type: Literal["generic"]

    heal: bool
    coordinates: None
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: bool
    connections: dict[str, Requirement]


class PickupNode(TypedDict):
    node_type: Literal["pickup"]

    heal: bool
    coordinates: None
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: Literal[False]
    connections: dict[str, Requirement]

    pickup_index: int
    location_category: Literal["major", "minor"]



class DockNode(TypedDict):
    node_type: Literal["dock"]

    heal: bool
    coordinates: Optional[Vector3]
    description: str
    layers: list[str]
    extra: dict
    valid_starting_location: bool
    connections: dict[str, Requirement]

    dock_type: DockType
    default_connection: AbsoluteLocation
    default_dock_weakness: DockType
    exclude_from_dock_rando: bool
    incompatible_dock_weaknesses: list
    override_default_open_requirement: None
    override_default_lock_requirement: None


Node: TypeAlias = PickupNode | GenericNode | EventNode | DockNode


class Area(TypedDict):
    default_node: str
    extra: Optional[dict]
    nodes: dict[str, Node]

class Region(TypedDict):
    name: str
    areas: dict[str, Area]