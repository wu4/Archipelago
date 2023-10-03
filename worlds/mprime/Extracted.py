# pyright: reportGeneralTypeIssues=false
damage_resistances={'Damage': {'GravitySuit': 0.800000011920929, 'VariaSuit': 0.8999999761581421, 'PhazonSuit': 0.5}, 'HeatDamage1': {'GravitySuit': 0.0, 'VariaSuit': 0.0, 'PhazonSuit': 0.0}, 'Phazon': {'PhazonSuit': 0.0}}
items=['Power Beam', 'Ice Beam', 'Wave Beam', 'Plasma Beam', 'Missile', 'Scan Visor', 'Morph Ball Bomb', 'Power Bomb', 'Flamethrower', 'Thermal Visor', 'Charge Beam', 'Super Missile', 'Grapple Beam', 'X-Ray Visor', 'Ice Spreader', 'Space Jump Boots', 'Morph Ball', 'Combat Visor', 'Boost Ball', 'Spider Ball', 'Power Suit', 'Gravity Suit', 'Varia Suit', 'Phazon Suit', 'Energy Tank', 'Wavebuster', 'Artifact of Truth', 'Artifact of Strength', 'Artifact of Elder', 'Artifact of Wild', 'Artifact of Lifegiver', 'Artifact of Warrior', 'Artifact of Chozo', 'Artifact of Nature', 'Artifact of Sun', 'Artifact of World', 'Artifact of Spirit', 'Artifact of Newborn', 'Nothing', 'Main Power Bomb', 'Missile Launcher']
from Options import Range

class Dash(Range):
    """By locking onto an enemy or scan point and strafing left or right, Samus' momentum can be maintainted. If this trick is enabled, the player may be expected to abuse this quirk to cross large gaps.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/Dash_Jump_(Prime))"""
    display_name = "Combat/Scan Dash"
    range_start = 0
    range_end = 5
    default = 0
class Knowledge(Range):
    """Some destructible objects have vulnerabilities other than those which the player is informed of. Enabling this trick may require players to apply this knowledge in order to progress."""
    display_name = "Knowledge"
    range_start = 0
    range_end = 5
    default = 0
class Combat(Range):
    """If this trick is enabled, the player may be expected to defeat enemies and bosses with fewer items and less health. On Beginner or higher, Charge Beam may be locked behind many of the game's mandatory fights."""
    display_name = "Combat"
    range_start = 0
    range_end = 5
    default = 0
class LJump(Range):
    """By holding and releasing the L button at specific points in a jump, Samus can jump further than normal. If this trick is enabled, the player may be expected to cross some gaps in this way."""
    display_name = "L-Jump"
    range_start = 0
    range_end = 5
    default = 0
class InvisibleObjects(Range):
    """Some objects that normally need visors to be seen, such as Power Conduits or Invisible Platforms, can still be used without the appropriate visor. If enabled, the player may be expected to use these objects even though they cannot see them."""
    display_name = "Invisible Objects"
    range_start = 0
    range_end = 5
    default = 0
class DBoosting(Range):
    """Some damage sources give Samus extra velocity, which can be used to give her a small boost. Enabling this trick may force players to use this to their advantage."""
    display_name = "Damage Boosting"
    range_start = 0
    range_end = 5
    default = 0
class Movement(Range):
    """A broad category for non-obvious movement which can't easily be classified using other tricks. Enabling this will require the player to have a greater understanding of movement and physics in Metroid Prime."""
    display_name = "Movement"
    range_start = 0
    range_end = 5
    default = 0
class SJump(Range):
    """By L-Jumping into sloped surfaces in a specific manner, Samus' jumps can gain extra height due to quirks in the game's physics engine. Enabling this trick may require the player to abuse this extra height to reach places which would otherwise be inaccessible.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/Slope_Jump)"""
    display_name = "Slope Jump"
    range_start = 0
    range_end = 5
    default = 0
class Standable(Range):
    """Samus can maneuver in unexpected ways by standing on small ledges, vines, railings, and other unlikely objects. Enabling this trick may mean that players are expected to climb on the scenery to reach unintended places."""
    display_name = "Standable Terrain"
    range_start = 0
    range_end = 5
    default = 0
class BJ(Range):
    """By using the vanilla Bomb Jump mechanic in unexpected locations, Samus can clear jumps normally meant to require the use of other items. Enabling this trick means that the player may be expected to use standard bomb jumps in places other than morph tunnels."""
    display_name = "Bomb Jump"
    range_start = 0
    range_end = 5
    default = 0
class StandEnemies(Range):
    """Samus can stand on top of some non-obvious enemies, such as Baby Sheegoths, and jump off of them for extra height. Enabling this trick means that players may be expected to abuse this mechanic to reach uninteded places."""
    display_name = "Jump Off Enemies"
    range_start = 0
    range_end = 5
    default = 0
class ClipThruObjects(Range):
    """When Samus reaches some in-game barriers from the wrong side, she may be able to clip through with the Boost Ball or a reposition. Enabling this trick will place this in logic."""
    display_name = "Clip Through Objects"
    range_start = 0
    range_end = 5
    default = 0
class RJump(Range):
    """This trick allows Samus to jump farther than usual by pressing R in the air. Enabling this trick means that players may be expected to perform R-Jumps to reach areas they otherwise couldn't.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/R-Jumping)"""
    display_name = "R-Jump"
    range_start = 0
    range_end = 5
    default = 0
class BSJ(Range):
    """Bomb Jumping and unmorphing forwards from an overhang to get an instant unmorph, then jumping within 2/5 of a second after leaving the ground gives Samus a height boost which can be used to reach higher ledges.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/Bomb_Space_Jump)"""
    display_name = "Bomb Space Jump"
    range_start = 0
    range_end = 5
    default = 0
class WallBoost(Range):
    """Using the Boost Ball, a well placed boost can be used to scale some terrain while morphed. For example, it is possible to leave Burn Dome without Bombs using this method."""
    display_name = "Wall Boost"
    range_start = 0
    range_end = 5
    default = 0
class BoostlessSpiner(Range):
    """Some spinners can be turned without the Boost Ball. The exact method required to do this varies. Enabling this trick may require spinners to be turned before obtaining the Boost Ball."""
    display_name = "Spinners without Boost"
    range_start = 0
    range_end = 5
    default = 0
class OoB(Range):
    """Samus can travel outside the room's boundaries to gain access to areas/rooms otherwise unreachable given the circumstances. Currently, enabling this trick will only affect single-room traversal.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/Out_of_Bounds)"""
    display_name = "Single Room Out of Bounds"
    range_start = 0
    range_end = 5
    default = 0
class HeatRun(Range):
    """Although Samus takes constant damage in heated rooms, she doesn't necessarily need protection to enter or traverse them. Enabling this trick may require the player to perform Heat Runs, where they are forced to endure heated rooms while still vulnerable to their damage. The logic will provide more Energy Tanks to account for the presence of Heat Runs, but at higher difficulties and with other tricks enabled, players may be expected to perform Heat Runs with less health."""
    display_name = "Heat Runs"
    range_start = 0
    range_end = 5
    default = 0
class CBJ(Range):
    """By abusing the Bomb Refill timer, Samus can reach heights that are normally inaccessible with a standard bomb jump. Enabling this trick allows logic to include High Bomb Jumps, Half Pipe Bomb Jumps, and Uber Bomb Jumps.
Check the wiki for more details. (https://wiki.metroidprime.run/wiki/Bomb_Jump)"""
    display_name = "Complex Bomb Jump"
    range_start = 0
    range_end = 5
    default = 0
class IS(Range):
    """Abuse infinite rotational speed to probe the room's collision tree and collect items otherwise out of reach."""
    display_name = "Infinite Speed"
    range_start = 0
    range_end = 5
    default = 0
class UnderwaterMovement(Range):
    """Abuse Slope Jumps and/or Bomb Jumps to circumvent the negative effects of being underwater without Gravity Suit."""
    display_name = "Gravityless Underwater Movement"
    range_start = 0
    range_end = 5
    default = 0
class IUJ(Range):
    """Similar to BSJs except you don't use bombs. Obstruct the camera in a way that will let Samus unmorph and be able to jump within 2/5 of a second after leaving the ground."""
    display_name = "Instant Unmorph Jump"
    range_start = 0
    range_end = 5
    default = 0

generated_options = {

    "scan_dash": Dash,
    "knowledge": Knowledge,
    "combat": Combat,
    "l_jump": LJump,
    "invisible_objects": InvisibleObjects,
    "damage_boosting": DBoosting,
    "movement": Movement,
    "slope_jump": SJump,
    "standable_terrain": Standable,
    "bomb_jump": BJ,
    "jump_off_enemies": StandEnemies,
    "clip_through_objects": ClipThruObjects,
    "r_jump": RJump,
    "bomb_space_jump": BSJ,
    "wall_boost": WallBoost,
    "spinners_without_boost": BoostlessSpiner,
    "single_room_oob": OoB,
    "heat_runs": HeatRun,
    "complex_bomb_jump": CBJ,
    "infinite_speed": IS,
    "gravityless_underwater_movement": UnderwaterMovement,
    "instant_unmorph_jump": IUJ,
}
from BaseClasses import MultiWorld, Region
from worlds.AutoWorld import World
from .Locations import MetroidPrimeLocation
from .Utils import region_format
from typing import Callable

locations = (
            "Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)",
            "Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)",
            "Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)",
            "Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)",
            "Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)",
            "Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)",
            "Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)",
            "Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)",
            "Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)",
            "Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)",
            "Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)",
            "Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)",
            "Pickup (Super Missile) (Observatory, Phendrana Drifts)",
            "Pickup (Energy Tank) (Transport Access, Phendrana Drifts)",
            "Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)",
            "Pickup (Thermal Visor) (Research Core, Phendrana Drifts)",
            "Pickup (Missile) (Frost Cave, Phendrana Drifts)",
            "Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)",
            "Pickup (Missile) (Research Lab Aether, Phendrana Drifts)",
            "Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)",
            "Pickup (Missile) (Gravity Chamber, Phendrana Drifts)",
            "Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)",
            "Pickup (Power Bomb) (Security Cave, Phendrana Drifts)",
            "Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)",
            "Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)",
            "Pickup (Missile) (Storage Cavern, Magmoor Caverns)",
            "Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)",
            "Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)",
            "Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)",
            "Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)",
            "Pickup (Missile) (Fiery Shores, Magmoor Caverns)",
            "Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)",
            "Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)",
            "Pickup (Missile) (Main Quarry, Phazon Mines)",
            "Pickup (Missile) (Security Access A, Phazon Mines)",
            "Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)",
            "Pickup (Flamethrower) (Storage Depot A, Phazon Mines)",
            "Pickup (Missile) (Elite Research, Phazon Mines)",
            "Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)",
            "Pickup (Missile) (Elite Control Access, Phazon Mines)",
            "Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)",
            "Pickup (Missile) (Phazon Processing Center, Phazon Mines)",
            "Pickup (Energy Tank) (Processing Center Access, Phazon Mines)",
            "Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)",
            "Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)",
            "Pickup (Missile) (Metroid Quarantine B, Phazon Mines)",
            "Pickup (Missile) (Metroid Quarantine A, Phazon Mines)",
            "Pickup (Missile) (Fungal Hall B, Phazon Mines)",
            "Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)",
            "Pickup (Missile) (Fungal Hall Access, Phazon Mines)",
            "Pickup (Missile Expansion) (Landing Site, Tallon Overworld)",
            "Pickup (Space Jump Boots) (Alcove, Tallon Overworld)",
            "Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)",
            "Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)",
            "Pickup (Missile Expansion) (Root Cave, Tallon Overworld)",
            "Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)",
            "Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)",
            "Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)",
            "Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",
            "Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)",
            "Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)",
            "Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)",
            "Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)",
            "Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)",
            "Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)",
            "Pickup (Energy Tank) (Main Plaza, Chozo Ruins)",
            "Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)",
            "Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)",
            "Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)",
            "Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)",
            "Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)",
            "Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)",
            "Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)",
            "Pickup (Missile Expansion) (Vault, Chozo Ruins)",
            "Pickup (Energy Tank) (Training Chamber, Chozo Ruins)",
            "Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)",
            "Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)",
            "Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)",
            "Pickup (Wavebuster) (Tower of Light, Chozo Ruins)",
            "Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)",
            "Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)",
            "Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)",
            "Pickup (Energy Tank) (Transport Access North, Chozo Ruins)",
            "Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)",
            "Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)",
            "Pickup (Varia Suit) (Sunchamber, Chozo Ruins)",
            "Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)",
            "Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)",
            "Pickup (Charge Beam) (Watery Hall, Chozo Ruins)",
            "Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)",
            "Pickup (Missile Expansion) (Dynamo, Chozo Ruins)",
            "Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)",
            "Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)",
            "Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)",
            "Pickup (Missile Expansion) (Furnace, Chozo Ruins)",
            "Pickup (Energy Tank) (Furnace, Chozo Ruins)",
            "Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)",
            "Pickup (Missile Expansion) (Crossway, Chozo Ruins)",
            "Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)",
            "Pickup (Ice Beam) (Antechamber, Chozo Ruins)",
)

items_every_room_locations = (
)

