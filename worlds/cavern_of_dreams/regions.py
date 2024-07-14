from __future__ import annotations

from BaseClasses import Region, Entrance, CollectionState, MultiWorld
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


class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"

    @override
    def can_reach(self, state: CollectionState):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in _get_reachable_regions(state, "default", self.player):
            return True

        for event_and_region_name in carryable_locations.keys():
            if not state.has(event_and_region_name, self.player):
                continue
            if self in _get_reachable_regions(state, event_and_region_name, self.player):
                return True

        return False


def _get_reachable_regions(state: CollectionState, event_and_region_name: str, player: int) -> set[Region]:
    return state._cavernofdreams_reachable_regions[event_and_region_name][player]


def _get_blocked_connections(state: CollectionState, event_and_region_name: str, player: int) -> set[Entrance]:
    return state._cavernofdreams_blocked_connections[event_and_region_name][player]


def _update_reachable_regions(self: CollectionState, player: int):
    self.stale[player] = False

    changed: bool = True

    while changed:
        changed = False
        changed |= _update_region_accessibility(
            self, "default", player,
            None,
            start=self.multiworld.get_region('Menu', player)
        )

        for event_and_region_name, temp_item in carryable_locations.items():
            if not self.has(event_and_region_name, player):
                continue

            self._cavernofdreams_carrying[player] = temp_item

            changed |= _update_region_accessibility(
                self, event_and_region_name, player,
                temp_item,
                start=self.multiworld.get_region(event_and_region_name, player)
            )

        self._cavernofdreams_carrying[player] = None


def _update_region_accessibility(
    self: CollectionState,
    event_and_region_name: str,
    player: int,
    temp_item: TempItem | None,
    start: Region
) -> bool:
    reachable_regions: set[Region] = _get_reachable_regions(self, event_and_region_name, player)
    blocked_connections: set[Entrance] = _get_blocked_connections(self, event_and_region_name, player)
    queue = deque(blocked_connections)

    changed: bool = False

    # init on first call - this can't be done on construction since the regions don't exist yet
    if start not in reachable_regions:
        reachable_regions.add(start)
        blocked_connections.update(start.exits)
        queue.extend(start.exits)

    self._cavernofdreams_carrying[player] = temp_item

    # run BFS on all connections, and keep track of those blocked by missing items
    while queue:
        connection: Entrance = queue.popleft()
        new_region = connection.connected_region
        if new_region in reachable_regions:
            blocked_connections.remove(connection)
            continue

        if not connection.can_reach(self):
            if temp_item is None:
                continue
            assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"
            # ok, thats fine. however, what if the player chooses to drop what they have?
            # TODO: check if paths are messed up as a result of this (they probably arent)
            self._cavernofdreams_carrying[player] = None
            can_reach_with_no_temp_item = connection.can_reach(self)
            if can_reach_with_no_temp_item and new_region not in _get_reachable_regions(self, "default", player):
                changed |= _update_region_accessibility(self, "default", player, None, new_region)
            self._cavernofdreams_carrying[player] = temp_item
            continue
        else:
            assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"

        changed = True
        reachable_regions.add(new_region)
        blocked_connections.remove(connection)
        blocked_connections.update(new_region.exits)
        queue.extend(new_region.exits)
        self.path[new_region] = (new_region.name, self.path.get(connection, None))

        # Retry connections if the new region can unblock them
        for new_entrance in self.multiworld.indirect_connections.get(new_region, set()):
            if new_entrance in blocked_connections and new_entrance not in queue:
                queue.append(new_entrance)

    return changed


class CavernOfDreamsCollectionState(metaclass=AutoLogicRegister):
    # this is kludge to make typing work correctly, AutoLogicRegister ignores it
    def __init__(self):
        super().__init__()
        self._cavernofdreams_player_ids: tuple[int, ...] = ()
        self._cavernofdreams_carrying: dict[int, TempItem | None] = {}
        self._cavernofdreams_reachable_regions: dict[str, dict[int, set[Region]]] = {}
        self._cavernofdreams_blocked_connections: dict[str, dict[int, set[Entrance]]] = {}

    def _cavernofdreams_has_shrooms_for(self, player: int, fella: str):
        if fella == "Lake":
            shrooms = 40
        elif fella == "Monster":
            shrooms = 80
        elif fella == "Palace":
            shrooms = 120
        elif fella == "Gallery":
            shrooms = 200
        self.has_group("Shroom", player, shrooms)
        return True

    def init_mixin(self, parent: MultiWorld):
        from .world import CavernOfDreamsWorld
        cod_ids = parent.get_game_players(CavernOfDreamsWorld.game) + parent.get_game_groups(CavernOfDreamsWorld.game)
        self._cavernofdreams_player_ids = cod_ids

        self._cavernofdreams_carrying = {player: None for player in cod_ids}
        reachable = {}
        blocked = {}
        for event_and_region_name in carryable_locations.keys():
            reachable[event_and_region_name] = {player: set() for player in cod_ids}
            blocked[event_and_region_name] = {player: set() for player in cod_ids}
        self._cavernofdreams_reachable_regions = reachable
        self._cavernofdreams_blocked_connections = blocked

    def copy_mixin(self, ret: CavernOfDreamsCollectionState) -> CavernOfDreamsCollectionState:
        cod_ids = self._cavernofdreams_player_ids
        ret._cavernofdreams_player_ids = cod_ids

        ret._cavernofdreams_carrying = copy.copy(self._cavernofdreams_carrying)

        reachable = {}
        for event_and_region_name, by_player in self._cavernofdreams_reachable_regions.items():
            reachable[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_reachable_regions = reachable

        blocked = {}
        for event_and_region_name, by_player in self._cavernofdreams_blocked_connections.items():
            blocked[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_blocked_connections = blocked

        return ret
