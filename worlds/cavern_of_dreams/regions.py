from __future__ import annotations
from collections.abc import Collection, Iterable, Iterator
from enum import Enum, IntFlag

from BaseClasses import Location, PathValue, Region, Entrance, CollectionState, MultiWorld
from ..AutoWorld import AutoLogicRegister
from .ap_generated.data import carryable_locations

import copy
from collections import Counter, deque
from typing import Callable, Literal, TypeAlias, TypeVar, override

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

# region_propogations = 0
# 
# location_earlyouts: Counter[CavernOfDreamsLocation] = Counter()
# location_checks: Counter[CavernOfDreamsLocation] = Counter()

class CavernOfDreamsLocation(Location):
    game = "Cavern of Dreams"

    carryable_access_rules: CarryableAccessRules
    not_carryable_access_rules: CarryableAccessRules

    parent_region: CavernOfDreamsRegion

    valid_accessible_carryables: set[TempItem | None]

    @override
    def can_reach(self, state: CollectionState) -> bool:
        # global location_checks, location_earlyouts
        # location_checks[self] += 1
        #if CarryableTestResult.SUCCESS in check_any_carryable_access(self, state):
            # location_earlyouts[self] += 1
            #return True

        return (self.parent_region.can_reach(state) and
                CarryableTestResult.SUCCESS in check_any_access(self, state))

    def simple_can_reach(self, state: CollectionState) -> bool:
        return self.parent_region.can_reach(state)

    @override
    def __init__(self, player: int, name: str = '', has_address: bool = False, parent: Optional[Region] = None):
        if has_address:
            # avoids circular imports
            from .world import CavernOfDreamsWorld
            address = CavernOfDreamsWorld.location_name_to_id[name]
        else:
            address = None
        super().__init__(player, name, address, parent)
        self.carryable_access_rules = {}
        self.not_carryable_access_rules = {}
        self.valid_accessible_carryables = set()

class CarryableTestResult(IntFlag):
    SUCCESS        = 0b001
    NEED_NONE      = 0b101
    FAIL           = 0b010


def check_any_carryable_access(
    node: CavernOfDreamsEntrance | CavernOfDreamsLocation,
    state: CollectionState
) -> CarryableTestResult:
    valid_carryables: set[TempItem | None] = set(
        carryable for carryable in (
            state.multiworld.get_region(name, node.player).carryable
            for name in _get_reachable_carryables(state, node.player)
            if node.parent_region in _get_reachable_regions(state, name, node.player)
        )
        if carryable in node.carryable_access_rules
        or not only_contains(carryable, node.not_carryable_access_rules)
    )

    for carryable in valid_carryables:
        if carryable is None: continue
        access_rule = node.carryable_access_rules[carryable]
        if access_rule(state):
            # if not self.hide_path:
            #     _add_entrance_path_node(self, state)
            return CarryableTestResult.SUCCESS

    region_carryables_len = len(valid_carryables)
    if region_carryables_len > 0:
        not_carryables = node.not_carryable_access_rules.keys()
        only_carryable = False
        if region_carryables_len == 1:
            only_carryable = next(iter(valid_carryables))
            not_carryables = filter(only_carryable.__ne__, not_carryables)
        # map(node.not_carryable_access_rules.__getitem__, not_carryables):
        for access_rule in (node.not_carryable_access_rules[carryable] for carryable in not_carryables):
            if access_rule(state):
                if only_carryable is None:
                    return CarryableTestResult.NEED_NONE
                # if not self.hide_path:
                #     _add_entrance_path_node(self, state)
                return CarryableTestResult.SUCCESS

    if rule := node.carryable_access_rules.get(None):
        if rule(state): return CarryableTestResult.NEED_NONE

    return CarryableTestResult.FAIL

def _get_accessible_carryables(state: CollectionState, region: CavernOfDreamsRegion, player: int):
    return state._cavernofdreams_accessible_carryables[player][region]

def check_any_access(
    node: CavernOfDreamsEntrance | CavernOfDreamsLocation,
    state: CollectionState
) -> CarryableTestResult:
    if node.access_rule(state):
        return CarryableTestResult.SUCCESS

    return check_any_carryable_access(node, state)

