from typing import TYPE_CHECKING
from .Extracted import items, locations

if TYPE_CHECKING:
    from BaseClasses import MultiWorld
    from . import MetroidPrimeWorld

def generate_itempool(world: "MetroidPrimeWorld", player: int) -> None:
    # Add items to the Multiworld.
    # If there are two of the same item, the item has to be twice in the pool.
    # Which items are added to the pool may depend on player settings,
    # e.g. custom win condition like triforce hunt.
    # Having an item in the start inventory won't remove it from the pool.
    # If an item can't have duplicates it has to be excluded manually.
    
    # as far as I know, Power Suit doesn't really even do anything
    # Randovania doesn't allow it to be shuffled either
    # probably a placeholder for the future

    world.multiworld.push_precollected(world.create_item('Power Suit'))
    world.remove_from_start_inventory.append('Power Suit')

    if not world.shuffle_power_beam:
        world.multiworld.push_precollected(world.create_item('Power Beam'))
        world.remove_from_start_inventory.append('Power Beam')
    if not world.shuffle_combat_visor:
        world.multiworld.push_precollected(world.create_item('Combat Visor'))
        world.remove_from_start_inventory.append('Combat Visor')
    if not world.shuffle_scan_visor:
        world.multiworld.push_precollected(world.create_item('Scan Visor'))
        world.remove_from_start_inventory.append('Scan Visor')

    # List of items to exclude, as a copy since it will be destroyed below
    exclude = [item for item in world.multiworld.precollected_items[player]]
    
    junk_count = 0

    item_count = 0
    for item in map(world.create_item, items):
        if item in exclude:
            exclude.remove(item)  # this is destructive. create unique list above
            world.multiworld.itempool.append(world.create_item("Nothing"))
        else:
            world.multiworld.itempool.append(item)
            item_count += 1
            if item.name == "Energy Tank":
                for i in range(14-1):
                    world.multiworld.itempool.append(world.create_item(item.name))
                    item_count += 1
            elif item.name == "Missile":
                for i in range(40-1):
                    world.multiworld.itempool.append(world.create_item(item.name))
                    item_count += 1
            elif item.name == "Power Bomb":
                for i in range(8-1):
                    world.multiworld.itempool.append(world.create_item(item.name))
                    item_count += 1
                

    # itempool and number of locations should match up.
    # If this is not the case we want to fill the itempool with junk.
    junk = item_count - (len(locations) - 1)  # calculate this based on player settings
    world.multiworld.itempool += [world.create_item("Nothing") for _ in range(junk)]