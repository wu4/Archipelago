from collections import deque
from collections.abc import Generator, Iterable
import logging
from typing import TYPE_CHECKING, Any, Callable, Counter

from BaseClasses import ItemClassification
from Fill import fill_restrictive
from ..custom_start_location import needs_starting_swim
from .restrictive_starts import process_restrictive_starts
from ..options import AirSwim, Carryablesanity, Difficulty, Gratitudesanity, Shroomsanity, StartLocation, SuperBounce, SuperBubbleJump
from ..ap_generated.data import item_groups, location_groups, all_items, vanilla_locations
from .sane_items import precollect_and_place_sane_items

all_items_as_set = set(all_items)
logger = logging.getLogger("Cavern of Dreams")

if TYPE_CHECKING:
    from BaseClasses import Item
    from ..world import CavernOfDreamsWorld

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

def get_pre_fill_items(self: "CavernOfDreamsWorld") -> list["Item"]:
    ret: list[Item] = []
    if self.options.carryablesanity != Carryablesanity.option_disable:
        ret.extend([self.create_item(item) for item in _all_carryable_items()])
    return ret

def pre_fill(self: "CavernOfDreamsWorld"):
    if self.options.carryablesanity != Carryablesanity.option_disable:
        _fill_carryablesanity(self)

kind_shuffle: list[tuple[list[str], list[str]]] = [
    # Deep Woods
    (["Apple"], [
        "Lostleaf Lake - Deep Woods Apple",
        "Lostleaf Lake - Deep Woods Jester Boots",
    ]),
    # ("Jester Boots", [
    #     "Lostleaf Lake - Deep Woods Apple",
    #     "Lostleaf Lake - Deep Woods Jester Boots",
    # ]),

    # Kerrington's boils
    (["Medicine"], [
        "Kerrington - Rain Medicine",

        "Shroom: Kerrington - Rain Entryway 1",
        "Shroom: Kerrington - Rain Entryway 2",
        "Shroom: Kerrington - Rain Entryway 3",
        "Shroom: Kerrington - Rain Entryway 4",

        "Shroom: Kerrington - Rain Below Boiler 1",
        "Shroom: Kerrington - Rain Below Boiler 2",
        "Shroom: Kerrington - Rain Below Boiler 3",

        "Shroom: Kerrington - Rain Plant Base",
        "Shroom: Kerrington - Rain Plant 1",
        "Shroom: Kerrington - Rain Plant 2",
        "Shroom: Kerrington - Rain Plant 3",
        "Shroom: Kerrington - Rain Plant 4",

        "Shroom: Kerrington - Rain Below Medicine 1",
        "Shroom: Kerrington - Rain Below Medicine 2",
        "Shroom: Kerrington - Rain Below Medicine 3",

        "Shroom: Kerrington - Lab Rain Connector 1",
        "Shroom: Kerrington - Lab Rain Connector 2",
        "Shroom: Kerrington - Lab Rain Connector 3",
        "Shroom: Kerrington - Lab Rain Connector 4",
        "Shroom: Kerrington - Lab Rain Connector 5",
        "Shroom: Kerrington - Lab Rain Connector 6",
    ]),

    # growing a tree in Gallery Lobby
    (["Apple"], [
        "Egg: Gallery Lobby - Lostleaf Lobby Entryway"
    ]),

    # growing a tree in the crypt
    # (["Apple"], [
    #     "Egg: Crypt - Shelwart's Gravestone"
    # ]),

    # backside apple
    (["Apple"], [
        "Lostleaf Lake - Crypt Apple"
    ]),

    # The Gobbler!
    (["Apple"], [
        "Shroom: Valley - Poms 1",
        "Shroom: Valley - Poms 2",
        "Shroom: Valley - Poms 3",
        "Shroom: Valley - Poms 4",
        "Shroom: Valley - Poms 5",

        "Shroom: Valley - Entry Tree 1",
        "Shroom: Valley - Entry Tree 2",
        "Shroom: Valley - Entry Tree 3",

        "Card: Valley - Above Pool",

        "Card: Valley - Snowcastle",
        "Egg: Valley - Snowcastle",

        "Shroom: Valley - Jester Boots 1",
        "Shroom: Valley - Jester Boots 2",
        "Shroom: Valley - Jester Boots 3",
        "Shroom: Valley - Jester Boots 4",
        "Shroom: Valley - Jester Boots 5",

        "Valley - Jester Boots",

        "Shroom: Valley - Pom Spire 1",
        "Shroom: Valley - Pom Spire 2",
        "Shroom: Valley - Pom Spire 3",
        "Shroom: Valley - Pom Spire 4",
        "Shroom: Valley - Pom Spire 5",

        "Shroom: Valley - Observatory Spire 1",
        "Shroom: Valley - Observatory Spire 2",
        "Shroom: Valley - Observatory Spire 3",
        "Shroom: Valley - Observatory Spire 4",
        "Shroom: Valley - Observatory Spire 5",

        "Lady Opal's Egg: Castle",

        "Card: Valley - Top of Observatory",

        "Card: Valley - Top of Palace",
        "Egg: Valley - Top of the Palace",

        "Shroom: Valley - Lake Corner 1",
        "Shroom: Valley - Lake Corner 2",
        "Shroom: Valley - Lake Corner 3",

        "Shroom: Valley - Lake Plants 1",
        "Shroom: Valley - Lake Plants 2",
        "Shroom: Valley - Lake Plants 3",
        "Shroom: Valley - Lake Plants 4",
        "Shroom: Valley - Lake Plants 5",
        "Shroom: Valley - Lake Plants 6",

        "Shroom: Valley - Lake Behind 1",
        "Shroom: Valley - Lake Behind 2",
        "Shroom: Valley - Lake Behind 3",

        "Shroom: Valley - Lake Gobbler 1",
        "Shroom: Valley - Lake Gobbler 2",
        "Shroom: Valley - Lake Gobbler 3",
    ]),

    # Sage's painting
    (["Sage's Gloves"], [
        "Card: Foyer - Water Lobby Entrance",
        "Egg: Foyer - Matryoshka Egg"
    ]),

    # Shelnert's painting
    (["Shelnert's Fish"], [
        "Card: Earth Lobby - Swamp Castle",
        "Egg: Earth Lobby - Skull's Eye",
        "Card: Earth Lobby - Swamp",
    ]),

    # Mr. Kerrington's painting
    (["Mr. Kerrington's Wings"], [
        "Fire Lobby - Shelnert's Fish",
        "Egg: Fire Lobby - Mr. Kerrington Painting"
    ]),

    # Flying to Water Drone
    (["Mr. Kerrington's Wings", "Jester Boots"], [
        "Egg: Airborne Armada - Mr. Kerrington's Tail",

        "Card: Airborne Armada - Broken Wing",

        "Card: Airborne Armada - Behind Entry Drone",

        "Shroom: Airborne Armada - Bouncy Shroom 1",
        "Shroom: Airborne Armada - Bouncy Shroom 3",
        "Shroom: Airborne Armada - Bouncy Shroom 2",
        "Shroom: Airborne Armada - Bouncy Shroom 4",
        "Shroom: Airborne Armada - Entry Pathway 5",
        "Shroom: Airborne Armada - Front Entrance 1",
        "Shroom: Airborne Armada - Front Entrance 2",
        "Shroom: Airborne Armada - Front Entrance 3",
        "Shroom: Airborne Armada - Side 1",
        "Shroom: Airborne Armada - Side 2",
        "Shroom: Airborne Armada - Side Yellow Ledge",
        "Shroom: Airborne Armada - Back Entrance 1",
        "Shroom: Airborne Armada - Back Entrance 2",
        "Shroom: Airborne Armada - Back Entrance 3",
        "Shroom: Airborne Armada - Back Entrance 4",
        "Shroom: Airborne Armada - Back Entrance 6",
        "Shroom: Airborne Armada - Back Entrance 5",
        "Shroom: Airborne Armada - Topside 1",
        "Shroom: Airborne Armada - Topside 2",
        "Shroom: Airborne Armada - Topside 3",
        "Shroom: Airborne Armada - Entry Pathway 1",
        "Shroom: Airborne Armada - Entry Pathway 2",
        "Shroom: Airborne Armada - Entry Pathway 3",
        "Shroom: Airborne Armada - Entry Pathway 4",
    ]),

    # Accessing the Drown painting
    (["Jester Boots"], [
        "Water Lobby - Jester Boots",
        "Water Lobby - Lady Opal's Head",
        "Egg: Water Lobby - Deepest Darkness",
        "Card: Water Lobby - Sewer Bottom",
        "Egg: Water Lobby - Sewer"
    ]),

    # Armada Lobby Jester Boots
    (["Jester Boots"], [
        "Shroom: Armada Lobby - Cliffside 1",
        "Shroom: Armada Lobby - Cliffside 2",
        "Shroom: Armada Lobby - Cliffside 3",
        "Shroom: Armada Lobby - Cliffside 4",
        "Shroom: Armada Lobby - Cliffside 5",

        "Armada Lobby - Jester Boots",
    ]),

    # Lady Opal's painting
    (["Lady Opal's Head"], [
        "Water Lobby - Jester Boots",
        "Water Lobby - Lady Opal's Head",
        "Egg: Water Lobby - Deepest Darkness",
        "Card: Water Lobby - Sewer Bottom",
        "Egg: Water Lobby - Sewer"
    ]),
]

