from worlds.AutoWorld import WebWorld, World
from .options import CavernOfDreamsOptions
from .logic import level_data
from .generated.data import all_items, all_locations
from collections import Counter

class CavernOfDreamsWorld(World):
    """Cavern of Dreams"""

    options_dataclass = CavernOfDreamsOptions
    #options: CavernOfDreamsOptions

    game = "Cavern of Dreams"
    # settings: ClassVar[MetroidPrimeSettings]
    topology_present = True

    #           lost leaf :)
    base_id = 0x1057_1eaf

    item_name_to_id = {name: id for
                       id, name in enumerate(all_items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(all_locations, base_id)}

    item_name_groups = {}

    remove_from_start_inventory: list[str]
    starting_items: Counter[str]

    # create_regions = generated.regions.create_regions_and_events

    # set_rules = generated.rules.set_rules
