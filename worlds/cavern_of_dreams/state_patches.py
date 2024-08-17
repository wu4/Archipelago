from collections import Counter
from collections.abc import Generator
from ..AutoWorld import AutoLogicRegister
from .ap_generated.data import carryable_locations
import copy

import typing
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from BaseClasses import CollectionState, Region, Entrance, PathValue, MultiWorld
    from .regions import CavernOfDreamsRegion, CavernOfDreamsEntrance
    from .types import MaybeTempItem, TempItem

# carryables + overrides
def add_region_entries(state: "CollectionState", carryable_region_name: str, player: int):
    state._cavernofdreams_reachable_regions.setdefault(carryable_region_name, {}).setdefault(player, set())
    state._cavernofdreams_blocked_connections.setdefault(carryable_region_name, {}).setdefault(player, set())

def get_reachable_regions(state: "CollectionState", carryable_region_name: str, player: int) -> set["CavernOfDreamsRegion"]:
    return state._cavernofdreams_reachable_regions[carryable_region_name][player]

def get_blocked_connections(state: "CollectionState", carryable_region_name: str, player: int) -> set["CavernOfDreamsEntrance"]:
    return state._cavernofdreams_blocked_connections[carryable_region_name][player]

def add_carryable_source(state: "CollectionState", player: int, region: "Region", carryable: "TempItem"):
    # print(f"adding {region}, {carryable}")
    state._cavernofdreams_carryable_sources[player][region.name, carryable] += 1

def remove_carryable_source(state: "CollectionState", player: int, region: "Region", carryable: "TempItem"):
    state._cavernofdreams_carryable_sources[player][region.name, carryable] -= 1

def get_carryable_sources(state: "CollectionState", player: int) -> Generator[tuple[str, "TempItem"], typing.Any, None]:
    sources = state._cavernofdreams_carryable_sources[player]
    for contained in sources:
        if sources[contained] <= 0: continue
        yield contained

# path generation
def get_current_start_region(state: "CollectionState", player: int) -> "Region":
    csr = state._cavernofdreams_current_start_region[player]
    if csr is None:
        return state.multiworld.get_region("Menu", player)
    return csr

def set_current_start_region(state: "CollectionState", player: int, region: "Region"):
    state._cavernofdreams_current_start_region[player] = region

def get_all_paths(state: "CollectionState", player: int) -> dict["Region", dict["Region | Entrance", "PathValue"]]:
    return state._cavernofdreams_paths[player]

def get_current_paths(state: "CollectionState", player: int) -> dict["Region | Entrance", "PathValue"]:
    return get_all_paths(state, player)[get_current_start_region(state, player)]

def add_entrance_path_node(entrance: "Entrance", state: "CollectionState", paths: dict["Region | Entrance", "PathValue"]):
    if not entrance in paths:
        paths[entrance] = (entrance.name, paths.get(entrance.parent_region, (entrance.parent_region.name, None)))

def add_region_path_node(region: "Region", connection: "Entrance", state: "CollectionState"):
    current_paths = get_current_paths(state, region.player)
    current_paths[region] = (region.name, current_paths.get(connection, None))

class CavernOfDreamsCollectionState(metaclass=AutoLogicRegister):
    # this is kludge to make typing work correctly
    # AutoLogicRegister ignores it
    def __init__(self):
        super().__init__()
        self._cavernofdreams_player_ids: tuple[int, ...] = ()
        self._cavernofdreams_reachable_regions: dict[str, dict[int, set[Region]]] = {}
        self._cavernofdreams_blocked_connections: dict[str, dict[int, set[Entrance]]] = {}
        self._cavernofdreams_carryable_sources: dict[int, Counter[tuple[str, "TempItem"]]] = {}
        self._cavernofdreams_current_start_region: dict[int, Region] = {}
        self._cavernofdreams_paths: dict[int, dict[Region, dict[Region | Entrance, PathValue]]] = {}

    def _cavernofdreams_has_shrooms_for(self, player: int, fella: str) -> bool:
        if fella == "Lake":
            shrooms = 40
        elif fella == "Monster":
            shrooms = 40 + 60
        elif fella == "Palace":
            shrooms = 40 + 60 + 80
        elif fella == "Gallery":
            shrooms = 40 + 60 + 80 + 100
        else:
            raise ValueError(f"invalid fella {fella}")
        return self.has("Shroom", player, shrooms)

    def init_mixin(self, parent: "MultiWorld"):
        # avoids circular imports
        from .world import CavernOfDreamsWorld
        game = CavernOfDreamsWorld.game

        cod_ids = parent.get_game_players(game) + parent.get_game_groups(game)
        self._cavernofdreams_player_ids = cod_ids

        reachable = {}
        blocked = {}
        for event_and_location_name in carryable_locations.keys():
            reachable[event_and_location_name] = {player: set() for player in cod_ids}
            blocked[event_and_location_name] = {player: set() for player in cod_ids}
        self._cavernofdreams_reachable_regions = reachable
        self._cavernofdreams_blocked_connections = blocked
        self._cavernofdreams_carryable_sources = {player: Counter() for player in cod_ids}
        self._cavernofdreams_current_start_region = {player: None for player in cod_ids}
        self._cavernofdreams_paths = {player: {} for player in cod_ids}

    def copy_mixin(self, ret: "CavernOfDreamsCollectionState") -> "CavernOfDreamsCollectionState":
        cod_ids = self._cavernofdreams_player_ids
        ret._cavernofdreams_player_ids = cod_ids

        reachable = {}
        for event_and_location_name, regions_by_player in self._cavernofdreams_reachable_regions.items():
            reachable[event_and_location_name] = {}
            for player in cod_ids:
                if (player_reachable := regions_by_player.get(player)) is None: continue
                reachable[event_and_location_name][player] = copy.copy(player_reachable)
        ret._cavernofdreams_reachable_regions = reachable

        blocked = {}
        for event_and_location_name, entrances_by_player in self._cavernofdreams_blocked_connections.items():
            blocked[event_and_location_name] = {}
            for player in cod_ids:
                if (player_blocked := entrances_by_player.get(player)) is None: continue
                blocked[event_and_location_name][player] = copy.copy(player_blocked)
        ret._cavernofdreams_blocked_connections = blocked

        ret._cavernofdreams_carryable_sources = {
            player: copy.copy(self._cavernofdreams_carryable_sources[player])
            for player in cod_ids
        }

        # NOTE: may need a deeper copy?
        ret._cavernofdreams_paths = {player: copy.copy(self._cavernofdreams_paths[player]) for player in cod_ids}

        ret._cavernofdreams_current_start_region = {player: self._cavernofdreams_current_start_region[player] for player in cod_ids}

        return ret
