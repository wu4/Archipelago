from typing import TYPE_CHECKING, override
from Options import Accessibility
import logging
from worlds.AutoWorld import WebWorld, World
from .options import CavernOfDreamsOptions
from .ap_generated.data import all_items, all_locations, item_groups
from .ap_generated.regions import create_regions
from .item_rando import create_items, get_pre_fill_items
from .items import CavernOfDreamsItem, CavernOfDreamsEvent

if TYPE_CHECKING:
    from BaseClasses import Region

all_items_with_extras = all_items

all_locations_with_extras = all_locations

logger = logging.getLogger("Cavern of Dreams")

class CavernOfDreamsWorld(World):
    """Cavern of Dreams"""

    options_dataclass = CavernOfDreamsOptions
    options: CavernOfDreamsOptions

    game = "Cavern of Dreams"
    # settings: ClassVar[MetroidPrimeSettings]
    topology_present = True

    #           lost leaf :)
    base_id = 0x1057_1eaf

    item_name_to_id = {name: id for
                       id, name in enumerate(all_items_with_extras, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(all_locations_with_extras, base_id)}

    item_name_groups = item_groups

    # remove_from_start_inventory: list[str]
    # starting_items: Counter[str]

    @override
    def create_regions(self):
        create_regions(self)
        # visualize_regions(
        #     self.get_region("Menu"),
        #     "wew.puml",
        #     show_other_regions = False
        # )

    create_items = create_items
    get_pre_fill_items = get_pre_fill_items

    @override
    def generate_early(self) -> None:
        if not (self.options.shroomsanity and self.options.eventsanity):
            self.multiworld.accessibility[self.player].value = Accessibility.option_minimal
            logger.warning(f"accessibility forced to 'minimal' for player {self.multiworld.get_player_name(self.player)} due to shroomsanity and/or eventsanity settings")

    @override
    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    @override
    def create_item(self, name: str) -> CavernOfDreamsItem:
        return CavernOfDreamsItem(name, self.item_name_to_id[name], self.player)

    def create_event(self, name: str, skippable: bool = False) -> CavernOfDreamsEvent:
        return CavernOfDreamsEvent(name, self.player, skippable)

    def create_nothing(self):
        return self.create_event("Nothing", True)

    # set_rules = generated.rules.set_rules

