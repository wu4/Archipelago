from __future__ import annotations
from collections.abc import Iterator

from BaseClasses import Location, PathValue, Region, Entrance, CollectionState, MultiWorld
from ..AutoWorld import AutoLogicRegister
from .ap_generated.data import carryable_locations

import copy
from collections import deque
from typing import Literal, TypeAlias, override

TempItem: TypeAlias = Literal[
    "Apple",
    "Medicine",
    "Bubble Conch",
    "Sage's Gloves",
    "Lady Opal's Head",
    "Shelnert's Fish",
    "Mr. Kerrington's Wings",

    "Jester Boots"
]


class CavernOfDreamsLocation(Location):
    game = "Cavern of Dreams"

    @override
    def can_reach(self, state: CollectionState) -> bool:
        # normally, we test access rule first for speed
        # but we cant afford that luxury here
        assert self.parent_region, "Can't reach location without region"

        if not self.parent_region.can_reach(state):
            return False

        if self.access_rule(state):
            return True

        cars = _get_reachable_carryables(state, self.player)
        for carryable_region_name in cars:
            carryable_region = state.multiworld.get_region(carryable_region_name, self.player)
            # assert isinstance(carryable_region, CavernOfDreamsCarryableRegion)
            if self.parent_region in _get_reachable_regions(state, carryable_region_name, self.player):
                _set_carryable(state, self.player, carryable_region.carryable)
                if self.access_rule(state):
                    _set_carryable(state, self.player, None)
                    return True

        _set_carryable(state, self.player, None)
        return False

    @override
    def __init__(self, player: int, name: str = '', has_address: bool = False, parent: Optional[Region] = None):
        if has_address:
            # avoids circular imports
            from .world import CavernOfDreamsWorld
            address = CavernOfDreamsWorld.location_name_to_id[name]
        else:
            address = None
        super().__init__(player, name, address, parent)

class CavernOfDreamsEntrance(Entrance):
    @override
    def can_reach(self, state: CollectionState) -> bool:
        # assert self.parent_region is not None
        if not self.parent_region.can_reach(state):
            return False

        if self.access_rule(state):
            if not self.hide_path:
                _add_entrance_path_node(self, state)
            return True

        cars = _get_reachable_carryables(state, self.player)
        for carryable_region_name in cars:
            carryable_region = state.multiworld.get_region(carryable_region_name, self.player)
            # assert isinstance(carryable_region, CavernOfDreamsCarryableRegion)
            if self.parent_region in _get_reachable_regions(state, carryable_region_name, self.player):
                _set_carryable(state, self.player, carryable_region.carryable)
                if self.access_rule(state):
                    _set_carryable(state, self.player, None)
                    if not self.hide_path:
                        _add_entrance_path_node(self, state)
                    return True

        _set_carryable(state, self.player, None)
        return False

class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"
    entrance_type = CavernOfDreamsEntrance

    @override
    def can_reach(self, state: CollectionState):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in _get_reachable_regions(state, "default", self.player):
            return True

        cars = _get_reachable_carryables(state, self.player)
        for carryable_region_name in cars:
            if self in _get_reachable_regions(state, carryable_region_name, self.player):
                # print(state.path)
                # print(f"{carryable_region_name} -> {self}")
                # print(list(item[0] for item in get_path(state, self)))
                # print(state.prog_items[self.player])
                return True

        return False

class CavernOfDreamsCarryableRegion(CavernOfDreamsRegion):
    carryable: TempItem

    def __init__(self, name: str, player: int, multiworld: MultiWorld, carryable: TempItem, hint: str | None = None):
        super().__init__(name, player, multiworld, hint)
        self.carryable = carryable

from itertools import zip_longest

def flist_to_iter(path_value: PathValue | None) -> Iterator[str]:
    while path_value:
        region_or_entrance, path_value = path_value
        yield region_or_entrance

