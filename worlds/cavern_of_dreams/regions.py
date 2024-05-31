from __future__ import annotations

from BaseClasses import Region, Entrance, CollectionState, MultiWorld
from AutoWorld import LogicMixin, AutoLogicRegister

import copy
from collections import deque
from typing import cast
from . import CavernOfDreamsWorld

throwables: dict[str, dict[str, str]] = {
    "Apple": {
        "Lostleaf Apple Tree": "LostleafLake/Start"
    },
    "Potion": {
        
    }
}

class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"

    def can_reach(self, state):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in _get_reachable_regions(state, "default", self.player):
            return True

        for inner in throwables.values():
            for event_name in inner.keys():
                if not state.has(event_name, self.player): continue
                if self not in _get_reachable_regions(state, event_name, self.player): continue
                return True

        return False

def _set_carrying_throwable(state: CollectionState, player: int, throwable_type: str | None):
    getattr(state, f"_cavernofdreams_carrying_throwable")[player] = throwable_type
    
def _get_carrying_throwable(state: CollectionState, player: int) -> str | None:
    return getattr(state, f"_cavernofdreams_carrying_throwable")[player]

def _get_reachable_regions(state: CollectionState, group_name: str, player: int) -> set[Region]:
    return getattr(state, f"_cavernofdreams_{group_name}_reachable_regions")[player]

def _get_blocked_connections(state: CollectionState, group_name: str, player: int) -> set[Entrance]:
    return getattr(state, f"_cavernofdreams_{group_name}_blocked_connections")[player]

def _update_reachable_regions(self: CollectionState, player: int):
    self.stale[player] = False

    _update_region_accessibility(
        self, "default", player,
        start = self.multiworld.get_region('Menu', player)
    )

    for throwable_type, inner in throwables.items():
        _set_carrying_throwable(self, player, throwable_type)

        for event_name, region_name in inner.items():
            if not self.has(event_name, player): continue

            _update_region_accessibility(
                self, event_name, player,
                start = self.multiworld.get_region(region_name, player)
            )

    _set_carrying_throwable(self, player, None)

def is_carrying(state: CollectionState, throwable_category: str | None, player: int) -> bool:
    return _get_carrying_throwable(state, player) == throwable_category

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
    def init_mixin(self, parent: MultiWorld):
        cod_ids = parent.get_game_players(CavernOfDreamsWorld.game) + parent.get_game_groups(CavernOfDreamsWorld.game)
        self._cavernofdreams_player_ids = cod_ids

        self._cavernofdreams_carrying_throwable = {player: None for player in cod_ids}
        for inner in throwables.values():
            for event_name in inner.keys():
                for attr_suffix in ["reachable_regions", "blocked_regions"]:
                    region_data_attrname = f"_cavernofdreams_{event_name}_{attr_suffix}"
                    setattr(self, region_data_attrname, {player: set() for player in cod_ids})

    def copy_mixin(self, ret) -> CollectionState:
        cod_ids = self._cavernofdreams_player_ids
        ret._cavernofdreams_player_ids = cod_ids

        ret._cavernofdreams_carrying_throwable = copy.copy(self._cavernofdreams_carrying_throwable)
        for inner in throwables.values():
            for event_name in inner.keys():
                for attr_suffix in ["reachable_regions", "blocked_regions"]:
                    region_data_attrname = f"_cavernofdreams_{event_name}_{attr_suffix}"
                    region_data = getattr(self, region_data_attrname)
                    setattr(ret, region_data_attrname, {player: copy.copy(region_data[player]) for player in cod_ids})

        return ret