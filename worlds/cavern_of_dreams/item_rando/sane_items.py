from collections.abc import Generator
from typing import TYPE_CHECKING, Any

from ..options import AirSwim, SuperBounce, SuperBubbleJump
from ..ap_generated.data import location_groups, vanilla_locations

if TYPE_CHECKING:
    from ..world import CavernOfDreamsWorld

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
    if self.options.super_bounce == SuperBounce.option_enable:
        yield "Super Bounce"
    if self.options.air_swim == AirSwim.option_enable:
        yield "Air Swim"
    if self.options.super_bubble_jump == SuperBubbleJump.option_enable:
        yield "Super Bubble Jump"

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

def precollect_and_place_sane_items(self: "CavernOfDreamsWorld") -> Generator[str, None, None]:
    for item_name in _get_unshuffled_vanilla_abilities(self):
        self.multiworld.push_precollected(self.create_item(item_name))

    for location in _get_sane_locations(self):
        vanilla_item_name = vanilla_locations[location]

        item = self.create_item(vanilla_item_name)
        vanilla_location = self.multiworld.get_location(location, self.player)
        vanilla_location.place_locked_item(item)

        yield vanilla_item_name
