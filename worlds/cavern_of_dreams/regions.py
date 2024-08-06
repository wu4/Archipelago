from collections.abc import Collection

from BaseClasses import Location, Region, Entrance, CollectionState, MultiWorld

from collections import deque
from typing import Callable, TypeAlias, TypeVar, final

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .types import MaybeTempItem, TempItem
    from BaseClasses import Item

from .state_patches import get_carryable_sources, get_reachable_regions, get_current_paths, get_all_paths, get_blocked_connections, get_current_start_region, set_current_start_region, add_entrance_path_node, add_region_path_node
from .carryables import CarryableTestResult, CavernOfDreamsCarryable, check_any_access, check_carryable_access

CarryableAccessRules: TypeAlias = dict["MaybeTempItem", Callable[[CollectionState], bool]]

def simple_can_reach(node: "CavernOfDreamsLocation | CavernOfDreamsEntrance", state: CollectionState) -> bool:
    # no access rule check
    return node.parent_region.can_reach(state)

class CavernOfDreamsLocation(Location):
    game = "Cavern of Dreams"

    parent_region: "CavernOfDreamsRegion"

    carryable_access_rules: CarryableAccessRules
    inverse_carryable_access_rules: CarryableAccessRules
    dont_care_access_rule: Callable[[CollectionState], bool] = staticmethod(lambda state: False)

    @final
    def access_rule(self, state: CollectionState) -> bool:
        if self.item is not None and isinstance(self.item, CavernOfDreamsCarryable) and self.item.carryable != "Jester Boots":
            if not state.has("Carry", self.player): return False
        return CarryableTestResult.SUCCESS in check_any_access(self, state)

    def __init__(self, player: int, name: str = '', has_address: bool = False, parent: Region | None = None):
        if has_address:
            # avoids circular imports
            from .world import CavernOfDreamsWorld
            address = CavernOfDreamsWorld.location_name_to_id[name]
        else:
            address = None

        super().__init__(player, name, address, parent)
        self.carryable_access_rules = {}
        self.inverse_carryable_access_rules = {}


class CavernOfDreamsEntrance(Entrance):
    connected_region: "CavernOfDreamsRegion"
    parent_region: "CavernOfDreamsRegion"

    carryable_access_rules: CarryableAccessRules
    inverse_carryable_access_rules: CarryableAccessRules
    dont_care_access_rule: Callable[[CollectionState], bool] = staticmethod(lambda state: False)

    @final
    def access_rule(self, state: CollectionState) -> bool:
        return CarryableTestResult.SUCCESS in check_any_access(self, state)

    def __init__(self, player: int, name: str = '', parent: Region = None):
        super().__init__(player, name, parent)
        self.carryable_access_rules = {}
        self.inverse_carryable_access_rules = {}

    # def can_reach(self, state: CollectionState) -> bool:
    #     # assert self.parent_region is not None
    #     return self.parent_region.can_reach(state) and CarryableTestResult.SUCCESS in check_any_access(self, state)

class CavernOfDreamsRegion(Region):
    game: str = "Cavern of Dreams"
    entrance_type = CavernOfDreamsEntrance

    locations: list[CavernOfDreamsLocation]
    exits: list[CavernOfDreamsEntrance]

    def can_reach(self, state: CollectionState):
        if state.stale[self.player]:
            _update_reachable_regions(state, self.player)

        if self in get_reachable_regions(state, "dont-care", self.player):
            return True

        return any(
            self in get_reachable_regions(state, carryable_region_name, self.player)
            for carryable_region_name, _carryable in get_carryable_sources(state, self.player)
        )

def _update_reachable_regions(state: CollectionState, player: int):
    # global region_propogations
    # region_propogations += 1
    state.stale[player] = False

    changed: bool = True
    menu_region = state.multiworld.get_region('Menu', player)

    while changed:
        changed = False
        changed |= _update_region_accessibility(
            state, "dont-care", player,
            None,
            start=menu_region
        )

        for carryable_region_name, carryable in get_carryable_sources(state, player):
            carryable_region = state.multiworld.get_region(carryable_region_name, player)
            # assert isinstance(carryable_region, CavernOfDreamsCarryableRegion)

            changed |= _update_region_accessibility(
                state, carryable_region_name, player,
                carryable,
                start=carryable_region
            )

def _update_region_accessibility(
    state: CollectionState,
    carryable_region_name: str,
    player: int,
    temp_item: "MaybeTempItem",
    start: CavernOfDreamsRegion
) -> bool:
    reachable_regions = get_reachable_regions(state, carryable_region_name, player)
    blocked_connections = get_blocked_connections(state, carryable_region_name, player)
    queue = deque(blocked_connections)

    paths = get_all_paths(state, player)
    if start not in paths:
        paths[start] = {}
    prev_start_region = get_current_start_region(state, player)
    set_current_start_region(state, player, start)

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

        if CarryableTestResult.FAIL in result:
            if "Victory" in connection.name:
                print(">>>", connection.name, result)
                print(state.prog_items)
            continue


        if CarryableTestResult.NEED_NONE in result:
            if new_region not in get_reachable_regions(state, "dont-care", player):
                add_entrance_path_node(connection, state, get_all_paths(state, player)[state.multiworld.get_region("Menu", player)])
                # _add_entrance_path_node(connection, state, get_all_paths(state, player).setdefault(new_region, {}))
                changed |= _update_region_accessibility(state, "dont-care", player, None, new_region)
            continue

        add_entrance_path_node(connection, state, get_current_paths(state, player))

        changed = True

        reachable_regions.add(new_region)
        blocked_connections.remove(connection)
        blocked_connections.update(new_region.exits)
        queue.extend(new_region.exits)

        add_region_path_node(new_region, connection, state)

        # Retry connections if the new region can unblock them
        for new_entrance in state.multiworld.indirect_connections.get(new_region, set()):
            if new_entrance in blocked_connections and new_entrance not in queue:
                queue.append(new_entrance)

    set_current_start_region(state, player, prev_start_region)
    return changed
