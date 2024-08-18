from collections.abc import Generator, Iterable, Iterator, Sequence
from Options import Accessibility, DeathLink
import logging
from worlds.AutoWorld import WebWorld, World

from .entrance_rando import create_and_link_entrances
from .carryables import CavernOfDreamsCarryable
from .state_patches import add_carryable_source, add_region_entries, remove_carryable_source
from .options import Carryablesanity, CavernOfDreamsOptions, ExcludeWings, Gratitudesanity, IncludeDoubleJump, ShuffleSwim, SplitTail
from .ap_generated.data import all_items, all_locations, item_groups
from .ap_generated.regions import create_regions as generated_create_regions
from . import item_rando
from .items import CavernOfDreamsItem, CavernOfDreamsEvent

from typing import TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
    from BaseClasses import Region, CollectionState, PathValue, Item, Location, MultiWorld

logger = logging.getLogger("Cavern of Dreams")

T = TypeVar("T")

def unique_only(ts: Iterable[T]) -> Sequence[T]:
  ret: list[T] = []
  for t in ts:
    if not t in ret:
      ret.append(t)
  return ret


class CavernOfDreamsWorld(World):
    """Cavern of Dreams"""

    options_dataclass = CavernOfDreamsOptions
    options: CavernOfDreamsOptions

    carryable_locations: list["Location"]
    pity_items: list[str]

    game = "Cavern of Dreams"
    # settings: ClassVar[MetroidPrimeSettings]
    topology_present = False
    entrance_map: list[tuple[str, str]]

    #           lost leaf :)
    base_id = 0x1057_1eaf

    item_name_to_id = {name: id for
                       id, name in enumerate(unique_only(all_items), base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(all_locations, base_id)}

    item_name_groups = item_groups

    # remove_from_start_inventory: list[str]
    # starting_items: Counter[str]

    def __init__(self, multiworld: "MultiWorld", player: int):
        self.carryable_locations = []
        self.entrance_map = []
        super().__init__(multiworld, player)

    def _adjust_teleport_prog_item(self, gratitude_name: str, state: "CollectionState", amount: int):
        if gratitude_name == "Gratitude 1":
            teleport_name = "Lake"
        elif gratitude_name == "Gratitude 2":
            teleport_name = "Armada"
        elif gratitude_name == "Gratitude 3":
            teleport_name = "Palace"
        elif gratitude_name == "Gratitude 4":
            teleport_name = "Gallery"
        else:
            raise ValueError(f"unknown gratitude {gratitude_name}")

        state.prog_items[self.player][f"Open {teleport_name} Lobby Teleport"] += amount

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        name = self.collect_item(state, item)
        if not name: return False

        if isinstance(item, CavernOfDreamsCarryable):
            remove_carryable_source(state, self.player, item.location.parent_region, item.carryable)
            return True

        if self.options.gratitudesanity != Gratitudesanity.option_split and item.name in item_groups["Gratitude"]:
            self._adjust_teleport_prog_item(item.name, state, -1)

        if item.name in item_groups["Egg"]:
            state.prog_items[self.player]["Egg"] -= 1
        # elif item.name in item_groups["Shroom"]:
        #     state.prog_items[self.player]["Shroom"] -= 1

        state.prog_items[self.player][name] -= 1

        return True

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        name = self.collect_item(state, item)
        if not name: return False

        if isinstance(item, CavernOfDreamsCarryable):
            if item.location is not None:
                add_region_entries(state, item.location.parent_region.name, item.player)
                add_carryable_source(state, item.player, item.location.parent_region, item.carryable)
            return True

        if self.options.gratitudesanity != Gratitudesanity.option_split and item.name in item_groups["Gratitude"]:
            self._adjust_teleport_prog_item(item.name, state, 1)

        if item.name in item_groups["Egg"]:
            state.prog_items[self.player]["Egg"] += 1
        # elif item.name in item_groups["Shroom"]:
        #     state.prog_items[self.player]["Shroom"] += 1

        state.prog_items[self.player][name] += 1

        return True

    def create_regions(self):
        self.carryable_locations = generated_create_regions(self)

        self.entrance_map = create_and_link_entrances(self)

    create_items = item_rando.create_items
    get_pre_fill_items = item_rando.get_pre_fill_items
    pre_fill = item_rando.pre_fill

    def fill_slot_data(self):
        return {
            "splitGratitude": self.options.gratitudesanity == 2,
            "startLocation": str(self.options.start_location),
            "entranceMap": self.entrance_map,
            "dropCarryables": not self.options.carry_through_doors,
            "pityItems": self.pity_items,
            "allowFun": self.options.allow_fun.value == 1,
            "deathLink": self.options.death_link == DeathLink.option_true,
        }

    def generate_early(self) -> None:
        if not self.options.shuffle_abilities:
            if self.options.split_tail:
                self.options.split_tail.value = SplitTail.option_false
                logger.warning(f"split tail disabled for player {self.multiworld.get_player_name(self.player)} due to ability shuffle being disabled")

        if self.options.carryablesanity != Carryablesanity.option_kind and not self.options.carry_through_doors:
            self.options.carryablesanity.value = Carryablesanity.option_kind
            logger.warning(f"carryablesanity forced to 'kind' for player {self.multiworld.get_player_name(self.player)} due to carry_through_doors being disabled")
        if self.options.accessibility != Accessibility.option_minimal:
            minimal_reasons: list[str] = []
            if self.options.entrance_rando:
                minimal_reasons.append("entrance rando")
            if self.options.carryablesanity == Carryablesanity.option_mean:
                minimal_reasons.append("mean carryablesanity")

            if minimal_reasons != []:
                self.options.accessibility.value = Accessibility.option_minimal
                minimal_reasons_str = " and ".join(minimal_reasons)
                logger.warning(f"accessibility forced to 'minimal' for player {self.multiworld.get_player_name(self.player)} due to {minimal_reasons_str}")

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_item(self, name: str) -> "Item":
        if name in item_groups["Carryable"]:
            return CavernOfDreamsCarryable(name, self.item_name_to_id[name], self.player)
        return CavernOfDreamsItem(name, self.item_name_to_id[name], self.player)

    def create_event(self, name: str, skippable: bool = False) -> CavernOfDreamsEvent:
        return CavernOfDreamsEvent(name, self.player, skippable)

    def create_nothing(self):
        return self.create_item("Nothing")
