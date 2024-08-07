from collections.abc import Collection
from enum import IntFlag

from .state_patches import get_reachable_regions, get_carryable_sources
from .items import CavernOfDreamsItem

from typing import TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
    from .regions import CavernOfDreamsEntrance, CavernOfDreamsLocation
    from BaseClasses import CollectionState
    from .types import MaybeTempItem, TempItem

class CavernOfDreamsCarryable(CavernOfDreamsItem):
    carryable: "TempItem"

    def __init__(self, name: str, code: int, player: int):
        super().__init__(name, code, player)
        self.carryable = name

class CarryableTestResult(IntFlag):
    SUCCESS        = 0b0001
    NEED_NONE      = 0b0011
    FAIL           = 0b0100
    NEVER          = 0b1100

def check_carryable_access(
    node: "CavernOfDreamsEntrance | CavernOfDreamsLocation",
    carryable: "MaybeTempItem",
    state: "CollectionState"
) -> CarryableTestResult:
    can_be_traversed = False
    if node.dont_care_access_rule:
        can_be_traversed = True
        if node.dont_care_access_rule(state): return CarryableTestResult.SUCCESS

    # e.g. not carrying jester boots
    for inverse_carryable, rule in node.inverse_carryable_access_rules.items():
        if carryable == inverse_carryable: continue
        can_be_traversed = True
        if rule(state): return CarryableTestResult.SUCCESS

    # requires carrying the current carryable
    if rule := node.carryable_access_rules.get(carryable):
        can_be_traversed = True
        if rule(state): return CarryableTestResult.SUCCESS

    if carryable is not None:
        # can drop carryable
        if rule := node.carryable_access_rules.get(None):
            can_be_traversed = True
            if rule(state): return CarryableTestResult.NEED_NONE

        # also can drop carryable
        if rule := node.inverse_carryable_access_rules.get(carryable):
            can_be_traversed = True
            if rule(state): return CarryableTestResult.NEED_NONE

    if can_be_traversed:
        return CarryableTestResult.FAIL
    else:
        return CarryableTestResult.NEVER

def check_any_access(
    node: "CavernOfDreamsEntrance | CavernOfDreamsLocation",
    state: "CollectionState"
) -> CarryableTestResult:
    if node.dont_care_access_rule and node.dont_care_access_rule(state):
        return CarryableTestResult.SUCCESS

    return check_any_carryable_access(node, state)

T = TypeVar("T")
def _only_contains(elem: T, elems: Collection[T]):
    return not (
        (elems_len := len(elems)) > 1
        or (elems_len == 1 and elem not in elems)
    )

def _get_valid_carryables(node: "CavernOfDreamsEntrance | CavernOfDreamsLocation", state: "CollectionState") -> set["MaybeTempItem"]:
    return set(
        carryable
        for region_name, carryable in get_carryable_sources(state, node.player)
        if node.parent_region in get_reachable_regions(state, region_name, node.player)
        if carryable in node.carryable_access_rules
        or not _only_contains(carryable, node.inverse_carryable_access_rules)
    )


def check_any_carryable_access(
    node: "CavernOfDreamsEntrance | CavernOfDreamsLocation",
    state: "CollectionState"
) -> CarryableTestResult:
    valid_carryables = _get_valid_carryables(node, state)

    for carryable in valid_carryables:
        if carryable is None: continue
        access_rule = node.carryable_access_rules[carryable]
        if access_rule(state):
            # if not self.hide_path:
            #     _add_entrance_path_node(self, state)
            return CarryableTestResult.SUCCESS

    region_carryables_len = len(valid_carryables)
    if region_carryables_len > 0:
        inverse_carryables = node.inverse_carryable_access_rules.keys()
        only_carryable = False
        if region_carryables_len == 1:
            only_carryable = next(iter(valid_carryables))
            inverse_carryables = filter(only_carryable.__ne__, inverse_carryables)

        for access_rule in (node.inverse_carryable_access_rules[carryable] for carryable in inverse_carryables):
            if access_rule(state):
                if only_carryable is None:
                    return CarryableTestResult.NEED_NONE
                # if not self.hide_path:
                #     _add_entrance_path_node(self, state)
                return CarryableTestResult.SUCCESS

    if rule := node.carryable_access_rules.get(None):
        if rule(state): return CarryableTestResult.NEED_NONE

    return CarryableTestResult.FAIL
