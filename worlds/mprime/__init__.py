from typing import ClassVar

from BaseClasses import MultiWorld, Region, ItemClassification
from worlds.AutoWorld import World
from .Settings import MetroidPrimeSettings
from . import data
from .Utils import region_format
from .Locations import locations, MetroidPrimeLocation
from .Items import items, MetroidPrimeItem, events_short_to_long

from . import Logic

def is_progression(name: str) -> bool:
    return not name in ["Energy Tank", "Missile", "Power Bomb"]

class MetroidPrimeWorld(World):
    """Metroid Prime"""

    option_definitions = data.options
    game = "Metroid Prime"
    settings: ClassVar[MetroidPrimeSettings]
    topology_present = True

    base_id = 0xbad_babe

    item_name_to_id = {name: id for
                       id, name in enumerate(items, base_id)}
    location_name_to_id = {name: id for
                           id, name in enumerate(locations, base_id)}

    item_name_groups = {}

    def create_regions(self) -> None:
        menu_region = Region("Menu", self.player, self.multiworld)
        self.multiworld.regions.append(menu_region)
        
        for region_name, region in data.regions.items():
            for area_name, area in region.items():
                for node_name, node in area.items():
                    if not "default" in node.layers: continue

                    location_name = region_format(node_name, area_name, region_name)
                    this_region = Region(location_name, self.player, self.multiworld)
                    self.multiworld.regions.append(this_region)
                    if isinstance(node, data.PickupNode):
                        this_location = MetroidPrimeLocation(
                            self.player,
                            location_name,
                            MetroidPrimeWorld.location_name_to_id[location_name],
                            this_region
                        )
                        this_region.locations.append(this_location)
                    elif isinstance(node, data.EventNode):
                        this_location = MetroidPrimeLocation(
                            self.player,
                            location_name,
                            None,
                            this_region
                        )
                        this_region.locations.append(this_location)

    def set_rules(self) -> None:
        menu_region = self.multiworld.get_region("Menu", self.player)
        menu_region.add_exits({
            region_format("Ship", "Landing Site", "Tallon Overworld"):
                "Start Game"
        })
        for region_name, region in data.regions.items():
            for area_name, area in region.items():
                for node_name, node in area.items():
                    if not "default" in node.layers: continue

                    location_name = region_format(node_name, area_name, region_name)
                    this_region = self.multiworld.get_region(location_name, self.player)
                    
                    if isinstance(node, data.DockNode):
                        connection_name = node.default_connection["node"]
                        connection_location_name = region_format(connection_name, node.default_connection["area"], node.default_connection["region"])
                        this_region.add_exits(
                            {
                                connection_location_name:
                                    f"{node_name} to {connection_name} ({area_name}, {region_name})"
                            },
                            {
                                connection_location_name:
                                    node.default_connection_rule(self.player)
                            }
                        )
                    
                    for connection_name, logic_generator in node.connections.items():
                        connection_location_name = region_format(connection_name, area_name, region_name)
                        this_region.add_exits(
                            {
                                connection_location_name:
                                    f"{node_name} to {connection_name} ({area_name}, {region_name})"
                            },
                            {
                                connection_location_name:
                                    logic_generator(self.player)
                            }
                        )

    def generate_basic(self) -> None:
        # place "Victory" at "Final Boss" and set collection as win condition
        endgame_location = self.multiworld.get_location("Event - Credits (Credits, End of Game)", self.player)
        event = self.create_event(events_short_to_long["Event43"])
        endgame_location.place_locked_item(event)
        self.multiworld.completion_condition[self.player] = lambda state: state.has("Victory", self.player)

    def create_item(self, name: str) -> MetroidPrimeItem:
        print(name)
        classification = ItemClassification.progression if is_progression(name) else \
                         ItemClassification.filler
        return MetroidPrimeItem(name, classification, self.item_name_to_id[name], self.player)
    
    def create_items(self) -> None:
        # Add items to the Multiworld.
        # If there are two of the same item, the item has to be twice in the pool.
        # Which items are added to the pool may depend on player settings,
        # e.g. custom win condition like triforce hunt.
        # Having an item in the start inventory won't remove it from the pool.
        # If an item can't have duplicates it has to be excluded manually.
        self.multiworld.precollected_items[self.player].append(self.create_item("Power Beam"))
        self.multiworld.precollected_items[self.player].append(self.create_item("Combat Visor"))
        self.multiworld.precollected_items[self.player].append(self.create_item("Scan Visor"))
        self.multiworld.precollected_items[self.player].append(self.create_item("Power Suit"))

        # List of items to exclude, as a copy since it will be destroyed below
        exclude = [item for item in self.multiworld.precollected_items[self.player]]

        item_count = 0
        for item in map(self.create_item, items):
            if item in exclude:
                exclude.remove(item)  # this is destructive. create unique list above
                # self.multiworld.itempool.append(self.create_item("Nothing"))
            else:
                self.multiworld.itempool.append(item)
                item_count += 1
                if item.name == "Energy Tank":
                    for i in range(13):
                        self.multiworld.itempool.append(self.create_item(item.name))
                        item_count += 1
                elif item.name == "Missile":
                    for i in range(40):
                        self.multiworld.itempool.append(self.create_item(item.name))
                        item_count += 1
                elif item.name == "Power Bomb":
                    for i in range(7):
                        self.multiworld.itempool.append(self.create_item(item.name))
                        item_count += 1
                        

        # itempool and number of locations should match up.
        # If this is not the case we want to fill the itempool with junk.
        junk = item_count - (len(locations) - 1)  # calculate this based on player settings
        self.multiworld.itempool += [self.create_item("Nothing") for _ in range(junk)]
        

    def create_event(self, event: str):
        # while we are at it, we can also add a helper to create events
        return MetroidPrimeItem(event, ItemClassification.progression, None, self.player)
