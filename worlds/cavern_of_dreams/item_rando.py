from collections.abc import Generator
from typing import TYPE_CHECKING, Any, Counter

from Fill import fill_restrictive
from .ap_generated.data import item_groups, location_groups, all_items, vanilla_locations_by_name, vanilla_locations

all_items_as_set = set(all_items)

if TYPE_CHECKING:
    from BaseClasses import Item, CollectionState, MultiWorld
    from .world import CavernOfDreamsWorld


def _get_unshuffled_vanilla_abilities(self: "CavernOfDreamsWorld") -> Generator[str, Any, None]:
    if not self.options.shuffle_swim:
        yield "Swim"
    if not self.options.shuffle_roll:
        yield "Roll"
    if not self.options.shuffle_high_jump:
        yield "High Jump"
    if not self.options.shuffle_sprint:
        yield "Sprint"
    if not self.options.shuffle_carry:
        yield "Carry"
    if not self.options.shuffle_climb:
        yield "Climb"
    if self.options.super_bounce == 1:
        yield "Super Bounce"
    if self.options.air_swim == 1:
        yield "Air Swim"
    if self.options.super_bubble_jump == 1:
        yield "Super Bubble Jump"


def _get_excluded_items(self: "CavernOfDreamsWorld") -> Generator[str, Any, None]:
    if not self.options.include_double_jump:
        yield "Double Jump"

    if self.options.exclude_flight:
        yield "Flight"

    if self.options.exclude_wings:
        yield "Wings"

    if self.options.split_tail:
        yield "Tail"
    else:
        yield "Aerial Tail"
        yield "Grounded Tail"

    if self.options.super_bounce == 0:
        yield "Super Bounce"

    if self.options.super_bubble_jump == 0:
        yield "Super Bubble Jump"

    if self.options.air_swim == 0:
        yield "Air Swim"

    if self.options.gratitudesanity != 2:
        for teleport in item_groups["Teleport"]:
            yield teleport


def _get_sane_locations(self: "CavernOfDreamsWorld") -> Generator[str, Any, None]:
    if not self.options.shuffle_abilities:
        for location in location_groups["Ability"]:
            yield location
    if not self.options.shroomsanity:
        for location in location_groups["Shroom"]:
            yield location
    if not self.options.eventsanity:
        for location in location_groups["Event"]:
            yield location
    if self.options.gratitudesanity == 0:
        for location in location_groups["Gratitude"]:
            yield location
    if self.options.carryablesanity == 0:
        for location in location_groups["Carryable"]:
            yield location

def _match_pool_size_with_locations(self: "CavernOfDreamsWorld", pending_item_pool: list["Item"]):
    pool_size = len(pending_item_pool)
    location_count = len(list(self.multiworld.get_unfilled_locations(self.player)))
    diff = location_count - pool_size

    if self.options.carryablesanity:
        diff -= len(location_groups["Carryable"])

    while diff > 0:
        pending_item_pool.append(self.create_nothing())
        diff -= 1

    while diff < 0:
        pending_item_pool.remove(next(item for item in pending_item_pool if item.name in item_groups["Card"]))
        diff += 1

def all_carryable_items():
    for location in location_groups["Carryable"]:
        yield vanilla_locations[location]

def get_pre_fill_items(self: "CavernOfDreamsWorld"):
    ret: list["Item"] = []

    # if self.options.carryablesanity:
    #     ret.extend(map(self.create_item, all_carryable_items()))

    return ret

def get_restrictive_start_items(self: "CavernOfDreamsWorld"):
    if self.options.gratitudesanity == 1:
        for item in item_groups["Gratitude"]:
            yield item
    elif self.options.gratitudesanity == 2:
        for item in item_groups["Teleport"]:
            yield item

    if self.options.shuffle_abilities:
        if self.options.split_tail:
            yield "Grounded Tail"
            yield "Aerial Tail"
        else:
            yield "Tail"
        if self.options.bubble_jump > 0:
            yield "Bubble"
        yield "Horn"

    if self.options.shuffle_high_jump:
        yield "High Jump"

def pre_fill(self: "CavernOfDreamsWorld"):
    if not self.options.shroomsanity:
        early_item = self.multiworld.random.choice(list(get_restrictive_start_items(self)))
        self.multiworld.local_early_items[self.player][early_item] = 1

    if self.options.carryablesanity:
        state = self.multiworld.get_all_state(False)

        carryables = list(map(self.create_item, all_carryable_items()))

        # print(self.carryable_locations)
        # for carryable in carryables:
        #     state.remove(carryable)

        # for location in self.carryable_locations:
        #     print(location.name)

        self.multiworld.random.shuffle(self.carryable_locations)

        fill_restrictive(
            self.multiworld,
            state,
            self.carryable_locations,
            carryables,
            single_player_placement=True,
            name="Carryablesanity"
        )

def create_items(self: "CavernOfDreamsWorld"):
    exclude = Counter(_get_excluded_items(self))
    unshuffled_vanilla_abilities = Counter(_get_unshuffled_vanilla_abilities(self)) - exclude

    pending_item_pool: list["Item"] = []

    for item_name in unshuffled_vanilla_abilities:
        for n in range(0, unshuffled_vanilla_abilities[item_name]):
            self.multiworld.push_precollected(self.create_item(item_name))

    for location in _get_sane_locations(self):
        vanilla_item_name = vanilla_locations[location]

        item = self.create_item(vanilla_item_name)
        vanilla_location = self.multiworld.get_location(location, self.player)
        vanilla_location.place_locked_item(item)

        exclude[vanilla_item_name] += 1

    # unsure if this is any different from exclude.update(unshuffled_vanilla_abilities)
    if self.options.carryablesanity:
        exclude.update(vanilla_locations[location] for location in location_groups["Carryable"])

    exclude.update(item.name for item in self.multiworld.precollected_items[self.player])

    for item_name in all_items:
        if exclude[item_name] > 0:
            exclude[item_name] -= 1
            continue
        item = self.create_item(item_name)
        pending_item_pool.append(item)

    _match_pool_size_with_locations(self, pending_item_pool)

    self.multiworld.itempool.extend(pending_item_pool)