def get_path(state: CollectionState, region: Region) -> list[tuple[str, str] | tuple[str, None]]:
    player = region.player
    all_paths = _get_all_paths(state, player)
    # menu = state.multiworld.get_region('Menu', player)
    result = next(filter(lambda r: region in r[1], all_paths.items()), None)
    if result is None:
        raise KeyError(f"unable to find valid path for {region}")
    start, paths = result

    reversed_path_as_flist: PathValue = paths.get(region, (str(region), None))
    string_path_flat = reversed(list(map(str, flist_to_iter(reversed_path_as_flist))))
    # Now we combine the flat string list into (region, exit) pairs
    pathsiter = iter(string_path_flat)
    pathpairs = zip_longest(pathsiter, pathsiter)
    ret = list(pathpairs)
    if start.name != "Menu":
        ret = get_path(state, start) + ret
    return ret

def _update_reachable_regions(state: CollectionState, player: int):
    state.stale[player] = False

    changed: bool = True

    while changed:
        changed = False
        changed |= _update_region_accessibility(
            state, "default", player,
            None,
            start=state.multiworld.get_region('Menu', player)
        )

        for carryable_region_name in _get_reachable_carryables(state, player):
            carryable_region = state.multiworld.get_region(carryable_region_name, player)
            # assert isinstance(carryable_region, CavernOfDreamsCarryableRegion)

            temp_item = carryable_region.carryable
            _set_carryable(state, player, temp_item)

            changed |= _update_region_accessibility(
                state, carryable_region_name, player,
                temp_item,
                start=carryable_region
            )

        _set_carryable(state, player, None)


def _update_region_accessibility(
    state: CollectionState,
    carryable_region_name: str,
    player: int,
    temp_item: TempItem | None,
    start: Region
) -> bool:
    reachable_regions: set[Region] = _get_reachable_regions(state, carryable_region_name, player)
    blocked_connections: set[Entrance] = _get_blocked_connections(state, carryable_region_name, player)
    queue = deque(blocked_connections)

    paths = _get_all_paths(state, player)
    if start not in paths:
        paths[start] = {}
    prev_start_region = _get_current_start_region(state, player)
    _set_current_start_region(state, player, start)

    changed: bool = False

    # init on first call - this can't be done on construction since the regions don't exist yet
    if start not in reachable_regions:
        reachable_regions.add(start)
        blocked_connections.update(start.exits)
        queue.extend(start.exits)

    _set_carryable(state, player, temp_item)

    # run BFS on all connections, and keep track of those blocked by missing items
    while queue:
        connection: Entrance = queue.popleft()
        new_region = connection.connected_region
        if new_region in reachable_regions:
            blocked_connections.remove(connection)
            continue

        assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"
        if not connection.can_reach(state):
            if temp_item is None:
                continue
            # ok, thats fine. however, what if the player chooses to drop what they have?
            _set_carryable(state, player, None)
            can_reach_with_no_temp_item = connection.can_reach(state)
            if can_reach_with_no_temp_item and new_region not in _get_reachable_regions(state, "default", player):
                # print(f"dropped {temp_item} to make it from {connection.parent_region} to {new_region}")
                changed |= _update_region_accessibility(state, "default", player, None, new_region)
            _set_carryable(state, player, temp_item)
            continue

        changed = True
        reachable_regions.add(new_region)
        blocked_connections.remove(connection)
        blocked_connections.update(new_region.exits)
        queue.extend(new_region.exits)
        _add_region_path_node(new_region, connection, state)

        # Retry connections if the new region can unblock them
        for new_entrance in state.multiworld.indirect_connections.get(new_region, set()):
            if new_entrance in blocked_connections and new_entrance not in queue:
                queue.append(new_entrance)

        if isinstance(new_region, CavernOfDreamsCarryableRegion):
            rcr = _get_reachable_carryables(state, player)
            if new_region.name not in rcr:
                rcr.append(new_region.name)

    _set_current_start_region(state, player, prev_start_region)
    return changed

# helper methods for path generation
def _get_current_start_region(state: CollectionState, player: int) -> Region:
    csr = state._cavernofdreams_current_start_region[player]
    if csr is None:
        return state.multiworld.get_region("Menu", player)
    return csr

def _set_current_start_region(state: CollectionState, player: int, region: Region):
    state._cavernofdreams_current_start_region[player] = region

def _get_all_paths(state: CollectionState, player: int) -> dict[Region, dict[Region | Entrance, PathValue]]:
    return state._cavernofdreams_paths[player]

