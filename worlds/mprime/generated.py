# pyright: reportGeneralTypeIssues=false
damage_resistances={'Damage': {'GravitySuit': 0.800000011920929, 'VariaSuit': 0.8999999761581421, 'PhazonSuit': 0.5}, 'HeatDamage1': {'GravitySuit': 0.0, 'VariaSuit': 0.0, 'PhazonSuit': 0.0}, 'Phazon': {'PhazonSuit': 0.0}}
items=['Power Beam', 'Ice Beam', 'Wave Beam', 'Plasma Beam', 'Missile', 'Scan Visor', 'Morph Ball Bomb', 'Power Bomb', 'Flamethrower', 'Thermal Visor', 'Charge Beam', 'Super Missile', 'Grapple Beam', 'X-Ray Visor', 'Ice Spreader', 'Space Jump Boots', 'Morph Ball', 'Combat Visor', 'Boost Ball', 'Spider Ball', 'Power Suit', 'Gravity Suit', 'Varia Suit', 'Phazon Suit', 'Energy Tank', 'Wavebuster', 'Artifact of Truth', 'Artifact of Strength', 'Artifact of Elder', 'Artifact of Wild', 'Artifact of Lifegiver', 'Artifact of Warrior', 'Artifact of Chozo', 'Artifact of Nature', 'Artifact of Sun', 'Artifact of World', 'Artifact of Spirit', 'Artifact of Newborn', 'Nothing', 'Main Power Bomb', 'Missile Launcher']
from dataclasses import dataclass
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

@dataclass
class GeneratedOptions:

    scan_dash: Dash
    knowledge: Knowledge
    combat: Combat
    l_jump: LJump
    invisible_objects: InvisibleObjects
    damage_boosting: DBoosting
    movement: Movement
    slope_jump: SJump
    standable_terrain: Standable
    bomb_jump: BJ
    jump_off_enemies: StandEnemies
    clip_through_objects: ClipThruObjects
    r_jump: RJump
    bomb_space_jump: BSJ
    wall_boost: WallBoost
    spinners_without_boost: BoostlessSpiner
    single_room_oob: OoB
    heat_runs: HeatRun
    complex_bomb_jump: CBJ
    infinite_speed: IS
    gravityless_underwater_movement: UnderwaterMovement
    instant_unmorph_jump: IUJ
from BaseClasses import MultiWorld, Region
from worlds.AutoWorld import World
from .locations import MetroidPrimeLocation
from .utils import region_format
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

