import logging
from typing import TYPE_CHECKING

from ..options import BubbleJump, Gratitudesanity, StartLocation
from ..ap_generated.data import item_groups

logger = logging.getLogger("Cavern of Dreams")

if TYPE_CHECKING:
    from ..world import CavernOfDreamsWorld

_always_restrictive: list[int] = [
    StartLocation.option_gallery_water,
    StartLocation.option_heavens_gate,
    StartLocation.option_lostleaf_crypt,
]

_shroomless_restrictive: list[int] = [
    StartLocation.option_sun_cavern,
    StartLocation.option_prismic_valley,
    StartLocation.option_prismic_palace,
    StartLocation.option_prismic_lobby
]

def _is_restrictive_start(self: "CavernOfDreamsWorld"):
    if self.options.shroomsanity:
        return self.options.start_location.value in _always_restrictive
    else:
        return self.options.start_location.value in [*_always_restrictive, *_shroomless_restrictive]

def _get_restrictive_start_items(self: "CavernOfDreamsWorld"):
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

def process_restrictive_starts(self: "CavernOfDreamsWorld"):
    if not _is_restrictive_start(self): return

    restrictive_start_items = [*_get_restrictive_start_items(self)]
    if restrictive_start_items != []:
        start_item = self.random.choice(restrictive_start_items)
        self.multiworld.local_early_items[self.player][start_item] = 1
    else:
        logger.warning(f"restrictive start detected, but no possible restrictive start items for player {self.multiworld.get_player_name(self.player)}")