def _match_pool_size_with_locations(self: "CavernOfDreamsWorld", pending_item_pool: list["Item"]):
    pool_size = len(pending_item_pool)
    location_count = len(self.multiworld.get_unfilled_locations(self.player))
    diff = location_count - pool_size

    if self.options.carryablesanity:
        diff -= len(location_groups["Carryable"])

    while diff > 0:
        pending_item_pool.append(self.create_item("Shroom"))
        diff -= 1


    if diff < 0:
        deletion_marks: deque[int] = deque()

        is_shroomsanity = self.options.shroomsanity == Shroomsanity.option_true

        item_filter: Callable[[Item], bool]
        if is_shroomsanity:
            item_filter = lambda x: x.name == "Shroom"
        else:
            item_filter = lambda x: x.name.startswith("Card:")

        for i, item in enumerate(pending_item_pool):
            if item_filter(item):
                deletion_marks.appendleft(i)
                diff += 1
                if diff == 0:
                    break

        for i in deletion_marks:
            del pending_item_pool[i]

def _all_carryable_items():
    for location in location_groups["Carryable"]:
        yield vanilla_locations[location]

def _fill_carryablesanity(world: "CavernOfDreamsWorld"):
    carryables = Counter(_all_carryable_items())

    locations_placed: list[str] = []

    def try_place_carryable(carryable_name: str, location_name: str):
        location = world.multiworld.get_location(location_name, world.player)
        if location.item is not None: return False

        location.place_locked_item(world.create_item(carryable_name))
        locations_placed.append(location_name)
        carryables[carryable_name] -= 1

        return True

    assert try_place_carryable("Jester Boots", "Lostleaf Lake - Deep Woods Jester Boots")

    # force_vanilla_deep_woods = world.options.carryablesanity == Carryablesanity.option_mean and not world.options.jester_boots_slope_movement
    # if force_vanilla_deep_woods:
    #     place_carryable("Apple", "Lostleaf Lake - Deep Woods Apple")

    if world.options.carryablesanity == Carryablesanity.option_kind:
        # if not world.options.carry_through_doors:
        #     del world.multiworld.regions.region_cache[world.player]["LAKE.Crypt.EggSoil.PlantableSoil"]
        #     del world.multiworld.regions.location_cache[world.player]["LAKE.Crypt.EggSoil"]

        for carryable_names, location_names in kind_shuffle:
            if not world.options.shroomsanity:
                location_names = list(filter(lambda x: not x.startswith("Shroom:"), location_names))
            location_names = list(filter(lambda location: location not in locations_placed, location_names))
            result = False
            while not result:
                result = try_place_carryable(world.random.choice(carryable_names), world.random.choice(location_names))

    carryables_to_rando: list[Item] = []
    for carryable_name in carryables:
        while carryables[carryable_name] > 0:
            carryables[carryable_name] -= 1
            carryables_to_rando.append(world.create_item(carryable_name))

    state = world.multiworld.get_all_state(False)

    carryable_locations = list(filter(lambda x: x.name not in locations_placed, world.carryable_locations))

    world.random.shuffle(carryable_locations)

    fill_restrictive(
        world.multiworld,
        state,
        carryable_locations,
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

# def _make_first_shrooms_progression(items: Iterable[str], count: int):
#     for item in items:
#         if item == "Shroom" and count > 0:
#             yield "Progression Shroom"
#             count -= 1
#             continue
#         yield item

def create_items(self: "CavernOfDreamsWorld"):
    exclude = Counter(_get_excluded_items(self))

    self.pity_items = list(_get_pity_items(self))
    for item_name in self.pity_items:
        self.multiworld.push_precollected(self.create_item(item_name))

    process_restrictive_starts(self)

    exclude += Counter(precollect_and_place_sane_items(self))

    exclude.update(item.name for item in self.get_pre_fill_items())

    exclude.update(item.name for item in self.multiworld.precollected_items[self.player])

    pending_item_pool = [
        self.create_item(item)
        for item in (Counter(all_items) - exclude).elements()
    ]

    _match_pool_size_with_locations(self, pending_item_pool)

    self.multiworld.itempool.extend(pending_item_pool)