def create_regions_and_events(self: World):
    multiworld = self.multiworld
    player = self.player
    def cr(region_name: str):
        return Region(region_name, player, multiworld)
    def cre(region_name: str, event_name: str, skippable: bool = False):
        this_region = cr(region_name)
        this_location = MetroidPrimeLocation(player, region_name, None, this_region)
        this_region.locations.append(this_location)
        event = self.create_event(event_name, skippable)
        this_location.place_locked_item(event)
        return this_region
    def crl(region_name: str):
        this_region = cr(region_name)
        this_location = MetroidPrimeLocation(player, region_name, self.location_name_to_id[region_name], this_region)
        this_region.locations.append(this_location)
        return this_region

    # will be implemented once Randovania does
    # create_items_every_room_region: Callable[[str], Region]
    # if world.items_every_room:
    #     create_items_every_room_region = create_region_with_location
    # else:
    #     create_items_every_room_region = create_region

    menu_region = Region("Menu", player, multiworld)
    multiworld.regions.extend((menu_region,cr("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)"),cr("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)"),cr("Save Station (Crater Entry Point, Impact Crater)"),cr("Door to Phazon Core (Crater Tunnel A, Impact Crater)"),cr("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)"),cr("Door to Crater Missile Station (Phazon Core, Impact Crater)"),cr("Door to Crater Tunnel A (Phazon Core, Impact Crater)"),cr("Door to Crater Tunnel B (Phazon Core, Impact Crater)"),cr("Door to Phazon Core (Crater Missile Station, Impact Crater)"),cr("Missile Station (Crater Missile Station, Impact Crater)"),cr("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)"),cr("Door to Phazon Core (Crater Tunnel B, Impact Crater)"),cr("Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)"),cr("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)"),cr("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)"),cr("Dock to Subchamber Two (Subchamber One, Impact Crater)"),cr("Dock to Subchamber One (Subchamber Two, Impact Crater)"),cr("Dock to Subchamber Three (Subchamber Two, Impact Crater)"),cr("Dock to Subchamber Four (Subchamber Three, Impact Crater)"),cr("Dock to Subchamber Two (Subchamber Three, Impact Crater)"),cr("Dock to Subchamber Five (Subchamber Four, Impact Crater)"),cr("Dock to Subchamber Three (Subchamber Four, Impact Crater)"),cr("Dock to Subchamber Four (Subchamber Five, Impact Crater)"),cr("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)"),cr("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)"),cr("Teleporter to Credits (Metroid Prime Lair, Impact Crater)"),cr("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)"),cr("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)"),cr("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)"),cr("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)"),crl("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)"),crl("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)"),cr("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)"),cr("Save Station (Save Station B, Phendrana Drifts)"),cr("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)"),cr("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)"),cr("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)"),cr("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)"),cr("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)"),cr("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)"),crl("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)"),cre("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", "Chozo Ice Temple Bomb Slot", False),cr("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)"),cr("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)"),cr("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)"),cr("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)"),crl("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)"),cr("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)"),cr("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)"),cr("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)"),crl("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)"),crl("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)"),cr("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)"),cr("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)"),cr("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)"),cr("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)"),cr("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)"),cr("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)"),cr("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)"),crl("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)"),cr("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)"),cr("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)"),cr("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)"),cr("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)"),crl("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)"),cr("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)"),cr("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)"),cr("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)"),crl("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)"),cr("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)"),cr("Save Station (Save Station A, Phendrana Drifts)"),cr("Door to Research Entrance (Specimen Storage, Phendrana Drifts)"),cr("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)"),cr("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)"),cr("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)"),cr("Door to Specimen Storage (Research Entrance, Phendrana Drifts)"),cr("Door to Map Station (Research Entrance, Phendrana Drifts)"),cr("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)"),cr("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)"),cr("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)"),cr("Door to Research Entrance (Map Station, Phendrana Drifts)"),cr("Map Station (Map Station, Phendrana Drifts)"),cr("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)"),cr("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)"),cr("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)"),cr("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)"),cr("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)"),cre("Event - Thardus (Quarantine Cave, Phendrana Drifts)", "Thardus", False),crl("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)"),cr("Room Center (Quarantine Cave, Phendrana Drifts)"),cr("Fight Trigger (Quarantine Cave, Phendrana Drifts)"),cr("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)"),cr("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)"),cre("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", "Research Lab Hydra Barrier", False),crl("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)"),cr("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)"),cr("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)"),cr("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)"),crl("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)"),cr("Door to Observatory (Observatory Access, Phendrana Drifts)"),cr("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)"),cr("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)"),cr("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)"),cr("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)"),cr("Door to Observatory Access (Observatory, Phendrana Drifts)"),cr("Door to West Tower Entrance (Observatory, Phendrana Drifts)"),cr("Door to Save Station D (Observatory, Phendrana Drifts)"),cre("Event - Observatory Activated (Observatory, Phendrana Drifts)", "Observatory Activated", True),crl("Pickup (Super Missile) (Observatory, Phendrana Drifts)"),cr("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)"),cr("Door to Frozen Pike (Transport Access, Phendrana Drifts)"),crl("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)"),cr("Door to West Tower (West Tower Entrance, Phendrana Drifts)"),cr("Door to Observatory (West Tower Entrance, Phendrana Drifts)"),cr("Door to Observatory (Save Station D, Phendrana Drifts)"),cr("Save Station (Save Station D, Phendrana Drifts)"),cr("Door to Pike Access (Frozen Pike, Phendrana Drifts)"),cr("Door to Transport Access (Frozen Pike, Phendrana Drifts)"),cr("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)"),cr("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)"),cr("Door to West Tower Entrance (West Tower, Phendrana Drifts)"),cr("Door to Control Tower (West Tower, Phendrana Drifts)"),cr("Door to Frozen Pike (Pike Access, Phendrana Drifts)"),cr("Door to Research Core (Pike Access, Phendrana Drifts)"),cr("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)"),cr("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)"),cr("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)"),cr("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)"),cr("Door to East Tower (Control Tower, Phendrana Drifts)"),cr("Door to West Tower (Control Tower, Phendrana Drifts)"),crl("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)"),cre("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", "Control Tower Tower", False),cr("Room Center (Control Tower, Phendrana Drifts)"),cre("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", "Control Tower Tower", False),cr("Fight Trigger (Control Tower, Phendrana Drifts)"),cre("Event - Control Tower Fight (Control Tower, Phendrana Drifts)", "Control Tower Fight", True),cr("Door to Pike Access (Research Core, Phendrana Drifts)"),cr("Door to Research Core Access (Research Core, Phendrana Drifts)"),crl("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)"),cre("Event - Research Core Power Outage (Research Core, Phendrana Drifts)", "Research Core Power Outage", False),cr("Door to Save Station C (Frost Cave, Phendrana Drifts)"),cr("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)"),cr("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)"),crl("Pickup (Missile) (Frost Cave, Phendrana Drifts)"),cr("Frost Cave Floor (Frost Cave, Phendrana Drifts)"),cre("Event - Ice Broken (Frost Cave, Phendrana Drifts)", "Frost Cave Ice Floor", False),cr("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)"),cr("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)"),cr("Door to Chamber Access (Hunter Cave, Phendrana Drifts)"),cr("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)"),cr("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)"),cr("Door to Control Tower (East Tower, Phendrana Drifts)"),cr("Door to Research Core (Research Core Access, Phendrana Drifts)"),cr("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)"),cr("Door to Frost Cave (Save Station C, Phendrana Drifts)"),cr("Save Station (Save Station C, Phendrana Drifts)"),cr("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)"),cr("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)"),cr("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)"),cr("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)"),cr("Door to Hunter Cave (Chamber Access, Phendrana Drifts)"),cr("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)"),cr("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)"),cr("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)"),cr("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)"),cr("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)"),cr("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)"),cr("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)"),crl("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)"),crl("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)"),cr("Lab Catwalk (Research Lab Aether, Phendrana Drifts)"),cr("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)"),cr("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)"),cr("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)"),cr("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)"),cr("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)"),cr("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)"),cr("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)"),crl("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)"),crl("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)"),cre("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", "Gravity Chamber Item (Lower)", False),cr("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)"),crl("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)"),cr("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)"),crl("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)"),cr("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)"),cr("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)"),cr("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)"),cr("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)"),cr("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)"),cr("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)"),cr("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)"),cr("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)"),cr("Save Station (Save Station Magmoor A, Magmoor Caverns)"),cr("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)"),cr("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)"),crl("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)"),cr("Next to Crates (Lava Lake, Magmoor Caverns)"),cr("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)"),cr("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)"),cr("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)"),cr("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)"),cr("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)"),crl("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)"),cr("Tunnel Entrance (Triclops Pit, Magmoor Caverns)"),cr("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)"),cr("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)"),cr("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)"),crl("Pickup (Missile) (Storage Cavern, Magmoor Caverns)"),cr("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)"),cr("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)"),cr("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)"),cr("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)"),cr("Middle Level (Monitor Station, Magmoor Caverns)"),cr("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)"),cr("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)"),crl("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)"),cr("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)"),cr("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)"),crl("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)"),cr("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)"),cr("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)"),cr("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)"),crl("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)"),cr("Room Center (Shore Tunnel, Magmoor Caverns)"),cr("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)"),cr("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)"),cr("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)"),cr("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)"),cr("Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)"),crl("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)"),crl("Pickup (Missile) (Fiery Shores, Magmoor Caverns)"),cr("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)"),cr("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)"),cr("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)"),cr("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)"),cr("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)"),cr("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)"),cr("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)"),cr("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)"),cr("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)"),cr("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)"),cr("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)"),cr("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)"),cr("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)"),cr("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)"),cr("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)"),cre("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", "Geothermal Core Puzzle", False),cr("First Spinner (Geothermal Core, Magmoor Caverns)"),cr("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)"),crl("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)"),cre("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", "Plasma Processing Item", False),cr("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)"),cr("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)"),cr("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)"),cr("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)"),cr("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)"),crl("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)"),cr("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)"),cr("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)"),cr("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)"),cr("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)"),cr("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)"),cr("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)"),cr("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)"),cr("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)"),cr("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)"),cr("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)"),cr("Save Station (Save Station Magmoor B, Magmoor Caverns)"),cr("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)"),cr("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)"),cr("Door to Main Quarry (Quarry Access, Phazon Mines)"),cr("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)"),cr("Door to Waste Disposal (Main Quarry, Phazon Mines)"),cr("Door to Quarry Access (Main Quarry, Phazon Mines)"),cr("Door to Save Station Mines A (Main Quarry, Phazon Mines)"),cr("Door to Security Access A (Main Quarry, Phazon Mines)"),crl("Pickup (Missile) (Main Quarry, Phazon Mines)"),cre("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", "Main Quarry Barrier", False),cr("Crane Platform (Main Quarry, Phazon Mines)"),cr("Door to Main Quarry (Waste Disposal, Phazon Mines)"),cr("Door to Ore Processing (Waste Disposal, Phazon Mines)"),cr("Door to Main Quarry (Save Station Mines A, Phazon Mines)"),cr("Save Station (Save Station Mines A, Phazon Mines)"),cre("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", "Phazon Mines Save Station A Barrier", False),cr("Door to Main Quarry (Security Access A, Phazon Mines)"),cr("Door to Mine Security Station (Security Access A, Phazon Mines)"),crl("Pickup (Missile) (Security Access A, Phazon Mines)"),cr("Door to Research Access (Ore Processing, Phazon Mines)"),cr("Door to Storage Depot B (Ore Processing, Phazon Mines)"),cr("Door to Waste Disposal (Ore Processing, Phazon Mines)"),cr("Door to Elevator Access A (Ore Processing, Phazon Mines)"),cr("Door to Security Access A (Mine Security Station, Phazon Mines)"),cr("Door to Security Access B (Mine Security Station, Phazon Mines)"),cr("Door to Storage Depot A (Mine Security Station, Phazon Mines)"),cre("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", "Mine Security Station Barrier", False),cre("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", "Mine Security Station Unlock Doors", False),cr("Room Center (Mine Security Station, Phazon Mines)"),cr("Door to Ore Processing (Research Access, Phazon Mines)"),cr("Door to Elite Research (Research Access, Phazon Mines)"),cr("Door to Ore Processing (Storage Depot B, Phazon Mines)"),crl("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)"),cre("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", "Storage Depot B Item", False),cr("Door to Ore Processing (Elevator Access A, Phazon Mines)"),cr("Door to Elevator A (Elevator Access A, Phazon Mines)"),cr("Door to Elite Research (Security Access B, Phazon Mines)"),cr("Door to Mine Security Station (Security Access B, Phazon Mines)"),cr("Door to Mine Security Station (Storage Depot A, Phazon Mines)"),crl("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)"),cr("Door to Research Access (Elite Research, Phazon Mines)"),cr("Door to Security Access B (Elite Research, Phazon Mines)"),cre("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", "Elite Research Rock Wall", False),crl("Pickup (Missile) (Elite Research, Phazon Mines)"),crl("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)"),cr("Top Floor (Elite Research, Phazon Mines)"),cr("Door to Elevator Access A (Elevator A, Phazon Mines)"),cr("Door to Elite Control Access (Elevator A, Phazon Mines)"),cr("Door to Elevator A (Elite Control Access, Phazon Mines)"),cr("Door to Elite Control (Elite Control Access, Phazon Mines)"),crl("Pickup (Missile) (Elite Control Access, Phazon Mines)"),cr("Door to Maintenance Tunnel (Elite Control, Phazon Mines)"),cr("Door to Elite Control Access (Elite Control, Phazon Mines)"),cr("Door to Ventilation Shaft (Elite Control, Phazon Mines)"),cre("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", "Elite Control Barriers", False),cre("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", "Elite Pirate Fight (Elite Control)", False),cr("Bottom Floor Center (Elite Control, Phazon Mines)"),cr("Door to Elite Control (Maintenance Tunnel, Phazon Mines)"),cr("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)"),cr("Door to Omega Research (Ventilation Shaft, Phazon Mines)"),cr("Door to Elite Control (Ventilation Shaft, Phazon Mines)"),crl("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)"),cr("Door to Transport Access (Phazon Processing Center, Phazon Mines)"),cr("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)"),cr("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)"),crl("Pickup (Missile) (Phazon Processing Center, Phazon Mines)"),cr("Door to Map Station Mines (Omega Research, Phazon Mines)"),cr("Door to Ventilation Shaft (Omega Research, Phazon Mines)"),cr("Door to Dynamo Access (Omega Research, Phazon Mines)"),cr("Door to Phazon Processing Center (Transport Access, Phazon Mines)"),cr("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)"),cr("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)"),cr("Door to Elite Quarters (Processing Center Access, Phazon Mines)"),cre("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", "Processing Center Access Barrier", False),crl("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)"),cr("Door to Omega Research (Map Station Mines, Phazon Mines)"),cr("Map Station (Map Station Mines, Phazon Mines)"),cr("Door to Central Dynamo (Dynamo Access, Phazon Mines)"),cr("Door to Omega Research (Dynamo Access, Phazon Mines)"),cre("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", "Elite Pirate Fight (Dynamo Access)", False),cr("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)"),cr("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)"),cr("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)"),cr("Door to Processing Center Access (Elite Quarters, Phazon Mines)"),cre("Event - Omega Pirate (Elite Quarters, Phazon Mines)", "Omega Pirate", False),crl("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)"),cr("Fight Trigger (Elite Quarters, Phazon Mines)"),cr("Door to Dynamo Access (Central Dynamo, Phazon Mines)"),cr("Door to Quarantine Access A (Central Dynamo, Phazon Mines)"),cr("Door to Save Station Mines B (Central Dynamo, Phazon Mines)"),cre("Event - Security Drone (Central Dynamo, Phazon Mines)", "Invisible Drone", False),crl("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)"),cr("Fight Trigger (Central Dynamo, Phazon Mines)"),cr("Room Bottom (Central Dynamo, Phazon Mines)"),cr("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)"),cr("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)"),cre("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", "Elite Quarters Access Barrier", False),cr("Door to Central Dynamo (Quarantine Access A, Phazon Mines)"),cr("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)"),cr("Door to Central Dynamo (Save Station Mines B, Phazon Mines)"),cr("Save Station (Save Station Mines B, Phazon Mines)"),cr("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)"),cr("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)"),cr("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)"),crl("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)"),cre("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", "Metroid Quarantine B Barrier", False),cr("Front of Barrier (Metroid Quarantine B, Phazon Mines)"),cr("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)"),cr("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)"),crl("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)"),cre("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", "Metroid Quarantine A Barrier", False),cr("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)"),cr("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)"),cr("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)"),cr("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)"),cr("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)"),cr("Save Station (Save Station Mines C, Phazon Mines)"),cr("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)"),cr("Door to Elevator B (Elevator Access B, Phazon Mines)"),cr("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)"),cr("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)"),cr("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)"),crl("Pickup (Missile) (Fungal Hall B, Phazon Mines)"),cr("Door to Elevator Access B (Elevator B, Phazon Mines)"),cr("Door to Fungal Hall Access (Elevator B, Phazon Mines)"),cr("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)"),cr("Missile Station (Missile Station Mines, Phazon Mines)"),cr("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)"),cr("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)"),crl("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)"),cr("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)"),cr("Door to Elevator B (Fungal Hall Access, Phazon Mines)"),crl("Pickup (Missile) (Fungal Hall Access, Phazon Mines)"),cr("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)"),cr("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)"),cr("Door to Gully (Landing Site, Tallon Overworld)"),cr("Door to Canyon Cavern (Landing Site, Tallon Overworld)"),cr("Door to Temple Hall (Landing Site, Tallon Overworld)"),cr("Door to Alcove (Landing Site, Tallon Overworld)"),cr("Door to Waterfall Cavern (Landing Site, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)"),cr("Ship (Landing Site, Tallon Overworld)"),cr("Door to Tallon Canyon (Gully, Tallon Overworld)"),cr("Door to Landing Site (Gully, Tallon Overworld)"),cr("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)"),cr("Door to Landing Site (Canyon Cavern, Tallon Overworld)"),cr("Door to Temple Security Station (Temple Hall, Tallon Overworld)"),cr("Door to Landing Site (Temple Hall, Tallon Overworld)"),cr("Door to Landing Site (Alcove, Tallon Overworld)"),crl("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)"),cr("Door to Landing Site (Waterfall Cavern, Tallon Overworld)"),cr("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)"),cr("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)"),cr("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)"),cr("Door to Gully (Tallon Canyon, Tallon Overworld)"),cr("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)"),cr("Half Pipe (Tallon Canyon, Tallon Overworld)"),cr("Door to Temple Hall (Temple Security Station, Tallon Overworld)"),cr("Door to Temple Lobby (Temple Security Station, Tallon Overworld)"),cr("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)"),cr("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)"),cr("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)"),cr("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)"),cr("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)"),cr("Door to Root Cave (Root Tunnel, Tallon Overworld)"),cr("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)"),cr("Door to Artifact Temple (Temple Lobby, Tallon Overworld)"),cr("Door to Temple Security Station (Temple Lobby, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)"),cr("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)"),cr("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)"),cr("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)"),cr("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)"),cr("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)"),cr("Door to Transport Tunnel B (Root Cave, Tallon Overworld)"),cr("Door to Root Tunnel (Root Cave, Tallon Overworld)"),cr("Door to Arbor Chamber (Root Cave, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)"),cr("Door to Temple Lobby (Artifact Temple, Tallon Overworld)"),crl("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)"),cre("Event - Meta Ridley (Artifact Temple, Tallon Overworld)", "Meta Ridley", False),cr("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)"),cr("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)"),cr("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)"),cr("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)"),cr("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)"),cr("Door to Root Cave (Transport Tunnel B, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)"),cr("Door to Root Cave (Arbor Chamber, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)"),cre("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", "Main Ventilation Shaft Section B Conduit", False),cr("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)"),cr("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)"),cr("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)"),cr("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)"),cr("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)"),cr("Door to Reactor Access (Reactor Core, Tallon Overworld)"),cr("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)"),cr("Room Bottom (Reactor Core, Tallon Overworld)"),cre("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", "Reactor Core Conduits", False),cr("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)"),cr("Door to Reactor Core (Reactor Access, Tallon Overworld)"),cr("Door to Savestation (Reactor Access, Tallon Overworld)"),cre("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", "Reactor Access Conduits", False),cr("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),cr("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),crl("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)"),cre("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", "Cargo Freight Lift to Deck Gamma Conduits", False),cr("Door to Reactor Access (Savestation, Tallon Overworld)"),cr("Save Station (Savestation, Tallon Overworld)"),cr("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)"),cr("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)"),cr("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)"),cr("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)"),cre("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", "Biohazard Containment Conduits", False),cr("Room Bottom (Biohazard Containment, Tallon Overworld)"),cr("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)"),cr("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)"),cr("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)"),cr("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)"),cr("Room Center (Biotech Research Area 1, Tallon Overworld)"),cre("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", "Biotech Research Area 1 Conduits", False),cr("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)"),cr("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)"),cr("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)"),cr("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)"),cr("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)"),cr("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)"),crl("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)"),cr("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)"),cr("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)"),cr("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)"),cr("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)"),cr("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)"),cre("Event - Open gate (Great Tree Hall, Tallon Overworld)", "Great Tree Hall Bars Unlocked", False),cr("Next to Spinner (Great Tree Hall, Tallon Overworld)"),cr("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)"),cr("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)"),cr("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)"),cr("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)"),cr("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)"),crl("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)"),cr("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)"),cr("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)"),cr("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)"),cr("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)"),cr("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)"),cr("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)"),crl("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)"),crl("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)"),cr("Behind PB Wall (Life Grove, Tallon Overworld)"),cr("Front of PB Wall (Life Grove, Tallon Overworld)"),cr("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)"),cr("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)"),cr("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)"),cr("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)"),cr("Door to Main Plaza (Ruins Entrance, Chozo Ruins)"),cr("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)"),cr("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)"),cr("Door to Ruins Entrance (Main Plaza, Chozo Ruins)"),cr("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)"),cr("Door to Nursery Access (Main Plaza, Chozo Ruins)"),cr("Door from Plaza Access (Main Plaza, Chozo Ruins)"),cr("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)"),crl("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)"),crl("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)"),crl("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)"),crl("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)"),cr("Locked Door Ledge (Main Plaza, Chozo Ruins)"),cr("Grapple Ledge (Main Plaza, Chozo Ruins)"),cr("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)"),cr("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)"),cr("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)"),cr("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)"),cr("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)"),cr("Door to Main Plaza (Nursery Access, Chozo Ruins)"),cr("Door to Main Plaza (Plaza Access, Chozo Ruins)"),cr("Door to Vault (Plaza Access, Chozo Ruins)"),cr("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)"),cr("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)"),cr("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)"),cr("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)"),cr("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)"),cr("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)"),cr("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)"),crl("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)"),crl("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)"),crl("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)"),cr("Pit (Ruined Shrine, Chozo Ruins)"),cre("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", "Beetle Battle", False),cre("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", "Ruined Shrine Item (Morph Ball)", False),cr("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)"),cr("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)"),cr("Door to Vault Access (Vault, Chozo Ruins)"),cr("Door to Plaza Access (Vault, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Vault, Chozo Ruins)"),cr("Door to Training Chamber Access (Training Chamber, Chozo Ruins)"),cr("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)"),crl("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)"),cre("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", "Chozo Ghosts (Training Chamber)", False),cre("Event - Unlock morph track (Training Chamber, Chozo Ruins)", "Training Chamber Exit Tunnel", False),cr("Door to Arboretum (Arboretum Access, Chozo Ruins)"),cr("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)"),cr("Door to Magma Pool (Meditation Fountain, Chozo Ruins)"),cr("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)"),cr("Door to Tower of Light (Tower of Light Access, Chozo Ruins)"),cr("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)"),cr("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)"),cr("Door to North Atrium (Ruined Nursery, Chozo Ruins)"),cr("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)"),cr("Door to Vault (Vault Access, Chozo Ruins)"),cr("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)"),cr("Door to Magma Pool (Training Chamber Access, Chozo Ruins)"),cr("Door to Training Chamber (Training Chamber Access, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)"),cr("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)"),cr("Door to Arboretum Access (Arboretum, Chozo Ruins)"),cr("Door to Gathering Hall Access (Arboretum, Chozo Ruins)"),cr("Front of Gate (Arboretum, Chozo Ruins)"),cre("Event - Open gate (Arboretum, Chozo Ruins)", "Arboretum Gate", False),cr("Door to Training Chamber Access (Magma Pool, Chozo Ruins)"),cr("Door to Meditation Fountain (Magma Pool, Chozo Ruins)"),crl("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)"),cr("Door to Tower of Light Access (Tower of Light, Chozo Ruins)"),cr("Door to Tower Chamber (Tower of Light, Chozo Ruins)"),crl("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)"),cr("Door to Ruined Nursery (Save Station 1, Chozo Ruins)"),cr("Save Station (Save Station 1, Chozo Ruins)"),cr("Door to Ruined Nursery (North Atrium, Chozo Ruins)"),cr("Door to Ruined Gallery (North Atrium, Chozo Ruins)"),cr("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)"),cr("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)"),cr("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)"),cr("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)"),cr("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)"),cr("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)"),cr("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)"),cr("Door to Arboretum (Gathering Hall Access, Chozo Ruins)"),cr("Door to Tower of Light (Tower Chamber, Chozo Ruins)"),crl("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)"),cr("Door to North Atrium (Ruined Gallery, Chozo Ruins)"),cr("Door to Totem Access (Ruined Gallery, Chozo Ruins)"),cr("Door to Map Station (Ruined Gallery, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)"),crl("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)"),cr("Door to Sun Tower Access (Sun Tower, Chozo Ruins)"),cr("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)"),cre("Event - Unlock spider track (Sun Tower, Chozo Ruins)", "Sun Tower Spider Track Unlocked", False),cre("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", "Sunchamber Chozo Ghosts Layer Activated", False),cre("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", "Sunchamber Chozo Ghosts Layer Activated", False),cr("Door to Hive Totem (Transport Access North, Chozo Ruins)"),cr("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)"),crl("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)"),cr("Door to Sunchamber (Sunchamber Access, Chozo Ruins)"),cr("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)"),cr("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)"),cr("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)"),cr("Door to Save Station 2 (Gathering Hall, Chozo Ruins)"),cr("Door to East Atrium (Gathering Hall, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)"),cr("Door to Ruined Gallery (Totem Access, Chozo Ruins)"),cr("Door to Hive Totem (Totem Access, Chozo Ruins)"),cr("Door to Ruined Gallery (Map Station, Chozo Ruins)"),cr("Map Station (Map Station, Chozo Ruins)"),cr("Door to Sunchamber (Sun Tower Access, Chozo Ruins)"),cr("Door to Sun Tower (Sun Tower Access, Chozo Ruins)"),cr("Door to Totem Access (Hive Totem, Chozo Ruins)"),cr("Door to Transport Access North (Hive Totem, Chozo Ruins)"),crl("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)"),cre("Event - Hive Mecha (Hive Totem, Chozo Ruins)", "Hive Mecha", False),cre("Event - Fallen Rubble (Hive Totem, Chozo Ruins)", "Chozo - Fallen Rubble", False),cr("Door to Sun Tower Access (Sunchamber, Chozo Ruins)"),cr("Door to Sunchamber Access (Sunchamber, Chozo Ruins)"),crl("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)"),crl("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)"),cre("Event - Flaahgra (Sunchamber, Chozo Ruins)", "Flaahgra", False),cre("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", "Chozo Ghosts (Sunchamber)", False),cr("Before Fight (Front) (Sunchamber, Chozo Ruins)"),cr("Before Fight (Back) (Sunchamber, Chozo Ruins)"),cr("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)"),cr("Door to Watery Hall (Watery Hall Access, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)"),cr("Door to Gathering Hall (Save Station 2, Chozo Ruins)"),cr("Save Station (Save Station 2, Chozo Ruins)"),cr("Door to Gathering Hall (East Atrium, Chozo Ruins)"),cr("Door to Energy Core Access (East Atrium, Chozo Ruins)"),cr("Door to Dynamo Access (Watery Hall, Chozo Ruins)"),cr("Door to Watery Hall Access (Watery Hall, Chozo Ruins)"),crl("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)"),cre("Event - Open gate (Watery Hall, Chozo Ruins)", "Watery Hall Gate", False),cr("Behind Gate (Watery Hall, Chozo Ruins)"),cr("Door to Energy Core (Energy Core Access, Chozo Ruins)"),cr("Door to East Atrium (Energy Core Access, Chozo Ruins)"),cr("Door to Watery Hall (Dynamo Access, Chozo Ruins)"),cr("Door to Dynamo (Dynamo Access, Chozo Ruins)"),cr("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)"),cr("Door to West Furnace Access (Energy Core, Chozo Ruins)"),cr("Door to Energy Core Access (Energy Core, Chozo Ruins)"),cre("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", "West Furnace Access Door Unlocked", False),cr("Door to Dynamo Access (Dynamo, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)"),crl("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)"),cr("Door to Burn Dome (Burn Dome Access, Chozo Ruins)"),cr("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)"),cr("Spawn Point (Burn Dome Access, Chozo Ruins)"),cr("Door to Energy Core (West Furnace Access, Chozo Ruins)"),cr("Door to Furnace (West Furnace Access, Chozo Ruins)"),cr("Door to Burn Dome Access (Burn Dome, Chozo Ruins)"),crl("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)"),cre("Event - Incinerator Drone (Burn Dome, Chozo Ruins)", "Incinerator Drone", False),cr("Before Fight (Burn Dome, Chozo Ruins)"),cr("Door to East Furnace Access (Furnace, Chozo Ruins)"),cr("Door to West Furnace Access (Furnace, Chozo Ruins)"),cr("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Furnace, Chozo Ruins)"),crl("Pickup (Energy Tank) (Furnace, Chozo Ruins)"),cr("Under Spider Track (Furnace, Chozo Ruins)"),cr("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)"),cr("Door to Furnace (East Furnace Access, Chozo Ruins)"),cr("Door to Crossway (Crossway Access West, Chozo Ruins)"),cr("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)"),cr("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)"),cr("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)"),cr("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)"),cr("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)"),cr("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)"),crl("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)"),cre("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Bomb Slots", False),cre("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Barrier", False),cr("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)"),cre("Event - Statue Moved (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Statue", False),cre("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", "Hall of the Elders Unlock Doors", False),cr("Room Center (Hall of the Elders, Chozo Ruins)"),cr("Behind Barrier (Hall of the Elders, Chozo Ruins)"),cr("Door to Crossway Access South (Crossway, Chozo Ruins)"),cr("Door to Crossway Access West (Crossway, Chozo Ruins)"),cr("Door to Elder Hall Access (Crossway, Chozo Ruins)"),crl("Pickup (Missile Expansion) (Crossway, Chozo Ruins)"),cre("Event - Activate Bomb Slots (Crossway, Chozo Ruins)", "Crossway Bomb Slots", False),cr("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)"),cr("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)"),cr("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)"),cr("Door to Crossway (Elder Hall Access, Chozo Ruins)"),cr("Door to Crossway (Crossway Access South, Chozo Ruins)"),cr("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)"),cr("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)"),crl("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)"),cr("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)"),cr("Door to Transport Access South (Reflecting Pool, Chozo Ruins)"),cr("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)"),cr("Door to Antechamber (Reflecting Pool, Chozo Ruins)"),cre("Event - Drain water (Reflecting Pool, Chozo Ruins)", "Reflecting Pool Water Drained", False),cr("Door to Reflecting Pool (Save Station 3, Chozo Ruins)"),cr("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)"),cr("Save Station (Save Station 3, Chozo Ruins)"),cr("Door to Reflecting Pool (Transport Access South, Chozo Ruins)"),cr("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)"),cr("Door to Reflecting Pool (Antechamber, Chozo Ruins)"),crl("Pickup (Ice Beam) (Antechamber, Chozo Ruins)"),cr("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)"),cr("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)"),cr("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)"),cr("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)"),cre("Event - Credits (Credits, End of Game)", "Credits", False),))
    menu_region.add_exits({
        region_format("Ship", "Landing Site", "Tallon Overworld"):
        # region_format("Ship Save", "Exterior Docking Hangar", "Frigate Orpheon"):
            "Start Game"
    })