def check_carryable_access(
    node: CavernOfDreamsEntrance | CavernOfDreamsLocation,
    carryable: TempItem | None,
    state: CollectionState
) -> CarryableTestResult:
    if node.access_rule(state):
        return CarryableTestResult.SUCCESS

    # e.g. not carrying jester boots
    for not_carryable, rule in node.not_carryable_access_rules.items():
        if carryable == not_carryable: continue
        if rule(state): return CarryableTestResult.SUCCESS

    # requires carrying the current carryable
    if rule := node.carryable_access_rules.get(carryable):
        if rule(state): return CarryableTestResult.SUCCESS

    if carryable is not None:
        # can drop carryable
        if rule := node.carryable_access_rules.get(None):
            if rule(state): return CarryableTestResult.NEED_NONE

        # also can drop carryable
        if rule := node.not_carryable_access_rules.get(carryable):
            if rule(state): return CarryableTestResult.NEED_NONE

    return CarryableTestResult.FAIL

CarryableAccessRules: TypeAlias = dict[TempItem | None, Callable[[CollectionState], bool]]



class CavernOfDreamsEntrance(Entrance):
    carryable_access_rules: CarryableAccessRules
    not_carryable_access_rules: CarryableAccessRules

    valid_accessible_carryables: set[TempItem | None]

    connected_region: CavernOfDreamsRegion
    parent_region: CavernOfDreamsRegion

    @override
    def __init__(self, player: int, name: str = '', parent: Region = None):
        super().__init__(player, name, parent)
        self.carryable_access_rules = {}
        self.not_carryable_access_rules = {}
        self.valid_accessible_carryables = set()

    def simple_can_reach(self, state: CollectionState) -> bool:
        return self.parent_region.can_reach(state)

    @override
    def can_reach(self, state: CollectionState) -> bool:
        # assert self.parent_region is not None
        return self.parent_region.can_reach(state) and CarryableTestResult.SUCCESS in check_any_access(self, state)

T = TypeVar("T")
def only_contains(elem: T, elems: Collection[T]):
    return not (
        (elems_len := len(elems)) > 1
        or (elems_len == 1 and elem not in elems)
    )

class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"
    entrance_type = CavernOfDreamsEntrance

    locations: list[CavernOfDreamsLocation]
    exits: list[CavernOfDreamsEntrance]

    @override
    def can_reach(self, state: CollectionState):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in _get_reachable_regions(state, "default", self.player):
            return True

        return any(
            self in _get_reachable_regions(state, name, self.player)
            for name in _get_reachable_carryables(state, self.player)
        )

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
    # global region_propogations
    # region_propogations += 1
    state.stale[player] = False

    regions_to_propogate: set[CavernOfDreamsRegion] = set()

    changed: bool = True
    menu_region = state.multiworld.get_region('Menu', player)

    while changed:
        changed = False
        changed |= _update_region_accessibility(
            state, "default", player,
            None,
            start=menu_region
        )

        for carryable_region_name in _get_reachable_carryables(state, player):
            carryable_region = state.multiworld.get_region(carryable_region_name, player)
            # assert isinstance(carryable_region, CavernOfDreamsCarryableRegion)

            changed |= _update_region_accessibility(
                state, carryable_region_name, player,
                carryable_region.carryable,
                start=carryable_region
            )

def _update_region_accessibility(
    state: CollectionState,
    carryable_region_name: str,
    player: int,
    temp_item: TempItem | None,
    start: CavernOfDreamsRegion
) -> bool:
    reachable_regions = _get_reachable_regions(state, carryable_region_name, player)
    blocked_connections = _get_blocked_connections(state, carryable_region_name, player)
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

    # run BFS on all connections, and keep track of those blocked by missing items
    while queue:
        connection: Entrance = queue.popleft()
        new_region = connection.connected_region
        if new_region in reachable_regions:
            blocked_connections.remove(connection)
            continue

        assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"

        result = check_carryable_access(connection, temp_item, state)
        # print(">>>", connection.name, result)
        # print(state.prog_items)

        if CarryableTestResult.FAIL in result:
            continue

        if CarryableTestResult.NEED_NONE in result:
            if new_region not in _get_reachable_regions(state, "default", player):
                changed |= _update_region_accessibility(state, "default", player, None, new_region)
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

# TODO: refactor everything to take Regions instead of strs

def _get_reachable_regions(state: CollectionState, carryable_region_name: str, player: int) -> set[CavernOfDreamsRegion]:
    return state._cavernofdreams_reachable_regions[carryable_region_name][player]

def _get_blocked_connections(state: CollectionState, carryable_region_name: str, player: int) -> set[CavernOfDreamsEntrance]:
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
