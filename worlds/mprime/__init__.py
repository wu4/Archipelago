from typing import ClassVar
from collections import Counter

from BaseClasses import Item
from worlds.AutoWorld import World
from .settings import MetroidPrimeSettings
from . import generated
from .generated import items, locations
# from .Extracted import set_rules, create_regions, items, locations
from .options import MetroidPrimeOptions
from .Items import MetroidPrimeItem, MetroidPrimeEvent
from .item_pool import generate_itempool

from . import logic

class MetroidPrimeWorld(World):
    """Metroid Prime"""

    options_dataclass = MetroidPrimeOptions
    options: MetroidPrimeOptions

    game = "Metroid Prime"
    settings: ClassVar[MetroidPrimeSettings]
    topology_present = True

    base_id = 0xbad_babe

    item_name_to_id = {name: id for
                       id, name in enumerate(items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(locations, base_id)}

    item_name_groups = {}

    remove_from_start_inventory: list[str]
    starting_items: Counter[str]

    create_regions = generated.create_regions_and_events

    set_rules = generated.set_rules

    def generate_basic(self) -> None:
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Credits", self.player)
    
    def generate_early(self) -> None:
        # from Options import Range, Toggle, VerifyKeys
        # for (option_name, option) in options.items():
        #     result = getattr(self.multiworld, option_name)[self.player]
        #     if isinstance(result, Range):
        #         option_value = int(result)
        #     elif isinstance(result, Toggle):
        #         option_value = bool(result)
        #     elif isinstance(result, VerifyKeys):
        #         option_value = result.value
        #     else:
        #         option_value = result.current_key
        #     setattr(self, option_name, option_value)

        return super().generate_early()

    def create_item(self, name: str) -> MetroidPrimeItem:
        return MetroidPrimeItem(name, self.item_name_to_id[name], self.player)

    def create_event(self, event: str, skippable: bool = False) -> MetroidPrimeEvent:
        return MetroidPrimeEvent(event, self.player, skippable)

    def create_items(self) -> None:
        self.remove_from_start_inventory = []

        generate_itempool(self, self.player)

        self.starting_items = Counter()
        removed_items = []
        for item in self.multiworld.precollected_items[self.player]:
            if item.name in self.remove_from_start_inventory:
                self.remove_from_start_inventory.remove(item.name)
                removed_items.append(item.name)
            else:
                self.starting_items[item.name] += 1
                # Call the junk fill and get a replacement
                if item in self.multiworld.itempool:
                    self.multiworld.itempool.remove(item)
                    self.multiworld.itempool.append(self.create_item("Nothing"))