from BaseClasses import MultiWorld, CollectionState
from worlds.AutoWorld import World
from typing import Callable

ConnectionRule = Callable[[CollectionState], bool]

ConnectionTuple = tuple[str, ConnectionRule]
RegionRules = tuple[str, tuple[ConnectionTuple, ...]]

def add_exits_to_world(world: MultiWorld, player: int, regions: tuple[RegionRules, ...]):
    for region_name, exits in regions:
        region = world.get_region(region_name, player)
        for connecting_region_name, rule in exits:
            region.connect(world.get_region(connecting_region_name, player), None, rule)

ConnectionDict = dict[str, ConnectionRule]

def set_rules(self: World):
    print("rules start!")
    multiworld = self.multiworld
    p = self.player
    o = self.options
    from . import logic as l

    t: ConnectionDict = {
        "Shoot Super Missile": lambda s:(s.has('Power Beam', p) and l.has_missiles(s, p, 5) and s.has('Charge Beam', p) and s.has('Super Missile', p) and t['Can Use Arm Cannon'](s)),
        "Have all Beams": lambda s:(s.has('Power Beam', p) and s.has('Wave Beam', p) and s.has('Ice Beam', p) and s.has('Plasma Beam', p) and t['Can Use Arm Cannon'](s)),
        "Heat-Resisting Suit": lambda s:(s.has('Gravity Suit', p) or s.has('Varia Suit', p) or s.has('Phazon Suit', p)),
        "Can Use Arm Cannon": lambda s:(s.has('Combat Visor', p) or s.has('Thermal Visor', p) or s.has('X-Ray Visor', p)),
        "Shoot Any Beam": lambda s:(t['Can Use Arm Cannon'](s) and (s.has('Power Beam', p) or s.has('Wave Beam', p) or s.has('Ice Beam', p) or s.has('Plasma Beam', p))),
        "Shoot Power Beam": lambda s:(s.has('Power Beam', p) and t['Can Use Arm Cannon'](s)),
        "Shoot Wave Beam": lambda s:(s.has('Wave Beam', p) and t['Can Use Arm Cannon'](s)),
        "Shoot Ice Beam": lambda s:(s.has('Ice Beam', p) and t['Can Use Arm Cannon'](s)),
        "Shoot Plasma Beam": lambda s:(s.has('Plasma Beam', p) and t['Can Use Arm Cannon'](s)),
        "Use Grapple Beam": lambda s:(s.has('Grapple Beam', p) and t['Can Use Arm Cannon'](s)),
        "Open Normal Door": lambda s:(t['Shoot Any Beam'](s) or (s.has('Morph Ball', p) and s.has('Morph Ball Bomb', p) and s.has('Scan Visor', p))),
        "Move Past Scatter Bombu": lambda s:(s.has('Morph Ball', p) or (o.movement.value>=1 and l.can_sustain_damage(s,p,12,'Damage')) or o.movement.value>=2 or l.can_sustain_damage(s,p,30,'Damage') or t['Shoot Wave Beam'](s)),
    }

    dock_requirements: ConnectionDict = {
        "Normal Door": lambda s:t['Open Normal Door'](s),
        "Normal Door (Forced)": lambda s:t['Open Normal Door'](s),
        "Ice Door": lambda s:t['Shoot Ice Beam'](s),
        "Wave Door": lambda s:t['Shoot Wave Beam'](s),
        "Plasma Door": lambda s:t['Shoot Plasma Beam'](s),
        "Missile Blast Shield": lambda s:(lambda _:True and (l.has_missiles(s, p, 1) and t['Shoot Any Beam'](s))),
        "Missile Blast Shield (randomprime)": lambda s:(lambda _:True and (l.has_missiles(s, p, 1) and t['Shoot Any Beam'](s))),
        "Permanently Locked": lambda _:False,
        "Circular Door": lambda s:t['Open Normal Door'](s),
        "Square Door": None,
        "Super Missile Blast Shield": lambda s:(t['Open Normal Door'](s) and t['Shoot Super Missile'](s)),
        "Power Bomb Blast Shield": lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball', p) and s.has('Power Bomb', p))),
        "Wavebuster Blast Shield": lambda s:(t['Shoot Wave Beam'](s) and (s.has('Charge Beam', p) and l.has_missiles(s, p, 11) and s.has('Wavebuster', p) and t['Shoot Wave Beam'](s))),
        "Ice Spreader Blast Shield": lambda s:(t['Shoot Ice Beam'](s) and (s.has('Charge Beam', p) and l.has_missiles(s, p, 10) and s.has('Ice Spreader', p) and t['Shoot Ice Beam'](s))),
        "Flamethrower Blast Shield": lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Charge Beam', p) and l.has_missiles(s, p, 10) and s.has('Flamethrower', p) and t['Shoot Plasma Beam'](s))),
        "Charge Beam Blast Shield": lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and s.has('Charge Beam', p))),
        "Bomb Blast Shield": lambda s:(t['Open Normal Door'](s) and (t['Open Normal Door'](s) and s.has('Morph Ball', p) and s.has('Morph Ball Bomb', p))),
        "Morph Ball Door": lambda s:(s.has('Morph Ball', p) and (s.has('Power Beam', p) or s.has('Ice Beam', p) or s.has('Wave Beam', p) or s.has('Plasma Beam', p)) and (s.has('Combat Visor', p) or s.has('Thermal Visor', p) or s.has('X-Ray Visor', p) or s.has('Scan Visor', p))),
        "Open Passage": lambda s:((s.has('Power Beam', p) or s.has('Ice Beam', p) or s.has('Wave Beam', p) or s.has('Plasma Beam', p)) and (s.has('Combat Visor', p) or s.has('Thermal Visor', p) or s.has('X-Ray Visor', p))),
        "Closed Passage": lambda _:False,
        "Not Determined": lambda _:False,
        "Teleporter": None,
    }

    add_exits_to_world(multiworld, p, (
            (
            "Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", (
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", (
                ("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Save Station (Crater Entry Point, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Save Station (Crater Entry Point, Impact Crater)", (
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Phazon Core (Crater Tunnel A, Impact Crater)", (
                ("Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crater Tunnel A (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Entry Point (Crater Tunnel A, Impact Crater)", (
                ("Door to Phazon Core (Crater Tunnel A, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crater Tunnel A (Crater Entry Point, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Missile Station (Phazon Core, Impact Crater)", (
                ("Door to Crater Tunnel A (Phazon Core, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crater Tunnel B (Phazon Core, Impact Crater)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 5, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 4, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bbYIFF00zYM?t=24117', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}]}}]}}),
                ("Door to Phazon Core (Crater Missile Station, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Tunnel A (Phazon Core, Impact Crater)", (
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bbYIFF00zYM?t=24029', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Phazon Core (Crater Tunnel A, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Tunnel B (Phazon Core, Impact Crater)", (
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phazon Core (Crater Tunnel B, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Core (Crater Missile Station, Impact Crater)", (
                ("Missile Station (Crater Missile Station, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Missile Station (Crater Missile Station, Impact Crater)", (
                ("Door to Phazon Core (Crater Missile Station, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", (
                ("Door to Phazon Core (Crater Tunnel B, Impact Crater)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 5, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 40, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Core (Crater Tunnel B, Impact Crater)", (
                ("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 5, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 40, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Crater Tunnel B (Phazon Core, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)", (
                ("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", (
                ("Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", (
                ("Dock to Subchamber Two (Subchamber One, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'and', 'data': {'comment': 'Fight Without Power Beam', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Flamethrower', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 25, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 54, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}),
                ("Dock to Subchamber One (Phazon Infusion Chamber, Impact Crater)", dock_requirements['Closed Passage']),
            )
            ),
            (
            "Dock to Subchamber Two (Subchamber One, Impact Crater)", (
                ("Dock from Phazon Infusion Chamber (Subchamber One, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber One (Subchamber Two, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber One (Subchamber Two, Impact Crater)", (
                ("Dock to Subchamber Three (Subchamber Two, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'and', 'data': {'comment': 'Fight Without Power Beam', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 25, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Flamethrower', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'Dodge/Tank Charge Attacks', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 76, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 119, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}),
                ("Dock to Subchamber Two (Subchamber One, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Three (Subchamber Two, Impact Crater)", (
                ("Dock to Subchamber One (Subchamber Two, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber Two (Subchamber Three, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Four (Subchamber Three, Impact Crater)", (
                ("Dock to Subchamber Two (Subchamber Three, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber Three (Subchamber Four, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Two (Subchamber Three, Impact Crater)", (
                ("Dock to Subchamber Four (Subchamber Three, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'and', 'data': {'comment': 'Fight Without Power Beam', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 25, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Flamethrower', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'Dodge/Tank Charge Attacks', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 76, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 179, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}),
                ("Dock to Subchamber Three (Subchamber Two, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Five (Subchamber Four, Impact Crater)", (
                ("Dock to Subchamber Three (Subchamber Four, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber Four (Subchamber Five, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Three (Subchamber Four, Impact Crater)", (
                ("Dock to Subchamber Five (Subchamber Four, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Have all Beams'}, {'type': 'and', 'data': {'comment': 'Abuse Exo Color Swaps', 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': 'Dodge/Tank Charge Attacks', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 99, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 239, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 149, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Dock to Subchamber Four (Subchamber Three, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Four (Subchamber Five, Impact Crater)", (
                ("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber Five (Subchamber Four, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", (
                ("Dock to Subchamber Four (Subchamber Five, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", (
                ("Teleporter to Credits (Metroid Prime Lair, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Finding Essence', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'Dodging Shockwave Attacks', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'Killing Metroids', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 5, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'Health Requirements', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 5, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 149, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 249, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 299, 'negate': False}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Dock to Metroid Prime Lair (Subchamber Five, Impact Crater)", dock_requirements['Open Passage']),
            )
            ),
            (
            "Teleporter to Credits (Metroid Prime Lair, Impact Crater)", (
                ("Dock to Subchamber Five (Metroid Prime Lair, Impact Crater)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Credits (Credits, End of Game)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/P09IVaDB0qg', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'Crystallites - Two Dashes', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)", {'type': 'template', 'data': 'Shoot Plasma Beam'}),
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}),
                ("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=VgXr4JJDIK4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/WCAMYqZ0HnU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3NCX-z9ZlkE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': 'https://youtu.be/i1CJ_nBioSg', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}]}}),
                ("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Power', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Wave', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'template', 'data': 'Move Past Scatter Bombu'}]}}),
                ("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", (
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Power', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Wave', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'template', 'data': 'Move Past Scatter Bombu'}]}}),
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", (
                ("Save Station (Save Station B, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station B, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Save Station B, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Ruins Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", (
                ("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Plaza Walkway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", (
                ("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'template', 'data': 'Move Past Scatter Bombu'}]}}),
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", (
                ("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}]}}, {'type': 'template', 'data': 'Move Past Scatter Bombu'}]}}),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/LoMIQJ7KCvM?t=59', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 50, 'negate': False}}]}}]}}]}}),
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event18', 'amount': 1, 'negate': False}}),
                ("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", (
                ("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event18', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/LoMIQJ7KCvM?t=144', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event18', 'amount': 1, 'negate': True}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event18', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/4CEDjoJf05g', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/b__DpiqBClE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/_tAyGmcRUH0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/0welXKqaL84', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/zmfRbFW7iTs', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 10, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/C34D7YoR89s', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/aEXs3IcpLY0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 10, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'DBoosting', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}),
                ("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)", (
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/33NNFgHw8e4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}]}}]}}),
                ("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/pdTiFz6aaBU', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/0eT32t8eA7c', 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/5LUAYPIwSEA', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)", {'type': 'template', 'data': 'Shoot Plasma Beam'}),
                ("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ice Ruins East (Plaza Walkway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", (
                ("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", (
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
                ("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins West (Courtyard Entryway, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", (
                ("Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ice Ruins West (Canyon Entryway, Phendrana Drifts)", (
                ("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", (
                ("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 25, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 17, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'Without Arm Cannon', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 100, 'negate': False}}]}}]}}),
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", (
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/-TyAn6wnWrw', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/ECz9JOIU_m0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}]}}),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yd36sVzpFuY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/ECz9JOIU_m0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yAZtvzGa3jM', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yAZtvzGa3jM?t=7', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yu8HqtvPWFs', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/jUuK_MgVrZQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", (
                ("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'Triple Boost - https://youtu.be/MARCa8m6ehQ?t=57', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", (
                ("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/tAOAGwmIt_k', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", (
                ("Save Station (Save Station A, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station A, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Research Entrance (Specimen Storage, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Specimen Storage (Research Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Specimen Storage, Phendrana Drifts)", (
                ("Door to Research Entrance (Specimen Storage, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", (
                ("Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Courtyard (Quarantine Access, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Specimen Storage (Research Entrance, Phendrana Drifts)", (
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Research Entrance (Specimen Storage, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Map Station (Research Entrance, Phendrana Drifts)", (
                ("Door to Specimen Storage (Research Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Research Entrance (Map Station, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", (
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to North Quarantine Tunnel (Quarantine Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Entrance (Map Station, Phendrana Drifts)", (
                ("Map Station (Map Station, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Map Station (Map Station, Phendrana Drifts)", (
                ("Door to Research Entrance (Map Station, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Hydra Lab Entryway (Research Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Entrance (Hydra Lab Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/jePin3nMhZk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': 'https://youtu.be/nRqjTUYEwIE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/8gjVJtRv0IQ?t=17', 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/8gjVJtRv0IQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}]}}),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/zsr_gmeBc-0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/VYNNHlviYJY?t=30', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/VYNNHlviYJY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Event - Thardus (Quarantine Cave, Phendrana Drifts)", (
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)", (
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Room Center (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/O0i-qUDJ-Y0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/hXvb7HxVP2U', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'DBoosting', 'amount': 5, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'DBoosting', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 30, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': True}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/vm1iRJSc0mw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'or', 'data': {'comment': 'https://youtu.be/j1n_eD5X_sU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/0V8nQpAi4fM', 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/j1n_eD5X_sU', 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/-Qg-WRKp63Y', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/-Qg-WRKp63Y?t=7', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': False}}]}}),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Fight Trigger (Quarantine Cave, Phendrana Drifts)", (
                ("Event - Thardus (Quarantine Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'Vision Requirements', 'items': [{'type': 'or', 'data': {'comment': 'Finding Weakpoints with thermal', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'Finding Weakpoints with bombs (not in scan data so combat trick)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'Avoiding Thermal Only Fight', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Thermal Only fight', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 5, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': 'Weapon Requirements', 'items': [{'type': 'or', 'data': {'comment': 'Any beam but Ice', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Power', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Wave', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'Missile Strat (Allows Ice only fight)', 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 80, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 40, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': 'Dodge roll phase Requirements', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event17', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event20', 'amount': 1, 'negate': False}}),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event20', 'amount': 1, 'negate': False}}),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_labs', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)", {'type': 'template', 'data': 'Shoot Super Missile'}),
                ("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", (
                ("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", (
                ("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Observatory (Observatory Access, Phendrana Drifts)", (
                ("Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Hydra (Observatory Access, Phendrana Drifts)", (
                ("Door to Observatory (Observatory Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=kpbBzBjYxJk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/1eYUaaC5aPE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/APHumwVABLE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Observatory Access (Observatory, Phendrana Drifts)", (
                ("Door to Save Station D (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}]}}),
                ("Event - Observatory Activated (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/irV01RQ3vMo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Observatory (Observatory Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/6W7_rc5y8X8?t=18', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/63HHfqC9jFA', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Observatory (West Tower Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Save Station D (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/38sI_6QMsk0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/RHqNT4sQ8l4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Observatory (Save Station D, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Event - Observatory Activated (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Pickup (Super Missile) (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}]}}),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event21', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frozen Pike (Transport Access, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}]}}),
                ("Door to Transport Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", {'type': 'template', 'data': 'Shoot Plasma Beam'}),
            )
            ),
            (
            "Door to West Tower (West Tower Entrance, Phendrana Drifts)", (
                ("Door to Observatory (West Tower Entrance, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to West Tower Entrance (West Tower, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Observatory (West Tower Entrance, Phendrana Drifts)", (
                ("Door to West Tower (West Tower Entrance, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Observatory (Save Station D, Phendrana Drifts)", (
                ("Save Station (Save Station D, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station D, Phendrana Drifts)", (
                ("Door to Observatory (Save Station D, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Pike Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Transport Access (Frozen Pike, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/S4831hWNEfY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Xul1w1SsPew', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/S4831hWNEfY?t=20', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frozen Pike (Pike Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frozen Pike (Transport Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bbYIFF00zYM?t=22984', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event49', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event49', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/wHFI_ddzWYA', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/z_DxqQ66tQY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (West Tower, Phendrana Drifts)", (
                ("Door to Control Tower (West Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to West Tower (West Tower Entrance, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Control Tower (West Tower, Phendrana Drifts)", (
                ("Door to West Tower Entrance (West Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Tower (Control Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frozen Pike (Pike Access, Phendrana Drifts)", (
                ("Door to Research Core (Pike Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core (Pike Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Pike Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Pike Access (Research Core, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", (
                ("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/1sDazah_y0w', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", (
                ("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to East Tower (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Control Tower (East Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}),
                ("Fight Trigger (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Control Tower (West Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event47', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=aRTUlWDOl84', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Room Center (Control Tower, Phendrana Drifts)", (
                ("Door to East Tower (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Tower (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event57', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event47', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/aRTUlWDOl84', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Fight Trigger (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", (
                ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Fight Trigger (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event57', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}]}}),
                ("Event - Control Tower Fight (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 100, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event57', 'amount': 1, 'negate': True}}]}}),
            )
            ),
            (
            "Event - Control Tower Fight (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Pike Access (Research Core, Phendrana Drifts)", (
                ("Door to Research Core Access (Research Core, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event19', 'amount': 1, 'negate': True}}]}}),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Research Core (Pike Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Core, Phendrana Drifts)", (
                ("Door to Pike Access (Research Core, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Research Core (Research Core Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", (
                ("Event - Research Core Power Outage (Research Core, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Research Core Power Outage (Research Core, Phendrana Drifts)", (
                ("Door to Pike Access (Research Core, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Save Station C (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frost Cave (Save Station C, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}),
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Ice Broken (Frost Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ANylQeC3en4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile) (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yS2j17CntJQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Frost Cave Floor (Frost Cave, Phendrana Drifts)", (
                ("Door to Save Station C (Frost Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/8y87p0uGneM', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}]}}),
                ("Pickup (Missile) (Frost Cave, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event45', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Event - Ice Broken (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/wmwIhBC7OSQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/wmwIhBC7OSQ?t=12', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", (
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': 'https://youtu.be/QI_8AWgk6ts', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': 'https://youtu.be/iYX3Bt8Vnnw?t=12', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/iYX3Bt8Vnnw?t=2', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/oPvUjPIBQQo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/eUjS8NryIl8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 3, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': 'https://youtu.be/Rw8w0ZSjeOc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Chamber Access (Hunter Cave, Phendrana Drifts)", (
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hunter Cave (Chamber Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': 'https://youtu.be/oPvUjPIBQQo?t=27', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}),
                ("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", (
                ("Door to Control Tower (East Tower, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Control Tower (East Tower, Phendrana Drifts)", (
                ("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to East Tower (Control Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core (Research Core Access, Phendrana Drifts)", (
                ("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Research Core Access (Research Core, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", (
                ("Door to Research Core (Research Core Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Save Station C, Phendrana Drifts)", (
                ("Save Station (Save Station C, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station C (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Save Station (Save Station C, Phendrana Drifts)", (
                ("Door to Frost Cave (Save Station C, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", (
                ("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Chamber Access, Phendrana Drifts)", (
                ("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", (
                ("Door to Hunter Cave (Chamber Access, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", (
                ("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", (
                ("Door to Hunter Cave (Lake Tunnel, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", (
                ("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", (
                ("Door to East Tower (Aether Lab Entryway, Phendrana Drifts)", {'type': 'template', 'data': 'Move Past Scatter Bombu'}),
                ("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", (
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", (
                ("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}]}}),
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/GMFocTIJ_8Y', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Research Lab Aether (Research Core Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)", (
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile) (Research Lab Aether, Phendrana Drifts)", (
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Lab Catwalk (Research Lab Aether, Phendrana Drifts)", (
                ("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/GMFocTIJ_8Y?t=26', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/ig_3kiPFlJw (SJ Speed Strategy)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/k7ylvABQ_Oo?t=37', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/xFqiwtdAQ7k', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}]}}),
                ("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", (
                ("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=1-jXmt9cIzI', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Use Grapple Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event49', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/V_CBSW0l8Hs', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/6HGs473mXh8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/E65HYxLnOZQ?t=59', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 5, 'negate': False}}]}}]}}]}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}]}}]}}),
                ("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/zSFCrCKbmYo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=k7ylvABQ_Oo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/QF5LBG-rr6w', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Pickup (Missile) (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", (
                ("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", (
                ("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", (
                ("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", (
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", (
                ("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", (
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", (
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Burning Trail (Transport to Chozo Ruins North, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Chozo Ruins North (Burning Trail, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", (
                ("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}]}}]}}),
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}]}}]}}),
                ("Door to Lake Tunnel (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", (
                ("Save Station (Save Station Magmoor A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station Magmoor A, Magmoor Caverns)", (
                ("Door to Burning Trail (Save Station Magmoor A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", (
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 2, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/TjoCnZ4e8LU', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 190, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/DnktNBI_DQI', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 190, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 140, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 110, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 10, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", (
                ("Next to Crates (Lava Lake, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 285, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 250, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 265, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 255, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 360, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 325, 'negate': False}}]}}]}}]}}]}}]}}]}}]}}),
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 150, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Next to Crates (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 25, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 115, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 10, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 155, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 10, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 340, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 265, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 305, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 245, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 270, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 360, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 340, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 365, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 320, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 340, 'negate': False}}]}}]}}]}}]}}]}}]}}]}}]}}]}}),
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 2, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 80, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/TjoCnZ4e8LU', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/DnktNBI_DQI', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 95, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 110, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/puEX6Ofl_5k', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 280, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/C7caSCXbLFc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 155, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/DWJhZjuiMKY', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 220, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/Auy_WagsHf4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 255, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 225, 'negate': False}}]}}]}}]}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 145, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 110, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", (
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 150, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 140, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 130, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/puEX6Ofl_5k', 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 130, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/C7caSCXbLFc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 60, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/DWJhZjuiMKY', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 100, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/Auy_WagsHf4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 200, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 180, 'negate': False}}]}}]}}]}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 95, 'negate': False}}]}}]}}]}}),
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 145, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 110, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 145, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 95, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Tunnel Entrance (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 185, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 145, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 130, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 150, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 130, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}),
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}),
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", (
                ("Pickup (Missile) (Storage Cavern, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile) (Storage Cavern, Magmoor Caverns)", (
                ("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", (
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/8Xzak1I7Fx8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 235, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/KuvfXDG6Wt8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 15, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}]}}]}}),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 230, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Gg96zB6NmI8', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}),
                ("Middle Level (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': 'Combat traversal example with Combat Dash and Standable: https://youtu.be/G71ZZKcC7wU', 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': 'Combat traversal example with Combat Dash and Standable: https://youtu.be/G71ZZKcC7wU', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 255, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 85, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 415, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 8, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 320, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 440, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 60, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 315, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 205, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", (
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 235, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 299, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/YD4FKuH406E', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}]}}]}}]}}),
                ("Middle Level (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}]}}]}}),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}]}}]}}),
                ("Middle Level (Monitor Station, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 70, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 30, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 2, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 60, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}),
                ("Middle Level (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'Standable for fast ascent with SJ: https://youtu.be/SxJp9io5Gds', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 430, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 255, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 65, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 354, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 8, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 300, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 205, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 35, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 235, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 119, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Middle Level (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 55, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 54, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}]}}]}}),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'Example with Standable and Dash: https://youtu.be/Hdr0jzVoMnc', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 235, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 319, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/YD4FKuH406E', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 219, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=0hJhOR1YmAs', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 154, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 54, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/uowYhKwb4B0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 250, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 150, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 185, 'negate': False}}]}}]}}]}}),
                ("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/uowYhKwb4B0?t=45', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 240, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 140, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}]}}]}}),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 80, 'negate': False}}]}}]}}]}}),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 90, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", (
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 40, 'negate': False}}]}}]}}),
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
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 20, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", (
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 80, 'negate': False}}]}}]}}),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 70, 'negate': False}}]}}]}}]}}),
                ("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 30, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 55, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 35, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 55, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 45, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 35, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 35, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/QX7J-L3B0Hs', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 85, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Ym7dbJ0o8VQ', 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Room Center (Shore Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 60, 'negate': False}}]}}]}}),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}]}}]}}),
                ("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", (
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Phendrana Drifts (Transport to Phendrana Drifts North, Magmoor Caverns)", (
                ("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns West, Phendrana Drifts)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", (
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 30, 'negate': False}}]}}]}}),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 239, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 50, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 235, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 189, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 230, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 279, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 30, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 245, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 15, 'negate': False}}]}}]}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 245, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/sbwLymFj43s', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 270, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/nWCD5bVO1QA', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 315, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 215, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)", (
                ("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 25, 'negate': False}}]}}]}}),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", (
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 55, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ZCiHkUyTMm8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Pickup (Missile) (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 10, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}]}}]}}]}}),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 220, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 185, 'negate': False}}]}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 40, 'negate': False}}]}}]}}),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 250, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 210, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 35, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 175, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 185, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 35, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 215, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 50, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 175, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 25, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 25, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 130, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 115, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 275, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 170, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 15, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 165, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 140, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 215, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 45, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 59, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 45, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 59, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", (
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", (
                ("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 65, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 50, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 60, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 185, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 85, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 160, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 80, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 120, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 70, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/9jk5s2W6yhY', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 10, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 110, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 95, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 75, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 200, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 150, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 125, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 85, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/TleaFWdVhUg', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 15, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/OK3lSWvTKKU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 135, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 85, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Ue9T-9SY0o4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 145, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 95, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 20, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/6tAv_ivVvAQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 120, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 60, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 3, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 200, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 55, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 50, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/6tAv_ivVvAQ?t=37', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 285, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 3, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 60, 'negate': False}}]}}]}}),
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco?t=24', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 105, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco?t=40', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 120, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco?t=31', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 105, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco?t=49', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v2uQH10pPco?t=14', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 185, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 230, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 75, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': True}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}]}}),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/4uV36UbD2b4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event22', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/Edzhf9hl0w8', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 185, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 300, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 70, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 85, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': True}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}]}}),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/svpG1lg1ahw', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': True}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", (
                ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/OwsVX5HEGVQ?t=7', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}),
            )
            ),
            (
            "First Spinner (Geothermal Core, Magmoor Caverns)", (
                ("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BoostlessSpiner', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=OwsVX5HEGVQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event46', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", (
                ("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)", (
                ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Plasma Beam (Plasma Processing, Magmoor Caverns)", (
                ("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 80, 'negate': False}}]}}]}}),
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 40, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 100, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 80, 'negate': False}}]}}]}}),
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3N7BMPBBHsI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3N7BMPBBHsI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 75, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': 'https://youtu.be/qnOw1NJdHDg?t=17', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}),
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': 'https://youtu.be/qnOw1NJdHDg', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", (
                ("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", (
                ("Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (Transport Tunnel C, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", (
                ("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", (
                ("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport Tunnel C (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Phendrana Drifts South (Transport Tunnel C, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Phendrana Drifts (Transport to Phendrana Drifts South, Magmoor Caverns)", (
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", (
                ("Save Station (Save Station Magmoor B, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station Magmoor B, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts South (Save Station Magmoor B, Magmoor Caverns)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", (
                ("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Quarry (Quarry Access, Phazon Mines)", (
                ("Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld South (Quarry Access, Phazon Mines)", (
                ("Door to Main Quarry (Quarry Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarry Access (Transport to Tallon Overworld South, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Waste Disposal (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Crane Platform (Main Quarry, Phazon Mines)", {'type': 'template', 'data': 'Use Grapple Beam'}),
                ("Door to Main Quarry (Waste Disposal, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Quarry Access (Main Quarry, Phazon Mines)", (
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}]}}),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", {'type': 'or', 'data': {'comment': 'https://youtu.be/8hDg9fJZH1c', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Security Access A (Main Quarry, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event23', 'amount': 1, 'negate': False}}),
                ("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Crane Platform (Main Quarry, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/lhgy7ja-uMU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Grapple', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/w6UegkJsX2c', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Main Quarry (Quarry Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Save Station Mines A (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Security Access A (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event23', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_upper_mines', 'amount': 1, 'negate': False}}]}}),
                ("Door to Main Quarry (Security Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Main Quarry, Phazon Mines)", (
                ("Crane Platform (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", (
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Crane Platform (Main Quarry, Phazon Mines)", (
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/gdX17ZXOKuo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/DJzZA1VrvEY', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/pebPvJHAFxk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/mVH_SHAqZFE', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile) (Main Quarry, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/i_l-GC9z9eI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=TgGo2RyY79w', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/J0IPE2WIXXw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/KitFN4fnGkk', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Main Quarry (Waste Disposal, Phazon Mines)", (
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ore Processing (Waste Disposal, Phazon Mines)", (
                ("Door to Main Quarry (Waste Disposal, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Main Quarry (Save Station Mines A, Phazon Mines)", (
                ("Save Station (Save Station Mines A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event34', 'amount': 1, 'negate': False}}]}}),
                ("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Save Station (Save Station Mines A, Phazon Mines)", (
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event34', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", (
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Main Quarry (Security Access A, Phazon Mines)", (
                ("Door to Mine Security Station (Security Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile) (Security Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Security Access A (Main Quarry, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Mine Security Station (Security Access A, Phazon Mines)", (
                ("Door to Main Quarry (Security Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Security Access A, Phazon Mines)", (
                ("Door to Main Quarry (Security Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Research Access (Ore Processing, Phazon Mines)", (
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Shoot Power Beam'}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/gnqifLICKyo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Ore Processing (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Storage Depot B (Ore Processing, Phazon Mines)", (
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/oRZOljmytRQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/7ATtR9o9PRw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 50, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ore Processing (Storage Depot B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Waste Disposal (Ore Processing, Phazon Mines)", (
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator Access A (Ore Processing, Phazon Mines)", (
                ("Door to Research Access (Ore Processing, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/vA9uH9u1RjE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Wf1Pz9bXAgQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Ore Processing (Elevator Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access A (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Mine Security Station (Security Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access B (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Mine Security Station (Security Access B, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Storage Depot A (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event35', 'amount': 1, 'negate': False}}]}}),
                ("Door to Mine Security Station (Storage Depot A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", (
                ("Room Center (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", (
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Room Center (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Room Center (Mine Security Station, Phazon Mines)", (
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event55', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event55', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Storage Depot A (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event35', 'amount': 1, 'negate': False}}]}}),
                ("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event55', 'amount': 1, 'negate': True}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Ore Processing (Research Access, Phazon Mines)", (
                ("Door to Elite Research (Research Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/X-6LeSNC5LM?t=757', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Research Access (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Research (Research Access, Phazon Mines)", (
                ("Door to Ore Processing (Research Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Research Access (Elite Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ore Processing (Storage Depot B, Phazon Mines)", (
                ("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)", (
                ("Door to Ore Processing (Storage Depot B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Storage Depot B Item (Storage Depot B, Phazon Mines)", (
                ("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ore Processing (Elevator Access A, Phazon Mines)", (
                ("Door to Elevator A (Elevator Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator A (Elevator Access A, Phazon Mines)", (
                ("Door to Ore Processing (Elevator Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/X-6LeSNC5LM?t=408', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Door to Elevator Access A (Elevator A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Research (Security Access B, Phazon Mines)", (
                ("Door to Mine Security Station (Security Access B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Security Access B (Elite Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Mine Security Station (Security Access B, Phazon Mines)", (
                ("Door to Elite Research (Security Access B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Mine Security Station (Storage Depot A, Phazon Mines)", (
                ("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Storage Depot A (Mine Security Station, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Flamethrower) (Storage Depot A, Phazon Mines)", (
                ("Door to Mine Security Station (Storage Depot A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Research Access (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event24', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ljX553EUfX4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Elite Research (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access B (Elite Research, Phazon Mines)", (
                ("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'phazon_elite_without_dynamo', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Top Floor (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Standable for fast ascent: https://youtu.be/ezNh_4a3uNg', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}),
                ("Door to Elite Research (Security Access B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile) (Elite Research, Phazon Mines)", (
                ("Top Floor (Elite Research, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", (
                ("Door to Security Access B (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Top Floor (Elite Research, Phazon Mines)", (
                ("Door to Research Access (Elite Research, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event24', 'amount': 1, 'negate': False}}),
                ("Door to Security Access B (Elite Research, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}),
                ("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/qQOtfh5u_bQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BoostlessSpiner', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Pickup (Missile) (Elite Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event24', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Elevator Access A (Elevator A, Phazon Mines)", (
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Elevator A (Elevator Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control Access (Elevator A, Phazon Mines)", (
                ("Door to Elevator Access A (Elevator A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elevator A (Elite Control Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator A (Elite Control Access, Phazon Mines)", (
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile) (Elite Control Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/yIYfpeVsYCU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=2kknFYIyAEo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'DBoosting', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 100, 'negate': False}}]}}]}}]}}),
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control (Elite Control Access, Phazon Mines)", (
                ("Door to Elevator A (Elite Control Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=8jxY6XLwTzE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Elite Control Access (Elite Control, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile) (Elite Control Access, Phazon Mines)", (
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Maintenance Tunnel (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elite Control (Maintenance Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control Access (Elite Control, Phazon Mines)", (
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", {'type': 'or', 'data': {'comment': 'https://youtu.be/mx0rQa9ZAY4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event51', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/86eWOxO83Zk', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Elite Control, Phazon Mines)", (
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event26', 'amount': 1, 'negate': False}}),
                ("Door to Elite Control (Ventilation Shaft, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", (
                ("Bottom Floor Center (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Bottom Floor Center (Elite Control, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elite Control Access (Elite Control, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event51', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/lmEsr1Y1izM', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Ventilation Shaft (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event26', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/VOesQWYfL-4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event51', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event51', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/VOesQWYfL-4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", {'type': 'or', 'data': {'comment': 'https://youtu.be/mx0rQa9ZAY4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Elite Control (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Maintenance Tunnel (Elite Control, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Elite Control (Maintenance Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Ventilation Shaft, Phazon Mines)", (
                ("Door to Elite Control (Ventilation Shaft, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/P5YAnNux51U', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}]}}]}}),
                ("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control (Ventilation Shaft, Phazon Mines)", (
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ventilation Shaft (Elite Control, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)", (
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Transport Access (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Phazon Processing Center (Transport Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", (
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Halfway up: https://youtu.be/vOr2W2ut25k All the way up: https://youtu.be/gU2yAun0Zvg', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 4, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': True}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Power Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 45, 'negate': False}}]}}]}}),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 45, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/SjS_b_HBmqE', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 65, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': True}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Power Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/cxZ7-YewvDw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': True}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event56', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Power Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Map Station Mines (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Omega Research (Map Station Mines, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Omega Research, Phazon Mines)", (
                ("Door to Map Station Mines (Omega Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}),
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Dynamo Access (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/uxpkppiw3O8', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Transport Access, Phazon Mines)", (
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Transport Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event32', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 99, 'negate': False}}]}}]}}]}}),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Processing Center Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event32', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 99, 'negate': False}}]}}]}}]}}),
                ("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Processing Center Access (Elite Quarters, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Energy Tank) (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Omega Research (Map Station Mines, Phazon Mines)", (
                ("Map Station (Map Station Mines, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Map Station Mines (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Map Station (Map Station Mines, Phazon Mines)", (
                ("Door to Omega Research (Map Station Mines, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Central Dynamo (Dynamo Access, Phazon Mines)", (
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event50', 'amount': 1, 'negate': False}}]}}),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}),
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Dynamo Access, Phazon Mines)", (
                ("Door to Central Dynamo (Dynamo Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event50', 'amount': 1, 'negate': False}}]}}),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", (
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", {'type': 'or', 'data': {'comment': 'https://youtu.be/20peXRPG-e0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns South, Phazon Mines)", (
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Phazon Mines (Transport to Phazon Mines West, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", (
                ("Door to Processing Center Access (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event31', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=fMCAymS0zYE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Fight Trigger (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Processing Center Access (Elite Quarters, Phazon Mines)", (
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event31', 'amount': 1, 'negate': False}}]}}),
                ("Fight Trigger (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Omega Pirate (Elite Quarters, Phazon Mines)", (
                ("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)", (
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Fight Trigger (Elite Quarters, Phazon Mines)", (
                ("Event - Omega Pirate (Elite Quarters, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Have all Beams'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/xJxxT3yuXZ8 1-Cycle Strats', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/lX3IAoDGC30', 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 30, 'negate': False}}]}}]}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/kAvAMLyvQTk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 5, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 500, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 800, 'negate': False}}]}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
            )
            ),
            (
            "Door to Dynamo Access (Central Dynamo, Phazon Mines)", (
                ("Fight Trigger (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Central Dynamo (Dynamo Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Quarantine Access A (Central Dynamo, Phazon Mines)", (
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': 'Achieving the Infinite Speed without going up to hit the fight trigger: https://youtu.be/LRmJn2BAYwc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'IS', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 280, 'negate': False}}]}}),
                ("Room Bottom (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Central Dynamo (Quarantine Access A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Save Station Mines B (Central Dynamo, Phazon Mines)", (
                ("Room Bottom (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Central Dynamo (Save Station Mines B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Security Drone (Central Dynamo, Phazon Mines)", (
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'Destroying the drone requires Samus being able to take 400 more damage during item acquisition. The video shows how to avoid destroying it. https://youtu.be/LRmJn2BAYwc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'IS', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 680, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", (
                ("Room Bottom (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Fight Trigger (Central Dynamo, Phazon Mines)", (
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': False}}),
                ("Event - Security Drone (Central Dynamo, Phazon Mines)", {'type': 'or', 'data': {'comment': 'Easy kills - Wavebuster (no X-Ray): https://youtu.be/3Y2n-boOGUw Super Missiles: https://youtu.be/aprVv7pePYc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 100, 'negate': False}}]}}),
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': 'Skipping the Security Drone trigger to take 400 less damage during item acquisition: https://youtu.be/LRmJn2BAYwc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'IS', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 280, 'negate': False}}]}}),
                ("Room Bottom (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Room Bottom (Central Dynamo, Phazon Mines)", (
                ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': 'The Security Drone event triggers door locks on all doors in Central Dynamo except for the door to Quarantine Access A.', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Ice', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Save Station Mines B (Central Dynamo, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}),
                ("Fight Trigger (Central Dynamo, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': 'Fast climb with Standable: https://youtu.be/MtpgWKgaF-U', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/GTSoLLbo2vk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event25', 'amount': 1, 'negate': True}}]}}]}}),
            )
            ),
            (
            "Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", (
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event30', 'amount': 1, 'negate': False}}]}}),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}]}}),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event30', 'amount': 1, 'negate': False}}]}}),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}]}}),
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Central Dynamo (Quarantine Access A, Phazon Mines)", (
                ("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", (
                ("Door to Central Dynamo (Quarantine Access A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Central Dynamo (Save Station Mines B, Phazon Mines)", (
                ("Save Station (Save Station Mines B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station Mines B (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Save Station (Save Station Mines B, Phazon Mines)", (
                ("Door to Central Dynamo (Save Station Mines B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", (
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=h9of56WsG4s', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'https://www.youtube.com/watch?v=v3VMpJELp_4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/wXxYBRIgDb4?t=62', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}]}}),
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}),
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/MwycHUSwAaQ?t=10', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/MwycHUSwAaQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 125, 'negate': False}}]}}]}}),
                ("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)", {'type': 'template', 'data': 'Shoot Super Missile'}),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}]}}),
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event29', 'amount': 1, 'negate': False}}),
                ("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", (
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Front of Barrier (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 150, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 50, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}),
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event29', 'amount': 1, 'negate': False}}),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", (
                ("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event28', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/x036CC58IZ8?t=9', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 3, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}]}}]}}),
                ("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event28', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 200, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 150, 'negate': False}}]}}]}}]}}),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}),
                ("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/tQzvoPTimww?t=35', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=EgTFsy2qGh8&t=28s', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event28', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 99, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 75, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 55, 'negate': False}}]}}]}}]}}),
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/zPD0diebSX8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/tQzvoPTimww', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}]}}),
            )
            ),
            (
            "Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event28', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_lower_mines', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/tQzvoPTimww?t=19', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 2, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", (
                ("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 150, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 150, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 300, 'negate': False}}]}}]}}),
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 150, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/nZafCBqD5EQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 100, 'negate': False}}]}}]}}),
                ("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", (
                ("Save Station (Save Station Mines C, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Save Station (Save Station Mines C, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Save Station Mines C, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", (
                ("Door to Elevator B (Elevator Access B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator B (Elevator Access B, Phazon Mines)", (
                ("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elevator Access B (Elevator B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", (
                ("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v_MgT0eE-LY?t=10', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v_MgT0eE-LY?t=37', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/v_MgT0eE-LY?t=21', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/HbzeA1Z4_nc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Ice Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 4, 'negate': False}}]}}]}}),
                ("Pickup (Missile) (Fungal Hall B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Fungal Hall B, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Elevator Access B (Elevator B, Phazon Mines)", (
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Elevator B (Elevator Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall Access (Elevator B, Phazon Mines)", (
                ("Door to Elevator Access B (Elevator B, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", (
                ("Missile Station (Missile Station Mines, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Missile Station (Missile Station Mines, Phazon Mines)", (
                ("Door to Fungal Hall B (Missile Station Mines, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 30, 'negate': False}}]}}]}}]}}),
                ("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 1299, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 1199, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 1099, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 999, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 30, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 200, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 300, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 400, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", (
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/0MdHYuM1mIQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=0oZ7WaA8P4I', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile) (Fungal Hall Access, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PhazonSuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Phazon', 'amount': 100, 'negate': False}}]}}]}}]}}),
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elevator B (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://www.youtube.com/watch?v=CeQFOSCvZPE', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 5, 'negate': False}}]}}]}}),
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", (
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'template', 'data': 'Use Grapple Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}]}}]}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 4, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 599, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 299, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 299, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 4, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Plasma', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 299, 'negate': False}}]}}]}}]}}),
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Gully (Landing Site, Tallon Overworld)", (
                ("Door to Alcove (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Landing Site (Gully, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Canyon Cavern (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Landing Site (Canyon Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Hall (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Landing Site (Temple Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Alcove (Landing Site, Tallon Overworld)", (
                ("Door to Gully (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Landing Site (Alcove, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Waterfall Cavern (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Landing Site (Waterfall Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Landing Site, Tallon Overworld)", (
                ("Ship (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Ship (Landing Site, Tallon Overworld)", (
                ("Door to Gully (Landing Site, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/koDuUn-oyW0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=CKdG2oDcI6w', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}]}}]}}),
                ("Door to Canyon Cavern (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Hall (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Door to Tallon Canyon (Gully, Tallon Overworld)", (
                ("Door to Landing Site (Gully, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gully (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Gully, Tallon Overworld)", (
                ("Door to Tallon Canyon (Gully, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Gully (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", (
                ("Door to Landing Site (Canyon Cavern, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Canyon Cavern, Tallon Overworld)", (
                ("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Canyon Cavern (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Security Station (Temple Hall, Tallon Overworld)", (
                ("Door to Landing Site (Temple Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Hall (Temple Security Station, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Temple Hall, Tallon Overworld)", (
                ("Door to Temple Security Station (Temple Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Hall (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Landing Site (Alcove, Tallon Overworld)", (
                ("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Alcove (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Space Jump Boots) (Alcove, Tallon Overworld)", (
                ("Door to Landing Site (Alcove, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Landing Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Landing Site (Waterfall Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tallon Canyon (Canyon Cavern, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gully (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Tallon Canyon (Gully, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", (
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Half Pipe (Tallon Canyon, Tallon Overworld)", (
                ("Door to Canyon Cavern (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gully (Tallon Canyon, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Temple Hall (Temple Security Station, Tallon Overworld)", (
                ("Door to Temple Lobby (Temple Security Station, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Security Station (Temple Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Lobby (Temple Security Station, Tallon Overworld)", (
                ("Door to Temple Hall (Temple Security Station, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Security Station (Temple Lobby, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Wl0L20SepgM', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=CSN7vHMJTZM', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/X1rAc0AROx8', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/X1rAc0AROx8?t=19', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/X1rAc0AROx8?t=8', 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=JgYL5t7JpuM', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/4U3HKuFJo4k', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/aSuUqNP1VhI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/IlJq4ySwgVY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': 'https://youtu.be/HoHCPganAI0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}),
                ("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", (
                ("Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tallon Canyon (Transport Tunnel A, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel A (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Cave (Root Tunnel, Tallon Overworld)", (
                ("Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Tallon Canyon (Root Tunnel, Tallon Overworld)", (
                ("Door to Root Cave (Root Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Root Tunnel (Tallon Canyon, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Artifact Temple (Temple Lobby, Tallon Overworld)", (
                ("Door to Temple Security Station (Temple Lobby, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Security Station (Temple Lobby, Tallon Overworld)", (
                ("Door to Artifact Temple (Temple Lobby, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Temple Lobby (Temple Security Station, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Frigate Access Tunnel, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Chozo Ruins West (Transport Tunnel A, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", (
                ("Door to Transport Tunnel A (Transport to Chozo Ruins West, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Tunnel B (Root Cave, Tallon Overworld)", (
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Root Cave (Transport Tunnel B, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Tunnel (Root Cave, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': 'https://youtu.be/x2zjlvSy0Og', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/i2J6z6wrLGw', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/imhkxmwiU9o', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'IUJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 5, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Root Cave (Root Tunnel, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Arbor Chamber (Root Cave, Tallon Overworld)", (
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/UVXjHNV3dWU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}),
                ("Door to Root Cave (Arbor Chamber, Tallon Overworld)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Arbor Chamber (Root Cave, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Temple Lobby (Artifact Temple, Tallon Overworld)", (
                ("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Meta Ridley (Artifact Temple, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Chozo', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Elder', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Lifegiver', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Nature', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Newborn', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spirit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Strength', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Sun', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Truth', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Warrior', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Wild', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'World', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 400, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 300, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 100, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 4, 'negate': False}}]}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event2', 'amount': 1, 'negate': False}}),
                ("Door to Artifact Temple (Temple Lobby, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Meta Ridley (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", (
                ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", (
                ("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=VNl_mxt2ybQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Root Cave (Transport Tunnel B, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)", (
                ("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Root Cave (Transport Tunnel B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Root Cave (Arbor Chamber, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Arbor Chamber (Root Cave, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)", (
                ("Door to Root Cave (Arbor Chamber, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event36', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_frigate', 'amount': 1, 'negate': False}}]}}),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'backwards_frigate', 'amount': 1, 'negate': True}}]}}),
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event36', 'amount': 1, 'negate': False}}),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", (
                ("Door to Transport Tunnel C (Transport to Chozo Ruins East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", (
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns East (Transport Tunnel B, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns East, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Transport to Magmoor Caverns East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", (
                ("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Reactor Access (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reactor Core (Main Ventilation Shaft Section A, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Room Bottom (Reactor Core, Tallon Overworld)", (
                ("Door to Reactor Access (Reactor Core, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event37', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/FS571wDqNh4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://media.discordapp.net/attachments/532853087224856587/882821020493426708/nsj_no_grav_reactor_core.mp4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 4, 'negate': False}}]}}]}}),
                ("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", (
                ("Room Bottom (Reactor Core, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Reactor Core (Reactor Access, Tallon Overworld)", (
                ("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event38', 'amount': 1, 'negate': False}}]}}),
                ("Door to Savestation (Reactor Access, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Reactor Access (Reactor Core, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Savestation (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reactor Access (Savestation, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", (
                ("Door to Reactor Core (Reactor Access, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event40', 'amount': 1, 'negate': False}}),
                ("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/F203AupXoIs', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/JtPEH93DuBI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/gnlZwhxuLas', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", dock_requirements['Square Door']),
            )
            ),
            (
            "Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", (
                ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Reactor Access (Savestation, Tallon Overworld)", (
                ("Save Station (Savestation, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Savestation (Reactor Access, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Savestation, Tallon Overworld)", (
                ("Door to Reactor Access (Savestation, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", (
                ("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", (
                ("Door to Cargo Freight Lift to Deck Gamma (Deck Beta Transit Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", (
                ("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Biohazard Containment (Deck Beta Transit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", (
                ("Room Bottom (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Room Bottom (Biohazard Containment, Tallon Overworld)", (
                ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event41', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}]}}),
            )
            ),
            (
            "Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", (
                ("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", (
                ("Door to Biohazard Containment (Deck Beta Security Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Biotech Research Area 1 (Deck Beta Security Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Room Center (Biotech Research Area 1, Tallon Overworld)", (
                ("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/j49rhEIA-vk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/qAzRTa_tdDs', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event42', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/qAzRTa_tdDs?t=36', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/j49rhEIA-vk?t=38', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Thermal', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", (
                ("Room Center (Biotech Research Area 1, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", (
                ("Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Biotech Research Area 1 (Deck Beta Conduit Hall, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", (
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", (
                ("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/64pUwifXQzI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'Slowly Float Up Method', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/Dk7zplDvTZk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=c4NX1k6p-gE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/3s1SrxoMF_Y', 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/ih5KCjnUE_0 (With Gravity Suit)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}]}}),
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/3s1SrxoMF_Y', 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/ih5KCjnUE_0 (With Gravity Suit)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/3s1SrxoMF_Y', 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/ih5KCjnUE_0 (With Gravity Suit)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/XZXc1oJHHAc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}]}}),
                ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", (
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Bh4su3o-QQw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=_r-Pu5wZAek', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'StandEnemies', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 200, 'negate': False}}]}}]}}]}}),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/OtFv_-BEUfc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=Eeqt9aYPOX0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event1', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=8RA6ZOd5RSo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'X-Ray', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'InvisibleObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=21VlPG6TbY4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", (
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=QhCdABOjjhg', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 5, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Open gate (Great Tree Hall, Tallon Overworld)", (
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Next to Spinner (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event1', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=8RA6ZOd5RSo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Open gate (Great Tree Hall, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)", (
                ("Door to Great Tree Hall (Great Tree Chamber, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", (
                ("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", (
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/KwbsbH0mOqU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", (
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ghTNeSeVkcM', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/e9LJa7G60yE?t=16', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/e9LJa7G60yE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", (
                ("Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Transport Tunnel E, Tallon Overworld)", (
                ("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", (
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Chozo Ruins South (Transport Tunnel D, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", (
                ("Door to Transport Tunnel D (Transport to Chozo Ruins South, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", (
                ("Front of PB Wall (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)", (
                ("Front of PB Wall (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)", (
                ("Behind PB Wall (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Behind PB Wall (Life Grove, Tallon Overworld)", (
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bbYIFF00zYM?t=17638', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': 'https://www.youtube.com/watch?v=Kn65gJzeOwA (Manip with Gravity Suit)', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BoostlessSpiner', 'amount': 3, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/F2K62ZJ0lxM', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Front of PB Wall (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Front of PB Wall (Life Grove, Tallon Overworld)", (
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': 'https://youtu.be/CYMF6f2-Ht4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}]}}),
                ("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Behind PB Wall (Life Grove, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", (
                ("Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Phazon Mines East (Transport Tunnel E, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Teleporter to Phazon Mines (Transport to Phazon Mines East, Tallon Overworld)", (
                ("Door to Transport Tunnel E (Transport to Phazon Mines East, Tallon Overworld)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Phazon Mines)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld North, Chozo Ruins)", (
                ("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins West, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Main Plaza (Ruins Entrance, Chozo Ruins)", (
                ("Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld North (Ruins Entrance, Chozo Ruins)", (
                ("Door to Main Plaza (Ruins Entrance, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruins Entrance (Transport to Tallon Overworld North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}),
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'or', 'data': {'comment': 'https://youtu.be/7y7ZLBz3B1s', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/vk-C7kDPk10', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ivVhW1cxIz8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=kuaxthAhm54', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event54', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'DBoosting', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruins Entrance (Main Plaza, Chozo Ruins)", (
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Nursery Access (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ne8ap0xa_UE', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=wN2_EBHi-Fw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': 'https://youtu.be/G4PZlf7AYMU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Main Plaza (Ruins Entrance, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Nursery Access (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Plaza (Nursery Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door from Plaza Access (Main Plaza, Chozo Ruins)", (
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Main Plaza (Plaza Access, Chozo Ruins)", dock_requirements['Permanently Locked']),
            )
            ),
            (
            "Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Main Plaza, Chozo Ruins)", (
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)", (
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Locked Door Ledge (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door from Plaza Access (Main Plaza, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'misc', 'name': 'main_plaza_door', 'amount': 1, 'negate': False}}),
                ("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Grapple Ledge (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/ohV8u9oQFrc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}]}}]}}),
                ("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}]}}),
            )
            ),
            (
            "Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", (
                ("Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Ruined Shrine Access, Chozo Ruins)", (
                ("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", (
                ("Door to Main Plaza (Nursery Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Nursery Access, Chozo Ruins)", (
                ("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Nursery Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Main Plaza (Plaza Access, Chozo Ruins)", (
                ("Door to Vault (Plaza Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door from Plaza Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault (Plaza Access, Chozo Ruins)", (
                ("Door to Main Plaza (Plaza Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Plaza Access (Vault, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", (
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", (
                ("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", (
                ("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Fountain Access (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/OcHxU-t-WYk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/SbmRjJ04Lfk', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)", (
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/mmOJBhUouY4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Pit (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", (
                ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/93RLiYdob9Q', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}]}}]}}),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/93RLiYdob9Q', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/w0TIiZwv3Gk', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}]}}]}}]}}),
                ("Pit (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': 'https://youtu.be/3lkjUSO9tN4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}),
                ("Door to Ruined Shrine (Ruined Shrine Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pit (Ruined Shrine, Chozo Ruins)", (
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=nJVx6BVzXNc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event52', 'amount': 1, 'negate': True}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event53', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event52', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", (
                ("Pit (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", (
                ("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", (
                ("Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Nursery Access (Eyon Tunnel, Chozo Ruins)", (
                ("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Eyon Tunnel (Nursery Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault Access (Vault, Chozo Ruins)", (
                ("Door to Plaza Access (Vault, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Vault, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/tYcfbQYgiNE', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Vault (Vault Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plaza Access (Vault, Chozo Ruins)", (
                ("Door to Vault Access (Vault, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Vault (Plaza Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Vault, Chozo Ruins)", (
                ("Door to Vault Access (Vault, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Training Chamber Access (Training Chamber, Chozo Ruins)", (
                ("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event12', 'amount': 1, 'negate': False}}),
                ("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event11', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/a9jqExemHx0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
                ("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", {'type': 'template', 'data': 'Shoot Power Beam'}),
                ("Event - Unlock morph track (Training Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event11', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event12', 'amount': 1, 'negate': False}}),
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event11', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Unlock morph track (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Arboretum (Arboretum Access, Chozo Ruins)", (
                ("Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Arboretum Access (Arboretum, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Ruined Fountain (Arboretum Access, Chozo Ruins)", (
                ("Door to Arboretum (Arboretum Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Arboretum Access (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Magma Pool (Meditation Fountain, Chozo Ruins)", (
                ("Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Meditation Fountain (Magma Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain (Meditation Fountain, Chozo Ruins)", (
                ("Door to Magma Pool (Meditation Fountain, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tower of Light (Tower of Light Access, Chozo Ruins)", (
                ("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", (
                ("Door to Tower of Light (Tower of Light Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Nursery (Save Station 1, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to North Atrium (Ruined Nursery, Chozo Ruins)", (
                ("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Nursery (North Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/y1qS7oPqynY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/y1qS7oPqynY?t=12', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}]}}]}}]}}]}}),
                ("Door to Ruined Nursery (Eyon Tunnel, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)", (
                ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Vault (Vault Access, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Vault Access (Vault, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", (
                ("Door to Vault (Vault Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Magma Pool (Training Chamber Access, Chozo Ruins)", (
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Training Chamber (Training Chamber Access, Chozo Ruins)", (
                ("Door to Magma Pool (Training Chamber Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)", (
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", (
                ("Front of Gate (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event9', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/tM_opp9ottU?t=9', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Arboretum Access (Arboretum, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Arboretum (Arboretum Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall Access (Arboretum, Chozo Ruins)", (
                ("Door to Arboretum Access (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Front of Gate (Arboretum, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to Arboretum (Gathering Hall Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Front of Gate (Arboretum, Chozo Ruins)", (
                ("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event9', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/tM_opp9ottU', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Open gate (Arboretum, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Event - Open gate (Arboretum, Chozo Ruins)", (
                ("Front of Gate (Arboretum, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Training Chamber Access (Magma Pool, Chozo Ruins)", (
                ("Door to Meditation Fountain (Magma Pool, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 70, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Standable terrain method: https://www.youtube.com/watch?v=eklXYB2qJ9E', 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 220, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}]}}]}}),
                ("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 60, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Magma Pool (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Meditation Fountain (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Use Grapple Beam'}, {'type': 'template', 'data': 'Heat-Resisting Suit'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/3JG613NSYcQ', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=2ezw9IFPJlY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/fVdrtd-aB0U', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage2', 'amount': 50, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 99, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Magma Pool (Meditation Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Heat-Resisting Suit'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'HeatDamage1', 'amount': 35, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'HeatRun', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Tower of Light Access (Tower of Light, Chozo Ruins)", (
                ("Door to Tower Chamber (Tower of Light, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3S7uWW56RKo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=YMk1EDV95h0', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 2, 'negate': False}}]}}]}}),
                ("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 36, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/2jyvwogPSDI', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/nm2qvbKNAIw', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bJHqj9OAxFo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/O_dTcT7p-fc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'RJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Tower of Light (Tower of Light Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Tower Chamber (Tower of Light, Chozo Ruins)", (
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tower of Light (Tower Chamber, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Wavebuster) (Tower of Light, Chozo Ruins)", (
                ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ruined Nursery (Save Station 1, Chozo Ruins)", (
                ("Save Station (Save Station 1, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station 1 (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 1, Chozo Ruins)", (
                ("Door to Ruined Nursery (Save Station 1, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ruined Nursery (North Atrium, Chozo Ruins)", (
                ("Door to Ruined Gallery (North Atrium, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to North Atrium (Ruined Nursery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Gallery (North Atrium, Chozo Ruins)", (
                ("Door to Ruined Nursery (North Atrium, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Vault Access (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Magmoor Caverns (Transport to Magmoor Caverns North, Chozo Ruins)", (
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins North, Magmoor Caverns)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", (
                ("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", (
                ("Door to Arboretum (Sunchamber Lobby, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", (
                ("Door to Arboretum (Gathering Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Arboretum (Gathering Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Tower of Light (Tower Chamber, Chozo Ruins)", (
                ("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Tower Chamber (Tower of Light, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)", (
                ("Door to Tower of Light (Tower Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to North Atrium (Ruined Gallery, Chozo Ruins)", (
                ("Door to Totem Access (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Map Station (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/u1g4iTohZHk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Ruined Gallery (North Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Totem Access (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Gallery (Totem Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Map Station (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Ruined Gallery (Map Station, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)", (
                ("Door to North Atrium (Ruined Gallery, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Sun Tower Access (Sun Tower, Chozo Ruins)", (
                ("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}]}}),
                ("Door to Sun Tower (Sun Tower Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event5', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/h2Ma9F4CYuA', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/A1MgdWHbUZ8', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 5, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 4, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 5, 'negate': False}}]}}]}}]}}]}}),
                ("Event - Unlock spider track (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event5', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}]}}),
                ("Door to Sun Tower (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Unlock spider track (Sun Tower, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/spZZY6E95ZU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'Damage', 'amount': 20, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'Roll down to the gap in the track and back up to trigger ghosts, skipping super missiles. This connection makes fighting Flaahgra without Spider Ball a dangerous action.', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/pEruOGbEteI', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'IUJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}]}}),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Hive Totem (Transport Access North, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", (
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}]}}),
                ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Access North, Chozo Ruins)", (
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Sunchamber (Sunchamber Access, Chozo Ruins)", (
                ("Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sunchamber Access (Sunchamber, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Lobby (Sunchamber Access, Chozo Ruins)", (
                ("Door to Sunchamber (Sunchamber Access, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': True}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event8', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Sunchamber Access (Sunchamber Lobby, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station 2 (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Gathering Hall (Gathering Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station 2 (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Gathering Hall (Save Station 2, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to East Atrium (Gathering Hall, Chozo Ruins)", (
                ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://clips.twitch.tv/ProductiveAbrasiveTurnipGingerPower', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Gathering Hall (East Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)", (
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Ruined Gallery (Totem Access, Chozo Ruins)", (
                ("Door to Hive Totem (Totem Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Totem Access (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hive Totem (Totem Access, Chozo Ruins)", (
                ("Door to Ruined Gallery (Totem Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Totem Access (Hive Totem, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Gallery (Map Station, Chozo Ruins)", (
                ("Map Station (Map Station, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Map Station (Ruined Gallery, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Map Station (Map Station, Chozo Ruins)", (
                ("Door to Ruined Gallery (Map Station, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Sunchamber (Sun Tower Access, Chozo Ruins)", (
                ("Door to Sun Tower (Sun Tower Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sun Tower (Sun Tower Access, Chozo Ruins)", (
                ("Door to Sunchamber (Sun Tower Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Totem Access (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event16', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3li4ZI5Vjn8', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/ILsjQYIJ64U', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 30, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'misc', 'name': 'dock_rando', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/jVDIATzTDHA', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}]}}),
                ("Event - Hive Mecha (Hive Totem, Chozo Ruins)", {'type': 'template', 'data': 'Shoot Power Beam'}),
                ("Door to Hive Totem (Totem Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Access North (Hive Totem, Chozo Ruins)", (
                ("Door to Totem Access (Hive Totem, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event54', 'amount': 1, 'negate': False}}]}}),
                ("Event - Hive Mecha (Hive Totem, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Event - Fallen Rubble (Hive Totem, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Hive Mecha (Hive Totem, Chozo Ruins)", (
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Fallen Rubble (Hive Totem, Chozo Ruins)", (
                ("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Sun Tower Access (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Before Fight (Back) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sunchamber (Sun Tower Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Sunchamber Access (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Sunchamber (Sunchamber Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Varia Suit) (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)", (
                ("Before Fight (Front) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Flaahgra (Sunchamber, Chozo Ruins)", (
                ("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", (
                ("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Before Fight (Front) (Sunchamber, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event8', 'amount': 1, 'negate': False}}]}}),
                ("Door to Sunchamber Access (Sunchamber, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event8', 'amount': 1, 'negate': False}}),
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Requirements for destroying the bomb slots', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'Requirements for getting to the bomb slots', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 10, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'Requirements for shooting the first dish', 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Any Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Wavebuster', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 230, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event6', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Before Fight (Back) (Sunchamber, Chozo Ruins)", (
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': 'Flahgra can be defeated without shooting the first dish if coming from Sun Tower Access and before starting the fight', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'Requirements for destroying the bomb slots', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 4, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': 'Requirements for getting to the center island', 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", (
                ("Door to Watery Hall (Watery Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Watery Hall Access (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall (Watery Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)", (
                ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Gathering Hall (Save Station 2, Chozo Ruins)", (
                ("Save Station (Save Station 2, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station 2 (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 2, Chozo Ruins)", (
                ("Door to Gathering Hall (Save Station 2, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Gathering Hall (East Atrium, Chozo Ruins)", (
                ("Door to Energy Core Access (East Atrium, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Energy Core Access (East Atrium, Chozo Ruins)", (
                ("Door to Gathering Hall (East Atrium, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Atrium (Energy Core Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Dynamo Access (Watery Hall, Chozo Ruins)", (
                ("Behind Gate (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Watery Hall (Dynamo Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Watery Hall Access (Watery Hall, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 57, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 25, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 15, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/Jla-gYSErGc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': True}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'misc', 'name': 'NoGravity', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'UnderwaterMovement', 'amount': 1, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/HDYJkv3MUVI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 65, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 20, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Event - Open gate (Watery Hall, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Behind Gate (Watery Hall, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event10', 'amount': 1, 'negate': False}}),
                ("Door to Watery Hall (Watery Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Charge Beam) (Watery Hall, Chozo Ruins)", (
                ("Behind Gate (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event7', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 42, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'GravitySuit', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'damage', 'name': 'RuinsWater', 'amount': 25, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Event - Open gate (Watery Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Behind Gate (Watery Hall, Chozo Ruins)", (
                ("Door to Dynamo Access (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/bh18bp4makg', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'OoB', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://www.youtube.com/watch?v=LdBFCaOFDE4', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 4, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event10', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 1, 'negate': False}}]}}]}}),
                ("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Energy Core (Energy Core Access, Chozo Ruins)", (
                ("Door to East Atrium (Energy Core Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to East Atrium (Energy Core Access, Chozo Ruins)", (
                ("Door to Energy Core (Energy Core Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Energy Core Access (East Atrium, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Watery Hall (Dynamo Access, Chozo Ruins)", (
                ("Door to Dynamo (Dynamo Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Dynamo Access (Watery Hall, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Dynamo (Dynamo Access, Chozo Ruins)", (
                ("Door to Watery Hall (Dynamo Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to West Furnace Access (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Energy Core (West Furnace Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Energy Core Access (Energy Core, Chozo Ruins)", (
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Door to West Furnace Access (Energy Core, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event3', 'amount': 1, 'negate': False}}),
                ("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}]}}),
                ("Door to Energy Core (Energy Core Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", (
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Dynamo Access (Dynamo, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Missile', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Any Beam'}]}}),
                ("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Dynamo (Dynamo Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Dynamo, Chozo Ruins)", (
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)", (
                ("Door to Dynamo Access (Dynamo, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Burn Dome (Burn Dome Access, Chozo Ruins)", (
                ("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/8fd9Yppb8FI', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Spawn Point (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
            )
            ),
            (
            "Door to Energy Core (West Furnace Access, Chozo Ruins)", (
                ("Door to Furnace (West Furnace Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Furnace Access (Energy Core, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Furnace (West Furnace Access, Chozo Ruins)", (
                ("Door to Energy Core (West Furnace Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burn Dome Access (Burn Dome, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Before Fight (Burn Dome, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)", (
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)", (
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event39', 'amount': 1, 'negate': False}}),
                ("Before Fight (Burn Dome, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Incinerator Drone (Burn Dome, Chozo Ruins)", (
                ("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Before Fight (Burn Dome, Chozo Ruins)", (
                ("Event - Incinerator Drone (Burn Dome, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}),
            )
            ),
            (
            "Door to East Furnace Access (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Furnace (East Furnace Access, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to West Furnace Access (Furnace, Chozo Ruins)", (
                ("Pickup (Energy Tank) (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}]}}),
                ("Under Spider Track (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Door to Furnace (West Furnace Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Furnace, Chozo Ruins)", (
                ("Under Spider Track (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Pickup (Energy Tank) (Furnace, Chozo Ruins)", (
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'Wall Boost - https://youtu.be/a6_Dsl3YoDY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Under Spider Track (Furnace, Chozo Ruins)", (
                ("Door to East Furnace Access (Furnace, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}),
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}),
                ("Pickup (Missile Expansion) (Furnace, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/BmQavi7dXuw', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/pgnVJwrKkq4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/PBLQI6B9CMo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/WHfsu7MQJzo', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", (
                ("Door to Furnace (East Furnace Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Furnace (East Furnace Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to East Furnace Access (Furnace, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway (Crossway Access West, Chozo Ruins)", (
                ("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/vNNsjns1HzM?t=23', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/vNNsjns1HzM?t=2', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", (
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hall of the Elders (East Furnace Access, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event44', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'ClipThruObjects', 'amount': 3, 'negate': False}}]}}]}}),
                ("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event14', 'amount': 1, 'negate': False}}]}}),
            )
            ),
            (
            "Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", (
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", (
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}]}}),
                ("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event14', 'amount': 1, 'negate': False}}, {'type': 'template', 'data': 'Shoot Ice Beam'}]}}),
                ("Event - Statue Moved (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Plasma Beam'}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event14', 'amount': 1, 'negate': False}}]}}),
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Wave Beam'}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event14', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}]}}]}}),
            )
            ),
            (
            "Event - Statue Moved (Hall of the Elders, Chozo Ruins)", (
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Room Center (Hall of the Elders, Chozo Ruins)", (
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}]}}),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", {'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}),
                ("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event44', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 2, 'negate': False}}]}}]}}),
                ("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/rbZwkpF8UIo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 5, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}]}}),
                ("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Power Beam'}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Charge', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Combat', 'amount': 1, 'negate': False}}]}}]}}),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 4, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event15', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 1, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=e-3y7ykkEwU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'IUJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 3, 'negate': False}}]}}]}}]}}]}}]}}]}}]}}),
            )
            ),
            (
            "Behind Barrier (Hall of the Elders, Chozo Ruins)", (
                ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event48', 'amount': 1, 'negate': False}}]}}),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=_GG9XoOsDos', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event15', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/lOQVD6oRwGU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': 'https://www.youtube.com/watch?v=3tb2eY1zUWc', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}]}}]}}]}}]}}]}}),
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event15', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/3tb2eY1zUWc', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/lOQVD6oRwGU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
                ("Room Center (Hall of the Elders, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event15', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/lOQVD6oRwGU', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 1, 'negate': False}}]}}]}}]}}]}}),
            )
            ),
            (
            "Door to Crossway Access South (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Crossway (Crossway Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Crossway Access West (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access South (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=ykuj3JfVb_4', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}]}}]}}),
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Elder Hall Access (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Pickup (Missile Expansion) (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'events', 'name': 'Event13', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/L5NhPyLZIeQ', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Spider', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 2, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/_l8o8V3lkaY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'LJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': 'https://youtu.be/5_MnKo9X_-0', 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=rdTVYzudgrY', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://www.youtube.com/watch?v=xyJMJhYt81Q', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BJ', 'amount': 3, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Dash', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Event - Activate Bomb Slots (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'template', 'data': 'Shoot Super Missile'}, {'type': 'resource', 'data': {'type': 'items', 'name': 'Scan', 'amount': 1, 'negate': False}}]}}),
                ("Door to Crossway (Elder Hall Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Event - Activate Bomb Slots (Crossway, Chozo Ruins)", (
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Reflecting Pool Access, Chozo Ruins)", (
                ("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", (
                ("Door to Crossway (Elder Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Crossway (Elder Hall Access, Chozo Ruins)", (
                ("Door to Hall of the Elders (Elder Hall Access, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Crossway (Crossway Access South, Chozo Ruins)", (
                ("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Crossway Access South (Crossway, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}]}}),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", (
                ("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)", (
                ("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", (
                ("Door to Transport Access South (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool (Save Station 3, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport Access South (Reflecting Pool, Chozo Ruins)", (
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool (Transport Access South, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", (
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'events', 'name': 'Event4', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': 'https://youtu.be/rPgTD35efHo', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}]}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'tricks', 'name': 'CBJ', 'amount': 4, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'BSJ', 'amount': 4, 'negate': False}}]}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 3, 'negate': False}}]}}]}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/NRtv6aOpssk', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'SJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 1, 'negate': False}}]}}]}}),
                ("Event - Drain water (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'PowerBomb', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Knowledge', 'amount': 1, 'negate': False}}]}}]}}]}}),
                ("Door to Reflecting Pool (Reflecting Pool Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Antechamber (Reflecting Pool, Chozo Ruins)", (
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Reflecting Pool (Antechamber, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Event - Drain water (Reflecting Pool, Chozo Ruins)", (
                ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Reflecting Pool (Save Station 3, Chozo Ruins)", (
                ("Save Station (Save Station 3, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", (
                ("Save Station (Save Station 3, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/AFDSEx16464?t=27', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 4, 'negate': False}}]}}]}}]}}),
                ("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 3, Chozo Ruins)", (
                ("Door to Reflecting Pool (Save Station 3, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'MorphBall', 'amount': 1, 'negate': False}}, {'type': 'or', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Bombs', 'amount': 1, 'negate': False}}, {'type': 'and', 'data': {'comment': None, 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'SpaceJump', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Standable', 'amount': 2, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'Movement', 'amount': 3, 'negate': False}}]}}, {'type': 'and', 'data': {'comment': 'https://youtu.be/AFDSEx16464', 'items': [{'type': 'resource', 'data': {'type': 'items', 'name': 'Boost', 'amount': 1, 'negate': False}}, {'type': 'resource', 'data': {'type': 'tricks', 'name': 'WallBoost', 'amount': 5, 'negate': False}}]}}]}}]}}),
            )
            ),
            (
            "Door to Reflecting Pool (Transport Access South, Chozo Ruins)", (
                ("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Access South (Reflecting Pool, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", (
                ("Door to Reflecting Pool (Transport Access South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Reflecting Pool (Antechamber, Chozo Ruins)", (
                ("Pickup (Ice Beam) (Antechamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Ice Beam) (Antechamber, Chozo Ruins)", (
                ("Door to Reflecting Pool (Antechamber, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
            )
            ),
            (
            "Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld East, Chozo Ruins)", (
                ("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins East, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", (
                ("Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Door to Transport to Tallon Overworld South (Transport Access South, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Teleporter to Tallon Overworld (Transport to Tallon Overworld South, Chozo Ruins)", (
                ("Door to Transport Access South (Transport to Tallon Overworld South, Chozo Ruins)", {'type': 'and', 'data': {'comment': None, 'items': []}}),
                ("Teleporter to Chozo Ruins (Transport to Chozo Ruins South, Tallon Overworld)", dock_requirements['Teleporter']),
            )
            ),
            (
            "Event - Credits (Credits, End of Game)", (
            )
            ),
    ))
    print("rules end!")