from typing import TypedDict, Optional
from .shared import AbsoluteLocation
from .requirement import Requirement


class ItemExtra(TypedDict):
    item_id: int

class Item(TypedDict):
    long_name: str
    max_capacity: int
    extra: ItemExtra

class Event(TypedDict):
    long_name: str
    extra: dict
    
class Trick(TypedDict):
    long_name: str
    description: str
    extra: dict
    
class Damage(TypedDict):
    long_name: str
    extra: dict
    
class Version(TypedDict):
    long_name: str
    extra: dict

class Misc(TypedDict):
    long_name: str
    extra: dict
    
class DamageReduction(TypedDict):
    name: str
    multiplier: float

class DamageReductions(TypedDict):
    name: str
    reductions: list[DamageReduction]

class ResourceDatabase(TypedDict):
    items: dict[str, Item]
    events: dict[str, Event]
    tricks: dict[str, Trick]
    damage: dict[str, Damage]
    versions: dict[str, Version]
    misc: dict[str, Misc]
    requirement_template: dict[str, Requirement]
    damage_reductions: list[DamageReductions]
    energy_tank_item_index: str
    
    
class DockWeaknessExtra(TypedDict):
    shieldType: str
    
class DockWeaknessLock(TypedDict):
    lock_type: str
    requirement: Requirement

class DockWeaknessEntry(TypedDict):
    requirement: Requirement
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
    victory_condition: Requirement
    dock_weakness_database: DockWeaknessDatabase
    used_trick_levels: dict[str, list[int]]
    regions: list[str]