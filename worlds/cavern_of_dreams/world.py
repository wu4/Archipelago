from typing import TYPE_CHECKING, TextIO
from collections.abc import Iterator
from Options import Accessibility
import logging
from worlds.AutoWorld import WebWorld, World
from .options import CavernOfDreamsOptions
from .ap_generated.data import all_items, all_locations, item_groups
from .ap_generated.regions import create_regions
from . import item_rando
from .items import CavernOfDreamsItem, CavernOfDreamsEvent
from .regions import get_all_paths

if TYPE_CHECKING:
    from BaseClasses import Region, CollectionState, PathValue

all_items_with_extras = all_items + ["Nothing"]

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

    def create_regions(self):
        create_regions(self)
        # visualize_regions(
        #     self.get_region("Menu"),
        #     "wew.puml",
        #     show_other_regions = False
        # )

    create_items = item_rando.create_items
    get_pre_fill_items = item_rando.get_pre_fill_items

    def post_fill(self) -> None:
        return super().post_fill()

    def fill_slot_data(self):# -> Mapping[str, Any]:
        return {
            "splitGratitude": self.options.gratitudesanity == 2
        }

    def generate_early(self) -> None:
        if not (self.options.shroomsanity and self.options.eventsanity):
            self.multiworld.accessibility[self.player].value = Accessibility.option_minimal
            logger.warning(f"accessibility forced to 'minimal' for player {self.multiworld.get_player_name(self.player)} due to shroomsanity and/or eventsanity settings")

    def set_rules(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_item(self, name: str) -> CavernOfDreamsItem:
        return CavernOfDreamsItem(name, self.item_name_to_id[name], self.player)

    def create_event(self, name: str, skippable: bool = False) -> CavernOfDreamsEvent:
        return CavernOfDreamsEvent(name, self.player, skippable)

    def create_nothing(self):
        return self.create_item("Nothing")

    @staticmethod
    def get_spoiler_path(state: "CollectionState", region: "Region") -> list[tuple[str, str] | tuple[str, None]]:
        from itertools import zip_longest

        def flist_to_iter(path_value: "PathValue | None") -> Iterator[str]:
            while path_value:
                region_or_entrance, path_value = path_value
                yield region_or_entrance

        all_paths = get_all_paths(state, region.player)
        # menu = state.multiworld.get_region('Menu', player)
        result = next(filter(lambda r: region in r[1], all_paths.items()), None)
        if result is None:
            raise KeyError(f"unable to find valid path for {region}")
        start, paths = result

        reversed_path_as_flist: PathValue = paths.get(region, (str(region), None))
        string_path_flat = reversed(list(map(str, flist_to_iter(reversed_path_as_flist))))
        # Now we combine the flat string list into (region, exit) pairs
        pathsiter = iter(string_path_flat)
        pathpairs = zip_longest(pathsiter, pathsiter)
        ret = list(pathpairs)
        if start.name != "Menu":
            ret = CavernOfDreamsWorld.get_spoiler_path(state, start) + ret
        return ret

    # set_rules = generated.rules.set_rules