def _get_current_paths(state: CollectionState, player: int) -> dict[Region | Entrance, PathValue]:
    return _get_all_paths(state, player)[_get_current_start_region(state, player)]

def _add_entrance_path_node(entrance: Entrance, state: CollectionState):
    current_paths = _get_current_paths(state, entrance.player)
    if not entrance in current_paths:
        current_paths[entrance] = (entrance.name, current_paths.get(entrance.parent_region, (entrance.parent_region.name, None)))

def _add_region_path_node(region: Region, connection: Entrance, state: CollectionState):
    current_paths = _get_current_paths(state, region.player)
    current_paths[region] = (region.name, current_paths.get(connection, None))

# helper methods for carryables + overrides
def _get_carryable(state: CollectionState, player: int) -> TempItem | None:
    return state._cavernofdreams_carrying[player]

def _set_carryable(state: CollectionState, player: int, temp_item: TempItem | None):
    state._cavernofdreams_carrying[player] = temp_item

def _get_reachable_carryables(state: CollectionState, player: int) -> list[str]:
    return state._cavernofdreams_reachable_carryables[player]

def _get_reachable_regions(state: CollectionState, carryable_region_name: str, player: int) -> set[Region]:
    return state._cavernofdreams_reachable_regions[carryable_region_name][player]

def _get_blocked_connections(state: CollectionState, carryable_region_name: str, player: int) -> set[Entrance]:
    return state._cavernofdreams_blocked_connections[carryable_region_name][player]

class CavernOfDreamsCollectionState(metaclass=AutoLogicRegister):
    # this is kludge to make typing work correctly
    # AutoLogicRegister ignores it
    def __init__(self):
        super().__init__()
        self._cavernofdreams_player_ids: tuple[int, ...] = ()
        self._cavernofdreams_carrying: dict[int, TempItem | None] = {}
        self._cavernofdreams_reachable_regions: dict[str, dict[int, set[Region]]] = {}
        self._cavernofdreams_blocked_connections: dict[str, dict[int, set[Entrance]]] = {}
        self._cavernofdreams_reachable_carryables: dict[int, list[str]] = {}
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
        return self.has_group("Shroom", player, shrooms)

    def init_mixin(self, parent: MultiWorld):
        # avoids circular imports
        from .world import CavernOfDreamsWorld
        game = CavernOfDreamsWorld.game

        cod_ids = parent.get_game_players(game) + parent.get_game_groups(game)
        self._cavernofdreams_player_ids = cod_ids

        self._cavernofdreams_carrying = {player: None for player in cod_ids}
        reachable = {}
        blocked = {}
        for event_and_region_name in carryable_locations.keys():
            reachable[event_and_region_name] = {player: set() for player in cod_ids}
            blocked[event_and_region_name] = {player: set() for player in cod_ids}
        self._cavernofdreams_reachable_regions = reachable
        self._cavernofdreams_blocked_connections = blocked
        self._cavernofdreams_reachable_carryables = {player: [] for player in cod_ids}
        self._cavernofdreams_current_start_region = {player: None for player in cod_ids}
        self._cavernofdreams_paths = {player: {} for player in cod_ids}

    def copy_mixin(self, ret: CavernOfDreamsCollectionState) -> CavernOfDreamsCollectionState:
        cod_ids = self._cavernofdreams_player_ids
        ret._cavernofdreams_player_ids = cod_ids

        ret._cavernofdreams_carrying = copy.copy(self._cavernofdreams_carrying)
        ret._cavernofdreams_reachable_carryables = {
            player: [item for item in self._cavernofdreams_reachable_carryables[player]]
            for player in cod_ids
        }

        reachable = {}
        for event_and_region_name, by_player in self._cavernofdreams_reachable_regions.items():
            reachable[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_reachable_regions = reachable

        blocked = {}
        for event_and_region_name, by_player in self._cavernofdreams_blocked_connections.items():
            blocked[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_blocked_connections = blocked

        # NOTE: may need a deeper copy?
        ret._cavernofdreams_paths = {player: copy.copy(self._cavernofdreams_paths[player]) for player in cod_ids}

        ret._cavernofdreams_current_start_region = {player: self._cavernofdreams_current_start_region[player] for player in cod_ids}

        return ret
