# pyright: reportUninitializedInstanceVariable=false
from __future__ import annotations

from BaseClasses import Region, Entrance, CollectionState, MultiWorld
from ..AutoWorld import AutoLogicRegister

import copy
from collections import deque
from typing import Literal, TypeAlias, override
from . import CavernOfDreamsWorld

Throwable: TypeAlias = Literal[
    "Apple",
    "Medicine",
    "Bubble Conch",
    "Sage's Gloves",
    "Lady Opal's Head",
    "Shelnert's Fish",
    "Mr. Kerrington's Wings",
]

hardcoded_throwable_sources: dict[str, Throwable] = {
    "LOSTLEAF_1": "Apple"
}

class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"

    @override
    def can_reach(self, state: CollectionState):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in _get_reachable_regions(state, "default", self.player):
            return True

        for event_and_region_name in hardcoded_throwable_sources.keys():
            if not state.has(event_and_region_name, self.player): continue
            if self not in _get_reachable_regions(state, event_and_region_name, self.player): continue
            return True

        return False

def _get_reachable_regions(state: CollectionState, group_name: str, player: int) -> set[Region]:
    return state._cavernofdreams_reachable_regions[group_name][player]

def _get_blocked_connections(state: CollectionState, group_name: str, player: int) -> set[Entrance]:
    return state._cavernofdreams_blocked_connections[group_name][player]

def _update_reachable_regions(self: CollectionState, player: int):
    self.stale[player] = False

    _update_region_accessibility(
        self, "default", player,
        start = self.multiworld.get_region('Menu', player)
    )

    for event_and_region_name, throwable in hardcoded_throwable_sources.items():
        if not self.has(event_and_region_name, player): continue

        self._cavernofdreams_carrying_throwable[player] = throwable

        _update_region_accessibility(
            self, event_and_region_name, player,
            start = self.multiworld.get_region(event_and_region_name, player)
        )

    self._cavernofdreams_carrying_throwable[player] = None

def _update_region_accessibility(self: CollectionState, group_name: str, player: int, start: Region):
    rrp: set[Region] = _get_reachable_regions(self, group_name, player)
    bc: set[Entrance] = _get_blocked_connections(self, group_name, player)
    queue = deque(bc)

    # init on first call - this can't be done on construction since the regions don't exist yet
    if start not in rrp:
        rrp.add(start)
        bc.update(start.exits)
        queue.extend(start.exits)

    # run BFS on all connections, and keep track of those blocked by missing items
    while queue:
        connection: Entrance = queue.popleft()
        new_region = connection.connected_region
        if new_region in rrp:
            bc.remove(connection)
        elif connection.can_reach(self):
            assert new_region, f"tried to search through an Entrance \"{connection}\" with no Region"
            rrp.add(new_region)
            bc.remove(connection)
            bc.update(new_region.exits)
            queue.extend(new_region.exits)
            self.path[new_region] = (new_region.name, self.path.get(connection, None))

            # Retry connections if the new region can unblock them
            for new_entrance in self.multiworld.indirect_connections.get(new_region, set()):
                if new_entrance in bc and new_entrance not in queue:
                    queue.append(new_entrance)

class CavernOfDreamsCollectionState(metaclass=AutoLogicRegister):
    _cavernofdreams_player_ids: tuple[int, ...]
    _cavernofdreams_wearing_jester_boots: dict[int, bool]
    _cavernofdreams_carrying_throwable: dict[int, Throwable | None]
    _cavernofdreams_reachable_regions: dict[str, dict[int, set[Region]]]
    _cavernofdreams_blocked_connections: dict[str, dict[int, set[Entrance]]]

    def init_mixin(self, parent: MultiWorld):
        cod_ids = parent.get_game_players(CavernOfDreamsWorld.game) + parent.get_game_groups(CavernOfDreamsWorld.game)
        self._cavernofdreams_player_ids = cod_ids

        self._cavernofdreams_wearing_jester_boots = {player: False for player in cod_ids}
        self._cavernofdreams_carrying_throwable = {player: None for player in cod_ids}
        reachable = {}
        blocked = {}
        for event_and_region_name in hardcoded_throwable_sources.keys():
            reachable[event_and_region_name] = {player: set() for player in cod_ids}
            blocked[event_and_region_name] = {player: set() for player in cod_ids}
        self._cavernofdreams_reachable_regions = reachable
        self._cavernofdreams_blocked_connections = blocked

    def copy_mixin(self, ret: CavernOfDreamsCollectionState) -> CavernOfDreamsCollectionState:
        cod_ids = self._cavernofdreams_player_ids
        ret._cavernofdreams_player_ids = cod_ids
        ret._cavernofdreams_wearing_jester_boots = copy.copy(self._cavernofdreams_wearing_jester_boots)

        ret._cavernofdreams_carrying_throwable = copy.copy(self._cavernofdreams_carrying_throwable)

        reachable = {}
        for event_and_region_name, by_player in self._cavernofdreams_reachable_regions.items():
            reachable[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_reachable_regions = reachable

        blocked = {}
        for event_and_region_name, by_player in self._cavernofdreams_blocked_connections.items():
            blocked[event_and_region_name] = {player: copy.copy(by_player[player]) for player in cod_ids}
        ret._cavernofdreams_blocked_connections = blocked

        return ret
