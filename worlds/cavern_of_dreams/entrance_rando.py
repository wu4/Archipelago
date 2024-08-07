from typing import TYPE_CHECKING, Callable

from BaseClasses import CollectionState

from .options import Carryablesanity
from .regions import CavernOfDreamsEntrance
from .ap_generated.entrance_rando import parent_regions
if TYPE_CHECKING:
    from .world import CavernOfDreamsWorld

def randomize_entrances(
    world: "CavernOfDreamsWorld",
    entrances: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    as_dict = dict(entrances)
    shuffled_values = list(as_dict.values())
    world.random.shuffle(shuffled_values)
    return list(zip(as_dict, shuffled_values))

def make_entrance_underwater(entrance: "CavernOfDreamsEntrance"):
    old_access_rule = entrance.access_rule
    entrance.access_rule = lambda state: state.has("Swim") and old_access_rule(state)

# def no_carryables(entrance: "CavernOfDreamsEntrance"):
#     none_access_rules: list[Callable[[CollectionState], bool]] = []
# 
#     none_access_rule = entrance.carryable_access_rules.get(None, None)
#     if none_access_rule is not None:
#         none_access_rules.append(none_access_rule)
#     entrance.carryable_access_rules = {}
# 
#     if entrance.dont_care_access_rule != CavernOfDreamsEntrance.dont_care_access_rule:
#         none_access_rules.append(entrance.dont_care_access_rule)
#         entrance.dont_care_access_rule = CavernOfDreamsEntrance.dont_care_access_rule
# 
#     for carryable, rule in entrance.inverse_carryable_access_rules.items():
#         if carryable is None: continue
#         none_access_rules.append(rule)
#     entrance.inverse_carryable_access_rules = {}
# 
#     entrance.carryable_access_rules[None] = lambda state: any(map(lambda rule: rule(state), none_access_rules))

def link_entrances(world: "CavernOfDreamsWorld", entrance_map: list[tuple[str,str]], entrances: dict[str, tuple[CavernOfDreamsEntrance | None, bool]]):
    is_kind_carryablesanity = world.options.carryablesanity == Carryablesanity.option_kind
    for from_entrance_name, to_entrance_name in entrance_map:
        from_entrance, _ = entrances[from_entrance_name]
        if from_entrance is None: continue
        _, to_entrance_underwater = entrances[to_entrance_name]

        if is_kind_carryablesanity:
            from_entrance.reject_carryables = True

        if to_entrance_underwater:
            make_entrance_underwater(from_entrance)

        from_parent_region = parent_regions[from_entrance_name]
        from_entrance.parent_region = world.multiworld.get_region(from_parent_region, world.player)
        from_entrance.parent_region.exits.append(from_entrance)
        to_parent_region = parent_regions[to_entrance_name]
        from_entrance.connect(world.multiworld.get_region(to_parent_region, world.player))
