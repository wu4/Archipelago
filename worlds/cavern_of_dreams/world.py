from collections.abc import Generator, Iterable, Iterator, Sequence
from Options import Accessibility
import logging
from worlds.AutoWorld import WebWorld, World

from .entrance_rando import create_and_link_entrances
from .carryables import CavernOfDreamsCarryable
from .state_patches import add_carryable_source, add_region_entries, remove_carryable_source
from .options import Carryablesanity, CavernOfDreamsOptions, ExcludeWings, IncludeDoubleJump, ShuffleSwim, SplitTail
from .ap_generated.data import all_items, all_locations, item_groups
from .ap_generated.regions import create_regions as generated_create_regions
from . import item_rando
from .items import CavernOfDreamsItem, CavernOfDreamsEvent

from typing import TYPE_CHECKING, TypeVar
if TYPE_CHECKING:
    from BaseClasses import Region, CollectionState, PathValue, Item, Location, MultiWorld

all_items_with_extras = all_items + ["Nothing"]

all_locations_with_extras = all_locations

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
                       id, name in enumerate(unique_only(all_items_with_extras), base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(all_locations_with_extras, base_id)}

    item_name_groups = item_groups

    # remove_from_start_inventory: list[str]
    # starting_items: Counter[str]

    def __init__(self, multiworld: "MultiWorld", player: int):
        self.carryable_locations = []
        self.entrance_map = []
        super().__init__(multiworld, player)

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        name = self.collect_item(state, item)
        if not name: return False

        if isinstance(item, CavernOfDreamsCarryable):
            remove_carryable_source(state, self.player, item.location.parent_region, item.carryable)
            return True

        if item.name in item_groups["Egg"]:
            state.prog_items[self.player]["Egg"] -= 1
        elif item.name in item_groups["Shroom"]:
            state.prog_items[self.player]["Shroom"] -= 1

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

        if item.name in item_groups["Egg"]:
            state.prog_items[self.player]["Egg"] += 1
        elif item.name in item_groups["Shroom"]:
            state.prog_items[self.player]["Shroom"] += 1

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
            "dropCarryables": self.options.carryablesanity == Carryablesanity.option_kind,
            "pityItems": self.pity_items
        }

    def generate_early(self) -> None:
        if not self.options.shuffle_abilities:
            if self.options.split_tail:
                self.options.split_tail.value = SplitTail.option_false
                logger.warning(f"split tail disabled for player {self.multiworld.get_player_name(self.player)} due to ability shuffle being disabled")

        if self.options.entrance_rando:
            if self.options.accessibility != Accessibility.option_minimal:
                self.options.accessibility.value = Accessibility.option_minimal
                logger.warning(f"accessibility forced to 'minimal' for player {self.multiworld.get_player_name(self.player)} due to entrance rando")
        elif self.options.carryablesanity == Carryablesanity.option_mean:
            if self.options.accessibility != Accessibility.option_minimal:
                self.options.accessibility.value = Accessibility.option_minimal
                logger.warning(f"accessibility forced to 'minimal' for player {self.multiworld.get_player_name(self.player)} due to carryablesanity settings")

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