def create_regions(world: World, multiworld: MultiWorld, player: int):
    def create_region(region_name: str):
        return Region(region_name, player, multiworld)
    def create_region_with_event(region_name: str, event_name: str, skippable: bool = False):
        this_region = create_region(region_name)
        this_location = MetroidPrimeLocation(player, region_name, None, this_region)
        this_region.locations.append(this_location)
        event = world.create_event(event_name, skippable)
        this_location.place_locked_item(event)
        return this_region
    def create_region_with_location(region_name: str):
        this_region = create_region(region_name)
        this_location = MetroidPrimeLocation(player, region_name, world.location_name_to_id[region_name], this_region)
        this_region.locations.append(this_location)
        return this_region

    # will be implemented once Randovania does
    # create_items_every_room_region: Callable[[str], Region]
    # if world.items_every_room:
    #     create_items_every_room_region = create_region_with_location
    # else:
    #     create_items_every_room_region = create_region

    menu_region = Region("Menu", player, multiworld)
    multiworld.regions.extend((
        menu_region,
                create_region("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)"),
                create_region("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)"),
                create_region("Save Station (Crater Entry Point, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crater Entry Point, Impact Crater)"),
                create_region("Door to Phazon Core (Crater Tunnel A, Impact Crater)"),
                create_region("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crater Tunnel A, Impact Crater)"),
                create_region("Door to Crater Missile Station (Phazon Core, Impact Crater)"),
                create_region("Door to Crater Tunnel A (Phazon Core, Impact Crater)"),
                create_region("Door to Crater Tunnel B (Phazon Core, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Phazon Core, Impact Crater)"),
                create_region("Door to Phazon Core (Crater Missile Station, Impact Crater)"),
                create_region("Missile Station (Crater Missile Station, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crater Missile Station, Impact Crater)"),
                create_region("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)"),
                create_region("Door to Phazon Core (Crater Tunnel B, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crater Tunnel B, Impact Crater)"),
                create_region("Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)"),
                create_region("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Phazon Infusion Chamber, Impact Crater)"),
                create_region("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)"),
                create_region("Dock to Subchamber Two (Subchamber One, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Subchamber One, Impact Crater)"),
                create_region("Dock to Subchamber One (Subchamber Two, Impact Crater)"),
                create_region("Dock to Subchamber Three (Subchamber Two, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Subchamber Two, Impact Crater)"),
                create_region("Dock to Subchamber Four (Subchamber Three, Impact Crater)"),
                create_region("Dock to Subchamber Two (Subchamber Three, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Subchamber Three, Impact Crater)"),
                create_region("Dock to Subchamber Five (Subchamber Four, Impact Crater)"),
                create_region("Dock to Subchamber Three (Subchamber Four, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Subchamber Four, Impact Crater)"),
                create_region("Dock to Subchamber Four (Subchamber Five, Impact Crater)"),
                create_region("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Subchamber Five, Impact Crater)"),
                create_region("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)"),
                create_region("Teleporter to Credits (Metroid Prime Lair, Impact Crater)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Metroid Prime Lair, Impact Crater)"),
                create_region("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)"),
                create_region("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Magmoor Caverns West, Phendrana Drifts)"),
                create_region("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Shoreline Entrance, Phendrana Drifts)"),
                create_region("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)"),
                create_region_with_location("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)"),
                create_region("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Temple Entryway, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)"),
                create_region("Save Station (Save Station B, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station B, Phendrana Drifts)"),
                create_region("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ruins Entryway, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)"),
                create_region("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Plaza Walkway, Phendrana Drifts)"),
                create_region("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)"),
                create_region("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ice Ruins Access, Phendrana Drifts)"),
                create_region("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)"),
                create_region("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)"),
                create_region_with_location("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)"),
                create_region_with_event("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", "Chozo Ice Temple Bomb Slot", False),
                create_region("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)"),
                create_region("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)"),
                create_region("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)"),
                create_region("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)"),
                create_region_with_location("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)"),
                create_region("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)"),
                create_region("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)"),
                create_region("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)"),
                create_region_with_location("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)"),
                create_region("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)"),
                create_region("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Chapel Tunnel, Phendrana Drifts)"),
                create_region("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)"),
                create_region("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Courtyard Entryway, Phendrana Drifts)"),
                create_region("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)"),
                create_region("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Canyon Entryway, Phendrana Drifts)"),
                create_region("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)"),
                create_region_with_location("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)"),
                create_region("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)"),
                create_region_with_location("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)"),
                create_region("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)"),
                create_region_with_location("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)"),
                create_region("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)"),
                create_region("Save Station (Save Station A, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station A, Phendrana Drifts)"),
                create_region("Door to Research Entrance (Specimen Storage, Phendrana Drifts)"),
                create_region("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Specimen Storage, Phendrana Drifts)"),
                create_region("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)"),
                create_region("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Quarantine Access, Phendrana Drifts)"),
                create_region("Door to Specimen Storage (Research Entrance, Phendrana Drifts)"),
                create_region("Door to Map Station (Research Entrance, Phendrana Drifts)"),
                create_region("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Research Entrance, Phendrana Drifts)"),
                create_region("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)"),
                create_region("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (North Quarantine Tunnel, Phendrana Drifts)"),
                create_region("Door to Research Entrance (Map Station, Phendrana Drifts)"),
                create_region("Map Station (Map Station, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Map Station, Phendrana Drifts)"),
                create_region("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)"),
                create_region("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Hydra Lab Entryway, Phendrana Drifts)"),
                create_region("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)"),
                create_region("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)"),
                create_region("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)"),
                create_region_with_event("Event - Thardus (Quarantine Cave, Phendrana Drifts)", "Thardus", False),
                create_region_with_location("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)"),
                create_region("Room Center (Quarantine Cave, Phendrana Drifts)"),
                create_region("Fight Trigger (Quarantine Cave, Phendrana Drifts)"),
                create_region("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)"),
                create_region("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)"),
                create_region_with_event("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", "Research Lab Hydra Barrier", False),
                create_region_with_location("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)"),
                create_region("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)"),
                create_region("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (South Quarantine Tunnel, Phendrana Drifts)"),
                create_region("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)"),
                create_region("Door to Observatory (Observatory Access, Phendrana Drifts)"),
                create_region("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Observatory Access, Phendrana Drifts)"),
                create_region("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)"),
                create_region("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)"),
                create_region("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Magmoor Caverns South, Phendrana Drifts)"),
                create_region("Door to Observatory Access (Observatory, Phendrana Drifts)"),
                create_region("Door to West Tower Entrance (Observatory, Phendrana Drifts)"),
                create_region("Door to Save Station D (Observatory, Phendrana Drifts)"),
                create_region_with_event("Event - Observatory Activated (Observatory, Phendrana Drifts)", "Observatory Activated", True),
                create_region_with_location("Pickup (Super Missile) (Observatory, Phendrana Drifts)"),
                create_region("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)"),
                create_region("Door to Frozen Pike (Transport Access, Phendrana Drifts)"),
                create_region_with_location("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)"),
                create_region("Door to West Tower (West Tower Entrance, Phendrana Drifts)"),
                create_region("Door to Observatory (West Tower Entrance, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (West Tower Entrance, Phendrana Drifts)"),
                create_region("Door to Observatory (Save Station D, Phendrana Drifts)"),
                create_region("Save Station (Save Station D, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station D, Phendrana Drifts)"),
                create_region("Door to Pike Access (Frozen Pike, Phendrana Drifts)"),
                create_region("Door to Transport Access (Frozen Pike, Phendrana Drifts)"),
                create_region("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)"),
                create_region("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Frozen Pike, Phendrana Drifts)"),
                create_region("Door to West Tower Entrance (West Tower, Phendrana Drifts)"),
                create_region("Door to Control Tower (West Tower, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (West Tower, Phendrana Drifts)"),
                create_region("Door to Frozen Pike (Pike Access, Phendrana Drifts)"),
                create_region("Door to Research Core (Pike Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Pike Access, Phendrana Drifts)"),
                create_region("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)"),
                create_region("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Frost Cave Access, Phendrana Drifts)"),
                create_region("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)"),
                create_region("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Hunter Cave Access, Phendrana Drifts)"),
                create_region("Door to East Tower (Control Tower, Phendrana Drifts)"),
                create_region("Door to West Tower (Control Tower, Phendrana Drifts)"),
                create_region_with_location("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)"),
                create_region_with_event("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", "Control Tower Tower", False),
                create_region("Room Center (Control Tower, Phendrana Drifts)"),
                create_region_with_event("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", "Control Tower Tower", False),
                create_region("Fight Trigger (Control Tower, Phendrana Drifts)"),
                create_region_with_event("Event - Control Tower Fight (Control Tower, Phendrana Drifts)", "Control Tower Fight", True),
                create_region("Door to Pike Access (Research Core, Phendrana Drifts)"),
                create_region("Door to Research Core Access (Research Core, Phendrana Drifts)"),
                create_region_with_location("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)"),
                create_region_with_event("Event - Research Core Power Outage (Research Core, Phendrana Drifts)", "Research Core Power Outage", False),
                create_region("Door to Save Station C (Frost Cave, Phendrana Drifts)"),
                create_region("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)"),
                create_region("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile) (Frost Cave, Phendrana Drifts)"),
                create_region("Frost Cave Floor (Frost Cave, Phendrana Drifts)"),
                create_region_with_event("Event - Ice Broken (Frost Cave, Phendrana Drifts)", "Frost Cave Ice Floor", False),
                create_region("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)"),
                create_region("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)"),
                create_region("Door to Chamber Access (Hunter Cave, Phendrana Drifts)"),
                create_region("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Hunter Cave, Phendrana Drifts)"),
                create_region("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)"),
                create_region("Door to Control Tower (East Tower, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (East Tower, Phendrana Drifts)"),
                create_region("Door to Research Core (Research Core Access, Phendrana Drifts)"),
                create_region("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Research Core Access, Phendrana Drifts)"),
                create_region("Door to Frost Cave (Save Station C, Phendrana Drifts)"),
                create_region("Save Station (Save Station C, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station C, Phendrana Drifts)"),
                create_region("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)"),
                create_region("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Upper Edge Tunnel, Phendrana Drifts)"),
                create_region("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)"),
                create_region("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Lower Edge Tunnel, Phendrana Drifts)"),
                create_region("Door to Hunter Cave (Chamber Access, Phendrana Drifts)"),
                create_region("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Chamber Access, Phendrana Drifts)"),
                create_region("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)"),
                create_region("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Lake Tunnel, Phendrana Drifts)"),
                create_region("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)"),
                create_region("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Aether Lab Entryway, Phendrana Drifts)"),
                create_region("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)"),
                create_region("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)"),
                create_region_with_location("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)"),
                create_region("Lab Catwalk (Research Lab Aether, Phendrana Drifts)"),
                create_region("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)"),
                create_region("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)"),
                create_region("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)"),
                create_region("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)"),
                create_region("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Phendrana's Edge, Phendrana Drifts)"),
                create_region("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)"),
                create_region("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)"),
                create_region_with_location("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)"),
                create_region_with_location("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)"),
                create_region_with_event("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", "Gravity Chamber Item (Lower)", False),
                create_region("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)"),
                create_region_with_location("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)"),
                create_region("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)"),
                create_region_with_location("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)"),
                create_region("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)"),
                create_region("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Chozo Ruins North, Magmoor Caverns)"),
                create_region("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)"),
                create_region("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)"),
                create_region("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Burning Trail, Magmoor Caverns)"),
                create_region("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)"),
                create_region("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Lake Tunnel, Magmoor Caverns)"),
                create_region("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)"),
                create_region("Save Station (Save Station Magmoor A, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station Magmoor A, Magmoor Caverns)"),
                create_region("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)"),
                create_region("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)"),
                create_region_with_location("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)"),
                create_region("Next to Crates (Lava Lake, Magmoor Caverns)"),
                create_region("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)"),
                create_region("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Pit Tunnel, Magmoor Caverns)"),
                create_region("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)"),
                create_region("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)"),
                create_region("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)"),
                create_region_with_location("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)"),
                create_region("Tunnel Entrance (Triclops Pit, Magmoor Caverns)"),
                create_region("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)"),
                create_region("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Monitor Tunnel, Magmoor Caverns)"),
                create_region("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)"),
                create_region_with_location("Pickup (Missile) (Storage Cavern, Magmoor Caverns)"),
                create_region("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)"),
                create_region("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)"),
                create_region("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)"),
                create_region("Middle Level (Monitor Station, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Monitor Station, Magmoor Caverns)"),
                create_region("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)"),
                create_region("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)"),
                create_region_with_location("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)"),
                create_region("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)"),
                create_region("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)"),
                create_region_with_location("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)"),
                create_region("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)"),
                create_region("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)"),
                create_region("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)"),
                create_region_with_location("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)"),
                create_region("Room Center (Shore Tunnel, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)"),
                create_region("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Phendrana Drifts North, Magmoor Caverns)"),
                create_region("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)"),
                create_region("Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)"),
                create_region_with_location("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)"),
                create_region_with_location("Pickup (Missile) (Fiery Shores, Magmoor Caverns)"),
                create_region("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)"),
                create_region("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)"),
                create_region("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel B, Magmoor Caverns)"),
                create_region("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)"),
                create_region("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Tallon Overworld West, Magmoor Caverns)"),
                create_region("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)"),
                create_region("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Twin Fires Tunnel, Magmoor Caverns)"),
                create_region("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)"),
                create_region("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Twin Fires, Magmoor Caverns)"),
                create_region("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)"),
                create_region("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (North Core Tunnel, Magmoor Caverns)"),
                create_region("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)"),
                create_region("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)"),
                create_region("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)"),
                create_region_with_event("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", "Geothermal Core Puzzle", False),
                create_region("First Spinner (Geothermal Core, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Geothermal Core, Magmoor Caverns)"),
                create_region("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)"),
                create_region_with_location("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)"),
                create_region_with_event("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", "Plasma Processing Item", False),
                create_region("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)"),
                create_region("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (South Core Tunnel, Magmoor Caverns)"),
                create_region("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)"),
                create_region("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)"),
                create_region_with_location("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)"),
                create_region("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)"),
                create_region("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Workstation Tunnel, Magmoor Caverns)"),
                create_region("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)"),
                create_region("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel C, Magmoor Caverns)"),
                create_region("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)"),
                create_region("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Phazon Mines West, Magmoor Caverns)"),
                create_region("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)"),
                create_region("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)"),
                create_region("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Phendrana Drifts South, Magmoor Caverns)"),
                create_region("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)"),
                create_region("Save Station (Save Station Magmoor B, Magmoor Caverns)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station Magmoor B, Magmoor Caverns)"),
                create_region("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)"),
                create_region("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Tallon Overworld South, Phazon Mines)"),
                create_region("Door to Main Quarry (Quarry Access, Phazon Mines)"),
                create_region("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Quarry Access, Phazon Mines)"),
                create_region("Door to Waste Disposal (Main Quarry, Phazon Mines)"),
                create_region("Door to Quarry Access (Main Quarry, Phazon Mines)"),
                create_region("Door to Save Station Mines A (Main Quarry, Phazon Mines)"),
                create_region("Door to Security Access A (Main Quarry, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Main Quarry, Phazon Mines)"),
                create_region_with_event("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", "Main Quarry Barrier", False),
                create_region("Crane Platform (Main Quarry, Phazon Mines)"),
                create_region("Door to Main Quarry (Waste Disposal, Phazon Mines)"),
                create_region("Door to Ore Processing (Waste Disposal, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Waste Disposal, Phazon Mines)"),
                create_region("Door to Main Quarry (Save Station Mines A, Phazon Mines)"),
                create_region("Save Station (Save Station Mines A, Phazon Mines)"),
                create_region_with_event("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", "Phazon Mines Save Station A Barrier", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station Mines A, Phazon Mines)"),
                create_region("Door to Main Quarry (Security Access A, Phazon Mines)"),
                create_region("Door to Mine Security Station (Security Access A, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Security Access A, Phazon Mines)"),
                create_region("Door to Research Access (Ore Processing, Phazon Mines)"),
                create_region("Door to Storage Depot B (Ore Processing, Phazon Mines)"),
                create_region("Door to Waste Disposal (Ore Processing, Phazon Mines)"),
                create_region("Door to Elevator Access A (Ore Processing, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ore Processing, Phazon Mines)"),
                create_region("Door to Security Access A (Mine Security Station, Phazon Mines)"),
                create_region("Door to Security Access B (Mine Security Station, Phazon Mines)"),
                create_region("Door to Storage Depot A (Mine Security Station, Phazon Mines)"),
                create_region_with_event("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", "Mine Security Station Barrier", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Mine Security Station, Phazon Mines)"),
                create_region_with_event("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", "Mine Security Station Unlock Doors", False),
                create_region("Room Center (Mine Security Station, Phazon Mines)"),
                create_region("Door to Ore Processing (Research Access, Phazon Mines)"),
                create_region("Door to Elite Research (Research Access, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Research Access, Phazon Mines)"),
                create_region("Door to Ore Processing (Storage Depot B, Phazon Mines)"),
                create_region_with_location("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)"),
                create_region_with_event("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", "Storage Depot B Item", False),
                create_region("Door to Ore Processing (Elevator Access A, Phazon Mines)"),
                create_region("Door to Elevator A (Elevator Access A, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elevator Access A, Phazon Mines)"),
                create_region("Door to Elite Research (Security Access B, Phazon Mines)"),
                create_region("Door to Mine Security Station (Security Access B, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Security Access B, Phazon Mines)"),
                create_region("Door to Mine Security Station (Storage Depot A, Phazon Mines)"),
                create_region_with_location("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)"),
                create_region("Door to Research Access (Elite Research, Phazon Mines)"),
                create_region("Door to Security Access B (Elite Research, Phazon Mines)"),
                create_region_with_event("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", "Elite Research Rock Wall", False),
                create_region_with_location("Pickup (Missile) (Elite Research, Phazon Mines)"),
                create_region_with_location("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)"),
                create_region("Top Floor (Elite Research, Phazon Mines)"),
                create_region("Door to Elevator Access A (Elevator A, Phazon Mines)"),
                create_region("Door to Elite Control Access (Elevator A, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elevator A, Phazon Mines)"),
                create_region("Door to Elevator A (Elite Control Access, Phazon Mines)"),
                create_region("Door to Elite Control (Elite Control Access, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Elite Control Access, Phazon Mines)"),
                create_region("Door to Maintenance Tunnel (Elite Control, Phazon Mines)"),
                create_region("Door to Elite Control Access (Elite Control, Phazon Mines)"),
                create_region("Door to Ventilation Shaft (Elite Control, Phazon Mines)"),
                create_region_with_event("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", "Elite Control Barriers", False),
                create_region_with_event("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", "Elite Pirate Fight (Elite Control)", False),
                create_region("Bottom Floor Center (Elite Control, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elite Control, Phazon Mines)"),
                create_region("Door to Elite Control (Maintenance Tunnel, Phazon Mines)"),
                create_region("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Maintenance Tunnel, Phazon Mines)"),
                create_region("Door to Omega Research (Ventilation Shaft, Phazon Mines)"),
                create_region("Door to Elite Control (Ventilation Shaft, Phazon Mines)"),
                create_region_with_location("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)"),
                create_region("Door to Transport Access (Phazon Processing Center, Phazon Mines)"),
                create_region("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)"),
                create_region("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Phazon Processing Center, Phazon Mines)"),
                create_region("Door to Map Station Mines (Omega Research, Phazon Mines)"),
                create_region("Door to Ventilation Shaft (Omega Research, Phazon Mines)"),
                create_region("Door to Dynamo Access (Omega Research, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Omega Research, Phazon Mines)"),
                create_region("Door to Phazon Processing Center (Transport Access, Phazon Mines)"),
                create_region("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Access, Phazon Mines)"),
                create_region("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)"),
                create_region("Door to Elite Quarters (Processing Center Access, Phazon Mines)"),
                create_region_with_event("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", "Processing Center Access Barrier", False),
                create_region_with_location("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)"),
                create_region("Door to Omega Research (Map Station Mines, Phazon Mines)"),
                create_region("Map Station (Map Station Mines, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Map Station Mines, Phazon Mines)"),
                create_region("Door to Central Dynamo (Dynamo Access, Phazon Mines)"),
                create_region("Door to Omega Research (Dynamo Access, Phazon Mines)"),
                create_region_with_event("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", "Elite Pirate Fight (Dynamo Access)", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Dynamo Access, Phazon Mines)"),
                create_region("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)"),
                create_region("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Magmoor Caverns South, Phazon Mines)"),
                create_region("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)"),
                create_region("Door to Processing Center Access (Elite Quarters, Phazon Mines)"),
                create_region_with_event("Event - Omega Pirate (Elite Quarters, Phazon Mines)", "Omega Pirate", False),
                create_region_with_location("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)"),
                create_region("Fight Trigger (Elite Quarters, Phazon Mines)"),
                create_region("Door to Dynamo Access (Central Dynamo, Phazon Mines)"),
                create_region("Door to Quarantine Access A (Central Dynamo, Phazon Mines)"),
                create_region("Door to Save Station Mines B (Central Dynamo, Phazon Mines)"),
                create_region_with_event("Event - Security Drone (Central Dynamo, Phazon Mines)", "Invisible Drone", False),
                create_region_with_location("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)"),
                create_region("Fight Trigger (Central Dynamo, Phazon Mines)"),
                create_region("Room Bottom (Central Dynamo, Phazon Mines)"),
                create_region("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)"),
                create_region("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)"),
                create_region_with_event("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", "Elite Quarters Access Barrier", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Elite Quarters Access, Phazon Mines)"),
                create_region("Door to Central Dynamo (Quarantine Access A, Phazon Mines)"),
                create_region("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Quarantine Access A, Phazon Mines)"),
                create_region("Door to Central Dynamo (Save Station Mines B, Phazon Mines)"),
                create_region("Save Station (Save Station Mines B, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station Mines B, Phazon Mines)"),
                create_region("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)"),
                create_region("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)"),
                create_region("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)"),
                create_region_with_event("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", "Metroid Quarantine B Barrier", False),
                create_region("Front of Barrier (Metroid Quarantine B, Phazon Mines)"),
                create_region("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)"),
                create_region("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)"),
                create_region_with_event("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", "Metroid Quarantine A Barrier", False),
                create_region("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)"),
                create_region("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)"),
                create_region("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)"),
                create_region("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Quarantine Access B, Phazon Mines)"),
                create_region("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)"),
                create_region("Save Station (Save Station Mines C, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station Mines C, Phazon Mines)"),
                create_region("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)"),
                create_region("Door to Elevator B (Elevator Access B, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elevator Access B, Phazon Mines)"),
                create_region("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)"),
                create_region("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)"),
                create_region("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Fungal Hall B, Phazon Mines)"),
                create_region("Door to Elevator Access B (Elevator B, Phazon Mines)"),
                create_region("Door to Fungal Hall Access (Elevator B, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elevator B, Phazon Mines)"),
                create_region("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)"),
                create_region("Missile Station (Missile Station Mines, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Missile Station Mines, Phazon Mines)"),
                create_region("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)"),
                create_region("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)"),
                create_region_with_location("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)"),
                create_region("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)"),
                create_region("Door to Elevator B (Fungal Hall Access, Phazon Mines)"),
                create_region_with_location("Pickup (Missile) (Fungal Hall Access, Phazon Mines)"),
                create_region("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)"),
                create_region("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Fungal Hall A, Phazon Mines)"),
                create_region("Door to Gully (Landing Site, Tallon Overworld)"),
                create_region("Door to Canyon Cavern (Landing Site, Tallon Overworld)"),
                create_region("Door to Temple Hall (Landing Site, Tallon Overworld)"),
                create_region("Door to Alcove (Landing Site, Tallon Overworld)"),
                create_region("Door to Waterfall Cavern (Landing Site, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)"),
                create_region("Ship (Landing Site, Tallon Overworld)"),
                create_region("Door to Tallon Canyon (Gully, Tallon Overworld)"),
                create_region("Door to Landing Site (Gully, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Gully, Tallon Overworld)"),
                create_region("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)"),
                create_region("Door to Landing Site (Canyon Cavern, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Canyon Cavern, Tallon Overworld)"),
                create_region("Door to Temple Security Station (Temple Hall, Tallon Overworld)"),
                create_region("Door to Landing Site (Temple Hall, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Temple Hall, Tallon Overworld)"),
                create_region("Door to Landing Site (Alcove, Tallon Overworld)"),
                create_region_with_location("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)"),
                create_region("Door to Landing Site (Waterfall Cavern, Tallon Overworld)"),
                create_region("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Waterfall Cavern, Tallon Overworld)"),
                create_region("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)"),
                create_region("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)"),
                create_region("Door to Gully (Tallon Canyon, Tallon Overworld)"),
                create_region("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)"),
                create_region("Half Pipe (Tallon Canyon, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Tallon Canyon, Tallon Overworld)"),
                create_region("Door to Temple Hall (Temple Security Station, Tallon Overworld)"),
                create_region("Door to Temple Lobby (Temple Security Station, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Temple Security Station, Tallon Overworld)"),
                create_region("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)"),
                create_region("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)"),
                create_region("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)"),
                create_region("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)"),
                create_region("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel A, Tallon Overworld)"),
                create_region("Door to Root Cave (Root Tunnel, Tallon Overworld)"),
                create_region("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Root Tunnel, Tallon Overworld)"),
                create_region("Door to Artifact Temple (Temple Lobby, Tallon Overworld)"),
                create_region("Door to Temple Security Station (Temple Lobby, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Temple Lobby, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)"),
                create_region("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Frigate Access Tunnel, Tallon Overworld)"),
                create_region("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)"),
                create_region("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)"),
                create_region("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)"),
                create_region("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Chozo Ruins West, Tallon Overworld)"),
                create_region("Door to Transport Tunnel B (Root Cave, Tallon Overworld)"),
                create_region("Door to Root Tunnel (Root Cave, Tallon Overworld)"),
                create_region("Door to Arbor Chamber (Root Cave, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)"),
                create_region("Door to Temple Lobby (Artifact Temple, Tallon Overworld)"),
                create_region_with_location("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)"),
                create_region_with_event("Event - Meta Ridley (Artifact Temple, Tallon Overworld)", "Meta Ridley", False),
                create_region("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)"),
                create_region("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Main Ventilation Shaft Section C, Tallon Overworld)"),
                create_region("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)"),
                create_region("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel C, Tallon Overworld)"),
                create_region("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)"),
                create_region("Door to Root Cave (Transport Tunnel B, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)"),
                create_region("Door to Root Cave (Arbor Chamber, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)"),
                create_region_with_event("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", "Main Ventilation Shaft Section B Conduit", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Main Ventilation Shaft Section B, Tallon Overworld)"),
                create_region("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)"),
                create_region("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Chozo Ruins East, Tallon Overworld)"),
                create_region("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)"),
                create_region("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Magmoor Caverns East, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)"),
                create_region("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Main Ventilation Shaft Section A, Tallon Overworld)"),
                create_region("Door to Reactor Access (Reactor Core, Tallon Overworld)"),
                create_region("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)"),
                create_region("Room Bottom (Reactor Core, Tallon Overworld)"),
                create_region_with_event("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", "Reactor Core Conduits", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Reactor Core, Tallon Overworld)"),
                create_region("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)"),
                create_region("Door to Reactor Core (Reactor Access, Tallon Overworld)"),
                create_region("Door to Savestation (Reactor Access, Tallon Overworld)"),
                create_region_with_event("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", "Reactor Access Conduits", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Reactor Access, Tallon Overworld)"),
                create_region("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),
                create_region("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),
                create_region_with_location("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),
                create_region_with_event("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", "Cargo Freight Lift to Deck Gamma Conduits", False),
                create_region("Door to Reactor Access (Savestation, Tallon Overworld)"),
                create_region("Save Station (Savestation, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Savestation, Tallon Overworld)"),
                create_region("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)"),
                create_region("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Deck Beta Transit Hall, Tallon Overworld)"),
                create_region("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)"),
                create_region("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)"),
                create_region_with_event("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", "Biohazard Containment Conduits", False),
                create_region("Room Bottom (Biohazard Containment, Tallon Overworld)"),
                create_region("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)"),
                create_region("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Deck Beta Security Hall, Tallon Overworld)"),
                create_region("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)"),
                create_region("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)"),
                create_region("Room Center (Biotech Research Area 1, Tallon Overworld)"),
                create_region_with_event("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", "Biotech Research Area 1 Conduits", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Biotech Research Area 1, Tallon Overworld)"),
                create_region("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)"),
                create_region("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Deck Beta Conduit Hall, Tallon Overworld)"),
                create_region("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)"),
                create_region("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Connection Elevator to Deck Beta, Tallon Overworld)"),
                create_region("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)"),
                create_region("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)"),
                create_region_with_location("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)"),
                create_region("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)"),
                create_region("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)"),
                create_region("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)"),
                create_region("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)"),
                create_region("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)"),
                create_region_with_event("Event - Open gate (Great Tree Hall, Tallon Overworld)", "Great Tree Hall Bars Unlocked", False),
                create_region("Next to Spinner (Great Tree Hall, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Great Tree Hall, Tallon Overworld)"),
                create_region("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)"),
                create_region("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)"),
                create_region("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel D, Tallon Overworld)"),
                create_region("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)"),
                create_region("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)"),
                create_region_with_location("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)"),
                create_region("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)"),
                create_region("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)"),
                create_region("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Tunnel E, Tallon Overworld)"),
                create_region("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)"),
                create_region("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Chozo Ruins South, Tallon Overworld)"),
                create_region("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)"),
                create_region_with_location("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)"),
                create_region_with_location("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)"),
                create_region("Behind PB Wall (Life Grove, Tallon Overworld)"),
                create_region("Front of PB Wall (Life Grove, Tallon Overworld)"),
                create_region("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)"),
                create_region("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Phazon Mines East, Tallon Overworld)"),
                create_region("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)"),
                create_region("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Tallon Overworld North, Chozo Ruins)"),
                create_region("Door to Main Plaza (Ruins Entrance, Chozo Ruins)"),
                create_region("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ruins Entrance, Chozo Ruins)"),
                create_region("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)"),
                create_region("Door to Ruins Entrance (Main Plaza, Chozo Ruins)"),
                create_region("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)"),
                create_region("Door to Nursery Access (Main Plaza, Chozo Ruins)"),
                create_region("Door from Plaza Access (Main Plaza, Chozo Ruins)"),
                create_region("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)"),
                create_region_with_location("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)"),
                create_region("Locked Door Ledge (Main Plaza, Chozo Ruins)"),
                create_region("Grapple Ledge (Main Plaza, Chozo Ruins)"),
                create_region("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)"),
                create_region("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ruined Fountain Access, Chozo Ruins)"),
                create_region("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)"),
                create_region("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Ruined Shrine Access, Chozo Ruins)"),
                create_region("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)"),
                create_region("Door to Main Plaza (Nursery Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Nursery Access, Chozo Ruins)"),
                create_region("Door to Main Plaza (Plaza Access, Chozo Ruins)"),
                create_region("Door to Vault (Plaza Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Plaza Access, Chozo Ruins)"),
                create_region("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)"),
                create_region("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Piston Tunnel, Chozo Ruins)"),
                create_region("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)"),
                create_region("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)"),
                create_region("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)"),
                create_region("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)"),
                create_region("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)"),
                create_region_with_location("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)"),
                create_region("Pit (Ruined Shrine, Chozo Ruins)"),
                create_region_with_event("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", "Beetle Battle", False),
                create_region_with_event("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", "Ruined Shrine Item (Morph Ball)", False),
                create_region("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)"),
                create_region("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Eyon Tunnel, Chozo Ruins)"),
                create_region("Door to Vault Access (Vault, Chozo Ruins)"),
                create_region("Door to Plaza Access (Vault, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Vault, Chozo Ruins)"),
                create_region("Door to Training Chamber Access (Training Chamber, Chozo Ruins)"),
                create_region("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)"),
                create_region_with_event("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", "Chozo Ghosts (Training Chamber)", False),
                create_region_with_event("Event - Unlock morph track (Training Chamber, Chozo Ruins)", "Training Chamber Exit Tunnel", False),
                create_region("Door to Arboretum (Arboretum Access, Chozo Ruins)"),
                create_region("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Arboretum Access, Chozo Ruins)"),
                create_region("Door to Magma Pool (Meditation Fountain, Chozo Ruins)"),
                create_region("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Meditation Fountain, Chozo Ruins)"),
                create_region("Door to Tower of Light (Tower of Light Access, Chozo Ruins)"),
                create_region("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Tower of Light Access, Chozo Ruins)"),
                create_region("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)"),
                create_region("Door to North Atrium (Ruined Nursery, Chozo Ruins)"),
                create_region("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)"),
                create_region("Door to Vault (Vault Access, Chozo Ruins)"),
                create_region("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Vault Access, Chozo Ruins)"),
                create_region("Door to Magma Pool (Training Chamber Access, Chozo Ruins)"),
                create_region("Door to Training Chamber (Training Chamber Access, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)"),
                create_region("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)"),
                create_region("Door to Arboretum Access (Arboretum, Chozo Ruins)"),
                create_region("Door to Gathering Hall Access (Arboretum, Chozo Ruins)"),
                create_region("Front of Gate (Arboretum, Chozo Ruins)"),
                create_region_with_event("Event - Open gate (Arboretum, Chozo Ruins)", "Arboretum Gate", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Arboretum, Chozo Ruins)"),
                create_region("Door to Training Chamber Access (Magma Pool, Chozo Ruins)"),
                create_region("Door to Meditation Fountain (Magma Pool, Chozo Ruins)"),
                create_region_with_location("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)"),
                create_region("Door to Tower of Light Access (Tower of Light, Chozo Ruins)"),
                create_region("Door to Tower Chamber (Tower of Light, Chozo Ruins)"),
                create_region_with_location("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)"),
                create_region("Door to Ruined Nursery (Save Station 1, Chozo Ruins)"),
                create_region("Save Station (Save Station 1, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station 1, Chozo Ruins)"),
                create_region("Door to Ruined Nursery (North Atrium, Chozo Ruins)"),
                create_region("Door to Ruined Gallery (North Atrium, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (North Atrium, Chozo Ruins)"),
                create_region("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)"),
                create_region("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)"),
                create_region("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)"),
                create_region("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Magmoor Caverns North, Chozo Ruins)"),
                create_region("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)"),
                create_region("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Sunchamber Lobby, Chozo Ruins)"),
                create_region("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)"),
                create_region("Door to Arboretum (Gathering Hall Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Gathering Hall Access, Chozo Ruins)"),
                create_region("Door to Tower of Light (Tower Chamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)"),
                create_region("Door to North Atrium (Ruined Gallery, Chozo Ruins)"),
                create_region("Door to Totem Access (Ruined Gallery, Chozo Ruins)"),
                create_region("Door to Map Station (Ruined Gallery, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)"),
                create_region("Door to Sun Tower Access (Sun Tower, Chozo Ruins)"),
                create_region("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)"),
                create_region_with_event("Event - Unlock spider track (Sun Tower, Chozo Ruins)", "Sun Tower Spider Track Unlocked", False),
                create_region_with_event("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", "Sunchamber Chozo Ghosts Layer Activated", False),
                create_region_with_event("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", "Sunchamber Chozo Ghosts Layer Activated", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Sun Tower, Chozo Ruins)"),
                create_region("Door to Hive Totem (Transport Access North, Chozo Ruins)"),
                create_region("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)"),
                create_region_with_location("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)"),
                create_region("Door to Sunchamber (Sunchamber Access, Chozo Ruins)"),
                create_region("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Sunchamber Access, Chozo Ruins)"),
                create_region("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)"),
                create_region("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)"),
                create_region("Door to Save Station 2 (Gathering Hall, Chozo Ruins)"),
                create_region("Door to East Atrium (Gathering Hall, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)"),
                create_region("Door to Ruined Gallery (Totem Access, Chozo Ruins)"),
                create_region("Door to Hive Totem (Totem Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Totem Access, Chozo Ruins)"),
                create_region("Door to Ruined Gallery (Map Station, Chozo Ruins)"),
                create_region("Map Station (Map Station, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Map Station, Chozo Ruins)"),
                create_region("Door to Sunchamber (Sun Tower Access, Chozo Ruins)"),
                create_region("Door to Sun Tower (Sun Tower Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Sun Tower Access, Chozo Ruins)"),
                create_region("Door to Totem Access (Hive Totem, Chozo Ruins)"),
                create_region("Door to Transport Access North (Hive Totem, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)"),
                create_region_with_event("Event - Hive Mecha (Hive Totem, Chozo Ruins)", "Hive Mecha", False),
                create_region_with_event("Event - Fallen Rubble (Hive Totem, Chozo Ruins)", "Chozo - Fallen Rubble", False),
                create_region("Door to Sun Tower Access (Sunchamber, Chozo Ruins)"),
                create_region("Door to Sunchamber Access (Sunchamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)"),
                create_region_with_event("Event - Flaahgra (Sunchamber, Chozo Ruins)", "Flaahgra", False),
                create_region_with_event("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", "Chozo Ghosts (Sunchamber)", False),
                create_region("Before Fight (Front) (Sunchamber, Chozo Ruins)"),
                create_region("Before Fight (Back) (Sunchamber, Chozo Ruins)"),
                create_region("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)"),
                create_region("Door to Watery Hall (Watery Hall Access, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)"),
                create_region("Door to Gathering Hall (Save Station 2, Chozo Ruins)"),
                create_region("Save Station (Save Station 2, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station 2, Chozo Ruins)"),
                create_region("Door to Gathering Hall (East Atrium, Chozo Ruins)"),
                create_region("Door to Energy Core Access (East Atrium, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (East Atrium, Chozo Ruins)"),
                create_region("Door to Dynamo Access (Watery Hall, Chozo Ruins)"),
                create_region("Door to Watery Hall Access (Watery Hall, Chozo Ruins)"),
                create_region_with_location("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)"),
                create_region_with_event("Event - Open gate (Watery Hall, Chozo Ruins)", "Watery Hall Gate", False),
                create_region("Behind Gate (Watery Hall, Chozo Ruins)"),
                create_region("Door to Energy Core (Energy Core Access, Chozo Ruins)"),
                create_region("Door to East Atrium (Energy Core Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Energy Core Access, Chozo Ruins)"),
                create_region("Door to Watery Hall (Dynamo Access, Chozo Ruins)"),
                create_region("Door to Dynamo (Dynamo Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Dynamo Access, Chozo Ruins)"),
                create_region("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)"),
                create_region("Door to West Furnace Access (Energy Core, Chozo Ruins)"),
                create_region("Door to Energy Core Access (Energy Core, Chozo Ruins)"),
                create_region_with_event("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", "West Furnace Access Door Unlocked", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Energy Core, Chozo Ruins)"),
                create_region("Door to Dynamo Access (Dynamo, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)"),
                create_region("Door to Burn Dome (Burn Dome Access, Chozo Ruins)"),
                create_region("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)"),
                create_region("Spawn Point (Burn Dome Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Burn Dome Access, Chozo Ruins)"),
                create_region("Door to Energy Core (West Furnace Access, Chozo Ruins)"),
                create_region("Door to Furnace (West Furnace Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (West Furnace Access, Chozo Ruins)"),
                create_region("Door to Burn Dome Access (Burn Dome, Chozo Ruins)"),
                create_region_with_location("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)"),
                create_region_with_event("Event - Incinerator Drone (Burn Dome, Chozo Ruins)", "Incinerator Drone", False),
                create_region("Before Fight (Burn Dome, Chozo Ruins)"),
                create_region("Door to East Furnace Access (Furnace, Chozo Ruins)"),
                create_region("Door to West Furnace Access (Furnace, Chozo Ruins)"),
                create_region("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Furnace, Chozo Ruins)"),
                create_region_with_location("Pickup (Energy Tank) (Furnace, Chozo Ruins)"),
                create_region("Under Spider Track (Furnace, Chozo Ruins)"),
                create_region("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)"),
                create_region("Door to Furnace (East Furnace Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (East Furnace Access, Chozo Ruins)"),
                create_region("Door to Crossway (Crossway Access West, Chozo Ruins)"),
                create_region("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crossway Access West, Chozo Ruins)"),
                create_region("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)"),
                create_region("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)"),
                create_region("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)"),
                create_region("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)"),
                create_region("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)"),
                create_region_with_location("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)"),
                create_region_with_event("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Bomb Slots", False),
                create_region_with_event("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Barrier", False),
                create_region("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)"),
                create_region_with_event("Event - Statue Moved (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Statue", False),
                create_region_with_event("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Unlock Doors", False),
                create_region("Room Center (Hall of the Elders, Chozo Ruins)"),
                create_region("Behind Barrier (Hall of the Elders, Chozo Ruins)"),
                create_region("Door to Crossway Access South (Crossway, Chozo Ruins)"),
                create_region("Door to Crossway Access West (Crossway, Chozo Ruins)"),
                create_region("Door to Elder Hall Access (Crossway, Chozo Ruins)"),
                create_region_with_location("Pickup (Missile Expansion) (Crossway, Chozo Ruins)"),
                create_region_with_event("Event - Activate Bomb Slots (Crossway, Chozo Ruins)", "Crossway Bomb Slots", False),
                create_region("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)"),
                create_region("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Reflecting Pool Access, Chozo Ruins)"),
                create_region("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)"),
                create_region("Door to Crossway (Elder Hall Access, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Elder Hall Access, Chozo Ruins)"),
                create_region("Door to Crossway (Crossway Access South, Chozo Ruins)"),
                create_region("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Crossway Access South, Chozo Ruins)"),
                create_region("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)"),
                create_region("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)"),
                create_region("Door to Transport Access South (Reflecting Pool, Chozo Ruins)"),
                create_region("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)"),
                create_region("Door to Antechamber (Reflecting Pool, Chozo Ruins)"),
                create_region_with_event("Event - Drain water (Reflecting Pool, Chozo Ruins)", "Reflecting Pool Water Drained", False),
                # create_items_every_room_region("Pickup (Items Every Room) (Reflecting Pool, Chozo Ruins)"),
                create_region("Door to Reflecting Pool (Save Station 3, Chozo Ruins)"),
                create_region("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)"),
                create_region("Save Station (Save Station 3, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Save Station 3, Chozo Ruins)"),
                create_region("Door to Reflecting Pool (Transport Access South, Chozo Ruins)"),
                create_region("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport Access South, Chozo Ruins)"),
                create_region("Door to Reflecting Pool (Antechamber, Chozo Ruins)"),
                create_region_with_location("Pickup (Ice Beam) (Antechamber, Chozo Ruins)"),
                create_region("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)"),
                create_region("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Tallon Overworld East, Chozo Ruins)"),
                create_region("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)"),
                create_region("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)"),
                # create_items_every_room_region("Pickup (Items Every Room) (Transport to Tallon Overworld South, Chozo Ruins)"),
                create_region_with_event("Event - Credits (Credits, End of Game)", "Credits", False),
    ))
    menu_region.add_exits({
        region_format("Ship", "Landing Site", "Tallon Overworld"):
        # region_format("Ship Save", "Exterior Docking Hangar", "Frigate Orpheon"):
            "Start Game"
    })
from BaseClasses import MultiWorld, CollectionState
from typing import Callable

ConnectionDict = tuple[str, Callable[[CollectionState], bool]]
NodePair = tuple[str, tuple[ConnectionDict, ...]]

def add_exits_to_world(world: MultiWorld, player: int, regions: tuple[NodePair, ...]):
    for region_name, exits in regions:
        region = world.get_region(region_name, player)
        for connecting_region_name, rule in exits:
            region.connect(world.get_region(connecting_region_name, player), None, rule)

def set_rules(multiworld: MultiWorld, player: int):
    templates = {
        "Shoot Super Missile": lambda logic: ( logic.has('Power Beam', player) and logic.metroid_prime_has_missiles(player, 5) and logic.has('Charge Beam', player) and logic.has('Super Missile', player) and templates['Can Use Arm Cannon'](logic) ),
        "Have all Beams": lambda logic: ( logic.has('Power Beam', player) and logic.has('Wave Beam', player) and logic.has('Ice Beam', player) and logic.has('Plasma Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Heat-Resisting Suit": lambda logic: ( logic.has('Gravity Suit', player) or logic.has('Varia Suit', player) or logic.has('Phazon Suit', player) ),
        "Can Use Arm Cannon": lambda logic: ( logic.has('Combat Visor', player) or logic.has('Thermal Visor', player) or logic.has('X-Ray Visor', player) ),
        "Shoot Any Beam": lambda logic: ( templates['Can Use Arm Cannon'](logic) and ( logic.has('Power Beam', player) or logic.has('Wave Beam', player) or logic.has('Ice Beam', player) or logic.has('Plasma Beam', player) ) ),
        "Shoot Power Beam": lambda logic: ( logic.has('Power Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Shoot Wave Beam": lambda logic: ( logic.has('Wave Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Shoot Ice Beam": lambda logic: ( logic.has('Ice Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Shoot Plasma Beam": lambda logic: ( logic.has('Plasma Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Use Grapple Beam": lambda logic: ( logic.has('Grapple Beam', player) and templates['Can Use Arm Cannon'](logic) ),
        "Open Normal Door": lambda logic: ( templates['Shoot Any Beam'](logic) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Scan Visor', player) ) ),
        "Move Past Scatter Bombu": lambda logic: ( logic.has('Morph Ball', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 12, 'Damage') ) or logic.multiworld.movement[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 30, 'Damage') or templates['Shoot Wave Beam'](logic) ),
    }
    dock_requirements = {
        "Normal Door": templates['Open Normal Door'],
        "Normal Door (Forced)": templates['Open Normal Door'],
        "Ice Door": templates['Shoot Ice Beam'],
        "Wave Door": templates['Shoot Wave Beam'],
        "Plasma Door": templates['Shoot Plasma Beam'],
        "Missile Blast Shield": lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) ),
        "Missile Blast Shield (randomprime)": lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) ),
        "Circular Door": templates['Open Normal Door'],
        "Square Door": None,
        "Super Missile Blast Shield": (templates['Open Normal Door']) and (templates['Shoot Super Missile']),
        "Power Bomb Blast Shield": (templates['Open Normal Door']) and (lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
        "Wavebuster Blast Shield": (templates['Shoot Wave Beam']) and (lambda logic: ( logic.has('Charge Beam', player) and logic.metroid_prime_has_missiles(player, 11) and logic.has('Wavebuster', player) and templates['Shoot Wave Beam'](logic) )),
        "Ice Spreader Blast Shield": (templates['Shoot Ice Beam']) and (lambda logic: ( logic.has('Charge Beam', player) and logic.metroid_prime_has_missiles(player, 10) and logic.has('Ice Spreader', player) and templates['Shoot Ice Beam'](logic) )),
        "Flamethrower Blast Shield": (templates['Shoot Plasma Beam']) and (lambda logic: ( logic.has('Charge Beam', player) and logic.metroid_prime_has_missiles(player, 10) and logic.has('Flamethrower', player) and templates['Shoot Plasma Beam'](logic) )),
        "Charge Beam Blast Shield": (templates['Open Normal Door']) and (lambda logic: ( templates['Shoot Any Beam'](logic) and logic.has('Charge Beam', player) )),
        "Bomb Blast Shield": (templates['Open Normal Door']) and (lambda logic: ( templates['Open Normal Door'](logic) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
        "Morph Ball Door": lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Power Beam', player) or logic.has('Ice Beam', player) or logic.has('Wave Beam', player) or logic.has('Plasma Beam', player) ) and ( logic.has('Combat Visor', player) or logic.has('Thermal Visor', player) or logic.has('X-Ray Visor', player) or logic.has('Scan Visor', player) ) ),
        "Open Passage": lambda logic: ( ( logic.has('Power Beam', player) or logic.has('Ice Beam', player) or logic.has('Wave Beam', player) or logic.has('Plasma Beam', player) ) and ( logic.has('Combat Visor', player) or logic.has('Thermal Visor', player) or logic.has('X-Ray Visor', player) ) ),
        "Teleporter": None,
    }
    add_exits_to_world(multiworld, player, (
            (
            "Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", (
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", None),
                ("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", (
                ("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", None),
                ("Save Station (Crater Entry Point, Impact Crater)", None),
                ("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Save Station (Crater Entry Point, Impact Crater)", (
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", None),
            )
            ),
            (
            "Door to Phazon Core (Crater Tunnel A, Impact Crater)", (
                ("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", None),
                ("Door to Crater Tunnel A (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", (
                ("Door to Phazon Core (Crater Tunnel A, Impact Crater)", None),
                ("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Missile Station (Phazon Core, Impact Crater)", (
                ("Door to Crater Tunnel A (Phazon Core, Impact Crater)", None),
                ("Door to Crater Tunnel B (Phazon Core, Impact Crater)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 5 and ( logic.multiworld.l_jump[player].value >= 4 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.jump_off_enemies[player].value >= 5 ) )),
                ("Door to Phazon Core (Crater Missile Station, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Tunnel A (Phazon Core, Impact Crater)", (
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 4 ) or ( logic.has('Scan Visor', player) and logic.multiworld.l_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.slope_jump[player].value >= 4 ) )),
                ("Door to Phazon Core (Crater Tunnel A, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Tunnel B (Phazon Core, Impact Crater)", (
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", None),
                ("Door to Phazon Core (Crater Tunnel B, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Core (Crater Missile Station, Impact Crater)", (
                ("Missile Station (Crater Missile Station, Impact Crater)", None),
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Missile Station (Crater Missile Station, Impact Crater)", (
                ("Door to Phazon Core (Crater Missile Station, Impact Crater)", None),
            )
            ),
            (
            "Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", (
                ("Door to Phazon Core (Crater Tunnel B, Impact Crater)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 5, 'Damage') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Spider Ball', player) or ( logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 40, 'Damage') and logic.multiworld.movement[player].value >= 1 ) ) ) )),
                ("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Core (Crater Tunnel B, Impact Crater)", (
                ("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 5, 'Damage') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Spider Ball', player) or ( logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 40, 'Damage') and logic.multiworld.movement[player].value >= 1 ) ) ) )),
                ("Door to Crater Tunnel B (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)", (
                ("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", None),
                ("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", (
                ("Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)", None),
                ("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", (
                ("Dock to Subchamber Two (Subchamber One, Impact Crater)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) and ( templates['Shoot Power Beam'](logic) or ( logic.has('Plasma Beam', player) and logic.has('Flamethrower', player) and logic.metroid_prime_has_missiles(player, 25) and logic.has('Charge Beam', player) and logic.multiworld.combat[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 ) ) and ( logic.metroid_prime_can_sustain_damage(player, 54, 'Damage') or logic.multiworld.combat[player].value >= 1 ) )),
            )
            ),
            (
            "Dock to Subchamber Two (Subchamber One, Impact Crater)", (
                ("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", None),
                ("Dock to Subchamber One (Subchamber Two, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber One (Subchamber Two, Impact Crater)", (
                ("Dock to Subchamber Three (Subchamber Two, Impact Crater)", lambda logic: ( templates['Shoot Wave Beam'](logic) and templates['Shoot Ice Beam'](logic) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) and ( templates['Shoot Power Beam'](logic) or ( logic.has('Plasma Beam', player) and logic.has('Charge Beam', player) and logic.metroid_prime_has_missiles(player, 25) and logic.multiworld.combat[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 and logic.has('Flamethrower', player) ) ) and ( ( logic.metroid_prime_can_sustain_damage(player, 76, 'Damage') or logic.has('Morph Ball', player) or logic.multiworld.combat[player].value >= 1 ) ) and ( logic.metroid_prime_can_sustain_damage(player, 119, 'Damage') or logic.multiworld.combat[player].value >= 1 ) )),
                ("Dock to Subchamber Two (Subchamber One, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Three (Subchamber Two, Impact Crater)", (
                ("Dock to Subchamber One (Subchamber Two, Impact Crater)", None),
                ("Dock to Subchamber Two (Subchamber Three, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Four (Subchamber Three, Impact Crater)", (
                ("Dock to Subchamber Two (Subchamber Three, Impact Crater)", None),
                ("Dock to Subchamber Three (Subchamber Four, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Two (Subchamber Three, Impact Crater)", (
                ("Dock to Subchamber Four (Subchamber Three, Impact Crater)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) and templates['Shoot Wave Beam'](logic) and templates['Shoot Ice Beam'](logic) and templates['Shoot Plasma Beam'](logic) and ( templates['Shoot Power Beam'](logic) or ( logic.has('Charge Beam', player) and logic.metroid_prime_has_missiles(player, 25) and logic.has('Flamethrower', player) and logic.multiworld.combat[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 ) ) and ( ( logic.metroid_prime_can_sustain_damage(player, 76, 'Damage') or logic.has('Morph Ball', player) or logic.multiworld.combat[player].value >= 1 ) ) and ( logic.metroid_prime_can_sustain_damage(player, 179, 'Damage') or logic.multiworld.combat[player].value >= 1 ) )),
                ("Dock to Subchamber Three (Subchamber Two, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Five (Subchamber Four, Impact Crater)", (
                ("Dock to Subchamber Three (Subchamber Four, Impact Crater)", None),
                ("Dock to Subchamber Four (Subchamber Five, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Three (Subchamber Four, Impact Crater)", (
                ("Dock to Subchamber Five (Subchamber Four, Impact Crater)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) and ( templates['Have all Beams'](logic) or ( templates['Shoot Any Beam'](logic) and logic.multiworld.combat[player].value >= 3 ) ) and ( ( logic.has('Morph Ball', player) or logic.metroid_prime_can_sustain_damage(player, 99, 'Damage') or logic.multiworld.combat[player].value >= 1 ) and ( ( logic.metroid_prime_can_sustain_damage(player, 239, 'Damage') or logic.multiworld.combat[player].value >= 2 ) or ( logic.metroid_prime_can_sustain_damage(player, 149, 'Damage') and logic.multiworld.combat[player].value >= 1 ) ) ) )),
                ("Dock to Subchamber Four (Subchamber Three, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Four (Subchamber Five, Impact Crater)", (
                ("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", None),
                ("Dock to Subchamber Five (Subchamber Four, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", (
                ("Dock to Subchamber Four (Subchamber Five, Impact Crater)", None),
                ("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", (
                ("Teleporter to Credits (Metroid Prime Lair, Impact Crater)", lambda logic: ( logic.has('Phazon Suit', player) and ( ( logic.has('X-Ray Visor', player) and logic.has('Thermal Visor', player) ) or logic.multiworld.invisible_objects[player].value >= 3 ) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 ) and ( ( logic.has('Space Jump Boots', player) or logic.multiworld.combat[player].value >= 3 ) ) and ( ( logic.has('Morph Ball', player) and logic.count('Power Bomb', player) >= 2 ) or ( templates['Shoot Ice Beam'](logic) and logic.metroid_prime_has_missiles(player, 5) ) or logic.multiworld.combat[player].value >= 3 ) and ( logic.multiworld.combat[player].value >= 5 or ( logic.multiworld.combat[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 99, 'Damage') ) or ( logic.multiworld.combat[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 149, 'Damage') ) or ( logic.multiworld.combat[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 199, 'Damage') ) or ( logic.multiworld.combat[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 249, 'Damage') ) or logic.metroid_prime_can_sustain_damage(player, 299, 'Damage') ) and templates['Shoot Any Beam'](logic) )),
                ("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Teleporter to Credits (Metroid Prime Lair, Impact Crater)", (
                ("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", None),
                ("Event - Credits (Credits, End of Game)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", None),
                ("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", None),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 3) ) )),
                ("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 3) ) )),
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 3 ) or ( logic.multiworld.scan_dash[player].value >= 4 ) )),
                ("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) )),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) and logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) )),
                ("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)", templates['Shoot Plasma Beam']),
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( templates['Shoot Super Missile'](logic) and logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and logic.has('Spider Ball', player) )),
                ("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( logic.multiworld.scan_dash[player].value >= 2 and ( ( logic.has('Scan Visor', player) ) or ( logic.has('X-Ray Visor', player) ) ) )),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.multiworld.single_room_oob[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.has('Space Jump Boots', player) and logic.has('Boost Ball', player) and templates['Shoot Super Missile'](logic) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.movement[player].value >= 3 and not logic.metroid_prime_has_misc(player, 'dock_rando') )),
                ("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
            )
            ),
            (
            "Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.has('Plasma Beam', player) or logic.metroid_prime_has_missiles(player, 1) or ( logic.has('Charge Beam', player) and ( logic.has('Power Beam', player) or logic.has('Wave Beam', player) ) ) ) and templates['Move Past Scatter Bombu'](logic) )),
                ("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", (
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.metroid_prime_has_missiles(player, 1) or logic.has('Plasma Beam', player) or ( logic.has('Charge Beam', player) and ( logic.has('Power Beam', player) or logic.has('Wave Beam', player) ) ) ) and templates['Move Past Scatter Bombu'](logic) )),
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", (
                ("Save Station (Save Station B, Phendrana Drifts)", None),
                ("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station B, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", None),
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", None),
                ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", (
                ("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", None),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", None),
                ("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.has('Charge Beam', player) or logic.has('Plasma Beam', player) or logic.metroid_prime_has_missiles(player, 1) ) and templates['Move Past Scatter Bombu'](logic) )),
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", (
                ("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 1) or logic.has('Plasma Beam', player) ) and templates['Move Past Scatter Bombu'](logic) )),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.multiworld.jump_off_enemies[player].value >= 3 and logic.multiworld.movement[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 50, 'Damage') ) ) )),
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", lambda logic: logic.has('Chozo Ice Temple Bomb Slot', player)),
                ("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", None),
            )
            ),
            (
            "Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", None),
            )
            ),
            (
            "Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", (
                ("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", None),
                ("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", lambda logic: ( logic.has('Chozo Ice Temple Bomb Slot', player) )),
                ("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)", lambda logic: ( templates['Shoot Plasma Beam'](logic) and logic.has('Morph Ball', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 1 and not logic.has('Chozo Ice Temple Bomb Slot', player) ) or ( logic.has('Chozo Ice Temple Bomb Slot', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 ) ) )),
                ("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.has('Morph Ball Bomb', player) )),
            )
            ),
            (
            "Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 1 ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 3 ) )),
                ("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and ( ( ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.multiworld.l_jump[player].value >= 1 ) or ( not logic.has('Research Core Power Outage', player) and ( ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.multiworld.scan_dash[player].value >= 1 ) or logic.multiworld.scan_dash[player].value >= 2 ) ) or ( logic.has('Research Core Power Outage', player) and ( ( ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) ) ) ) ) or ( logic.has('Space Jump Boots', player) and ( ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or ( logic.multiworld.jump_off_enemies[player].value >= 1 and not logic.has('Research Core Power Outage', player) and logic.metroid_prime_can_sustain_damage(player, 10, 'Damage') ) or ( logic.multiworld.jump_off_enemies[player].value >= 2 and logic.has('Research Core Power Outage', player) ) or logic.multiworld.slope_jump[player].value >= 1 ) ) or ( logic.multiworld.jump_off_enemies[player].value >= 5 and not logic.has('Research Core Power Outage', player) and logic.multiworld.l_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 10, 'Damage') and logic.multiworld.damage_boosting[player].value >= 3 ) )),
                ("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", lambda logic: logic.has('Space Jump Boots', player)),
                ("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)", (
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) )),
            )
            ),
            (
            "Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.scan_dash[player].value >= 1 and not logic.has('Research Core Power Outage', player) ) )),
                ("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)", lambda logic: ( templates['Shoot Plasma Beam'](logic) and ( ( logic.has('Space Jump Boots', player) or ( logic.multiworld.standable_terrain[player].value >= 1 or logic.multiworld.l_jump[player].value >= 1 ) or ( ( not logic.has('Research Core Power Outage', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.has('Research Core Power Outage', player) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) ) ) ) )),
            )
            ),
            (
            "Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Spider Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) ) )),
                ("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)", templates['Shoot Plasma Beam']),
                ("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", None),
                ("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", (
                ("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", (
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
                ("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", None),
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", None),
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", (
                ("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", lambda logic: ( ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 25) ) or ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.combat[player].value >= 1 ) ) and templates['Shoot Any Beam'](logic) ) or ( logic.metroid_prime_has_missiles(player, 17) and templates['Shoot Any Beam'](logic) and logic.multiworld.combat[player].value >= 1 ) or ( logic.has('Morph Ball', player) and logic.multiworld.combat[player].value >= 3 and ( logic.has('Morph Ball Bomb', player) or logic.count('Power Bomb', player) >= 4 ) and logic.metroid_prime_can_sustain_damage(player, 100, 'Damage') ) )),
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", (
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.bomb_jump[player].value >= 1 and logic.has('Morph Ball Bomb', player) ) or ( logic.multiworld.slope_jump[player].value >= 3 ) ) )),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 2 or logic.multiworld.r_jump[player].value >= 2 ) ) or ( logic.has('Morph Ball', player) and ( ( logic.has('Scan Visor', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) or ( logic.has('Boost Ball', player) and logic.multiworld.bomb_jump[player].value >= 2 ) or ( logic.has('Boost Ball', player) and logic.has('Space Jump Boots', player) ) ) and logic.has('Morph Ball Bomb', player) ) )),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Boost Ball', player) or ( logic.has('Scan Visor', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) ) ) or ( logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 2 or logic.multiworld.r_jump[player].value >= 2 ) ) )),
                ("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) )),
                ("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", None),
                ("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
            )
            ),
            (
            "Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) )),
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( templates['Shoot Super Missile'](logic) and templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.multiworld.movement[player].value >= 2 ) )),
            )
            ),
            (
            "Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.multiworld.standable_terrain[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", (
                ("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.has('Scan Visor', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.movement[player].value >= 4 ) )),
                ("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", (
                ("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) ) or logic.multiworld.scan_dash[player].value >= 2 or ( logic.multiworld.standable_terrain[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", (
                ("Save Station (Save Station A, Phendrana Drifts)", None),
                ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station A, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Research Entrance (Specimen Storage, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", None),
                ("Door to Specimen Storage (Research Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", (
                ("Door to Research Entrance (Specimen Storage, Phendrana Drifts)", None),
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", None),
                ("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", None),
                ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Specimen Storage (Research Entrance, Phendrana Drifts)", (
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 or logic.has('Plasma Beam', player) or logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') ) and ( templates['Shoot Any Beam'](logic) or ( logic.has('Morph Ball', player) and logic.multiworld.combat[player].value >= 2 and ( logic.has('Morph Ball Bomb', player) or logic.count('Power Bomb', player) >= 4 ) ) ) )),
                ("Door to Research Entrance (Specimen Storage, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Map Station (Research Entrance, Phendrana Drifts)", (
                ("Door to Specimen Storage (Research Entrance, Phendrana Drifts)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 or logic.has('Plasma Beam', player) or logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') ) and ( templates['Shoot Any Beam'](logic) or ( logic.has('Morph Ball', player) and logic.multiworld.combat[player].value >= 2 and ( logic.has('Morph Ball Bomb', player) or logic.count('Power Bomb', player) >= 4 ) ) ) )),
                ("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", None),
                ("Door to Research Entrance (Map Station, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", (
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", None),
                ("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Entrance (Map Station, Phendrana Drifts)", (
                ("Map Station (Map Station, Phendrana Drifts)", None),
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Map Station (Map Station, Phendrana Drifts)", (
                ("Door to Research Entrance (Map Station, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 5 and logic.multiworld.r_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) )),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) and logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 )),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or logic.multiworld.r_jump[player].value >= 3 ) )),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Use Grapple Beam'](logic) or ( logic.has('Space Jump Boots', player) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.r_jump[player].value >= 4 ) ) )),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", None),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 and ( logic.multiworld.r_jump[player].value >= 4 or ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) ) )),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Use Grapple Beam'](logic) or ( logic.has('Space Jump Boots', player) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.r_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 ) ) )),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", lambda logic: logic.has('Morph Ball', player)),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Event - Thardus (Quarantine Cave, Phendrana Drifts)", (
                ("Room Center (Quarantine Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)", (
                ("Room Center (Quarantine Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Room Center (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Thardus', player) and ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 3 ) ) ) or ( ( logic.multiworld.jump_off_enemies[player].value >= 5 and ( logic.multiworld.damage_boosting[player].value >= 5 or ( logic.has('Space Jump Boots', player) and logic.multiworld.damage_boosting[player].value >= 4 ) ) and logic.metroid_prime_can_sustain_damage(player, 30, 'Damage') and not logic.has('Thardus', player) ) ) or ( logic.has('Spider Ball', player) and logic.has('Morph Ball', player) and logic.has('Space Jump Boots', player) and ( logic.multiworld.movement[player].value >= 2 or ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) ) ) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 and ( logic.multiworld.knowledge[player].value >= 2 or logic.has('Thardus', player) ) ) )),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", lambda logic: ( ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or ( templates['Use Grapple Beam'](logic) and ( logic.has('Space Jump Boots', player) or logic.multiworld.movement[player].value >= 3 ) ) ) )),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or logic.multiworld.slope_jump[player].value >= 4 ) ) or ( templates['Use Grapple Beam'](logic) and logic.multiworld.movement[player].value >= 2 ) or ( logic.has('Spider Ball', player) and ( logic.multiworld.movement[player].value >= 2 or ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) ) ) and ( ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or ( logic.multiworld.r_jump[player].value >= 3 ) ) ) or ( logic.has('Scan Visor', player) and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 4 ) ) ) and ( ( logic.multiworld.knowledge[player].value >= 2 ) or logic.has('Thardus', player) ) ) ) )),
                ("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Thardus', player) )),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Fight Trigger (Quarantine Cave, Phendrana Drifts)", (
                ("Event - Thardus (Quarantine Cave, Phendrana Drifts)", lambda logic: ( ( ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.combat[player].value >= 1 ) ) and ( logic.has('Combat Visor', player) or logic.has('X-Ray Visor', player) or ( ( logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 5 ) or ( logic.count('Power Bomb', player) >= 2 and logic.has('Morph Ball', player) and logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 4 and logic.multiworld.combat[player].value >= 2 ) ) ) ) and ( ( ( ( logic.has('Power Beam', player) or logic.has('Wave Beam', player) ) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 3 or ( logic.count('Power Bomb', player) >= 2 and logic.multiworld.combat[player].value >= 2 and logic.has('Morph Ball', player) ) ) ) or ( logic.has('Plasma Beam', player) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 ) ) ) or ( templates['Shoot Any Beam'](logic) and ( logic.metroid_prime_has_missiles(player, 80) or ( logic.metroid_prime_has_missiles(player, 5) and logic.multiworld.combat[player].value >= 3 ) or ( logic.metroid_prime_has_missiles(player, 40) and logic.count('Power Bomb', player) >= 2 and logic.has('Morph Ball', player) and logic.multiworld.combat[player].value >= 2 ) ) ) ) and ( logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') or ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or logic.multiworld.combat[player].value >= 1 ) ) ) )),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", lambda logic: ( logic.has('Thardus', player) )),
            )
            ),
            (
            "Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", lambda logic: logic.has('Research Lab Hydra Barrier', player)),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", lambda logic: logic.has('Scan Visor', player)),
                ("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", lambda logic: logic.has('Research Lab Hydra Barrier', player)),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) and logic.metroid_prime_has_misc(player, 'backwards_labs') )),
                ("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)", templates['Shoot Super Missile']),
                ("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", None),
            )
            ),
            (
            "Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", (
                ("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", (
                ("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
            )
            ),
            (
            "Door to Observatory (Observatory Access, Phendrana Drifts)", (
                ("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", None),
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", (
                ("Door to Observatory (Observatory Access, Phendrana Drifts)", None),
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.multiworld.slope_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 4 and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 4 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or logic.has('Spider Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_space_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 1 ) ) )),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", None),
                ("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", None),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Observatory Access (Observatory, Phendrana Drifts)", (
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) and ( logic.has('Observatory Activated', player) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or logic.multiworld.r_jump[player].value >= 3 ) )),
                ("Event - Observatory Activated (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Boost Ball', player) and not logic.has('Research Core Power Outage', player) and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.bomb_jump[player].value >= 3 ) ) )),
                ("Door to Observatory (Observatory Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) or ( ( logic.has('Space Jump Boots', player) and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or logic.multiworld.r_jump[player].value >= 2 ) ) ) or ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) )),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) or ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Scan Visor', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 4 ) )),
                ("Door to Observatory (West Tower Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Save Station D (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) or ( ( logic.has('Space Jump Boots', player) and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.r_jump[player].value >= 1 ) ) ) ) or ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) )),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Space Jump Boots', player) and logic.multiworld.bomb_space_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 ) ) )),
                ("Door to Observatory (Save Station D, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Event - Observatory Activated (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) )),
            )
            ),
            (
            "Pickup (Super Missile) (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) )),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda logic: ( logic.has('Observatory Activated', player) )),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", None),
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frozen Pike (Transport Access, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", None),
                ("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)", lambda logic: ( templates['Shoot Plasma Beam'](logic) or ( logic.has('Space Jump Boots', player) and logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 5 and logic.multiworld.jump_off_enemies[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') and logic.has('Charge Beam', player) and templates['Shoot Any Beam'](logic) ) )),
                ("Door to Transport Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", templates['Shoot Plasma Beam']),
            )
            ),
            (
            "Door to West Tower (West Tower Entrance, Phendrana Drifts)", (
                ("Door to Observatory (West Tower Entrance, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to West Tower Entrance (West Tower, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Observatory (West Tower Entrance, Phendrana Drifts)", (
                ("Door to West Tower (West Tower Entrance, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Observatory (Save Station D, Phendrana Drifts)", (
                ("Save Station (Save Station D, Phendrana Drifts)", None),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station D, Phendrana Drifts)", (
                ("Door to Observatory (Save Station D, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Pike Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Transport Access (Frozen Pike, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 2 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) ) ) or ( logic.multiworld.r_jump[player].value >= 3 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 ) )),
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", None),
                ("Door to Frozen Pike (Pike Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", None),
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 3 and ( ( not logic.has('Gravity Chamber Item (Lower)', player) and logic.has('X-Ray Visor', player) ) or ( logic.has('Gravity Chamber Item (Lower)', player) and templates['Shoot Ice Beam'](logic) ) ) and logic.multiworld.scan_dash[player].value >= 4 ) )),
                ("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", lambda logic: ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) ) ) ) or ( ( ( not logic.has('Gravity Suit', player) and logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_has_misc(player, 'NoGravity') and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) ) ) )),
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) ) ) )),
                ("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (West Tower, Phendrana Drifts)", (
                ("Door to Control Tower (West Tower, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to West Tower (West Tower Entrance, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Control Tower (West Tower, Phendrana Drifts)", (
                ("Door to West Tower Entrance (West Tower, Phendrana Drifts)", None),
                ("Door to West Tower (Control Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frozen Pike (Pike Access, Phendrana Drifts)", (
                ("Door to Research Core (Pike Access, Phendrana Drifts)", None),
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core (Pike Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Pike Access, Phendrana Drifts)", None),
                ("Door to Pike Access (Research Core, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", (
                ("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", lambda logic: logic.has('Morph Ball', player)),
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 3 ) )),
                ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", (
                ("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", None),
                ("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", None),
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to East Tower (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", None),
                ("Door to Control Tower (East Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", lambda logic: ( ( ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_space_jump[player].value >= 1 ) ) and logic.multiworld.knowledge[player].value >= 2 and logic.multiworld.movement[player].value >= 2 ) )),
                ("Fight Trigger (Control Tower, Phendrana Drifts)", None),
                ("Door to Control Tower (West Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", lambda logic: ( ( logic.has('Morph Ball', player) and ( ( logic.has('Control Tower Tower', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 3 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and ( logic.multiworld.single_room_oob[player].value >= 3 or ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.single_room_oob[player].value >= 2 ) ) ) )),
                ("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", lambda logic: ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) )),
            )
            ),
            (
            "Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.multiworld.standable_terrain[player].value >= 1 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
            )
            ),
            (
            "Room Center (Control Tower, Phendrana Drifts)", (
                ("Door to East Tower (Control Tower, Phendrana Drifts)", None),
                ("Door to West Tower (Control Tower, Phendrana Drifts)", lambda logic: ( logic.has('Control Tower Fight', player) or logic.has('Research Core Power Outage', player) or ( logic.multiworld.knowledge[player].value >= 2 and logic.multiworld.movement[player].value >= 2 and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) ) ) )),
                ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Control Tower Tower', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 4 and ( logic.multiworld.bomb_jump[player].value >= 1 or logic.multiworld.slope_jump[player].value >= 1 ) ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.single_room_oob[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 3 and ( logic.multiworld.movement[player].value >= 4 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) ) ) )),
                ("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and ( ( logic.has('Plasma Beam', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) ) )),
                ("Fight Trigger (Control Tower, Phendrana Drifts)", None),
            )
            ),
            (
            "Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", (
                ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", None),
            )
            ),
            (
            "Fight Trigger (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", lambda logic: ( logic.has('Control Tower Fight', player) or logic.has('Research Core Power Outage', player) )),
                ("Event - Control Tower Fight (Control Tower, Phendrana Drifts)", lambda logic: ( not logic.has('Research Core Power Outage', player) and templates['Shoot Any Beam'](logic) and ( logic.has('Charge Beam', player) or logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') or logic.multiworld.combat[player].value >= 2 or logic.has('Plasma Beam', player) ) and ( logic.multiworld.combat[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 100, 'Damage') ) and not logic.has('Control Tower Fight', player) )),
            )
            ),
            (
            "Event - Control Tower Fight (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Pike Access (Research Core, Phendrana Drifts)", (
                ("Door to Research Core Access (Research Core, Phendrana Drifts)", lambda logic: ( ( logic.has('Research Core Power Outage', player) and templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) ) or not logic.has('Research Core Power Outage', player) )),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to Research Core (Pike Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Core, Phendrana Drifts)", (
                ("Door to Pike Access (Research Core, Phendrana Drifts)", None),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to Research Core (Research Core Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", (
                ("Event - Research Core Power Outage (Research Core, Phendrana Drifts)", None),
            )
            ),
            (
            "Event - Research Core Power Outage (Research Core, Phendrana Drifts)", (
                ("Door to Pike Access (Research Core, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Save Station C (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
                ("Door to Frost Cave (Save Station C, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) )),
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
                ("Event - Ice Broken (Frost Cave, Phendrana Drifts)", lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and ( ( templates['Use Grapple Beam'](logic) and ( logic.has('Space Jump Boots', player) or logic.multiworld.slope_jump[player].value >= 1 ) ) or ( logic.has('Scan Visor', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 1 ) ) ) or ( logic.has('Space Jump Boots', player) and templates['Shoot Ice Beam'](logic) and logic.multiworld.jump_off_enemies[player].value >= 3 ) ) )),
                ("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
                ("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile) (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( ( logic.has('Gravity Suit', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.gravityless_underwater_movement[player].value >= 4 ) ) ) )),
            )
            ),
            (
            "Frost Cave Floor (Frost Cave, Phendrana Drifts)", (
                ("Door to Save Station C (Frost Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or logic.multiworld.slope_jump[player].value >= 2 ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.multiworld.bomb_jump[player].value >= 3 ) )),
                ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.multiworld.slope_jump[player].value >= 2 and templates['Use Grapple Beam'](logic) and logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or ( logic.multiworld.slope_jump[player].value >= 2 or logic.multiworld.l_jump[player].value >= 2 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) ) )),
                ("Pickup (Missile) (Frost Cave, Phendrana Drifts)", lambda logic: logic.has('Frost Cave Ice Floor', player)),
            )
            ),
            (
            "Event - Ice Broken (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.scan_dash[player].value >= 3 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) or logic.multiworld.l_jump[player].value >= 2 ) ) ) )),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", None),
                ("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", (
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or logic.multiworld.slope_jump[player].value >= 2 ) ) or ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.r_jump[player].value >= 3 ) or ( ( logic.multiworld.r_jump[player].value >= 2 and logic.multiworld.movement[player].value >= 2 ) ) ) ) )),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 3 and logic.has('Gravity Suit', player) ) or ( logic.metroid_prime_has_missiles(player, 3) and templates['Shoot Any Beam'](logic) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.multiworld.l_jump[player].value >= 2 ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 3 ) ) ) )),
                ("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Chamber Access (Hunter Cave, Phendrana Drifts)", (
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", None),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", None),
                ("Door to Hunter Cave (Chamber Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) ) and ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) ) )),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 )),
                ("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", (
                ("Door to Control Tower (East Tower, Phendrana Drifts)", None),
                ("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Control Tower (East Tower, Phendrana Drifts)", (
                ("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to East Tower (Control Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core (Research Core Access, Phendrana Drifts)", (
                ("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", None),
                ("Door to Research Core Access (Research Core, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", (
                ("Door to Research Core (Research Core Access, Phendrana Drifts)", None),
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Save Station C, Phendrana Drifts)", (
                ("Save Station (Save Station C, Phendrana Drifts)", None),
                ("Door to Save Station C (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Save Station (Save Station C, Phendrana Drifts)", (
                ("Door to Frost Cave (Save Station C, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", (
                ("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Chamber Access, Phendrana Drifts)", (
                ("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", None),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", (
                ("Door to Hunter Cave (Chamber Access, Phendrana Drifts)", None),
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", (
                ("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", (
                ("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", (
                ("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", templates['Move Past Scatter Bombu']),
                ("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", (
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", lambda logic: ( ( logic.has('Scan Visor', player) and templates['Shoot Any Beam'](logic) ) or ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) or ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or ( templates['Shoot Plasma Beam'](logic) and logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", (
                ("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)", lambda logic: ( ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) ) )),
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", lambda logic: ( logic.has('Scan Visor', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.l_jump[player].value >= 1 ) )),
                ("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)", (
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", None),
            )
            ),
            (
            "Pickup (Missile) (Research Lab Aether, Phendrana Drifts)", (
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", None),
            )
            ),
            (
            "Lab Catwalk (Research Lab Aether, Phendrana Drifts)", (
                ("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.standable_terrain[player].value >= 1 and ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.l_jump[player].value >= 1 ) ) ) )),
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", None),
                ("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.standable_terrain[player].value >= 1 ) ) )),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) ) ) or ( ( logic.has('Gravity Suit', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.wall_boost[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) and logic.multiworld.movement[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.l_jump[player].value >= 1 ) )),
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", None),
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or ( logic.multiworld.standable_terrain[player].value >= 2 ) ) ) or ( logic.has('Morph Ball Bomb', player) and ( ( templates['Use Grapple Beam'](logic) and logic.multiworld.bomb_jump[player].value >= 4 ) or ( logic.has('Scan Visor', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.scan_dash[player].value >= 5 and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.bomb_jump[player].value >= 4 ) ) and logic.has('Morph Ball', player) ) )),
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) ) or logic.multiworld.clip_through_objects[player].value >= 3 )),
                ("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", lambda logic: logic.has('Morph Ball', player)),
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", None),
                ("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or logic.multiworld.standable_terrain[player].value >= 2 or logic.multiworld.slope_jump[player].value >= 2 or logic.multiworld.r_jump[player].value >= 2 or logic.multiworld.l_jump[player].value >= 2 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) or ( templates['Use Grapple Beam'](logic) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 4 ) ) ) )),
            )
            ),
            (
            "Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", (
                ("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) )),
                ("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", None),
                ("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.slope_jump[player].value >= 3 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) ) or ( templates['Shoot Plasma Beam'](logic) and templates['Use Grapple Beam'](logic) ) or ( logic.has('Gravity Chamber Item (Lower)', player) and ( ( ( logic.has('Charge Beam', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.jump_off_enemies[player].value >= 3 ) or ( logic.multiworld.jump_off_enemies[player].value >= 5 ) ) and templates['Shoot Any Beam'](logic) ) ) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 4 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 5 and logic.multiworld.standable_terrain[player].value >= 5 ) ) ) and templates['Shoot Wave Beam'](logic) and not logic.metroid_prime_has_misc(player, 'dock_rando') ) )),
                ("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) ) or ( ( logic.has('Gravity Suit', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 2 ) ) and logic.has('Morph Ball', player) ) ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 4 and logic.multiworld.gravityless_underwater_movement[player].value >= 4 and logic.metroid_prime_has_misc(player, 'NoGravity') ) )),
            )
            ),
            (
            "Pickup (Missile) (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", None),
            )
            ),
            (
            "Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", (
                ("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", (
                ("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)", None),
                ("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", (
                ("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", (
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", lambda logic: ( logic.has('Morph Ball', player) )),
            )
            ),
            (
            "Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", None),
                ("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", (
                ("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", (
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", None),
                ("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", (
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", None),
                ("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", None),
                ("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", None),
                ("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", (
                ("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') ) )),
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') ) )),
                ("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", (
                ("Save Station (Save Station Magmoor A, Magmoor Caverns)", None),
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station Magmoor A, Magmoor Caverns)", (
                ("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", None),
            )
            ),
            (
            "Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", (
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", lambda logic: ( logic.metroid_prime_has_missiles(player, 2) and templates['Shoot Any Beam'](logic) and ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 1 ) and ( ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.standable_terrain[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 190, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 190, 'HeatDamage1') ) ) ) ) )),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( ( logic.metroid_prime_can_sustain_damage(player, 140, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 110, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 10, 'HeatDamage2') ) or ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) ) ) ) ) )),
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", (
                ("Next to Crates (Lava Lake, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( ( templates['Heat-Resisting Suit'](logic) and ( logic.has('Morph Ball Bomb', player) or ( logic.count('Power Bomb', player) >= 2 and logic.multiworld.knowledge[player].value >= 1 ) ) ) or ( logic.multiworld.heat_runs[player].value >= 2 and ( ( logic.has('Morph Ball Bomb', player) and ( logic.metroid_prime_can_sustain_damage(player, 285, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 250, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and ( logic.metroid_prime_can_sustain_damage(player, 265, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 255, 'HeatDamage1') ) ) ) ) ) or ( logic.count('Power Bomb', player) >= 2 and logic.multiworld.knowledge[player].value >= 1 and ( logic.metroid_prime_can_sustain_damage(player, 360, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 325, 'HeatDamage1') ) ) ) ) ) ) )),
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and ( logic.metroid_prime_can_sustain_damage(player, 150, 'HeatDamage1') or ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') and ( logic.multiworld.scan_dash[player].value >= 2 or ( logic.has('Space Jump Boots', player) and logic.multiworld.movement[player].value >= 2 ) ) ) ) ) )),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') ) ) ) )),
            )
            ),
            (
            "Next to Crates (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and ( ( logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 25, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 115, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 10, 'HeatDamage2') ) or ( logic.has('Space Jump Boots', player) and ( ( logic.metroid_prime_can_sustain_damage(player, 155, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 10, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) ) ) ) ) )),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( ( templates['Heat-Resisting Suit'](logic) and ( logic.has('Morph Ball Bomb', player) or ( logic.count('Power Bomb', player) >= 2 and logic.multiworld.knowledge[player].value >= 1 ) ) ) or ( logic.multiworld.heat_runs[player].value >= 2 and ( ( logic.has('Morph Ball Bomb', player) and ( logic.metroid_prime_can_sustain_damage(player, 340, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 265, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and ( logic.metroid_prime_can_sustain_damage(player, 305, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 245, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 270, 'HeatDamage1') ) ) ) ) ) or ( logic.count('Power Bomb', player) >= 2 and logic.multiworld.knowledge[player].value >= 1 and ( logic.metroid_prime_can_sustain_damage(player, 360, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 340, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and ( logic.metroid_prime_can_sustain_damage(player, 365, 'HeatDamage1') or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 320, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 340, 'HeatDamage1') ) ) ) ) ) ) ) ) )),
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", lambda logic: ( logic.metroid_prime_has_missiles(player, 2) and templates['Shoot Any Beam'](logic) and ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 1 ) and ( ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage1') ) or ( logic.multiworld.standable_terrain[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) ) ) ) )),
            )
            ),
            (
            "Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 95, 'HeatDamage1') ) ) ) or ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) )),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) ) ) or ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) )),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.r_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 110, 'HeatDamage1') ) ) ) )),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 1) ) and ( ( logic.has('Space Jump Boots', player) and ( ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 ) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 280, 'HeatDamage1') ) ) ) or ( logic.multiworld.scan_dash[player].value >= 2 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 155, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') and logic.multiworld.r_jump[player].value >= 2 ) ) ) or ( logic.multiworld.standable_terrain[player].value >= 1 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 220, 'HeatDamage1') ) ) ) ) ) or ( logic.multiworld.l_jump[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( logic.has('X-Ray Visor', player) and logic.multiworld.invisible_objects[player].value >= 2 ) and ( ( logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 255, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 225, 'HeatDamage1') ) ) ) ) and templates['Shoot Any Beam'](logic) )),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 145, 'HeatDamage1') or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 110, 'HeatDamage1') and logic.has('Space Jump Boots', player) ) ) ) ) )),
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", (
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') or ( logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) ) )),
                ("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') or ( logic.has('Morph Ball', player) and logic.metroid_prime_can_sustain_damage(player, 150, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 140, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 130, 'HeatDamage1') ) ) ) ) ) )),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", lambda logic: ( ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 1) ) and ( ( logic.has('Space Jump Boots', player) and ( ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 ) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 130, 'HeatDamage1') ) ) ) or ( logic.multiworld.scan_dash[player].value >= 2 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage1') and logic.multiworld.r_jump[player].value >= 2 ) ) ) or ( logic.multiworld.standable_terrain[player].value >= 1 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage1') ) ) ) ) ) or ( logic.multiworld.l_jump[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 ) and ( ( logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 200, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 180, 'HeatDamage1') ) ) ) ) and templates['Shoot Any Beam'](logic) )),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 95, 'HeatDamage1') ) ) )),
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') or ( logic.has('Space Jump Boots', player) and ( logic.metroid_prime_can_sustain_damage(player, 145, 'HeatDamage1') or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 110, 'HeatDamage1') ) ) ) ) ) )),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 145, 'HeatDamage1') or ( logic.has('Space Jump Boots', player) and ( logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) ) ) )),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 95, 'HeatDamage1') ) ) )),
            )
            ),
            (
            "Tunnel Entrance (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage1') or ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 145, 'HeatDamage1') ) ) ) )),
                ("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 130, 'HeatDamage1') or ( logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) )),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( ( logic.metroid_prime_can_sustain_damage(player, 150, 'HeatDamage1') or ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 130, 'HeatDamage1') ) ) ) ) )),
            )
            ),
            (
            "Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) )),
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) )),
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", (
                ("Pickup (Missile) (Storage Cavern, Magmoor Caverns)", None),
                ("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile) (Storage Cavern, Magmoor Caverns)", (
                ("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", None),
            )
            ),
            (
            "Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", (
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 2 and ( ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 235, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) or templates['Heat-Resisting Suit'](logic) ) ) or ( logic.has('Scan Visor', player) and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 15, 'Damage') and logic.multiworld.movement[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.heat_runs[player].value >= 4 ) )),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and ( logic.metroid_prime_can_sustain_damage(player, 230, 'HeatDamage1') or ( logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) ) ) ) )),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) )),
                ("Middle Level (Monitor Station, Magmoor Caverns)", lambda logic: ( ( ( logic.multiworld.heat_runs[player].value >= 3 or templates['Heat-Resisting Suit'](logic) ) and ( templates['Shoot Any Beam'](logic) and ( ( logic.metroid_prime_can_sustain_damage(player, 255, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage2') and logic.multiworld.l_jump[player].value >= 2 ) or ( logic.has('Charge Beam', player) and logic.metroid_prime_can_sustain_damage(player, 415, 'HeatDamage1') ) or ( logic.metroid_prime_has_missiles(player, 8) and templates['Shoot Any Beam'](logic) and logic.metroid_prime_can_sustain_damage(player, 320, 'HeatDamage1') ) or ( logic.multiworld.combat[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 440, 'HeatDamage1') ) ) ) ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage2') and ( ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 315, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 205, 'HeatDamage1') ) ) ) )),
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", (
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 235, 'HeatDamage1') ) ) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 4 ) and ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and ( ( logic.has('Boost Ball', player) and logic.multiworld.l_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 299, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) ) ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) ) ) )),
                ("Middle Level (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') ) )),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') and ( logic.multiworld.scan_dash[player].value >= 2 or ( logic.has('Space Jump Boots', player) and logic.multiworld.r_jump[player].value >= 2 ) ) )),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", lambda logic: ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') and ( logic.multiworld.scan_dash[player].value >= 3 or logic.multiworld.r_jump[player].value >= 3 ) ) ) )),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') ) )),
                ("Middle Level (Monitor Station, Magmoor Caverns)", lambda logic: ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 70, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 30, 'Damage') and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.metroid_prime_has_missiles(player, 2) and templates['Shoot Any Beam'](logic) and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') and ( templates['Shoot Any Beam'](logic) or ( logic.has('Charge Beam', player) or logic.metroid_prime_has_missiles(player, 1) ) ) ) ) )),
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) )),
                ("Middle Level (Monitor Station, Magmoor Caverns)", lambda logic: ( ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.multiworld.combat[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 430, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 255, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage2') and logic.multiworld.l_jump[player].value >= 3 ) or ( logic.has('Charge Beam', player) and logic.metroid_prime_can_sustain_damage(player, 354, 'HeatDamage1') and templates['Shoot Any Beam'](logic) ) or ( logic.metroid_prime_has_missiles(player, 8) and templates['Shoot Any Beam'](logic) and logic.metroid_prime_can_sustain_damage(player, 300, 'HeatDamage1') ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 and ( ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 205, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') ) ) ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage2') and ( ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 235, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 119, 'HeatDamage1') ) ) ) )),
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Middle Level (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and ( ( logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 55, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.r_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 54, 'HeatDamage1') ) ) ) )),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') ) )),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.multiworld.scan_dash[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 235, 'HeatDamage1') ) ) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 4 ) and ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and ( ( logic.has('Boost Ball', player) and logic.multiworld.l_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 319, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 219, 'HeatDamage1') ) ) ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) ) ) )),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.l_jump[player].value >= 2 and ( ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 154, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 54, 'HeatDamage1') ) ) ) )),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) ) ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 250, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 150, 'HeatDamage1') ) ) ) ) )),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage1') ) ) )),
                ("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 240, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 140, 'HeatDamage1') ) ) ) ) )),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) ) )),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage1') ) ) )),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 90, 'HeatDamage1') ) ) )),
            )
            ),
            (
            "Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", (
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage1') ) )),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", (
                ("Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)", (
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage1') ) )),
            )
            ),
            (
            "Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", (
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage1') ) )),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 70, 'HeatDamage1') ) ) )),
                ("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 30, 'HeatDamage1') ) )),
            )
            ),
            (
            "Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 55, 'HeatDamage1') or ( logic.has('Morph Ball', player) and ( logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') or ( logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage1') ) ) ) ) ) )),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 55, 'HeatDamage1') or ( logic.has('Morph Ball', player) and ( logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage1') or ( logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage1') ) ) ) ) ) )),
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", lambda logic: ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 2 ) and ( ( logic.has('Space Jump Boots', player) and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage1') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') and logic.multiworld.movement[player].value >= 3 ) ) )),
            )
            ),
            (
            "Room Center (Shore Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage1') ) )),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') ) )),
                ("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') ) ) )),
            )
            ),
            (
            "Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", (
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", None),
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", (
                ("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", (
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 30, 'HeatDamage1') ) )),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.metroid_prime_can_sustain_damage(player, 239, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 50, 'HeatDamage2') ) or ( logic.multiworld.l_jump[player].value >= 1 and ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 235, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 189, 'HeatDamage1') ) or ( logic.metroid_prime_can_sustain_damage(player, 230, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') ) ) ) or ( logic.has('Space Jump Boots', player) and ( ( logic.metroid_prime_can_sustain_damage(player, 279, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 30, 'HeatDamage2') ) or ( logic.multiworld.r_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 245, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 15, 'HeatDamage2') ) ) ) ) and logic.multiworld.movement[player].value >= 1 ) )),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 245, 'HeatDamage1') ) ) ) or ( logic.multiworld.standable_terrain[player].value >= 1 and logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 270, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') ) ) ) or ( logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 315, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 215, 'HeatDamage1') ) ) ) )),
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)", (
                ("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 25, 'HeatDamage1') ) )),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", (
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 55, 'HeatDamage1') ) ) ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) ) )),
            )
            ),
            (
            "Pickup (Missile) (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 10, 'HeatDamage2') ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') ) ) )),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 2 ) and ( ( logic.multiworld.standable_terrain[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') and logic.metroid_prime_can_sustain_damage(player, 199, 'HeatDamage1') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.metroid_prime_can_sustain_damage(player, 220, 'HeatDamage1') or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage1') ) ) ) ) ) )),
            )
            ),
            (
            "Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage1') ) )),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 250, 'HeatDamage1') and logic.multiworld.l_jump[player].value >= 1 ) ) ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.has('Space Jump Boots', player) and ( ( logic.metroid_prime_can_sustain_damage(player, 210, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage2') ) or ( logic.multiworld.r_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') ) or ( logic.multiworld.l_jump[player].value >= 2 and ( ( logic.metroid_prime_can_sustain_damage(player, 175, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') ) ) ) ) ) or ( logic.multiworld.l_jump[player].value >= 2 and ( ( logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) ) ) or ( logic.metroid_prime_can_sustain_damage(player, 215, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 50, 'HeatDamage2') ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 175, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 25, 'HeatDamage2') ) ) and logic.multiworld.movement[player].value >= 1 ) or ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 4 ) and logic.has('Space Jump Boots', player) and logic.multiworld.r_jump[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 25, 'HeatDamage2') and ( logic.metroid_prime_can_sustain_damage(player, 130, 'HeatDamage1') or ( logic.has('Scan Visor', player) and logic.metroid_prime_can_sustain_damage(player, 115, 'HeatDamage1') ) ) ) )),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) and ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 275, 'HeatDamage1') and logic.multiworld.l_jump[player].value >= 1 ) ) ) or ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.l_jump[player].value >= 2 and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.heat_runs[player].value >= 3 ) and ( ( logic.metroid_prime_can_sustain_damage(player, 170, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 15, 'HeatDamage2') ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 165, 'HeatDamage1') ) or ( logic.multiworld.r_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 140, 'HeatDamage1') and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) ) ) ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 215, 'HeatDamage1') ) ) ) )),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) or ( ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage2') ) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') ) ) ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 59, 'HeatDamage1') ) ) ) )),
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) ) or ( ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 45, 'HeatDamage2') ) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') ) ) ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 59, 'HeatDamage1') ) ) ) )),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", None),
                ("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", None),
                ("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", (
                ("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 65, 'HeatDamage1') ) ) and ( logic.multiworld.l_jump[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 50, 'HeatDamage2') ) ) or ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and templates['Heat-Resisting Suit'](logic) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage2') and logic.multiworld.bomb_jump[player].value >= 1 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage1') ) ) and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 160, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage1') ) ) and not logic.metroid_prime_has_misc(player, 'dock_rando') ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 70, 'HeatDamage1') ) ) ) or ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.movement[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 10, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 110, 'HeatDamage1') ) ) ) )),
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and ( ( logic.has('Spider Ball', player) and templates['Heat-Resisting Suit'](logic) ) or ( logic.has('Morph Ball Bomb', player) and ( ( logic.multiworld.bomb_jump[player].value >= 2 and logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 95, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage1') ) ) ) or ( logic.multiworld.bomb_jump[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 200, 'HeatDamage2') and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 150, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') ) ) and logic.multiworld.l_jump[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) ) ) ) or ( logic.has('Space Jump Boots', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 125, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage1') ) ) and ( logic.multiworld.r_jump[player].value >= 3 or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 15, 'HeatDamage2') and logic.multiworld.movement[player].value >= 1 ) ) ) or ( logic.has('Scan Visor', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 3 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 135, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage1') ) ) and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 4 and ( templates['Heat-Resisting Suit'](logic) or ( logic.multiworld.heat_runs[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 145, 'HeatDamage1') ) or ( logic.multiworld.heat_runs[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 95, 'HeatDamage1') ) ) and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) )),
                ("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.r_jump[player].value >= 1 or ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or logic.multiworld.scan_dash[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 20, 'HeatDamage2') ) ) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) or templates['Use Grapple Beam'](logic) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage2') ) or ( logic.metroid_prime_has_missiles(player, 3) and templates['Shoot Any Beam'](logic) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.l_jump[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 200, 'HeatDamage2') and logic.multiworld.l_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 4 ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 55, 'HeatDamage2') and logic.multiworld.l_jump[player].value >= 1 ) )),
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.r_jump[player].value >= 1 or ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) or logic.multiworld.scan_dash[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 50, 'HeatDamage2') ) ) or ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 285, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) or templates['Use Grapple Beam'](logic) or ( logic.metroid_prime_has_missiles(player, 3) and templates['Shoot Any Beam'](logic) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 ) or logic.multiworld.scan_dash[player].value >= 4 or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage2') ) )),
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 105, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 120, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) )),
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 105, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) )),
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or logic.metroid_prime_can_sustain_damage(player, 230, 'HeatDamage2') or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage2') ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( not logic.has('Storage Depot B Item', player) and templates['Shoot Any Beam'](logic) ) )),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.jump_off_enemies[player].value >= 5 and logic.multiworld.movement[player].value >= 5 and logic.has('Boost Ball', player) and logic.has('Storage Depot B Item', player) ) )),
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", lambda logic: ( logic.has('Geothermal Core Puzzle', player) or ( logic.multiworld.clip_through_objects[player].value >= 3 ) )),
                ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 185, 'HeatDamage2') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 300, 'HeatDamage2') or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.movement[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 70, 'HeatDamage2') ) ) and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 85, 'HeatDamage2') ) or ( not logic.has('Storage Depot B Item', player) and templates['Shoot Any Beam'](logic) ) )),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or ( logic.multiworld.scan_dash[player].value >= 2 and ( logic.has('Scan Visor', player) or not logic.has('Storage Depot B Item', player) ) ) ) ) or ( templates['Use Grapple Beam'](logic) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", (
                ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) )),
            )
            ),
            (
            "First Spinner (Geothermal Core, Magmoor Caverns)", (
                ("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.spinners_without_boost[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 5 and logic.multiworld.movement[player].value >= 4 and ( logic.multiworld.r_jump[player].value >= 4 or ( logic.multiworld.scan_dash[player].value >= 4 and ( logic.has('Scan Visor', player) or logic.has('Storage Depot B Item', player) ) ) ) ) or ( logic.has('Boost Ball', player) and ( logic.has('Spider Ball', player) or ( logic.multiworld.slope_jump[player].value >= 1 ) ) ) ) ) or ( logic.has('Boost Ball', player) and logic.multiworld.bomb_jump[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 5 and not logic.has('Storage Depot B Item', player) and logic.has('Spider Ball', player) ) ) )),
            )
            ),
            (
            "Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", (
                ("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", None),
                ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)", (
                ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", None),
            )
            ),
            (
            "Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", (
                ("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)", None),
            )
            ),
            (
            "Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", lambda logic: ( templates['Shoot Any Beam'](logic) or logic.has('Space Jump Boots', player) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage2') ) or ( logic.multiworld.gravityless_underwater_movement[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage2') ) )),
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", lambda logic: ( templates['Shoot Any Beam'](logic) or logic.has('Space Jump Boots', player) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 40, 'HeatDamage2') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 100, 'HeatDamage2') ) or ( logic.multiworld.gravityless_underwater_movement[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 80, 'HeatDamage2') ) )),
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) ) and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) ) )),
                ("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Scan Visor', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 4 and logic.multiworld.clip_through_objects[player].value >= 3 and logic.has('Boost Ball', player) and logic.metroid_prime_can_sustain_damage(player, 75, 'HeatDamage2') ) or ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) ) ) and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 )),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( logic.multiworld.slope_jump[player].value >= 1 and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 )),
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", lambda logic: ( logic.multiworld.standable_terrain[player].value >= 1 and ( templates['Heat-Resisting Suit'](logic) or logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", None),
            )
            ),
            (
            "Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", (
                ("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", None),
                ("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", None),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", (
                ("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", None),
                ("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", (
                ("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", None),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", None),
                ("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", None),
                ("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", (
                ("Save Station (Save Station Magmoor B, Magmoor Caverns)", None),
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station Magmoor B, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", None),
            )
            ),
            (
            "Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", None),
                ("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", (
                ("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", None),
                ("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Quarry (Quarry Access, Phazon Mines)", (
                ("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", None),
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", (
                ("Door to Main Quarry (Quarry Access, Phazon Mines)", None),
                ("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Waste Disposal (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", None),
                ("Crane Platform (Main Quarry, Phazon Mines)", templates['Use Grapple Beam']),
                ("Door to Main Quarry (Waste Disposal, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Quarry Access (Main Quarry, Phazon Mines)", (
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) and templates['Use Grapple Beam'](logic) )),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or logic.multiworld.movement[player].value >= 2 or logic.has('Space Jump Boots', player) or logic.multiworld.l_jump[player].value >= 1 )),
                ("Door to Security Access A (Main Quarry, Phazon Mines)", lambda logic: logic.has('Main Quarry Barrier', player)),
                ("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", lambda logic: logic.has('Scan Visor', player)),
                ("Crane Platform (Main Quarry, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Grapple Beam', player) and logic.multiworld.movement[player].value >= 1 ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 and logic.multiworld.slope_jump[player].value >= 2 ) )),
                ("Door to Main Quarry (Quarry Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Save Station Mines A (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", None),
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Security Access A (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", lambda logic: ( logic.has('Main Quarry Barrier', player) or logic.metroid_prime_has_misc(player, 'backwards_upper_mines') )),
                ("Door to Main Quarry (Security Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Main Quarry, Phazon Mines)", (
                ("Crane Platform (Main Quarry, Phazon Mines)", None),
            )
            ),
            (
            "Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", None),
            )
            ),
            (
            "Crane Platform (Main Quarry, Phazon Mines)", (
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", lambda logic: ( templates['Use Grapple Beam'](logic) or ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.multiworld.r_jump[player].value >= 2 ) ) ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 3 ) )),
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", None),
                ("Pickup (Missile) (Main Quarry, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) or ( logic.multiworld.knowledge[player].value >= 2 and logic.multiworld.movement[player].value >= 2 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.l_jump[player].value >= 1 ) ) ) ) )),
            )
            ),
            (
            "Door to Main Quarry (Waste Disposal, Phazon Mines)", (
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ore Processing (Waste Disposal, Phazon Mines)", (
                ("Door to Main Quarry (Waste Disposal, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) )),
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Main Quarry (Save Station Mines A, Phazon Mines)", (
                ("Save Station (Save Station Mines A, Phazon Mines)", lambda logic: ( logic.has('Phazon Mines Save Station A Barrier', player) )),
                ("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Save Station (Save Station Mines A, Phazon Mines)", (
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", lambda logic: ( logic.has('Phazon Mines Save Station A Barrier', player) )),
            )
            ),
            (
            "Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", (
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", None),
            )
            ),
            (
            "Door to Main Quarry (Security Access A, Phazon Mines)", (
                ("Door to Mine Security Station (Security Access A, Phazon Mines)", None),
                ("Pickup (Missile) (Security Access A, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Security Access A (Main Quarry, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Mine Security Station (Security Access A, Phazon Mines)", (
                ("Door to Main Quarry (Security Access A, Phazon Mines)", None),
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Security Access A, Phazon Mines)", (
                ("Door to Main Quarry (Security Access A, Phazon Mines)", None),
            )
            ),
            (
            "Door to Research Access (Ore Processing, Phazon Mines)", (
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.count('Power Bomb', player) >= 3 and logic.multiworld.wall_boost[player].value >= 3 ) ) and templates['Shoot Power Beam'](logic) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 2 and ( templates['Shoot Power Beam'](logic) or logic.multiworld.combat[player].value >= 3 ) ) )),
                ("Door to Ore Processing (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Storage Depot B (Ore Processing, Phazon Mines)", (
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", lambda logic: ( ( templates['Use Grapple Beam'](logic) or ( logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 ) ) and ( templates['Shoot Wave Beam'](logic) or logic.metroid_prime_can_sustain_damage(player, 50, 'Damage') or logic.multiworld.combat[player].value >= 1 ) )),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", None),
                ("Door to Ore Processing (Storage Depot B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Waste Disposal (Ore Processing, Phazon Mines)", (
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", lambda logic: ( templates['Use Grapple Beam'](logic) or ( logic.has('Space Jump Boots', player) and ( logic.multiworld.r_jump[player].value >= 1 or logic.multiworld.l_jump[player].value >= 1 ) ) or logic.multiworld.standable_terrain[player].value >= 1 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) )),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", None),
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator Access A (Ore Processing, Phazon Mines)", (
                ("Door to Research Access (Ore Processing, Phazon Mines)", None),
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) and ( ( logic.has('Power Bomb', player) and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.l_jump[player].value >= 1 ) ) ) or ( logic.has('Scan Visor', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 4 ) ) ) or templates['Use Grapple Beam'](logic) or ( logic.has('Space Jump Boots', player) and ( ( logic.has('Power Bomb', player) and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.multiworld.r_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.count('Power Bomb', player) >= 4 and logic.multiworld.wall_boost[player].value >= 3 and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.l_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) ) ) )),
                ("Door to Ore Processing (Elevator Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access A (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", None),
                ("Door to Mine Security Station (Security Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access B (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", None),
                ("Door to Mine Security Station (Security Access B, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Storage Depot A (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", lambda logic: ( logic.has('Mine Security Station Barrier', player) )),
                ("Door to Mine Security Station (Storage Depot A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", None),
            )
            ),
            (
            "Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", (
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", None),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", None),
                ("Room Center (Mine Security Station, Phazon Mines)", None),
            )
            ),
            (
            "Room Center (Mine Security Station, Phazon Mines)", (
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", lambda logic: ( logic.has('Mine Security Station Unlock Doors', player) and ( ( templates['Shoot Ice Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 ) )),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", lambda logic: ( logic.has('Mine Security Station Unlock Doors', player) and ( ( templates['Shoot Ice Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 ) )),
                ("Door to Storage Depot A (Mine Security Station, Phazon Mines)", lambda logic: ( logic.has('Mine Security Station Barrier', player) )),
                ("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", lambda logic: ( not logic.has('Mine Security Station Unlock Doors', player) and templates['Shoot Wave Beam'](logic) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 3 or ( logic.multiworld.combat[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') ) ) )),
            )
            ),
            (
            "Door to Ore Processing (Research Access, Phazon Mines)", (
                ("Door to Elite Research (Research Access, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 2 ) )),
                ("Door to Research Access (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Research (Research Access, Phazon Mines)", (
                ("Door to Ore Processing (Research Access, Phazon Mines)", None),
                ("Door to Research Access (Elite Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ore Processing (Storage Depot B, Phazon Mines)", (
                ("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", None),
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)", (
                ("Door to Ore Processing (Storage Depot B, Phazon Mines)", None),
            )
            ),
            (
            "Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", (
                ("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)", None),
            )
            ),
            (
            "Door to Ore Processing (Elevator Access A, Phazon Mines)", (
                ("Door to Elevator A (Elevator Access A, Phazon Mines)", None),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator A (Elevator Access A, Phazon Mines)", (
                ("Door to Ore Processing (Elevator Access A, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Spider Ball', player) or ( logic.has('Space Jump Boots', player) and logic.has('Morph Ball Bomb', player) and templates['Shoot Wave Beam'](logic) and logic.multiworld.bomb_space_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 4 ) ) )),
                ("Door to Elevator Access A (Elevator A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Research (Security Access B, Phazon Mines)", (
                ("Door to Mine Security Station (Security Access B, Phazon Mines)", None),
                ("Door to Security Access B (Elite Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Mine Security Station (Security Access B, Phazon Mines)", (
                ("Door to Elite Research (Security Access B, Phazon Mines)", None),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Mine Security Station (Storage Depot A, Phazon Mines)", (
                ("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)", None),
                ("Door to Storage Depot A (Mine Security Station, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Flamethrower) (Storage Depot A, Phazon Mines)", (
                ("Door to Mine Security Station (Storage Depot A, Phazon Mines)", None),
            )
            ),
            (
            "Door to Research Access (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Elite Research Rock Wall', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 1 ) )),
                ("Door to Elite Research (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access B (Elite Research, Phazon Mines)", (
                ("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( logic.has('Invisible Drone', player) or logic.metroid_prime_has_misc(player, 'phazon_elite_without_dynamo') ) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 ) and templates['Shoot Any Beam'](logic) )),
                ("Top Floor (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) ) and ( ( templates['Shoot Power Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 ) and ( templates['Shoot Any Beam'](logic) or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) )),
                ("Door to Elite Research (Security Access B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", None),
            )
            ),
            (
            "Pickup (Missile) (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.multiworld.standable_terrain[player].value >= 1 )),
            )
            ),
            (
            "Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", (
                ("Door to Security Access B (Elite Research, Phazon Mines)", None),
            )
            ),
            (
            "Top Floor (Elite Research, Phazon Mines)", (
                ("Door to Research Access (Elite Research, Phazon Mines)", lambda logic: logic.has('Elite Research Rock Wall', player)),
                ("Door to Security Access B (Elite Research, Phazon Mines)", lambda logic: ( ( templates['Shoot Power Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 )),
                ("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and ( ( logic.multiworld.spinners_without_boost[player].value >= 2 and logic.has('Morph Ball Bomb', player) ) or ( logic.has('Boost Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) ) ) )),
                ("Pickup (Missile) (Elite Research, Phazon Mines)", lambda logic: ( logic.has('Elite Research Rock Wall', player) and ( logic.has('Space Jump Boots', player) or logic.multiworld.standable_terrain[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Elevator Access A (Elevator A, Phazon Mines)", (
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to Elevator A (Elevator Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control Access (Elevator A, Phazon Mines)", (
                ("Door to Elevator Access A (Elevator A, Phazon Mines)", None),
                ("Door to Elevator A (Elite Control Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator A (Elite Control Access, Phazon Mines)", (
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", None),
                ("Pickup (Missile) (Elite Control Access, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) or ( logic.multiworld.damage_boosting[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 100, 'Damage') ) ) )),
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control (Elite Control Access, Phazon Mines)", (
                ("Door to Elevator A (Elite Control Access, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) ) )),
                ("Door to Elite Control Access (Elite Control, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile) (Elite Control Access, Phazon Mines)", (
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", None),
            )
            ),
            (
            "Door to Maintenance Tunnel (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", None),
                ("Door to Elite Control (Maintenance Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control Access (Elite Control, Phazon Mines)", (
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') )),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Elite Pirate Fight (Elite Control)', player) or ( ( logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.movement[player].value >= 2 ) ) )),
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Elite Control, Phazon Mines)", (
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", lambda logic: ( logic.metroid_prime_has_misc(player, 'backwards_lower_mines') and logic.has('Scan Visor', player) )),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", lambda logic: logic.has('Elite Control Barriers', player)),
                ("Door to Elite Control (Ventilation Shaft, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", None),
            )
            ),
            (
            "Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", None),
            )
            ),
            (
            "Bottom Floor Center (Elite Control, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Elite Control, Phazon Mines)", None),
                ("Door to Elite Control Access (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Elite Pirate Fight (Elite Control)', player) or ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.movement[player].value >= 1 ) )),
                ("Door to Ventilation Shaft (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Elite Control Barriers', player) and ( ( logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.has('Elite Pirate Fight (Elite Control)', player) and ( templates['Shoot Ice Beam'](logic) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 ) ) ) )),
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and ( logic.has('Elite Pirate Fight (Elite Control)', player) or ( logic.multiworld.standable_terrain[player].value >= 2 ) ) )),
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", lambda logic: ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') )),
            )
            ),
            (
            "Door to Elite Control (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Maintenance Tunnel (Elite Control, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Elite Control (Maintenance Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Ventilation Shaft, Phazon Mines)", (
                ("Door to Elite Control (Ventilation Shaft, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and ( logic.multiworld.complex_bomb_jump[player].value >= 5 or ( logic.has('Space Jump Boots', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) ) ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 2 and not logic.metroid_prime_has_misc(player, 'dock_rando') ) )),
                ("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control (Ventilation Shaft, Phazon Mines)", (
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", None),
                ("Door to Ventilation Shaft (Elite Control, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)", (
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", None),
            )
            ),
            (
            "Door to Transport Access (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", None),
                ("Door to Phazon Processing Center (Transport Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", (
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", lambda logic: ( ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 2 or ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( ( logic.has('Spider Ball', player) and logic.multiworld.bomb_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 4 ) or ( logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.standable_terrain[player].value >= 5 and logic.multiworld.l_jump[player].value >= 4 ) ) ) ) and ( not logic.has('Plasma Processing Item', player) or ( logic.has('Plasma Processing Item', player) and ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) and templates['Shoot Power Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) ) ) )),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", lambda logic: ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 45, 'Phazon') ) )),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", lambda logic: ( ( ( ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 45, 'Phazon') ) ) and logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 1 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.metroid_prime_can_sustain_damage(player, 65, 'Phazon') and ( ( logic.has('Spider Ball', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 3 ) or ( logic.multiworld.bomb_space_jump[player].value >= 4 and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 3 ) ) ) ) and ( not logic.has('Plasma Processing Item', player) or ( logic.has('Plasma Processing Item', player) and ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) and templates['Shoot Power Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') ) ) ) )),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) and ( logic.has('X-Ray Visor', player) or logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( not logic.has('Plasma Processing Item', player) or ( logic.has('Plasma Processing Item', player) and ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) and templates['Shoot Power Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') ) ) ) )),
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", lambda logic: ( ( ( logic.has('Morph Ball', player) and ( logic.multiworld.l_jump[player].value >= 2 or ( logic.multiworld.bomb_jump[player].value >= 2 and logic.multiworld.invisible_objects[player].value >= 1 ) ) and ( ( logic.multiworld.complex_bomb_jump[player].value >= 3 and logic.multiworld.invisible_objects[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.bomb_jump[player].value >= 3 ) ) and logic.has('Morph Ball Bomb', player) ) or ( logic.has('Space Jump Boots', player) ) ) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", None),
            )
            ),
            (
            "Door to Map Station Mines (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Omega Research (Map Station Mines, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Omega Research, Phazon Mines)", (
                ("Door to Map Station Mines (Omega Research, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", lambda logic: ( ( templates['Shoot Power Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 )),
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Dynamo Access (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", lambda logic: ( ( logic.has('Scan Visor', player) or logic.has('Invisible Drone', player) ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 2 ) ) and ( ( templates['Shoot Power Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 ) )),
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Transport Access, Phazon Mines)", (
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or templates['Use Grapple Beam'](logic) or logic.multiworld.slope_jump[player].value >= 1 )),
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Transport Access, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or templates['Use Grapple Beam'](logic) or logic.multiworld.slope_jump[player].value >= 1 )),
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", lambda logic: ( ( logic.has('Processing Center Access Barrier', player) or logic.metroid_prime_has_misc(player, 'backwards_lower_mines') ) and ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 99, 'Phazon') ) ) )),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Processing Center Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", lambda logic: ( logic.has('Processing Center Access Barrier', player) and ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 199, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 99, 'Phazon') ) ) )),
                ("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", lambda logic: logic.has('Scan Visor', player)),
                ("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)", None),
                ("Door to Processing Center Access (Elite Quarters, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", None),
            )
            ),
            (
            "Pickup (Energy Tank) (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", None),
            )
            ),
            (
            "Door to Omega Research (Map Station Mines, Phazon Mines)", (
                ("Map Station (Map Station Mines, Phazon Mines)", None),
                ("Door to Map Station Mines (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Map Station (Map Station Mines, Phazon Mines)", (
                ("Door to Omega Research (Map Station Mines, Phazon Mines)", None),
            )
            ),
            (
            "Door to Central Dynamo (Dynamo Access, Phazon Mines)", (
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", lambda logic: ( not logic.has('Plasma Beam', player) or logic.has('Elite Pirate Fight (Dynamo Access)', player) )),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", lambda logic: logic.has('Plasma Beam', player)),
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Dynamo Access, Phazon Mines)", (
                ("Door to Central Dynamo (Dynamo Access, Phazon Mines)", lambda logic: ( not logic.has('Plasma Beam', player) or logic.has('Elite Pirate Fight (Dynamo Access)', player) )),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", lambda logic: logic.has('Plasma Beam', player)),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", (
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", lambda logic: ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') )),
            )
            ),
            (
            "Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", None),
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", (
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", None),
                ("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", (
                ("Door to Processing Center Access (Elite Quarters, Phazon Mines)", lambda logic: ( logic.has('Omega Pirate', player) and ( logic.has('Scan Visor', player) or ( logic.has('Space Jump Boots', player) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.bomb_space_jump[player].value >= 3 ) ) )),
                ("Fight Trigger (Elite Quarters, Phazon Mines)", None),
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Processing Center Access (Elite Quarters, Phazon Mines)", (
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", lambda logic: ( logic.has('Omega Pirate', player) )),
                ("Fight Trigger (Elite Quarters, Phazon Mines)", None),
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Omega Pirate (Elite Quarters, Phazon Mines)", (
                ("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)", None),
            )
            ),
            (
            "Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)", (
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", None),
            )
            ),
            (
            "Fight Trigger (Elite Quarters, Phazon Mines)", (
                ("Event - Omega Pirate (Elite Quarters, Phazon Mines)", lambda logic: ( logic.has('X-Ray Visor', player) and ( ( templates['Have all Beams'](logic) and logic.has('Charge Beam', player) and logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') ) or ( logic.has('Charge Beam', player) and logic.multiworld.combat[player].value >= 1 and ( logic.has('Plasma Beam', player) or ( ( templates['Shoot Super Missile'](logic) and logic.metroid_prime_has_missiles(player, 30) ) ) ) and logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) or ( logic.count('Power Bomb', player) >= 3 and logic.multiworld.combat[player].value >= 3 and logic.has('Morph Ball', player) ) or ( logic.multiworld.combat[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') ) or logic.multiworld.combat[player].value >= 5 or ( logic.multiworld.combat[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 500, 'Damage') ) or ( logic.multiworld.combat[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 800, 'Damage') ) ) and templates['Shoot Any Beam'](logic) )),
            )
            ),
            (
            "Door to Dynamo Access (Central Dynamo, Phazon Mines)", (
                ("Fight Trigger (Central Dynamo, Phazon Mines)", None),
                ("Door to Central Dynamo (Dynamo Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Quarantine Access A (Central Dynamo, Phazon Mines)", (
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.infinite_speed[player].value >= 2 and ( logic.has('Power Bomb', player) or logic.has('Morph Ball Bomb', player) ) and logic.metroid_prime_can_sustain_damage(player, 280, 'Damage') )),
                ("Room Bottom (Central Dynamo, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
                ("Door to Central Dynamo (Quarantine Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Save Station Mines B (Central Dynamo, Phazon Mines)", (
                ("Room Bottom (Central Dynamo, Phazon Mines)", None),
                ("Door to Central Dynamo (Save Station Mines B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Security Drone (Central Dynamo, Phazon Mines)", (
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.has('Power Bomb', player) and logic.multiworld.infinite_speed[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 680, 'Damage') ) ) )),
            )
            ),
            (
            "Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", (
                ("Room Bottom (Central Dynamo, Phazon Mines)", None),
            )
            ),
            (
            "Fight Trigger (Central Dynamo, Phazon Mines)", (
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", lambda logic: logic.has('Invisible Drone', player)),
                ("Event - Security Drone (Central Dynamo, Phazon Mines)", lambda logic: ( logic.multiworld.combat[player].value >= 1 or logic.metroid_prime_can_sustain_damage(player, 100, 'Damage') )),
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", lambda logic: ( logic.has('Boost Ball', player) and logic.has('Power Bomb', player) and logic.has('Morph Ball', player) and logic.multiworld.infinite_speed[player].value >= 2 and logic.multiworld.knowledge[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 280, 'Damage') )),
                ("Room Bottom (Central Dynamo, Phazon Mines)", None),
            )
            ),
            (
            "Room Bottom (Central Dynamo, Phazon Mines)", (
                ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( ( logic.has('Invisible Drone', player) and ( logic.has('Ice Beam', player) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) ) or logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Save Station Mines B (Central Dynamo, Phazon Mines)", lambda logic: ( not logic.has('Invisible Drone', player) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') or templates['Shoot Ice Beam'](logic) )),
                ("Fight Trigger (Central Dynamo, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 2 ) ) and ( templates['Shoot Ice Beam'](logic) or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') or logic.multiworld.combat[player].value >= 2 or not logic.has('Invisible Drone', player) ) )),
            )
            ),
            (
            "Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", (
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", lambda logic: ( logic.has('Elite Quarters Access Barrier', player) )),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", lambda logic: ( templates['Shoot Plasma Beam'](logic) )),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", lambda logic: ( logic.has('Elite Quarters Access Barrier', player) )),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", lambda logic: ( logic.metroid_prime_has_misc(player, 'backwards_lower_mines') )),
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", None),
            )
            ),
            (
            "Door to Central Dynamo (Quarantine Access A, Phazon Mines)", (
                ("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", None),
                ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", (
                ("Door to Central Dynamo (Quarantine Access A, Phazon Mines)", None),
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Central Dynamo (Save Station Mines B, Phazon Mines)", (
                ("Save Station (Save Station Mines B, Phazon Mines)", None),
                ("Door to Save Station Mines B (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Save Station (Save Station Mines B, Phazon Mines)", (
                ("Door to Central Dynamo (Save Station Mines B, Phazon Mines)", None),
            )
            ),
            (
            "Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", (
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 1 and ( templates['Use Grapple Beam'](logic) or logic.multiworld.l_jump[player].value >= 2 ) ) or ( logic.multiworld.scan_dash[player].value >= 3 ) ) and ( templates['Shoot Plasma Beam'](logic) or ( logic.multiworld.combat[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') ) ) ) or ( logic.has('Morph Ball', player) and ( ( logic.has('Spider Ball', player) and ( templates['Use Grapple Beam'](logic) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 4 ) ) ) or ( logic.has('Morph Ball Bomb', player) and logic.has('Scan Visor', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 2 ) ) and ( templates['Shoot Plasma Beam'](logic) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) ) )),
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", lambda logic: ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') )),
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 3 and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 3 ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 5 and logic.multiworld.single_room_oob[player].value >= 4 ) ) and ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) )),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.scan_dash[player].value >= 1 ) ) and ( ( templates['Shoot Plasma Beam'](logic) and templates['Shoot Wave Beam'](logic) ) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 125, 'Damage') ) )),
                ("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)", templates['Shoot Super Missile']),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) and logic.metroid_prime_has_misc(player, 'backwards_lower_mines') )),
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", lambda logic: logic.has('Metroid Quarantine B Barrier', player)),
                ("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", None),
            )
            ),
            (
            "Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", (
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", None),
            )
            ),
            (
            "Front of Barrier (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 150, 'Phazon') ) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 50, 'Phazon') ) ) and ( templates['Shoot Plasma Beam'](logic) or logic.multiworld.combat[player].value >= 2 or logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) )),
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", lambda logic: logic.has('Metroid Quarantine B Barrier', player)),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", lambda logic: logic.has('Scan Visor', player)),
            )
            ),
            (
            "Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", (
                ("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", lambda logic: logic.has('Scan Visor', player)),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Metroid Quarantine A Barrier', player) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 or ( logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 1 ) ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 and logic.multiworld.l_jump[player].value >= 3 ) ) )),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( templates['Shoot Ice Beam'](logic) and logic.multiworld.jump_off_enemies[player].value >= 4 and logic.multiworld.l_jump[player].value >= 1 ) or ( ( logic.has('Space Jump Boots', player) and logic.multiworld.jump_off_enemies[player].value >= 3 and templates['Shoot Ice Beam'](logic) ) ) )),
                ("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( logic.has('Metroid Quarantine A Barrier', player) or logic.metroid_prime_has_misc(player, 'backwards_lower_mines') ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 200, 'Phazon') ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 150, 'Phazon') ) ) )),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 2 and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or ( logic.multiworld.r_jump[player].value >= 4 and logic.multiworld.movement[player].value >= 4 ) ) ) )),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and logic.has('Morph Ball Bomb', player) ) or logic.multiworld.scan_dash[player].value >= 3 )),
                ("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 ) )),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or logic.multiworld.standable_terrain[player].value >= 1 )),
            )
            ),
            (
            "Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", None),
            )
            ),
            (
            "Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Metroid Quarantine A Barrier', player) and ( ( logic.has('Space Jump Boots', player) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 or ( logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 1 ) ) ) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 99, 'Phazon') ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 75, 'Phazon') ) or ( logic.multiworld.standable_terrain[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 55, 'Phazon') ) ) )),
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Spider Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) ) or ( ( logic.has('Scan Visor', player) and ( ( logic.has('Space Jump Boots', player) and logic.has('Power Bomb', player) and logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 ) ) ) ) ) )),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) or ( ( logic.multiworld.r_jump[player].value >= 4 and logic.multiworld.movement[player].value >= 3 ) ) ) and logic.has('Space Jump Boots', player) and ( logic.has('X-Ray Visor', player) or ( ( ( logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 1 ) or logic.multiworld.invisible_objects[player].value >= 2 ) ) ) )),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.count('Power Bomb', player) >= 2 )),
            )
            ),
            (
            "Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Metroid Quarantine A Barrier', player) or logic.metroid_prime_has_misc(player, 'backwards_lower_mines') )),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( ( logic.has('X-Ray Visor', player) or ( ( logic.has('Thermal Visor', player) and logic.multiworld.invisible_objects[player].value >= 1 ) ) or logic.multiworld.invisible_objects[player].value >= 2 ) and ( logic.has('Spider Ball', player) or ( ( logic.multiworld.standable_terrain[player].value >= 1 ) ) ) )),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.count('Power Bomb', player) >= 2 )),
            )
            ),
            (
            "Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", (
                ("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.metroid_prime_can_sustain_damage(player, 150, 'Phazon') and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('X-Ray Visor', player) and logic.multiworld.scan_dash[player].value >= 1 and logic.multiworld.l_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 150, 'Phazon') ) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 300, 'Phazon') ) )),
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.metroid_prime_can_sustain_damage(player, 150, 'Phazon') and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'Phazon') ) )),
                ("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", (
                ("Save Station (Save Station Mines C, Phazon Mines)", None),
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Save Station (Save Station Mines C, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", None),
            )
            ),
            (
            "Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", (
                ("Door to Elevator B (Elevator Access B, Phazon Mines)", None),
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator B (Elevator Access B, Phazon Mines)", (
                ("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", None),
                ("Door to Elevator Access B (Elevator B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", None),
                ("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", None),
                ("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", (
                ("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or logic.multiworld.slope_jump[player].value >= 2 ) )),
                ("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or ( logic.multiworld.slope_jump[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.has('Scan Visor', player) ) or ( logic.multiworld.standable_terrain[player].value >= 1 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) or ( templates['Shoot Ice Beam'](logic) and logic.multiworld.jump_off_enemies[player].value >= 4 ) )),
                ("Pickup (Missile) (Fungal Hall B, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", None),
            )
            ),
            (
            "Door to Elevator Access B (Elevator B, Phazon Mines)", (
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Door to Elevator B (Elevator Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall Access (Elevator B, Phazon Mines)", (
                ("Door to Elevator Access B (Elevator B, Phazon Mines)", None),
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", (
                ("Missile Station (Missile Station Mines, Phazon Mines)", None),
                ("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Missile Station (Missile Station Mines, Phazon Mines)", (
                ("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", None),
            )
            ),
            (
            "Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Boost Ball', player) or logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 30, 'Phazon') ) ) )),
                ("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Phazon Suit', player) or ( logic.has('Boost Ball', player) and ( ( logic.multiworld.movement[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 1299, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 1199, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 1099, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 5 and logic.metroid_prime_can_sustain_damage(player, 999, 'Phazon') ) ) ) ) )),
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 30, 'Phazon') ) ) ) ) )),
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Phazon Suit', player) or ( logic.has('Boost Ball', player) and ( ( logic.multiworld.movement[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 200, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 300, 'Phazon') ) or ( logic.multiworld.movement[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 400, 'Phazon') ) ) ) ) )),
            )
            ),
            (
            "Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", (
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.standable_terrain[player].value >= 3 and ( ( logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.multiworld.bomb_space_jump[player].value >= 3 ) ) ) )),
                ("Pickup (Missile) (Fungal Hall Access, Phazon Mines)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Phazon Suit', player) or ( logic.multiworld.movement[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 100, 'Phazon') ) ) )),
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elevator B (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", lambda logic: ( logic.multiworld.movement[player].value >= 1 or logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.multiworld.movement[player].value >= 5 ) )),
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", lambda logic: logic.has('Space Jump Boots', player)),
            )
            ),
            (
            "Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", (
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.slope_jump[player].value >= 1 ) )),
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", lambda logic: ( ( ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.r_jump[player].value >= 2 or templates['Use Grapple Beam'](logic) ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) or ( ( logic.has('Scan Visor', player) and ( ( logic.multiworld.scan_dash[player].value >= 4 and templates['Use Grapple Beam'](logic) ) or logic.multiworld.scan_dash[player].value >= 5 ) ) ) ) and ( ( logic.metroid_prime_has_missiles(player, 4) and templates['Shoot Ice Beam'](logic) ) or ( templates['Shoot Plasma Beam'](logic) and logic.has('Charge Beam', player) ) or ( logic.metroid_prime_can_sustain_damage(player, 599, 'Damage') ) or ( logic.metroid_prime_can_sustain_damage(player, 299, 'Damage') and logic.multiworld.combat[player].value >= 1 and logic.has('Space Jump Boots', player) ) or ( logic.metroid_prime_can_sustain_damage(player, 299, 'Damage') and logic.multiworld.combat[player].value >= 3 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.combat[player].value >= 2 ) or logic.multiworld.combat[player].value >= 4 or ( logic.has('Plasma Beam', player) and logic.multiworld.combat[player].value >= 1 ) or ( logic.has('Plasma Beam', player) and logic.metroid_prime_can_sustain_damage(player, 299, 'Damage') ) ) )),
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Gully (Landing Site, Tallon Overworld)", (
                ("Door to Alcove (Landing Site, Tallon Overworld)", None),
                ("Ship (Landing Site, Tallon Overworld)", None),
                ("Door to Landing Site (Gully, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Canyon Cavern (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", None),
                ("Door to Landing Site (Canyon Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Hall (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", None),
                ("Door to Landing Site (Temple Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Alcove (Landing Site, Tallon Overworld)", (
                ("Door to Gully (Landing Site, Tallon Overworld)", None),
                ("Ship (Landing Site, Tallon Overworld)", None),
                ("Door to Landing Site (Alcove, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Waterfall Cavern (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", None),
                ("Door to Landing Site (Waterfall Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", None),
            )
            ),
            (
            "Ship (Landing Site, Tallon Overworld)", (
                ("Door to Gully (Landing Site, Tallon Overworld)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 2 and not logic.metroid_prime_has_misc(player, 'dock_rando') ) )),
                ("Door to Canyon Cavern (Landing Site, Tallon Overworld)", None),
                ("Door to Temple Hall (Landing Site, Tallon Overworld)", None),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", None),
                ("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)", lambda logic: logic.has('Morph Ball', player)),
            )
            ),
            (
            "Door to Tallon Canyon (Gully, Tallon Overworld)", (
                ("Door to Landing Site (Gully, Tallon Overworld)", None),
                ("Door to Gully (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Gully, Tallon Overworld)", (
                ("Door to Tallon Canyon (Gully, Tallon Overworld)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or logic.has('Space Jump Boots', player) )),
                ("Door to Gully (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", (
                ("Door to Landing Site (Canyon Cavern, Tallon Overworld)", None),
                ("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Canyon Cavern, Tallon Overworld)", (
                ("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", None),
                ("Door to Canyon Cavern (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Security Station (Temple Hall, Tallon Overworld)", (
                ("Door to Landing Site (Temple Hall, Tallon Overworld)", None),
                ("Door to Temple Hall (Temple Security Station, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Temple Hall, Tallon Overworld)", (
                ("Door to Temple Security Station (Temple Hall, Tallon Overworld)", None),
                ("Door to Temple Hall (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Alcove, Tallon Overworld)", (
                ("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)", None),
                ("Door to Alcove (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Space Jump Boots) (Alcove, Tallon Overworld)", (
                ("Door to Landing Site (Alcove, Tallon Overworld)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.multiworld.slope_jump[player].value >= 1 or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Landing Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Landing Site (Waterfall Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", None),
                ("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", None),
                ("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gully (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Space Jump Boots', player) ) )),
                ("Door to Tallon Canyon (Gully, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", None),
                ("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Half Pipe (Tallon Canyon, Tallon Overworld)", (
                ("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", None),
                ("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", None),
                ("Door to Gully (Tallon Canyon, Tallon Overworld)", lambda logic: ( ( logic.has('Morph Ball Bomb', player) and logic.has('Morph Ball', player) and logic.has('Boost Ball', player) ) )),
                ("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Temple Hall (Temple Security Station, Tallon Overworld)", (
                ("Door to Temple Lobby (Temple Security Station, Tallon Overworld)", None),
                ("Door to Temple Security Station (Temple Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Lobby (Temple Security Station, Tallon Overworld)", (
                ("Door to Temple Hall (Temple Security Station, Tallon Overworld)", None),
                ("Door to Temple Security Station (Temple Lobby, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", lambda logic: ( templates['Use Grapple Beam'](logic) or ( ( logic.has('Space Jump Boots', player) and ( ( logic.has('Morph Ball', player) ) or ( logic.has('Scan Visor', player) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.has('Gravity Suit', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.l_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) ) ) or ( logic.has('Morph Ball', player) and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) ) )),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.has('Gravity Suit', player) or logic.multiworld.l_jump[player].value >= 1 or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) ) or ( logic.has('Scan Visor', player) and ( logic.multiworld.scan_dash[player].value >= 2 or ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 1 ) ) ) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_has_misc(player, 'NoGravity') and not logic.has('Gravity Suit', player) and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) or ( templates['Use Grapple Beam'](logic) and logic.multiworld.movement[player].value >= 1 ) or ( logic.has('Gravity Suit', player) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", None),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", lambda logic: ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.l_jump[player].value >= 3 ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 and logic.multiworld.movement[player].value >= 2 ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", lambda logic: ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 )),
                ("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", None),
                ("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", (
                ("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", None),
                ("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", None),
                ("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Cave (Root Tunnel, Tallon Overworld)", (
                ("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", None),
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", (
                ("Door to Root Cave (Root Tunnel, Tallon Overworld)", None),
                ("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Artifact Temple (Temple Lobby, Tallon Overworld)", (
                ("Door to Temple Security Station (Temple Lobby, Tallon Overworld)", None),
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Security Station (Temple Lobby, Tallon Overworld)", (
                ("Door to Artifact Temple (Temple Lobby, Tallon Overworld)", None),
                ("Door to Temple Lobby (Temple Security Station, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", None),
                ("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", None),
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
            )
            ),
            (
            "Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", None),
                ("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", (
                ("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Tunnel B (Root Cave, Tallon Overworld)", (
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", None),
                ("Door to Root Cave (Transport Tunnel B, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Tunnel (Root Cave, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", None),
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( templates['Use Grapple Beam'](logic) or ( logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) ) and ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) ) ) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 3 and logic.has('Power Bomb', player) and ( ( logic.multiworld.instant_unmorph_jump[player].value >= 4 and logic.multiworld.wall_boost[player].value >= 5 ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_space_jump[player].value >= 3 ) ) and ( logic.multiworld.movement[player].value >= 4 ) and ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 2 ) ) ) )),
                ("Door to Root Cave (Root Tunnel, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Arbor Chamber (Root Cave, Tallon Overworld)", (
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", None),
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", lambda logic: ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( logic.has('Space Jump Boots', player) or logic.multiworld.scan_dash[player].value >= 2 ) )),
                ("Door to Root Cave (Arbor Chamber, Tallon Overworld)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", None),
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", None),
                ("Door to Arbor Chamber (Root Cave, Tallon Overworld)", lambda logic: ( logic.has('Space Jump Boots', player) and ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Temple Lobby (Artifact Temple, Tallon Overworld)", (
                ("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)", None),
                ("Event - Meta Ridley (Artifact Temple, Tallon Overworld)", lambda logic: ( logic.has('Artifact of Chozo', player) and logic.has('Artifact of Elder', player) and logic.has('Artifact of Lifegiver', player) and logic.has('Artifact of Nature', player) and logic.has('Artifact of Newborn', player) and logic.has('Artifact of Spirit', player) and logic.has('Artifact of Strength', player) and logic.has('Artifact of Sun', player) and logic.has('Artifact of Truth', player) and logic.has('Artifact of Warrior', player) and logic.has('Artifact of Wild', player) and logic.has('Artifact of World', player) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) and ( logic.metroid_prime_can_sustain_damage(player, 400, 'Damage') or ( logic.multiworld.combat[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 300, 'Damage') ) or ( logic.multiworld.combat[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) or ( logic.multiworld.combat[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 100, 'Damage') ) or logic.multiworld.combat[player].value >= 4 ) and templates['Shoot Any Beam'](logic) )),
                ("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", lambda logic: logic.has('Meta Ridley', player)),
                ("Door to Artifact Temple (Temple Lobby, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", None),
            )
            ),
            (
            "Event - Meta Ridley (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", None),
            )
            ),
            (
            "Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) ) )),
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", lambda logic: logic.has('Morph Ball', player)),
                ("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", None),
                ("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Cave (Transport Tunnel B, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", None),
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", (
                ("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", None),
                ("Door to Root Cave (Transport Tunnel B, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Root Cave (Arbor Chamber, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)", None),
                ("Door to Arbor Chamber (Root Cave, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)", (
                ("Door to Root Cave (Arbor Chamber, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", lambda logic: ( logic.has('Main Ventilation Shaft Section B Conduit', player) or logic.metroid_prime_has_misc(player, 'backwards_frigate') )),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and templates['Shoot Wave Beam'](logic) and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.single_room_oob[player].value >= 4 and not logic.metroid_prime_has_misc(player, 'backwards_frigate') )),
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", lambda logic: logic.has('Main Ventilation Shaft Section B Conduit', player)),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", None),
                ("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", (
                ("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", None),
                ("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", (
                ("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", None),
                ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", None),
                ("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Reactor Access (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", None),
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", None),
                ("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Room Bottom (Reactor Core, Tallon Overworld)", (
                ("Door to Reactor Access (Reactor Core, Tallon Overworld)", lambda logic: ( logic.has('Reactor Core Conduits', player) and ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) )),
                ("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", lambda logic: ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 and logic.multiworld.gravityless_underwater_movement[player].value >= 4 ) )),
                ("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 3 ) ) )),
            )
            ),
            (
            "Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", None),
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Reactor Core (Reactor Access, Tallon Overworld)", (
                ("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", lambda logic: ( logic.has('Reactor Access Conduits', player) )),
                ("Door to Savestation (Reactor Access, Tallon Overworld)", None),
                ("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Door to Reactor Access (Reactor Core, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Savestation (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", None),
                ("Door to Reactor Access (Savestation, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", lambda logic: logic.has('Cargo Freight Lift to Deck Gamma Conduits', player)),
                ("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", lambda logic: ( templates['Shoot Any Beam'](logic) and ( logic.metroid_prime_has_missiles(player, 1) or logic.has('Charge Beam', player) ) )),
                ("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) ) ) or ( not logic.has('Gravity Suit', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) or ( logic.has('Morph Ball', player) and logic.multiworld.slope_jump[player].value >= 4 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) and logic.metroid_prime_has_misc(player, 'NoGravity') ) ) ) ) )),
                ("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", None),
                ("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", None),
            )
            ),
            (
            "Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Reactor Access (Savestation, Tallon Overworld)", (
                ("Save Station (Savestation, Tallon Overworld)", None),
                ("Door to Savestation (Reactor Access, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Savestation, Tallon Overworld)", (
                ("Door to Reactor Access (Savestation, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", (
                ("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", (
                ("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", (
                ("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", None),
                ("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", None),
                ("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", None),
            )
            ),
            (
            "Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", None),
            )
            ),
            (
            "Room Bottom (Biohazard Containment, Tallon Overworld)", (
                ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", lambda logic: ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 1 ) ) ) or ( ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) ) ) )),
                ("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", lambda logic: ( logic.has('Biohazard Containment Conduits', player) )),
                ("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)", lambda logic: ( templates['Shoot Super Missile'](logic) )),
            )
            ),
            (
            "Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", (
                ("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", (
                ("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", None),
                ("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", None),
                ("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Room Center (Biotech Research Area 1, Tallon Overworld)", (
                ("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", lambda logic: ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or logic.multiworld.standable_terrain[player].value >= 1 ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.gravityless_underwater_movement[player].value >= 1 and ( logic.multiworld.slope_jump[player].value >= 1 or logic.multiworld.standable_terrain[player].value >= 1 ) ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) )),
                ("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", lambda logic: ( logic.has('Biotech Research Area 1 Conduits', player) and ( ( logic.multiworld.l_jump[player].value >= 1 and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) ) ) or ( logic.has('Space Jump Boots', player) and ( logic.has('Gravity Suit', player) or ( logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) ) ) )),
                ("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", lambda logic: ( templates['Shoot Wave Beam'](logic) and ( logic.has('Thermal Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) )),
            )
            ),
            (
            "Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", (
                ("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", None),
                ("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", (
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", lambda logic: ( logic.has('Gravity Suit', player) or logic.has('Space Jump Boots', player) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) )),
                ("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", (
                ("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", lambda logic: ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) ) ) or ( logic.multiworld.gravityless_underwater_movement[player].value >= 4 and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 3 ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.slope_jump[player].value >= 4 ) ) ) )),
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Gravity Suit', player) and logic.has('Morph Ball Bomb', player) ) or ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) ) )),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Gravity Suit', player) )),
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.has('Gravity Suit', player) ) or ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) ) )),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Gravity Suit', player) and logic.has('Morph Ball Bomb', player) ) or ( not logic.has('Gravity Suit', player) and logic.metroid_prime_has_misc(player, 'NoGravity') and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) )),
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Gravity Suit', player) and logic.has('Morph Ball Bomb', player) ) or ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) ) )),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", lambda logic: ( ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) or logic.has('Space Jump Boots', player) or logic.has('Gravity Suit', player) )),
                ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", None),
                ("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", (
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", lambda logic: ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.jump_off_enemies[player].value >= 3 and logic.metroid_prime_can_sustain_damage(player, 200, 'Damage') ) ) )),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", lambda logic: ( ( logic.has('Space Jump Boots', player) and ( logic.multiworld.standable_terrain[player].value >= 1 or ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) ) ) or ( logic.has('Morph Ball', player) and ( ( logic.has('Spider Ball', player) and ( ( logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.bomb_jump[player].value >= 5 and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.movement[player].value >= 5 and logic.multiworld.scan_dash[player].value >= 4 ) ) ) )),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", lambda logic: ( logic.has('Great Tree Hall Bars Unlocked', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) )),
                ("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", lambda logic: ( ( logic.has('X-Ray Visor', player) or logic.multiworld.invisible_objects[player].value >= 1 ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) )),
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", None),
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", (
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", None),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Scan Visor', player) and logic.has('Morph Ball', player) and logic.multiworld.scan_dash[player].value >= 5 and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 5 ) ) ) )),
                ("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Open gate (Great Tree Hall, Tallon Overworld)", (
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", None),
            )
            ),
            (
            "Next to Spinner (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", lambda logic: ( logic.has('Great Tree Hall Bars Unlocked', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) )),
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", None),
                ("Event - Open gate (Great Tree Hall, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) )),
            )
            ),
            (
            "Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)", None),
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)", (
                ("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", None),
            )
            ),
            (
            "Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", (
                ("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", None),
                ("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", None),
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", (
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Boost Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.multiworld.wall_boost[player].value >= 2 ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) ) and logic.has('Power Bomb', player) )),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", (
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) ) )),
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Boost Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.multiworld.wall_boost[player].value >= 2 ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 ) ) and logic.has('Power Bomb', player) )),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 ) ) )),
            )
            ),
            (
            "Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) ) )),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
            )
            ),
            (
            "Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", (
                ("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", None),
                ("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", (
                ("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", None),
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", None),
                ("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", (
                ("Front of PB Wall (Life Grove, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)", (
                ("Front of PB Wall (Life Grove, Tallon Overworld)", None),
            )
            ),
            (
            "Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)", (
                ("Behind PB Wall (Life Grove, Tallon Overworld)", None),
            )
            ),
            (
            "Behind PB Wall (Life Grove, Tallon Overworld)", (
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", lambda logic: ( templates['Shoot Power Beam'](logic) and ( logic.has('Space Jump Boots', player) or ( ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) or logic.multiworld.scan_dash[player].value >= 4 ) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.multiworld.l_jump[player].value >= 3 and logic.multiworld.r_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 2 and ( logic.multiworld.slope_jump[player].value >= 3 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 4 ) ) and ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) or logic.multiworld.movement[player].value >= 4 ) ) ) ) ) and logic.has('Morph Ball', player) )),
                ("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.single_room_oob[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) or ( ( logic.has('Boost Ball', player) or logic.multiworld.spinners_without_boost[player].value >= 3 ) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) or ( logic.multiworld.l_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 2 ) ) ) ) )),
                ("Front of PB Wall (Life Grove, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
            )
            ),
            (
            "Front of PB Wall (Life Grove, Tallon Overworld)", (
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 and logic.multiworld.r_jump[player].value >= 2 )),
                ("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)", None),
                ("Behind PB Wall (Life Grove, Tallon Overworld)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) )),
            )
            ),
            (
            "Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", (
                ("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", None),
                ("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", (
                ("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", None),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", None),
                ("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", (
                ("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", None),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Plaza (Ruins Entrance, Chozo Ruins)", (
                ("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", None),
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", (
                ("Door to Main Plaza (Ruins Entrance, Chozo Ruins)", None),
                ("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", lambda logic: ( templates['Shoot Super Missile'](logic) and ( logic.has('Space Jump Boots', player) or logic.multiworld.movement[player].value >= 1 ) )),
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.movement[player].value >= 1 ) or logic.multiworld.movement[player].value >= 2 ) ) or ( logic.has('Space Jump Boots', player) and ( logic.multiworld.l_jump[player].value >= 2 or logic.multiworld.r_jump[player].value >= 2 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) or ( logic.multiworld.scan_dash[player].value >= 5 and logic.has('Chozo - Fallen Rubble', player) and logic.multiworld.damage_boosting[player].value >= 4 and logic.has('Scan Visor', player) ) )),
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruins Entrance (Main Plaza, Chozo Ruins)", (
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", None),
                ("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", None),
                ("Door to Nursery Access (Main Plaza, Chozo Ruins)", None),
                ("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 3 ) or ( logic.multiworld.movement[player].value >= 4 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 1 ) )),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 )),
                ("Door to Main Plaza (Ruins Entrance, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Nursery Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Door to Main Plaza (Nursery Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door from Plaza Access (Main Plaza, Chozo Ruins)", (
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( templates['Use Grapple Beam'](logic) or ( logic.has('Scan Visor', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 ) ) )),
                ("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Main Plaza, Chozo Ruins)", (
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)", (
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Locked Door Ledge (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Door from Plaza Access (Main Plaza, Chozo Ruins)", lambda logic: logic.metroid_prime_has_misc(player, 'main_plaza_door')),
                ("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Grapple Ledge (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( templates['Use Grapple Beam'](logic) and ( logic.has('Space Jump Boots', player) or logic.multiworld.movement[player].value >= 3 or logic.multiworld.standable_terrain[player].value >= 2 ) ) or ( logic.has('Space Jump Boots', player) and ( ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or logic.multiworld.standable_terrain[player].value >= 3 ) ) or ( logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 ) ) )),
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Space Jump Boots', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.movement[player].value >= 3 and logic.multiworld.single_room_oob[player].value >= 3 ) )),
                ("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)", None),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.l_jump[player].value >= 5 and logic.multiworld.single_room_oob[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 4 )),
            )
            ),
            (
            "Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", (
                ("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", None),
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", (
                ("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", None),
                ("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", (
                ("Door to Main Plaza (Nursery Access, Chozo Ruins)", None),
                ("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Nursery Access, Chozo Ruins)", (
                ("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", None),
                ("Door to Nursery Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Plaza Access, Chozo Ruins)", (
                ("Door to Vault (Plaza Access, Chozo Ruins)", None),
                ("Door from Plaza Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault (Plaza Access, Chozo Ruins)", (
                ("Door to Main Plaza (Plaza Access, Chozo Ruins)", None),
                ("Door to Plaza Access (Vault, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", (
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", (
                ("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", None),
                ("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", None),
                ("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", (
                ("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", None),
                ("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and ( logic.has('Flaahgra', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 3 ) ) )),
                ("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 )),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) )),
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", None),
                ("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", (
                ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", lambda logic: ( ( logic.has('Boost Ball', player) and logic.has('Morph Ball', player) and logic.has('Spider Ball', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 ) or ( logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 ) )),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 3 ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 ) ) )),
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 )),
                ("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
            )
            ),
            (
            "Pit (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.scan_dash[player].value >= 2 and ( logic.has('Scan Visor', player) or not logic.has('Beetle Battle', player) ) ) or ( logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.has('Morph Ball', player) and ( logic.has('Ruined Shrine Item (Morph Ball)', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) ) ) )),
                ("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
                ("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", lambda logic: ( templates['Shoot Any Beam'](logic) or ( logic.multiworld.combat[player].value >= 2 and logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.count('Power Bomb', player) >= 4 ) ) )),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or logic.has('Beetle Battle', player) or ( logic.multiworld.standable_terrain[player].value >= 2 and ( logic.multiworld.scan_dash[player].value >= 3 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 2 ) ) ) )),
            )
            ),
            (
            "Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", (
                ("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", (
                ("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", None),
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", (
                ("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", None),
                ("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault Access (Vault, Chozo Ruins)", (
                ("Door to Plaza Access (Vault, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Vault, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Space Jump Boots', player) and logic.count('Power Bomb', player) >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.knowledge[player].value >= 1 ) ) ) )),
                ("Door to Vault (Vault Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Access (Vault, Chozo Ruins)", (
                ("Door to Vault Access (Vault, Chozo Ruins)", None),
                ("Door to Vault (Plaza Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Vault, Chozo Ruins)", (
                ("Door to Vault Access (Vault, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Training Chamber Access (Training Chamber, Chozo Ruins)", (
                ("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", lambda logic: logic.has('Training Chamber Exit Tunnel', player)),
                ("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Boost Ball', player) and logic.has('Spider Ball', player) and ( ( logic.has('Chozo Ghosts (Training Chamber)', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.bomb_space_jump[player].value >= 5 and logic.multiworld.complex_bomb_jump[player].value >= 4 and logic.multiworld.movement[player].value >= 4 and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 ) ) ) )),
                ("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", templates['Shoot Power Beam']),
                ("Event - Unlock morph track (Training Chamber, Chozo Ruins)", lambda logic: ( logic.has('Chozo Ghosts (Training Chamber)', player) and logic.has('Boost Ball', player) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", lambda logic: logic.has('Training Chamber Exit Tunnel', player)),
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Spider Ball', player) or ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 2 ) ) or ( logic.multiworld.movement[player].value >= 4 ) ) and ( ( logic.has('Chozo Ghosts (Training Chamber)', player) ) or ( ( logic.has('Morph Ball Bomb', player) and logic.has('Space Jump Boots', player) and logic.multiworld.bomb_space_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.knowledge[player].value >= 2 ) ) ) )),
            )
            ),
            (
            "Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Unlock morph track (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Arboretum (Arboretum Access, Chozo Ruins)", (
                ("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", None),
                ("Door to Arboretum Access (Arboretum, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", (
                ("Door to Arboretum (Arboretum Access, Chozo Ruins)", None),
                ("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Magma Pool (Meditation Fountain, Chozo Ruins)", (
                ("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", None),
                ("Door to Meditation Fountain (Magma Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", (
                ("Door to Magma Pool (Meditation Fountain, Chozo Ruins)", None),
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tower of Light (Tower of Light Access, Chozo Ruins)", (
                ("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", None),
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", (
                ("Door to Tower of Light (Tower of Light Access, Chozo Ruins)", None),
                ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", None),
                ("Door to Ruined Nursery (Save Station 1, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to North Atrium (Ruined Nursery, Chozo Ruins)", (
                ("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", None),
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", None),
                ("Door to Ruined Nursery (North Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( ( logic.multiworld.standable_terrain[player].value >= 4 or ( ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) and ( logic.multiworld.movement[player].value >= 4 or ( ( logic.has('Boost Ball', player) and logic.multiworld.movement[player].value >= 2 ) ) ) ) ) )),
                ("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)", (
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Vault (Vault Access, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Vault Access (Vault, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", (
                ("Door to Vault (Vault Access, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Magma Pool (Training Chamber Access, Chozo Ruins)", (
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", None),
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Training Chamber (Training Chamber Access, Chozo Ruins)", (
                ("Door to Magma Pool (Training Chamber Access, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)", (
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", (
                ("Front of Gate (Arboretum, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( logic.has('Arboretum Gate', player) or ( logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 1 ) or ( logic.multiworld.bomb_jump[player].value >= 2 ) ) )),
                ("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Arboretum Access (Arboretum, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", None),
                ("Door to Arboretum (Arboretum Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall Access (Arboretum, Chozo Ruins)", (
                ("Door to Arboretum Access (Arboretum, Chozo Ruins)", None),
                ("Front of Gate (Arboretum, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) ) or logic.has('Space Jump Boots', player) )),
                ("Door to Arboretum (Gathering Hall Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Front of Gate (Arboretum, Chozo Ruins)", (
                ("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and ( logic.has('Arboretum Gate', player) or ( logic.multiworld.bomb_jump[player].value >= 3 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.has('Boost Ball', player) and logic.multiworld.single_room_oob[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.clip_through_objects[player].value >= 4 ) ) )),
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", None),
                ("Event - Open gate (Arboretum, Chozo Ruins)", lambda logic: logic.has('Scan Visor', player)),
            )
            ),
            (
            "Event - Open gate (Arboretum, Chozo Ruins)", (
                ("Front of Gate (Arboretum, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Training Chamber Access (Magma Pool, Chozo Ruins)", (
                ("Door to Meditation Fountain (Magma Pool, Chozo Ruins)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( ( templates['Heat-Resisting Suit'](logic) or ( logic.metroid_prime_can_sustain_damage(player, 70, 'HeatDamage1') and logic.multiworld.heat_runs[player].value >= 1 ) ) and logic.has('Space Jump Boots', player) and ( ( logic.multiworld.movement[player].value >= 2 and ( logic.metroid_prime_can_sustain_damage(player, 220, 'HeatDamage2') or logic.multiworld.standable_terrain[player].value >= 2 ) ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) ) ) )),
                ("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Power Bomb', player) and ( templates['Heat-Resisting Suit'](logic) or ( logic.metroid_prime_can_sustain_damage(player, 60, 'HeatDamage1') and logic.multiworld.heat_runs[player].value >= 1 ) ) )),
                ("Door to Magma Pool (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Meditation Fountain (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", lambda logic: ( ( templates['Use Grapple Beam'](logic) and templates['Heat-Resisting Suit'](logic) ) or ( logic.has('Space Jump Boots', player) and ( ( logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.movement[player].value >= 2 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 ) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 50, 'HeatDamage2') and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 ) ) and ( templates['Heat-Resisting Suit'](logic) or ( logic.metroid_prime_can_sustain_damage(player, 99, 'HeatDamage1') and logic.multiworld.heat_runs[player].value >= 1 ) ) ) )),
                ("Door to Magma Pool (Meditation Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", lambda logic: ( templates['Heat-Resisting Suit'](logic) or ( logic.metroid_prime_can_sustain_damage(player, 35, 'HeatDamage1') and logic.multiworld.heat_runs[player].value >= 1 ) )),
            )
            ),
            (
            "Door to Tower of Light Access (Tower of Light, Chozo Ruins)", (
                ("Door to Tower Chamber (Tower of Light, Chozo Ruins)", lambda logic: ( ( logic.has('Gravity Suit', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) or ( not logic.has('Gravity Suit', player) and logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_has_misc(player, 'NoGravity') and logic.multiworld.gravityless_underwater_movement[player].value >= 2 ) )),
                ("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)", lambda logic: ( ( logic.metroid_prime_has_missiles(player, 36) and templates['Shoot Any Beam'](logic) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 4 ) ) ) or ( logic.has('Space Jump Boots', player) and ( ( ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.multiworld.scan_dash[player].value >= 2 and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 3 ) or ( logic.multiworld.r_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 1 ) ) ) ) )),
                ("Door to Tower of Light (Tower of Light Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Tower Chamber (Tower of Light, Chozo Ruins)", (
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", None),
                ("Door to Tower of Light (Tower Chamber, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Wavebuster) (Tower of Light, Chozo Ruins)", (
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Ruined Nursery (Save Station 1, Chozo Ruins)", (
                ("Save Station (Save Station 1, Chozo Ruins)", None),
                ("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 1, Chozo Ruins)", (
                ("Door to Ruined Nursery (Save Station 1, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Ruined Nursery (North Atrium, Chozo Ruins)", (
                ("Door to Ruined Gallery (North Atrium, Chozo Ruins)", None),
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Gallery (North Atrium, Chozo Ruins)", (
                ("Door to Ruined Nursery (North Atrium, Chozo Ruins)", None),
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", None),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", (
                ("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", None),
                ("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", (
                ("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", None),
                ("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", (
                ("Door to Arboretum (Gathering Hall Access, Chozo Ruins)", None),
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Arboretum (Gathering Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", None),
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tower of Light (Tower Chamber, Chozo Ruins)", (
                ("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)", None),
                ("Door to Tower Chamber (Tower of Light, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)", (
                ("Door to Tower of Light (Tower Chamber, Chozo Ruins)", None),
            )
            ),
            (
            "Door to North Atrium (Ruined Gallery, Chozo Ruins)", (
                ("Door to Totem Access (Ruined Gallery, Chozo Ruins)", None),
                ("Door to Map Station (Ruined Gallery, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)", lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) )),
                ("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) )),
                ("Door to Ruined Gallery (North Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Totem Access (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", None),
                ("Door to Ruined Gallery (Totem Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Map Station (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", None),
                ("Door to Ruined Gallery (Map Station, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Sun Tower Access (Sun Tower, Chozo Ruins)", (
                ("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", lambda logic: ( logic.has('Flaahgra', player) )),
                ("Door to Sun Tower (Sun Tower Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) and ( logic.has('Sun Tower Spider Track Unlocked', player) or ( ( ( logic.has('Space Jump Boots', player) and logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.movement[player].value >= 3 ) or ( logic.multiworld.complex_bomb_jump[player].value >= 5 and logic.multiworld.movement[player].value >= 5 ) ) and ( ( logic.metroid_prime_has_missiles(player, 4) and templates['Shoot Any Beam'](logic) ) or logic.multiworld.combat[player].value >= 5 ) ) ) )),
                ("Event - Unlock spider track (Sun Tower, Chozo Ruins)", lambda logic: ( templates['Shoot Super Missile'](logic) and logic.has('Scan Visor', player) )),
                ("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) and logic.has('Sun Tower Spider Track Unlocked', player) and logic.has('Flaahgra', player) )),
                ("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Unlock spider track (Sun Tower, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 20, 'Damage') ) or ( logic.has('Spider Ball', player) ) or ( logic.multiworld.instant_unmorph_jump[player].value >= 5 and logic.has('Space Jump Boots', player) ) ) and logic.multiworld.knowledge[player].value >= 2 )),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.has('Spider Ball', player) )),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Hive Totem (Transport Access North, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)", None),
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", (
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) ) or ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) ) )),
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Access North, Chozo Ruins)", (
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Sunchamber (Sunchamber Access, Chozo Ruins)", (
                ("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", None),
                ("Door to Sunchamber Access (Sunchamber, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", (
                ("Door to Sunchamber (Sunchamber Access, Chozo Ruins)", lambda logic: ( not logic.has('Flaahgra', player) or ( logic.has('Flaahgra', player) and logic.has('Chozo Ghosts (Sunchamber)', player) ) )),
                ("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", None),
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", None),
                ("Door to Save Station 2 (Gathering Hall, Chozo Ruins)", None),
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) or logic.has('Space Jump Boots', player) or logic.multiworld.l_jump[player].value >= 1 or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) )),
                ("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station 2 (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", None),
                ("Door to Gathering Hall (Save Station 2, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to East Atrium (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Space Jump Boots', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Power Bomb', player) and logic.multiworld.scan_dash[player].value >= 5 and logic.multiworld.standable_terrain[player].value >= 5 and logic.has('Scan Visor', player) ) ) )),
                ("Door to Gathering Hall (East Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)", (
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Ruined Gallery (Totem Access, Chozo Ruins)", (
                ("Door to Hive Totem (Totem Access, Chozo Ruins)", None),
                ("Door to Totem Access (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hive Totem (Totem Access, Chozo Ruins)", (
                ("Door to Ruined Gallery (Totem Access, Chozo Ruins)", None),
                ("Door to Totem Access (Hive Totem, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Gallery (Map Station, Chozo Ruins)", (
                ("Map Station (Map Station, Chozo Ruins)", None),
                ("Door to Map Station (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Map Station (Map Station, Chozo Ruins)", (
                ("Door to Ruined Gallery (Map Station, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Sunchamber (Sun Tower Access, Chozo Ruins)", (
                ("Door to Sun Tower (Sun Tower Access, Chozo Ruins)", None),
                ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sun Tower (Sun Tower Access, Chozo Ruins)", (
                ("Door to Sunchamber (Sun Tower Access, Chozo Ruins)", None),
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Totem Access (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", lambda logic: ( logic.has('Hive Mecha', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.movement[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or ( logic.multiworld.slope_jump[player].value >= 2 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 and ( logic.metroid_prime_can_sustain_damage(player, 30, 'RuinsWater') or logic.has('Flaahgra', player) ) ) or ( not logic.metroid_prime_has_misc(player, 'dock_rando') and logic.multiworld.scan_dash[player].value >= 2 ) or ( logic.multiworld.knowledge[player].value >= 3 and logic.multiworld.movement[player].value >= 3 ) )),
                ("Event - Hive Mecha (Hive Totem, Chozo Ruins)", templates['Shoot Power Beam']),
                ("Door to Hive Totem (Totem Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Access North (Hive Totem, Chozo Ruins)", (
                ("Door to Totem Access (Hive Totem, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 1 ) or logic.has('Chozo - Fallen Rubble', player) )),
                ("Event - Hive Mecha (Hive Totem, Chozo Ruins)", None),
                ("Event - Fallen Rubble (Hive Totem, Chozo Ruins)", None),
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Hive Mecha (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Fallen Rubble (Hive Totem, Chozo Ruins)", (
                ("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Sun Tower Access (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", None),
                ("Before Fight (Back) (Sunchamber, Chozo Ruins)", None),
                ("Door to Sunchamber (Sun Tower Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Access (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", None),
                ("Door to Sunchamber (Sunchamber Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Varia Suit) (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Flaahgra (Sunchamber, Chozo Ruins)", (
                ("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", (
                ("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)", None),
            )
            ),
            (
            "Before Fight (Front) (Sunchamber, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)", lambda logic: ( logic.has('Flaahgra', player) or logic.has('Chozo Ghosts (Sunchamber)', player) )),
                ("Door to Sunchamber Access (Sunchamber, Chozo Ruins)", lambda logic: logic.has('Chozo Ghosts (Sunchamber)', player)),
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.multiworld.combat[player].value >= 1 and logic.count('Power Bomb', player) >= 4 ) ) and ( ( logic.metroid_prime_has_missiles(player, 10) and templates['Shoot Any Beam'](logic) ) or templates['Shoot Power Beam'](logic) or ( logic.multiworld.l_jump[player].value >= 1 and logic.has('Space Jump Boots', player) and logic.multiworld.combat[player].value >= 1 ) or ( logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.combat[player].value >= 2 ) ) and ( templates['Shoot Power Beam'](logic) or ( templates['Shoot Any Beam'](logic) and logic.metroid_prime_has_missiles(player, 1) ) ) ) or ( templates['Shoot Wave Beam'](logic) and logic.has('Wavebuster', player) and logic.metroid_prime_has_missiles(player, 230) and logic.multiworld.combat[player].value >= 3 and logic.has('Charge Beam', player) ) )),
                ("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", lambda logic: ( ( logic.has('Sunchamber Chozo Ghosts Layer Activated', player) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 2 ) ) and ( templates['Shoot Power Beam'](logic) and ( logic.has('Space Jump Boots', player) or logic.multiworld.l_jump[player].value >= 1 ) ) )),
            )
            ),
            (
            "Before Fight (Back) (Sunchamber, Chozo Ruins)", (
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", lambda logic: ( logic.multiworld.knowledge[player].value >= 1 and logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.count('Power Bomb', player) >= 4 ) and ( ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 ) or logic.multiworld.scan_dash[player].value >= 3 ) )),
            )
            ),
            (
            "Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", (
                ("Door to Watery Hall (Watery Hall Access, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)", lambda logic: ( ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) ) or ( templates['Shoot Power Beam'](logic) and logic.has('Charge Beam', player) and logic.multiworld.knowledge[player].value >= 1 ) )),
                ("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall (Watery Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", None),
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Gathering Hall (Save Station 2, Chozo Ruins)", (
                ("Save Station (Save Station 2, Chozo Ruins)", None),
                ("Door to Save Station 2 (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 2, Chozo Ruins)", (
                ("Door to Gathering Hall (Save Station 2, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Gathering Hall (East Atrium, Chozo Ruins)", (
                ("Door to Energy Core Access (East Atrium, Chozo Ruins)", None),
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Energy Core Access (East Atrium, Chozo Ruins)", (
                ("Door to Gathering Hall (East Atrium, Chozo Ruins)", None),
                ("Door to East Atrium (Energy Core Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Dynamo Access (Watery Hall, Chozo Ruins)", (
                ("Behind Gate (Watery Hall, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
                ("Door to Watery Hall (Dynamo Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Watery Hall Access (Watery Hall, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)", lambda logic: ( ( logic.metroid_prime_can_sustain_damage(player, 57, 'RuinsWater') or logic.has('Flaahgra', player) or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 25, 'RuinsWater') ) ) and ( ( logic.has('Gravity Suit', player) and logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 and logic.metroid_prime_can_sustain_damage(player, 15, 'RuinsWater') ) or ( not logic.has('Gravity Suit', player) and logic.multiworld.slope_jump[player].value >= 3 and logic.metroid_prime_has_misc(player, 'NoGravity') and logic.multiworld.gravityless_underwater_movement[player].value >= 3 ) or ( logic.has('Space Jump Boots', player) and ( logic.has('Gravity Suit', player) or ( logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.gravityless_underwater_movement[player].value >= 1 ) ) ) or ( logic.has('Gravity Suit', player) and logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 and ( ( logic.multiworld.movement[player].value >= 2 and logic.metroid_prime_can_sustain_damage(player, 65, 'RuinsWater') ) or ( logic.multiworld.movement[player].value >= 4 and logic.metroid_prime_can_sustain_damage(player, 20, 'RuinsWater') ) ) ) ) )),
                ("Event - Open gate (Watery Hall, Chozo Ruins)", lambda logic: logic.has('Scan Visor', player)),
                ("Behind Gate (Watery Hall, Chozo Ruins)", lambda logic: logic.has('Watery Hall Gate', player)),
                ("Door to Watery Hall (Watery Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Charge Beam) (Watery Hall, Chozo Ruins)", (
                ("Behind Gate (Watery Hall, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", lambda logic: ( logic.has('Flaahgra', player) or logic.metroid_prime_can_sustain_damage(player, 42, 'RuinsWater') or ( logic.has('Gravity Suit', player) and logic.metroid_prime_can_sustain_damage(player, 25, 'RuinsWater') ) )),
            )
            ),
            (
            "Event - Open gate (Watery Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", None),
            )
            ),
            (
            "Behind Gate (Watery Hall, Chozo Ruins)", (
                ("Door to Dynamo Access (Watery Hall, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) or ( logic.has('Boost Ball', player) and logic.multiworld.single_room_oob[player].value >= 3 and logic.multiworld.clip_through_objects[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 3 and ( logic.has('Space Jump Boots', player) or ( logic.multiworld.movement[player].value >= 4 ) ) ) ) )),
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", lambda logic: ( logic.has('Watery Hall Gate', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 1 ) )),
                ("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Energy Core (Energy Core Access, Chozo Ruins)", (
                ("Door to East Atrium (Energy Core Access, Chozo Ruins)", None),
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to East Atrium (Energy Core Access, Chozo Ruins)", (
                ("Door to Energy Core (Energy Core Access, Chozo Ruins)", None),
                ("Door to Energy Core Access (East Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall (Dynamo Access, Chozo Ruins)", (
                ("Door to Dynamo (Dynamo Access, Chozo Ruins)", None),
                ("Door to Dynamo Access (Watery Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Dynamo (Dynamo Access, Chozo Ruins)", (
                ("Door to Watery Hall (Dynamo Access, Chozo Ruins)", None),
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to West Furnace Access (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", None),
                ("Door to Energy Core (West Furnace Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Energy Core Access (Energy Core, Chozo Ruins)", (
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Door to West Furnace Access (Energy Core, Chozo Ruins)", lambda logic: logic.has('West Furnace Access Door Unlocked', player)),
                ("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) )),
                ("Door to Energy Core (Energy Core Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Dynamo Access (Dynamo, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)", lambda logic: ( logic.metroid_prime_has_missiles(player, 1) and templates['Shoot Any Beam'](logic) )),
                ("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Spider Ball', player) and ( logic.has('Space Jump Boots', player) or logic.multiworld.standable_terrain[player].value >= 1 or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) ) )),
                ("Door to Dynamo (Dynamo Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Dynamo, Chozo Ruins)", (
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)", (
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Burn Dome (Burn Dome Access, Chozo Ruins)", (
                ("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) )),
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Spawn Point (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
            )
            ),
            (
            "Door to Energy Core (West Furnace Access, Chozo Ruins)", (
                ("Door to Furnace (West Furnace Access, Chozo Ruins)", None),
                ("Door to West Furnace Access (Energy Core, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Furnace (West Furnace Access, Chozo Ruins)", (
                ("Door to Energy Core (West Furnace Access, Chozo Ruins)", None),
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burn Dome Access (Burn Dome, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
                ("Before Fight (Burn Dome, Chozo Ruins)", None),
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)", (
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)", (
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", lambda logic: logic.has('Incinerator Drone', player)),
                ("Before Fight (Burn Dome, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Incinerator Drone (Burn Dome, Chozo Ruins)", (
                ("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)", None),
            )
            ),
            (
            "Before Fight (Burn Dome, Chozo Ruins)", (
                ("Event - Incinerator Drone (Burn Dome, Chozo Ruins)", lambda logic: ( templates['Shoot Power Beam'](logic) or templates['Shoot Wave Beam'](logic) or templates['Shoot Ice Beam'](logic) )),
            )
            ),
            (
            "Door to East Furnace Access (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", None),
                ("Door to Furnace (East Furnace Access, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to West Furnace Access (Furnace, Chozo Ruins)", (
                ("Pickup (Energy Tank) (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 2 ) ) )),
                ("Under Spider Track (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Spider Ball', player) or logic.multiworld.standable_terrain[player].value >= 1 ) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) )),
                ("Door to Furnace (West Furnace Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", None),
                ("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", None),
            )
            ),
            (
            "Pickup (Energy Tank) (Furnace, Chozo Ruins)", (
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( ( ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) ) ) )),
            )
            ),
            (
            "Under Spider Track (Furnace, Chozo Ruins)", (
                ("Door to East Furnace Access (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or logic.multiworld.l_jump[player].value >= 1 )),
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 3 ) ) )),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", lambda logic: logic.has('Morph Ball', player)),
                ("Pickup (Missile Expansion) (Furnace, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Spider Ball', player) and ( ( logic.has('Power Bomb', player) and logic.has('Boost Ball', player) and ( logic.has('Morph Ball Bomb', player) or logic.multiworld.wall_boost[player].value >= 2 ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 3 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 ) or ( logic.has('Spider Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.multiworld.movement[player].value >= 1 ) ) ) ) ) ) )),
            )
            ),
            (
            "Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", (
                ("Door to Furnace (East Furnace Access, Chozo Ruins)", None),
                ("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Furnace (East Furnace Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", None),
                ("Door to East Furnace Access (Furnace, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway (Crossway Access West, Chozo Ruins)", (
                ("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 ) )),
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 3 ) )),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", (
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", lambda logic: logic.has('Scan Visor', player)),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Statue', player) or ( logic.has('Morph Ball', player) and logic.has('Boost Ball', player) and logic.multiworld.clip_through_objects[player].value >= 3 ) )),
                ("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) and logic.has('Hall of the Elders Bomb Slots', player) )),
            )
            ),
            (
            "Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", (
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", None),
            )
            ),
            (
            "Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", (
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) )),
                ("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) and logic.has('Hall of the Elders Bomb Slots', player) and templates['Shoot Ice Beam'](logic) )),
                ("Event - Statue Moved (Hall of the Elders, Chozo Ruins)", lambda logic: ( templates['Shoot Plasma Beam'](logic) and logic.has('Hall of the Elders Bomb Slots', player) )),
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", lambda logic: ( ( templates['Shoot Wave Beam'](logic) and logic.has('Hall of the Elders Bomb Slots', player) and logic.has('Hall of the Elders Unlock Doors', player) ) )),
            )
            ),
            (
            "Event - Statue Moved (Hall of the Elders, Chozo Ruins)", (
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
            )
            ),
            (
            "Room Center (Hall of the Elders, Chozo Ruins)", (
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) ) )),
                ("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) )),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", lambda logic: logic.has('Hall of the Elders Unlock Doors', player)),
                ("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Statue', player) and ( logic.has('Hall of the Elders Unlock Doors', player) or logic.multiworld.knowledge[player].value >= 2 ) )),
                ("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and ( ( logic.has('Spider Ball', player) and logic.has('Hall of the Elders Unlock Doors', player) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 1 ) or ( logic.has('Scan Visor', player) and logic.multiworld.bomb_jump[player].value >= 5 and logic.multiworld.scan_dash[player].value >= 4 and logic.multiworld.standable_terrain[player].value >= 1 ) ) )),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) )),
                ("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", lambda logic: ( templates['Shoot Power Beam'](logic) and ( logic.has('Charge Beam', player) or logic.multiworld.combat[player].value >= 1 ) )),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Unlock Doors', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.has('Morph Ball', player) and logic.multiworld.bomb_jump[player].value >= 4 ) or ( logic.has('Hall of the Elders Barrier', player) and ( logic.has('Space Jump Boots', player) or ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 1 ) or ( logic.has('Boost Ball', player) and logic.has('Scan Visor', player) and logic.multiworld.scan_dash[player].value >= 3 and logic.multiworld.instant_unmorph_jump[player].value >= 4 and logic.multiworld.movement[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.wall_boost[player].value >= 3 ) ) ) ) ) ) )),
            )
            ),
            (
            "Behind Barrier (Hall of the Elders, Chozo Ruins)", (
                ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) or logic.multiworld.movement[player].value >= 1 ) and logic.has('Hall of the Elders Unlock Doors', player) )),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Space Jump Boots', player) and logic.multiworld.knowledge[player].value >= 3 and logic.multiworld.l_jump[player].value >= 2 and logic.multiworld.standable_terrain[player].value >= 2 and ( logic.has('Hall of the Elders Barrier', player) or ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) and ( logic.multiworld.movement[player].value >= 2 or ( logic.multiworld.movement[player].value >= 1 and logic.has('Boost Ball', player) ) ) ) ) )),
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Scan Visor', player) )),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Barrier', player) or ( logic.has('Morph Ball', player) and ( logic.multiworld.movement[player].value >= 3 or ( logic.has('Boost Ball', player) and logic.multiworld.movement[player].value >= 2 ) ) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) ) )),
                ("Room Center (Hall of the Elders, Chozo Ruins)", lambda logic: ( logic.has('Hall of the Elders Barrier', player) or ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 1 ) ) ) )),
            )
            ),
            (
            "Door to Crossway Access South (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", None),
                ("Door to Crossway (Crossway Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway Access West (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access South (Crossway, Chozo Ruins)", None),
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and ( logic.has('Boost Ball', player) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.complex_bomb_jump[player].value >= 4 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 ) )),
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Elder Hall Access (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Crossway, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( ( logic.has('Morph Ball Bomb', player) and logic.has('Boost Ball', player) and logic.has('Crossway Bomb Slots', player) and ( logic.has('Spider Ball', player) or logic.multiworld.movement[player].value >= 2 ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.l_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 2 ) or ( logic.has('Boost Ball', player) and ( ( logic.multiworld.movement[player].value >= 3 ) or ( logic.has('Scan Visor', player) and logic.multiworld.movement[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 3 and logic.multiworld.scan_dash[player].value >= 4 ) ) ) or ( logic.has('Morph Ball Bomb', player) and logic.multiworld.bomb_jump[player].value >= 3 and logic.multiworld.standable_terrain[player].value >= 4 and logic.multiworld.scan_dash[player].value >= 4 and logic.has('Scan Visor', player) and logic.multiworld.bomb_space_jump[player].value >= 4 ) ) )),
                ("Event - Activate Bomb Slots (Crossway, Chozo Ruins)", lambda logic: ( templates['Shoot Super Missile'](logic) and logic.has('Scan Visor', player) )),
                ("Door to Crossway (Elder Hall Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Activate Bomb Slots (Crossway, Chozo Ruins)", (
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", None),
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", (
                ("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", None),
                ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", (
                ("Door to Crossway (Elder Hall Access, Chozo Ruins)", None),
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Crossway (Elder Hall Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", None),
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Crossway (Crossway Access South, Chozo Ruins)", (
                ("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Crossway Access South (Crossway, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access South, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) )),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", (
                ("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)", None),
                ("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)", (
                ("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", (
                ("Door to Transport Access South (Reflecting Pool, Chozo Ruins)", None),
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", None),
                ("Door to Reflecting Pool (Save Station 3, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport Access South (Reflecting Pool, Chozo Ruins)", (
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", None),
                ("Door to Reflecting Pool (Transport Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", (
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", lambda logic: ( ( logic.has('Morph Ball', player) and ( ( logic.has('Reflecting Pool Water Drained', player) and ( logic.has('Boost Ball', player) or logic.multiworld.movement[player].value >= 3 ) ) or ( logic.has('Morph Ball Bomb', player) and ( logic.multiworld.complex_bomb_jump[player].value >= 4 or logic.multiworld.bomb_space_jump[player].value >= 4 ) and logic.multiworld.standable_terrain[player].value >= 3 ) ) ) or ( logic.has('Space Jump Boots', player) and logic.multiworld.slope_jump[player].value >= 1 and logic.multiworld.standable_terrain[player].value >= 1 ) )),
                ("Event - Drain water (Reflecting Pool, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Power Bomb', player) and logic.multiworld.knowledge[player].value >= 1 ) ) )),
                ("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Antechamber (Reflecting Pool, Chozo Ruins)", (
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", None),
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", None),
                ("Door to Reflecting Pool (Antechamber, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Event - Drain water (Reflecting Pool, Chozo Ruins)", (
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Reflecting Pool (Save Station 3, Chozo Ruins)", (
                ("Save Station (Save Station 3, Chozo Ruins)", None),
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", (
                ("Save Station (Save Station 3, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 4 ) ) )),
                ("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 3, Chozo Ruins)", (
                ("Door to Reflecting Pool (Save Station 3, Chozo Ruins)", None),
                ("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", lambda logic: ( logic.has('Morph Ball', player) and ( logic.has('Morph Ball Bomb', player) or ( logic.has('Space Jump Boots', player) and logic.multiworld.standable_terrain[player].value >= 2 and logic.multiworld.movement[player].value >= 3 ) or ( logic.has('Boost Ball', player) and logic.multiworld.wall_boost[player].value >= 5 ) ) )),
            )
            ),
            (
            "Door to Reflecting Pool (Transport Access South, Chozo Ruins)", (
                ("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", None),
                ("Door to Transport Access South (Reflecting Pool, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", (
                ("Door to Reflecting Pool (Transport Access South, Chozo Ruins)", None),
                ("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Reflecting Pool (Antechamber, Chozo Ruins)", (
                ("Pickup (Ice Beam) (Antechamber, Chozo Ruins)", None),
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Ice Beam) (Antechamber, Chozo Ruins)", (
                ("Door to Reflecting Pool (Antechamber, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", None),
                ("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", (
                ("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", None),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", None),
                ("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", (
                ("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", None),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Event - Credits (Credits, End of Game)", (
            )
            ),
    ))