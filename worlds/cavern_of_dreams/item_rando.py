from typing import TYPE_CHECKING

from .ap_generated.data import item_groups, all_items, vanilla_locations_by_name

all_items_as_set = set(all_items)

if TYPE_CHECKING:
    from BaseClasses import Item
    from .world import CavernOfDreamsWorld
    from .items import CavernOfDreamsItem


def _place_in_vanilla_location(self: "CavernOfDreamsWorld", item: "CavernOfDreamsItem"):
    vanilla_location = self.multiworld.get_location(vanilla_locations_by_name[item.name], self.player)
    vanilla_location.place_locked_item(item)


def _get_unshuffled_vanilla_abilities(self: "CavernOfDreamsWorld"):
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


def _get_excluded_items(self: "CavernOfDreamsWorld"):
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


def _get_sane_items(self: "CavernOfDreamsWorld"):
    if not self.options.shuffle_abilities:
        for item in item_groups["Ability"]:
            yield item
    if not self.options.shroomsanity:
        for item in item_groups["Shroom"]:
            yield item
    if not self.options.eventsanity:
        for item in item_groups["Event"]:
            yield item
    if self.options.gratitudesanity == 0:
        for item in item_groups["Gratitude"]:
            yield item


def _match_pool_size_with_locations(self: "CavernOfDreamsWorld", pending_item_pool: list["Item"]):
    pool_size = len(pending_item_pool)
    location_count = len(list(self.multiworld.get_unfilled_locations(self.player)))
    diff = pool_size - location_count

    while diff > 0:
        for item in pending_item_pool:
            if item.name in item_groups["Card"]:
                pending_item_pool.remove(item)
                break
        diff -= 1

    while diff < 0:
        pending_item_pool.append(self.create_nothing())
        diff += 1


def get_pre_fill_items(self: "CavernOfDreamsWorld"):
    return []
    # return list(map(self.create_item, _get_sane_items(self)))


def create_items(self: "CavernOfDreamsWorld"):
    exclude = set(_get_excluded_items(self))
    unshuffled_vanilla_abilities = set(_get_unshuffled_vanilla_abilities(self))
    sane_items = set(_get_sane_items(self))

    pending_item_pool: list["Item"] = []

    for item in map(self.create_item, unshuffled_vanilla_abilities.difference(exclude)):
        self.multiworld.push_precollected(item)

    for item in map(self.create_item, sane_items.difference(exclude)):
        _place_in_vanilla_location(self, item)

    exclude.update(sane_items)

    # unsure if this is any different from exclude.update(unshuffled_vanilla_abilities)
    exclude.update(item.name for item in self.multiworld.precollected_items[self.player])

    for item in map(self.create_item, all_items_as_set.difference(exclude)):
        pending_item_pool.append(item)

    _match_pool_size_with_locations(self, pending_item_pool)

    self.multiworld.itempool.extend(pending_item_pool)
