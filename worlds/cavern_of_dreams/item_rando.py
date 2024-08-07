from collections.abc import Generator
import logging
from typing import TYPE_CHECKING, Any, Counter

from Fill import fill_restrictive
from worlds.cavern_of_dreams.custom_start_location import needs_starting_swim
from worlds.cavern_of_dreams.options import AirSwim, BubbleJump, Carryablesanity, Difficulty, Gratitudesanity, StartLocation, SuperBounce, SuperBubbleJump
from .ap_generated.data import item_groups, location_groups, all_items, vanilla_locations

all_items_as_set = set(all_items)
logger = logging.getLogger("Cavern of Dreams")

if TYPE_CHECKING:
    from BaseClasses import Item
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
    if self.options.super_bounce == SuperBounce.option_enable:
        yield "Super Bounce"
    if self.options.air_swim == AirSwim.option_enable:
        yield "Air Swim"
    if self.options.super_bubble_jump == SuperBubbleJump.option_enable:
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

    if self.options.super_bounce == SuperBounce.option_disable:
        yield "Super Bounce"

    if self.options.air_swim == AirSwim.option_disable:
        yield "Air Swim"

    if self.options.super_bubble_jump == SuperBubbleJump.option_disable:
        yield "Super Bubble Jump"

    if self.options.gratitudesanity != Gratitudesanity.option_split:
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

def get_pre_fill_items(self: "CavernOfDreamsWorld") -> list["Item"]:
    ret: list[Item] = []
    if self.options.carryablesanity != Carryablesanity.option_disable:
        ret.extend([self.create_item(item) for item in all_carryable_items()])
    return ret

def pre_fill(self: "CavernOfDreamsWorld"):
    if self.options.carryablesanity != Carryablesanity.option_disable:
        _fill_carryablesanity(self)

def _match_pool_size_with_locations(self: "CavernOfDreamsWorld", pending_item_pool: list["Item"]):
    pool_size = len(pending_item_pool)
    location_count = len(self.multiworld.get_unfilled_locations(self.player))
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

def get_restrictive_start_items(self: "CavernOfDreamsWorld"):
    if self.options.shuffle_abilities:
        if self.options.split_tail:
            yield "Grounded Tail"
            yield "Aerial Tail"
        else:
            yield "Tail"
        if self.options.bubble_jump != BubbleJump.option_disable:
            yield "Bubble"
        yield "Horn"
        yield "Wings"

    if self.options.shuffle_high_jump:
        yield "High Jump"

    if self.options.start_location == StartLocation.option_prismic_lobby:
        if self.options.entrance_rando:
            yield "Swim"

    elif self.options.start_location == StartLocation.option_prismic_palace:
        yield "Sprint"

    elif self.options.start_location == StartLocation.option_sun_cavern:
        yield "Bricked Egg"

        if self.options.shroomsanity:
            if self.options.shuffle_climb:
                yield "Climb"

        if self.options.gratitudesanity == Gratitudesanity.option_enable:
            for item in item_groups["Gratitude"]:
                yield item
        elif self.options.gratitudesanity == Gratitudesanity.option_split:
            for item in item_groups["Teleport"]:
                yield item

def _fill_carryablesanity(world: "CavernOfDreamsWorld"):
    carryables = Counter(all_carryable_items())

    if world.options.carryablesanity == Carryablesanity.option_kind:
        pass

    carryables_to_rando: list[Item] = []
    for carryable_name in carryables:
        while carryables[carryable_name] > 0:
            carryables[carryable_name] -= 1
            carryables_to_rando.append(world.create_item(carryable_name))

    state = world.multiworld.get_all_state(False)
    world.random.shuffle(world.carryable_locations)

    fill_restrictive(
        world.multiworld,
        state,
        world.carryable_locations,
        carryables_to_rando,
        single_player_placement=True,
        name="Carryablesanity"
    )

def _get_pity_items(self: "CavernOfDreamsWorld"):
    """
    BK is guaranteed in a lot of restrictive starts based on the starting
    location. This is just a way of reducing the chances.
    """
    start = self.options.start_location

    if needs_starting_swim(self.options):
        if self.options.shuffle_swim:
            yield "Swim"

    if start == StartLocation.option_lostleaf_crypt:
        possible_outcomes: list[list[str]] = []

        if self.options.split_tail:
            if self.options.ground_tail_jump:
                possible_outcomes.append(["Grounded Tail"])
            else:
                possible_outcomes.append(["Aerial Tail"])
        else:
            if self.options.ground_tail_jump or self.options.air_tail_jump:
                possible_outcomes.append(["Tail"])

        climb_template: list[str] = []
        if self.options.shuffle_climb:
            climb_template.append("Climb")

        possible_outcomes.append([*climb_template, "Horn"])

        if self.options.include_double_jump:
            if self.options.difficulty != Difficulty.option_beginner:
                possible_outcomes.append([*climb_template, "Double Jump"])
            else:
                possible_outcomes.append([*climb_template, "Double Jump", "Bubble"])

        for item in self.random.choice(possible_outcomes):
            yield item

    if self.options.entrance_rando:
        if start == StartLocation.option_armada_fire_drone:
            yield "Bubble"
    else:
        if start == StartLocation.option_armada_water_drone:
            if self.options.shuffle_carry:
                yield "Carry"

always_restrictive: list[int] = [
    StartLocation.option_gallery_water,
    StartLocation.option_heavens_gate,
    StartLocation.option_lostleaf_crypt,
]

shroomless_restrictive: list[int] = [
    StartLocation.option_sun_cavern,
    StartLocation.option_prismic_valley,
    StartLocation.option_prismic_palace,
    StartLocation.option_prismic_lobby
]

def _is_restrictive_start(self: "CavernOfDreamsWorld"):
    if self.options.shroomsanity:
        return self.options.start_location.value in always_restrictive
    else:
        return self.options.start_location.value in [*always_restrictive, *shroomless_restrictive]

def _place_sane_items(self: "CavernOfDreamsWorld"):
    for location in _get_sane_locations(self):
        vanilla_item_name = vanilla_locations[location]

        item = self.create_item(vanilla_item_name)
        vanilla_location = self.multiworld.get_location(location, self.player)
        vanilla_location.place_locked_item(item)

        yield vanilla_item_name

def create_items(self: "CavernOfDreamsWorld"):
    exclude = Counter(_get_excluded_items(self))
    unshuffled_vanilla_abilities = Counter(_get_unshuffled_vanilla_abilities(self))

    self.pity_items = list(_get_pity_items(self))
    for item_name in self.pity_items:
        self.multiworld.push_precollected(self.create_item(item_name))

    for item_name in unshuffled_vanilla_abilities.elements():
        self.multiworld.push_precollected(self.create_item(item_name))

    if _is_restrictive_start(self):
        restrictive_start_items = [*get_restrictive_start_items(self)]
        if restrictive_start_items != []:
            start_item = self.random.choice(restrictive_start_items)
            self.multiworld.local_early_items[self.player][start_item] = 1
        else:
            logger.warning(f"restrictive start detected, but no possible restrictive start items for player {self.multiworld.get_player_name(self.player)}")

    exclude += Counter(_place_sane_items(self))

    exclude.update(item.name for item in self.get_pre_fill_items())

    exclude.update(item.name for item in self.multiworld.precollected_items[self.player])

    pending_item_pool = [
        self.create_item(item)
        for item in (Counter(all_items) - exclude).elements()
    ]

    _match_pool_size_with_locations(self, pending_item_pool)

    self.multiworld.itempool.extend(pending_item_pool)
