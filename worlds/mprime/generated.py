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
    multiworld = self.multiworld
    player = self.player
    options = self.options
    from . import logic

    # from ast import BoolOp as BO, And as A, Constant as Co, Or as O, Name as N, Load as Lo, Attribute as At, Call as C, Subscript as S, Expression as E, arguments as ags, arg as a, Lambda as L
    from ast import And, Or, Not, Load
    from typing import Any
    from ast import BoolOp as BoolOp_
    def BoolOp(*args, **kwargs): return BoolOp_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import UnaryOp as UnaryOp_
    def UnaryOp(*args, **kwargs): return UnaryOp_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Constant as Constant_
    def Constant(*args, **kwargs): return Constant_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Name as Name_
    def Name(*args, **kwargs): return Name_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Attribute as Attribute_
    def Attribute(*args, **kwargs): return Attribute_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Call as Call_
    def Call(*args, **kwargs): return Call_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Subscript as Subscript_
    def Subscript(*args, **kwargs): return Subscript_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Expression as Expression_
    def Expression(*args, **kwargs): return Expression_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import arg as arg_
    def arg(*args, **kwargs): return arg_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Lambda as Lambda_
    def Lambda(*args, **kwargs): return Lambda_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import Compare as Compare_
    def Compare(*args, **kwargs): return Compare_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import GtE as GtE_
    def GtE(*args, **kwargs): return GtE_(*args, **kwargs, lineno=0, col_offset=0, end_lineno=0, end_col_offset=0)
    from ast import arguments as arguments_
    def arguments(*args, **kwargs): return arguments_(*args, **kwargs, kwonlyargs=[], kw_defaults=[], defaults=[])
    
    def s_has(item_name: str):
        return Call(Attribute(Name("state", Load()), "has", Load()), [Constant(item_name), Name("player", Load())], [])
    
    def s_gte(item_name: str, at_least: int):
        return Compare(Call(Attribute(Name("state", Load()), "count", Load()), [Constant(item_name), Name('player', Load())], []), [GtE()], [Constant(at_least)])

    def a(objs):
        return BoolOp(And(), [objs])
    
    def o(objs):
        return BoolOp(Or(), [objs])
    
     
    def e(b):
        import astvalidate
        # import ast
        # print(ast.dump(b, False))
        token = Expression(Lambda(arguments([], [arg('state')]), b), )
        # astvalidate.validate(token)
        nonlocal options
        nonlocal player
        nonlocal templates
        nonlocal logic
        # print(locals())
        return eval(compile(token, '<generated>', 'eval'), locals())

    templates: ConnectionDict = {
        "Shoot Super Missile": lambda state: (state.has('Power Beam', player) and logic.has_missiles(state, player, 5) and state.has('Charge Beam', player) and state.has('Super Missile', player) and templates['Can Use Arm Cannon'](state)),
        "Have all Beams": lambda state: (state.has('Power Beam', player) and state.has('Wave Beam', player) and state.has('Ice Beam', player) and state.has('Plasma Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Heat-Resisting Suit": lambda state: (state.has('Gravity Suit', player) or state.has('Varia Suit', player) or state.has('Phazon Suit', player)),
        "Can Use Arm Cannon": lambda state: (state.has('Combat Visor', player) or state.has('Thermal Visor', player) or state.has('X-Ray Visor', player)),
        "Shoot Any Beam": lambda state: (templates['Can Use Arm Cannon'](state) and (state.has('Power Beam', player) or state.has('Wave Beam', player) or state.has('Ice Beam', player) or state.has('Plasma Beam', player))),
        "Shoot Power Beam": lambda state: (state.has('Power Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Shoot Wave Beam": lambda state: (state.has('Wave Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Shoot Ice Beam": lambda state: (state.has('Ice Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Shoot Plasma Beam": lambda state: (state.has('Plasma Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Use Grapple Beam": lambda state: (state.has('Grapple Beam', player) and templates['Can Use Arm Cannon'](state)),
        "Open Normal Door": lambda state: (templates['Shoot Any Beam'](state) or (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player) and state.has('Scan Visor', player))),
        "Move Past Scatter Bombu": e(BoolOp(Or(), [Constant(True) if (options.movement.value >= 2) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('Damage')], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(12), Constant('Damage')], []) if (options.movement.value >= 1) else Constant(False)])),
    }
    dock_requirements: ConnectionDict = {
        "Normal Door": templates['Open Normal Door'],
        "Normal Door (Forced)": templates['Open Normal Door'],
        "Ice Door": templates['Shoot Ice Beam'],
        "Wave Door": templates['Shoot Wave Beam'],
        "Plasma Door": templates['Shoot Plasma Beam'],
        "Missile Blast Shield": lambda state: (logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state)),
        "Missile Blast Shield (randomprime)": lambda state: (logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state)),
        "Circular Door": templates['Open Normal Door'],
        "Square Door": None,
        "Super Missile Blast Shield": (templates['Open Normal Door']) and (templates['Shoot Super Missile']),
        "Power Bomb Blast Shield": (templates['Open Normal Door']) and (lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
        "Wavebuster Blast Shield": (templates['Shoot Wave Beam']) and (lambda state: (state.has('Charge Beam', player) and logic.has_missiles(state, player, 11) and state.has('Wavebuster', player) and templates['Shoot Wave Beam'](state))),
        "Ice Spreader Blast Shield": (templates['Shoot Ice Beam']) and (lambda state: (state.has('Charge Beam', player) and logic.has_missiles(state, player, 10) and state.has('Ice Spreader', player) and templates['Shoot Ice Beam'](state))),
        "Flamethrower Blast Shield": (templates['Shoot Plasma Beam']) and (lambda state: (state.has('Charge Beam', player) and logic.has_missiles(state, player, 10) and state.has('Flamethrower', player) and templates['Shoot Plasma Beam'](state))),
        "Charge Beam Blast Shield": (templates['Open Normal Door']) and (lambda state: (templates['Shoot Any Beam'](state) and state.has('Charge Beam', player))),
        "Bomb Blast Shield": (templates['Open Normal Door']) and (lambda state: (templates['Open Normal Door'](state) and state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
        "Morph Ball Door": lambda state: (state.has('Morph Ball', player) and (state.has('Power Beam', player) or state.has('Ice Beam', player) or state.has('Wave Beam', player) or state.has('Plasma Beam', player)) and (state.has('Combat Visor', player) or state.has('Thermal Visor', player) or state.has('X-Ray Visor', player) or state.has('Scan Visor', player))),
        "Open Passage": lambda state: ((state.has('Power Beam', player) or state.has('Ice Beam', player) or state.has('Wave Beam', player) or state.has('Plasma Beam', player)) and (state.has('Combat Visor', player) or state.has('Thermal Visor', player) or state.has('X-Ray Visor', player))),
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
                ("Door to Crater Tunnel B (Phazon Core, Impact Crater)", e(BoolOp(Or(), [Constant(True) if ((options.scan_dash.value >= 4 and options.standable_terrain.value >= 4 and options.jump_off_enemies.value >= 5)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 5) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]))),
                ("Door to Phazon Core (Crater Missile Station, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Crater Tunnel A (Phazon Core, Impact Crater)", (
                ("Door to Crater Missile Station (Phazon Core, Impact Crater)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4 and options.complex_bomb_jump.value >= 5 and options.slope_jump.value >= 3 and options.standable_terrain.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.l_jump.value >= 4 and options.standable_terrain.value >= 4 and options.scan_dash.value >= 4 and options.slope_jump.value >= 4) else Constant(False)]))),
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
                ("Door to Phazon Core (Crater Tunnel B, Impact Crater)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(5), Constant('Damage')], [])]) if (options.movement.value >= 1) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('Damage')], []) if (options.bomb_jump.value >= 1 and options.movement.value >= 1) else Constant(False)])])]))),
                ("Door to Crater Tunnel B (Phazon Infusion Chamber, Impact Crater)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Phazon Core (Crater Tunnel B, Impact Crater)", (
                ("Door to Phazon Infusion Chamber (Crater Tunnel B, Impact Crater)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(5), Constant('Damage')], [])]) if (options.movement.value >= 1) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('Damage')], []) if (options.bomb_jump.value >= 1 and options.movement.value >= 1) else Constant(False)])])]))),
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
                ("Dock to Subchamber Two (Subchamber One, Impact Crater)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flamethrower'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(25)], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]) if (options.combat.value >= 2 and options.knowledge.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(54), Constant('Damage')], [])]))),
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
                ("Dock to Subchamber Three (Subchamber Two, Impact Crater)", e(BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(25)], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flamethrower'), Name('player', Load())], [])]) if (options.combat.value >= 2 and options.knowledge.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(76), Constant('Damage')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(119), Constant('Damage')], [])]))),
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
                ("Dock to Subchamber Four (Subchamber Three, Impact Crater)", e(BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(25)], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flamethrower'), Name('player', Load())], [])]) if (options.combat.value >= 2 and options.knowledge.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(76), Constant('Damage')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(179), Constant('Damage')], [])]))),
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
                ("Dock to Subchamber Five (Subchamber Four, Impact Crater)", e(BoolOp(And(), [Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Have all Beams'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []) if (options.combat.value >= 3) else Constant(False)]), BoolOp(And(), [Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('Damage')], [])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(239), Constant('Damage')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(149), Constant('Damage')], []) if (options.combat.value >= 1) else Constant(False)])])]))),
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
                ("Teleporter to Credits (Metroid Prime Lair, Impact Crater)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 3) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 3) else BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(5)], [])])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 5) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(299), Constant('Damage')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('Damage')], []) if (options.combat.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(149), Constant('Damage')], []) if (options.combat.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('Damage')], []) if (options.combat.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(249), Constant('Damage')], []) if (options.combat.value >= 1) else Constant(False)])]))),
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
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (state.has('Charge Beam', player) or logic.has_missiles(state, player, 3)))),
                ("Door to Shoreline Entrance (Transport to Magmoor Caverns West, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", (
                ("Door to Transport to Magmoor Caverns West (Shoreline Entrance, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (state.has('Charge Beam', player) or logic.has_missiles(state, player, 3)))),
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", e(BoolOp(Or(), [Constant(True) if ((options.scan_dash.value >= 4)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 3) else Constant(False)]))),
                ("Door to Save Station B (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4) else Constant(False)]))),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player) and logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state))),
                ("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)", templates['Shoot Plasma Beam']),
                ("Door to Phendrana Shorelines (Shoreline Entrance, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", (
                ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", lambda state: (templates['Shoot Super Missile'](state) and state.has('Scan Visor', player) and state.has('Morph Ball', player) and state.has('Spider Ball', player))),
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
                ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 2) else Constant(False))),
                ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Super Missile'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], []))]) if (options.single_room_oob.value >= 3 and options.standable_terrain.value >= 3 and options.scan_dash.value >= 2 and options.movement.value >= 3) else Constant(False))),
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
                ("Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (state.has('Plasma Beam', player) or logic.has_missiles(state, player, 1) or (state.has('Charge Beam', player) and (state.has('Power Beam', player) or state.has('Wave Beam', player)))) and templates['Move Past Scatter Bombu'](state))),
                ("Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Temple Entryway, Phendrana Drifts)", (
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (logic.has_missiles(state, player, 1) or state.has('Plasma Beam', player) or (state.has('Charge Beam', player) and (state.has('Power Beam', player) or state.has('Wave Beam', player)))) and templates['Move Past Scatter Bombu'](state))),
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
                ("Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (state.has('Charge Beam', player) or state.has('Plasma Beam', player) or logic.has_missiles(state, player, 1)) and templates['Move Past Scatter Bombu'](state))),
                ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Phendrana Shorelines (Ice Ruins Access, Phendrana Drifts)", (
                ("Door to Ice Ruins East (Ice Ruins Access, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and (state.has('Charge Beam', player) or logic.has_missiles(state, player, 1) or state.has('Plasma Beam', player)) and templates['Move Past Scatter Bombu'](state))),
                ("Door to Ice Ruins Access (Phendrana Shorelines, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Temple Entryway (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('Damage')], []) if (options.jump_off_enemies.value >= 3 and options.movement.value >= 3 and options.scan_dash.value >= 4 and options.l_jump.value >= 2) else Constant(False)])]))),
                ("Door to Chozo Ice Temple (Temple Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", (
                ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", lambda state: state.has('Chozo Ice Temple Bomb Slot', player)),
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
                ("Door to Chapel Tunnel (Chozo Ice Temple, Phendrana Drifts)", lambda state: (state.has('Chozo Ice Temple Bomb Slot', player))),
                ("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo Ice Temple Bomb Slot'), Name('player', Load())], [])) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo Ice Temple Bomb Slot'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.l_jump.value >= 2) else Constant(False)])]))),
                ("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player) and logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state) and state.has('Morph Ball Bomb', player))),
            )
            ),
            (
            "Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 3) else Constant(False)]))),
                ("Door to Canyon Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.l_jump.value >= 1) else Constant(False), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.scan_dash.value >= 1) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.slope_jump.value >= 1) else BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('Damage')], [])]) if (options.jump_off_enemies.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], []) if (options.jump_off_enemies.value >= 2) else Constant(False)])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('Damage')], [])]) if (options.jump_off_enemies.value >= 5 and options.l_jump.value >= 1 and options.damage_boosting.value >= 3) else Constant(False)]))),
                ("Door to Ice Ruins West (Ruins Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", lambda state: state.has('Space Jump Boots', player)),
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
                ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)", (
                ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)", None),
                ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])) if (options.scan_dash.value >= 1) else Constant(False)]))),
                ("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Constant(True) if ((options.standable_terrain.value >= 1 or options.l_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])) if (options.scan_dash.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 1) else Constant(False)])])]))),
            )
            ),
            (
            "Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)", (
                ("Door to Plaza Walkway (Ice Ruins East, Phendrana Drifts)", None),
                ("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 4) else Constant(False)])]))),
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
                ("Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Chozo Ice Temple (Chapel Tunnel, Phendrana Drifts)", (
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
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
                ("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(25)], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.combat.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(17)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.combat.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Damage')], [])]) if (options.combat.value >= 3) else Constant(False)]))),
                ("Door to Chapel of the Elders (Chapel Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)", (
                ("Door to Chapel Tunnel (Chapel of the Elders, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
            )
            ),
            (
            "Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False)])]))),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if ((options.standable_terrain.value >= 2 or options.r_jump.value >= 2)) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.bomb_jump.value >= 3 and options.scan_dash.value >= 3 and options.standable_terrain.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False)])])]))),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.bomb_jump.value >= 3 and options.scan_dash.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if ((options.standable_terrain.value >= 2 or options.r_jump.value >= 2)) else Constant(False)]))),
                ("Door to Ruined Courtyard (Courtyard Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("Door to Ruined Courtyard (Save Station A, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)", e(Constant(True) if ((options.l_jump.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []))),
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
                ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)", e(Constant(True) if ((options.l_jump.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []))),
                ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Super Missile'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]))),
                ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []) if (options.movement.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "Front of Tunnel (Ruined Courtyard, Phendrana Drifts)", (
                ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)", None),
                ("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]))),
            )
            ),
            (
            "Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", (
                ("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.movement.value >= 4) else Constant(False)]))),
                ("Door to Phendrana Canyon (Canyon Entryway, Phendrana Drifts)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)", (
                ("Door to Canyon Entryway (Phendrana Canyon, Phendrana Drifts)", e(Constant(True) if (options.scan_dash.value >= 2 or (options.standable_terrain.value >= 1)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])])]))),
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
                ("Door to Map Station (Research Entrance, Phendrana Drifts)", e(BoolOp(And(), [Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])])]) if (options.combat.value >= 2) else Constant(False)])]))),
                ("Door to Research Entrance (Specimen Storage, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Map Station (Research Entrance, Phendrana Drifts)", (
                ("Door to Specimen Storage (Research Entrance, Phendrana Drifts)", e(BoolOp(And(), [Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])])]) if (options.combat.value >= 2) else Constant(False)])]))),
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
                ("Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Quarantine Access (North Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 5 and options.r_jump.value >= 3 and options.standable_terrain.value >= 3) else Constant(False))),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.scan_dash.value >= 2 and options.knowledge.value >= 2) else Constant(False))),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
                ("Door to Quarantine Cave (North Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.l_jump.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.r_jump.value >= 4) else Constant(False)])]))),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", None),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", (
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.l_jump.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.r_jump.value >= 4 and options.standable_terrain.value >= 3) else Constant(False)])]))),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", lambda state: state.has('Morph Ball', player)),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thardus'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 3) else Constant(False)])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('Damage')], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thardus'), Name('player', Load())], []))]) if (options.jump_off_enemies.value >= 5) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.damage_boosting.value >= 4) else Constant(False)]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.standable_terrain.value >= 2 and options.l_jump.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), Constant(True) if (options.knowledge.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thardus'), Name('player', Load())], [])])]))),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.movement.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])])]))),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.slope_jump.value >= 4) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []) if (options.movement.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.standable_terrain.value >= 4 and options.scan_dash.value >= 4) else Constant(False)]), Constant(True) if ((options.knowledge.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thardus'), Name('player', Load())], [])])])]))),
                ("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)", lambda state: (state.has('Thardus', player))),
                ("Fight Trigger (Quarantine Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Fight Trigger (Quarantine Cave, Phendrana Drifts)", (
                ("Event - Thardus (Quarantine Cave, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [BoolOp(Or(), [Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.combat.value >= 1) else Constant(False)]), BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Combat Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 5) else Constant(False), BoolOp(And(), [Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]) if (options.invisible_objects.value >= 4 and options.combat.value >= 2) else Constant(False)])])]), BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Beam'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Wave Beam'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(And(), [Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]) if (options.combat.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(80)], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(5)], []) if (options.combat.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(40)], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]) if (options.combat.value >= 2) else Constant(False)])])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])])])]))),
                ("Room Center (Quarantine Cave, Phendrana Drifts)", lambda state: (state.has('Thardus', player))),
            )
            ),
            (
            "Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", lambda state: state.has('Research Lab Hydra Barrier', player)),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", lambda state: state.has('Scan Visor', player)),
                ("Door to Research Lab Hydra (Hydra Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)", (
                ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)", lambda state: state.has('Research Lab Hydra Barrier', player)),
                ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player) and logic.has_misc(state, player, 'backwards_labs'))),
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
                ("Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (South Quarantine Tunnel, Phendrana Drifts)", (
                ("Door to Quarantine Cave (South Quarantine Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", (
                ("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)", (
                ("Morph Ball Door to Quarantine Cave (Quarantine Monitor, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)", (
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 4) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_space_jump.value >= 3 and options.standable_terrain.value >= 3 and options.l_jump.value >= 1) else Constant(False)])]))),
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
                ("Door to Save Station D (Observatory, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.r_jump.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Observatory Activated'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)])]))),
                ("Event - Observatory Activated (Observatory, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], []))]), Constant(True) if ((options.bomb_jump.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
                ("Door to Observatory (Observatory Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Observatory Activated'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", e(
                    BoolOp(Or(), [
                        Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Observatory Activated'), Name('player', Load())], []),
                        Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])
                            if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 2)
                            else Constant(False),
                        BoolOp(And(), [
                            Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []),
                            Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []),
                            Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])
                        ])
                            if (options.complex_bomb_jump.value >= 4 and options.scan_dash.value >= 3 and options.standable_terrain.value >= 4)
                            else Constant(False)
                    ])
                )),
                ("Door to Observatory (West Tower Entrance, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Save Station D (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Observatory Activated'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Pickup (Super Missile) (Observatory, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Observatory Activated'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.bomb_space_jump.value >= 3 and options.standable_terrain.value >= 3 and options.l_jump.value >= 2) else Constant(False)]))),
                ("Door to Observatory (Save Station D, Phendrana Drifts)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Event - Observatory Activated (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda state: (state.has('Space Jump Boots', player))),
            )
            ),
            (
            "Pickup (Super Missile) (Observatory, Phendrana Drifts)", (
                ("Door to Observatory Access (Observatory, Phendrana Drifts)", None),
                ("Door to West Tower Entrance (Observatory, Phendrana Drifts)", lambda state: (state.has('Observatory Activated', player))),
                ("Door to Save Station D (Observatory, Phendrana Drifts)", lambda state: (state.has('Observatory Activated', player))),
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
                ("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.clip_through_objects.value >= 3 and options.standable_terrain.value >= 3 and options.single_room_oob.value >= 5 and options.jump_off_enemies.value >= 5) else Constant(False)]))),
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
                ("Door to Transport Access (Frozen Pike, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 2) else Constant(False)])])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4) else Constant(False)]))),
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
                ("Door to Pike Access (Frozen Pike, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 2 and options.bomb_jump.value >= 3) else Constant(False), BoolOp(Or(), [BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Chamber Item (Lower)'), Name('player', Load())], [])), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Chamber Item (Lower)'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])])]) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 3 and options.scan_dash.value >= 4) else Constant(False)]))),
                ("Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)])]), BoolOp(Or(), [BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2) else Constant(False)])]))),
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave Access (Frozen Pike, Phendrana Drifts)", (
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4) else Constant(False), Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])]))),
                ("Door to Frozen Pike (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to West Tower Entrance (West Tower, Phendrana Drifts)", (
                ("Door to Control Tower (West Tower, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player))),
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
                ("Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", lambda state: state.has('Morph Ball', player)),
                ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Frost Cave Access, Phendrana Drifts)", (
                ("Door to Frozen Pike (Frost Cave Access, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.single_room_oob.value >= 3) else Constant(False)]))),
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
                ("Room Center (Control Tower, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_space_jump.value >= 1) else Constant(False)]))),
                ("Fight Trigger (Control Tower, Phendrana Drifts)", None),
                ("Door to Control Tower (West Tower, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Control Tower Tower'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 2) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 3 and options.single_room_oob.value >= 3) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and (options.single_room_oob.value >= 3 or (options.standable_terrain.value >= 2 and options.single_room_oob.value >= 2))) else Constant(False)]))),
                ("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)", lambda state: (templates['Shoot Any Beam'](state) and logic.has_missiles(state, player, 1))),
            )
            ),
            (
            "Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", e(BoolOp(Or(), [Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
            )
            ),
            (
            "Room Center (Control Tower, Phendrana Drifts)", (
                ("Door to East Tower (Control Tower, Phendrana Drifts)", None),
                ("Door to West Tower (Control Tower, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Control Tower Fight'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.wall_boost.value >= 2) else Constant(False)])]))),
                ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Control Tower Tower'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5 and options.standable_terrain.value >= 3 and options.single_room_oob.value >= 4 and (options.bomb_jump.value >= 1 or options.slope_jump.value >= 1)) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.single_room_oob.value >= 2 and options.standable_terrain.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4) else Constant(False)])]))),
                ("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 1 and options.standable_terrain.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False)])]))),
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
                ("Room Center (Control Tower, Phendrana Drifts)", lambda state: (state.has('Control Tower Fight', player) or state.has('Research Core Power Outage', player))),
                ("Event - Control Tower Fight (Control Tower, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Control Tower Fight'), Name('player', Load())], []))]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], [])]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Damage')], [])]))),
            )
            ),
            (
            "Event - Control Tower Fight (Control Tower, Phendrana Drifts)", (
                ("Room Center (Control Tower, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Pike Access (Research Core, Phendrana Drifts)", (
                ("Door to Research Core Access (Research Core, Phendrana Drifts)", e(BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], [])), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Research Core Power Outage'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])])]))),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player))),
                ("Door to Research Core (Pike Access, Phendrana Drifts)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Core, Phendrana Drifts)", (
                ("Door to Pike Access (Research Core, Phendrana Drifts)", None),
                ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player))),
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
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
                ("Event - Ice Broken (Frost Cave, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.slope_jump.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])]) if (options.jump_off_enemies.value >= 3) else Constant(False)])]))),
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
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False)])]))),
            )
            ),
            (
            "Frost Cave Floor (Frost Cave, Phendrana Drifts)", (
                ("Door to Save Station C (Frost Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.slope_jump.value >= 2) else BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False)]))),
                ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []) if (options.slope_jump.value >= 2 and options.l_jump.value >= 2) else Constant(False)]))),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 2 or options.l_jump.value >= 2)) else BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False)]))),
                ("Pickup (Missile) (Frost Cave, Phendrana Drifts)", lambda state: state.has('Frost Cave Ice Floor', player)),
            )
            ),
            (
            "Event - Ice Broken (Frost Cave, Phendrana Drifts)", (
                ("Frost Cave Floor (Frost Cave, Phendrana Drifts)", None),
            )
            ),
            (
            "Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False), Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2) or options.l_jump.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])]))),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", None),
                ("Door to Hunter Cave (Hunter Cave Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", (
                ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.slope_jump.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (((options.scan_dash.value >= 2) or (options.r_jump.value >= 3) or ((options.r_jump.value >= 2 and options.movement.value >= 2)))) else Constant(False)]))),
                ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]) if (options.slope_jump.value >= 3) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(3)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.l_jump.value >= 2 and options.slope_jump.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1 and options.l_jump.value >= 2) else Constant(False)])])]))),
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
                ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False)])]))),
                ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)", e(Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2) else Constant(False))),
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
                ("Door to Aether Lab Entryway (East Tower, Phendrana Drifts)", lambda state: (state.has('Scan Visor', player))),
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
                ("Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Frost Cave (Upper Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Hunter Cave (Lower Edge Tunnel, Phendrana Drifts)", (
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
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
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]) if (options.knowledge.value >= 1) else Constant(False), Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []) if (options.knowledge.value >= 1) else Constant(False)]))),
                ("Door to Research Lab Aether (Aether Lab Entryway, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", (
                ("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)", lambda state: ((templates['Shoot Any Beam'](state) and logic.has_missiles(state, player, 1)) or (state.has('Morph Ball', player) and state.has('Power Bomb', player)))),
                ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)", e(BoolOp(Or(), [Constant(True) if ((options.standable_terrain.value >= 2 and options.l_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False)]))),
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
                ("Door to Aether Lab Entryway (Research Lab Aether, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]))),
                ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)", None),
                ("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Constant(True) if ((options.standable_terrain.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
            )
            ),
            (
            "Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4) else Constant(False), Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.slope_jump.value >= 2 and options.wall_boost.value >= 2 and options.gravityless_underwater_movement.value >= 3) else Constant(False)])]))),
                ("Door to Phendrana's Edge (Lower Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Lower Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", None),
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.standable_terrain.value >= 2)) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []) if (options.bomb_jump.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5 and options.scan_dash.value >= 5 and options.standable_terrain.value >= 4 and options.bomb_jump.value >= 4) else Constant(False)])])]))),
                ("Door to Phendrana's Edge (Upper Edge Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", e(Constant(True) if (options.clip_through_objects.value >= 3) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]))),
                ("Door to Phendrana's Edge (Storage Cave, Phendrana Drifts)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", lambda state: state.has('Morph Ball', player)),
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)", (
                ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)", None),
                ("Door to Storage Cave (Phendrana's Edge, Phendrana Drifts)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]))),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.standable_terrain.value >= 2 or options.slope_jump.value >= 2 or options.r_jump.value >= 2 or options.l_jump.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 4) else Constant(False)])])]))),
            )
            ),
            (
            "Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", (
                ("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)", e(Constant(True) if ((options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]))),
                ("Door to Gravity Chamber (Lake Tunnel, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)", None),
                ("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Chamber Item (Lower)'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], []))]), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.jump_off_enemies.value >= 3) else Constant(False)]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3 and options.standable_terrain.value >= 3 and options.scan_dash.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 5 and options.standable_terrain.value >= 5) else Constant(False)])])])]))),
                ("Door to Gravity Chamber (Chamber Access, Phendrana Drifts)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)", (
                ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.scan_dash.value >= 3 and options.wall_boost.value >= 4 and options.standable_terrain.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.wall_boost.value >= 3 and options.slope_jump.value >= 4 and options.gravityless_underwater_movement.value >= 4) else Constant(False)]))),
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
                ("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
                ("Morph Ball Door to Security Cave (Phendrana's Edge, Phendrana Drifts)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Security Cave, Phendrana Drifts)", (
                ("Morph Ball Door to Phendrana's Edge (Security Cave, Phendrana Drifts)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2 and options.scan_dash.value >= 1) else Constant(False)]))),
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Burning Trail (Lake Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2 and options.scan_dash.value >= 1) else Constant(False)]))),
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
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(2)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(190), Constant('HeatDamage1')], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(190), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False)])])])]))),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(140), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(110), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('HeatDamage2')], [])]) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]))),
                ("Door to Lava Lake (Lake Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", (
                ("Next to Crates (Lava Lake, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]) if (options.knowledge.value >= 1) else Constant(False)])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(285), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(250), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(265), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(255), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False)])])])]), BoolOp(And(), [Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]) if (options.knowledge.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(360), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(325), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False)])])])])]))),
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], [])])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.movement.value >= 2) else Constant(False)])])]))),
                ("Next to Crates (Lava Lake, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False)])]))),
            )
            ),
            (
            "Next to Crates (Lava Lake, Magmoor Caverns)", (
                ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(25), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(115), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('HeatDamage2')], [])]) if (options.scan_dash.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(155), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('HeatDamage2')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]))),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]) if (options.knowledge.value >= 1) else Constant(False)])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(340), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(265), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(305), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(245), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(270), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]), BoolOp(And(), [Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(2)]) if (options.knowledge.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(360), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(340), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(365), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(320), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(340), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])])])])]))),
                ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(2)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage1')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False)])])])]))),
            )
            ),
            (
            "Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(95), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])])]))),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Lava Lake (Pit Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])])]))),
                ("Door to Pit Tunnel (Lava Lake, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(110), Constant('HeatDamage1')], [])]) if (options.r_jump.value >= 3) else Constant(False)])]))),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])]), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(280), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(155), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2 and options.r_jump.value >= 2) else Constant(False)]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(220), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(255), Constant('HeatDamage1')], []) if (options.slope_jump.value >= 3 and options.standable_terrain.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(225), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 4) else Constant(False)])])])]))),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(145), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(110), Constant('HeatDamage1')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.r_jump.value >= 2) else Constant(False)])])]))),
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", (
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], [])])]) if (options.heat_runs.value >= 2) else Constant(False)])]))),
                ("Door to Triclops Pit (Storage Cavern, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('HeatDamage1')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(140), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(130), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]))),
                ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])]), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(130), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2 and options.r_jump.value >= 2) else Constant(False)]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('HeatDamage1')], []) if (options.slope_jump.value >= 3 and options.standable_terrain.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(180), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 4) else Constant(False)])])])]))),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(95), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]))),
                ("Door to Triclops Pit (Pit Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(145), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(110), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]))),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(145), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])])]))),
                ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(95), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]))),
            )
            ),
            (
            "Tunnel Entrance (Triclops Pit, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(145), Constant('HeatDamage1')], [])])]) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Storage Cavern (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(130), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], [])])]) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(130), Constant('HeatDamage1')], [])])]) if (options.heat_runs.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)]))),
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Triclops Pit (Monitor Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)]))),
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
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 2 and options.slope_jump.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(235), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(15), Constant('Damage')], [])]) if (options.movement.value >= 3 and options.scan_dash.value >= 3 and options.heat_runs.value >= 4) else Constant(False)]))),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(230), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2) else Constant(False)])])]))),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Middle Level (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(415), Constant('HeatDamage1')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(8)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(320), Constant('HeatDamage1')], [])])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(255), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage2')], [])]) if (options.l_jump.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(440), Constant('HeatDamage1')], []) if (options.combat.value >= 2) else Constant(False)])])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage2')], []) if (options.scan_dash.value >= 4) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(315), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(205), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 5) else Constant(False)])])]))),
                ("Door to Monitor Station (Monitor Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", (
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(235), Constant('HeatDamage1')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.r_jump.value >= 3) else Constant(False)])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 4) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(299), Constant('HeatDamage1')], [])]) if (options.l_jump.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 4) else Constant(False)])])]))),
                ("Middle Level (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.r_jump.value >= 2) else Constant(False)]))),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", e(BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], [])]) if ((options.scan_dash.value >= 3 or options.r_jump.value >= 3)) else Constant(False)])]))),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Middle Level (Monitor Station, Magmoor Caverns)", e(BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('Damage')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(2)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage1')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])])])])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(70), Constant('HeatDamage1')], []) if (options.l_jump.value >= 2) else Constant(False)])]))),
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Middle Level (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(354), Constant('HeatDamage1')], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(8)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('HeatDamage1')], [])])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(430), Constant('HeatDamage1')], []) if (options.combat.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(255), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage2')], [])]) if (options.l_jump.value >= 3) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.scan_dash.value >= 3) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(205), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage2')], []) if (options.scan_dash.value >= 4) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(235), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(119), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 5) else Constant(False)])])]))),
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Middle Level (Monitor Station, Magmoor Caverns)", (
                ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], [])]) if (options.l_jump.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], [])]) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(54), Constant('HeatDamage1')], [])]) if (options.r_jump.value >= 2) else Constant(False)])]))),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(235), Constant('HeatDamage1')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.r_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.r_jump.value >= 3) else Constant(False)])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 4) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(319), Constant('HeatDamage1')], [])]) if (options.l_jump.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(219), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)])])]))),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(154), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(54), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])]))),
            )
            ),
            (
            "Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(250), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 5) else Constant(False)])])])]))),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]))),
                ("Door to Transport Tunnel A (Transport to Phendrana Drifts North, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(240), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(140), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 5) else Constant(False)])])])]))),
                ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]))),
                ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)", (
                ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]))),
                ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(90), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]))),
            )
            ),
            (
            "Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", (
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)]))),
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
                ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)", (
                ("Door to Monitor Station (Warrior Shrine, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(70), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]))),
                ("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage1')], [])])])])]) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage1')], [])])])])]) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", (
                ("Room Center (Shore Tunnel, Magmoor Caverns)", e(BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage1')], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage1')], [])]) if (options.bomb_jump.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.movement.value >= 3) else Constant(False)])]))),
            )
            ),
            (
            "Room Center (Shore Tunnel, Magmoor Caverns)", (
                ("Door to Monitor Station (Shore Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)]))),
                ("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]))),
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
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Fiery Shores (Shore Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(239), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('HeatDamage2')], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(230), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(235), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])]) if (options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(189), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 4) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(279), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(245), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(15), Constant('HeatDamage2')], [])]) if (options.r_jump.value >= 3) else Constant(False)])])])])]))),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(245), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(270), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(315), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(215), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])]))),
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)", (
                ("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(25), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)", (
                ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])])])]))),
            )
            ),
            (
            "Pickup (Missile) (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", e(BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('HeatDamage2')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.l_jump.value >= 2 and options.standable_terrain.value >= 1) else Constant(False)])]))),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []) if (options.standable_terrain.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('HeatDamage1')], [])]) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(220), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])])])])]))),
            )
            ),
            (
            "Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)", (
                ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]))),
                ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(250), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3 and options.l_jump.value >= 1) else Constant(False)])]), BoolOp(And(), [Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(215), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(175), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(25), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(210), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage2')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []) if (options.r_jump.value >= 3) else Constant(False), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(175), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False)])])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage2')], [])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])]) if (options.scan_dash.value >= 2) else Constant(False)])])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(25), Constant('HeatDamage2')], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(130), Constant('HeatDamage1')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(115), Constant('HeatDamage1')], [])])])]) if (options.r_jump.value >= 3 and options.scan_dash.value >= 4 and options.l_jump.value >= 2) else Constant(False), Constant(True) if (options.heat_runs.value >= 4) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])])]))),
                ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.scan_dash.value >= 3 and options.standable_terrain.value >= 3)) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False)])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(275), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3 and options.l_jump.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1 and options.l_jump.value >= 2) else Constant(False), Constant(True) if (options.heat_runs.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(170), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(15), Constant('HeatDamage2')], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(165), Constant('HeatDamage1')], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(140), Constant('HeatDamage1')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])]) if (options.r_jump.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], []) if (options.l_jump.value >= 2 and options.scan_dash.value >= 3 and options.standable_terrain.value >= 3) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(215), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])])]))),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage2')], []) if (options.movement.value >= 1) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], []) if (options.l_jump.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(59), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])])]))),
                ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Fiery Shores (Transport Tunnel B, Magmoor Caverns)", (
                ("Door to Transport to Tallon Overworld West (Transport Tunnel B, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('HeatDamage2')], []) if (options.movement.value >= 1) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], []) if (options.l_jump.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(59), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])])]))),
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
                ("Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]), Constant(True) if (options.l_jump.value >= 2) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('HeatDamage2')], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], [])) if (options.scan_dash.value >= 4 and options.standable_terrain.value >= 3) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(160), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(70), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(10), Constant('HeatDamage2')], []) if (options.standable_terrain.value >= 2 and options.movement.value >= 4) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(110), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])])]))),
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Tallon Overworld West (Twin Fires Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(95), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('HeatDamage2')], []) if (options.bomb_jump.value >= 4 and options.l_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])])])])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(15), Constant('HeatDamage2')], [])]) if (options.movement.value >= 1) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 2) else Constant(False), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(135), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False)])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(145), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(95), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 4) else Constant(False)])])])]))),
                ("Door to Twin Fires Tunnel (Transport to Tallon Overworld West, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.r_jump.value >= 1 or options.scan_dash.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage2')], []) if (options.scan_dash.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(3)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.scan_dash.value >= 2 and options.l_jump.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('HeatDamage2')], []) if (options.slope_jump.value >= 4 and options.l_jump.value >= 1 and options.gravityless_underwater_movement.value >= 4) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('HeatDamage2')], [])]) if (options.l_jump.value >= 1) else Constant(False)]))),
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Twin Fires Tunnel (Twin Fires, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", e(BoolOp(Or(), [Constant(True) if (options.scan_dash.value >= 4) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.r_jump.value >= 1 or options.scan_dash.value >= 1) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(285), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(3)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.scan_dash.value >= 2 and options.l_jump.value >= 2) else Constant(False)]))),
                ("Door to Twin Fires (Twin Fires Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(105), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(120), Constant('HeatDamage2')], []) if (options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3) else Constant(False)]))),
                ("Door to North Core Tunnel (Twin Fires, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", (
                ("Door to Twin Fires (North Core Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(105), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], []) if (options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2) else Constant(False)]))),
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(230), Constant('HeatDamage2')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage2')], [])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], [])), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage2')], [])]) if (options.movement.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 5 and options.jump_off_enemies.value >= 5 and options.movement.value >= 5) else Constant(False)]))),
                ("Door to Geothermal Core (North Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", e(Constant(True) if ((options.clip_through_objects.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Geothermal Core Puzzle'), Name('player', Load())], []))),
                ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", (
                ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(85), Constant('HeatDamage2')], [])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], [])), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(185), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('HeatDamage2')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(70), Constant('HeatDamage2')], [])]) if (options.movement.value >= 2) else Constant(False)])]))),
                ("First Spinner (Geothermal Core, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], []))]) if (options.scan_dash.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", (
                ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)]))),
            )
            ),
            (
            "First Spinner (Geothermal Core, Magmoor Caverns)", (
                ("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], [])]) if (options.scan_dash.value >= 4) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Storage Depot B Item'), Name('player', Load())], [])), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4 and options.scan_dash.value >= 5) else Constant(False)])]))),
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
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage2')], []) if (options.gravityless_underwater_movement.value >= 3 and options.slope_jump.value >= 3) else Constant(False)]))),
                ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", (
                ("Door to Geothermal Core (South Core Tunnel, Magmoor Caverns)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(40), Constant('HeatDamage2')], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('HeatDamage2')], [])]) if (options.bomb_jump.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(80), Constant('HeatDamage2')], []) if (options.gravityless_underwater_movement.value >= 3 and options.slope_jump.value >= 2) else Constant(False)]))),
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2 and options.slope_jump.value >= 1 and options.standable_terrain.value >= 1) else Constant(False)]), Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]))),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", e(BoolOp(And(), [Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2 and options.slope_jump.value >= 1 and options.standable_terrain.value >= 1) else Constant(False)])]))),
                ("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('HeatDamage2')], [])]) if (options.scan_dash.value >= 3 and options.single_room_oob.value >= 4 and options.clip_through_objects.value >= 3) else Constant(False), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])])]), Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]))),
                ("Door to Magmoor Workstation (South Core Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", e(Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []))),
                ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", e(Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []))),
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)", (
                ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)", e(Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []))),
                ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)", e(Constant(True) if (options.knowledge.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []))),
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
                ("Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Workstation Tunnel (Transport to Phazon Mines West, Magmoor Caverns)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Magmoor Workstation (Workstation Tunnel, Magmoor Caverns)", (
                ("Door to Transport to Phazon Mines West (Workstation Tunnel, Magmoor Caverns)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
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
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", lambda state: (state.has('Space Jump Boots', player) and templates['Use Grapple Beam'](state))),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", e(Constant(True) if (options.movement.value >= 2 or options.l_jump.value >= 1) else BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
                ("Door to Security Access A (Main Quarry, Phazon Mines)", lambda state: state.has('Main Quarry Barrier', player)),
                ("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)", lambda state: state.has('Scan Visor', player)),
                ("Crane Platform (Main Quarry, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Grapple Beam'), Name('player', Load())], []) if (options.movement.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.wall_boost.value >= 4 and options.slope_jump.value >= 2) else Constant(False)]))),
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
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", lambda state: (state.has('Main Quarry Barrier', player) or logic.has_misc(state, player, 'backwards_upper_mines'))),
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
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", e(BoolOp(Or(), [Constant(True) if ((options.scan_dash.value >= 3)) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("Door to Quarry Access (Main Quarry, Phazon Mines)", None),
                ("Pickup (Missile) (Main Quarry, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.knowledge.value >= 2 and options.movement.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])])]))),
            )
            ),
            (
            "Door to Main Quarry (Waste Disposal, Phazon Mines)", (
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
                ("Door to Waste Disposal (Main Quarry, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ore Processing (Waste Disposal, Phazon Mines)", (
                ("Door to Main Quarry (Waste Disposal, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])]))),
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Main Quarry (Save Station Mines A, Phazon Mines)", (
                ("Save Station (Save Station Mines A, Phazon Mines)", lambda state: (state.has('Phazon Mines Save Station A Barrier', player))),
                ("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)", lambda state: (state.has('Scan Visor', player))),
                ("Door to Save Station Mines A (Main Quarry, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Save Station (Save Station Mines A, Phazon Mines)", (
                ("Door to Main Quarry (Save Station Mines A, Phazon Mines)", lambda state: (state.has('Phazon Mines Save Station A Barrier', player))),
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
                ("Pickup (Missile) (Security Access A, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
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
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(3)])]) if (options.wall_boost.value >= 3) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 2 and options.slope_jump.value >= 2) else Constant(False), Constant(True) if (options.combat.value >= 3) else Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])])]))),
                ("Door to Ore Processing (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Storage Depot B (Ore Processing, Phazon Mines)", (
                ("Door to Waste Disposal (Ore Processing, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Constant(True) if ((options.standable_terrain.value >= 1)) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1) else Constant(False)]), Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('Damage')], [])])]))),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", None),
                ("Door to Ore Processing (Storage Depot B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Waste Disposal (Ore Processing, Phazon Mines)", (
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", e(BoolOp(Or(), [Constant(True) if (options.standable_terrain.value >= 1) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if ((options.r_jump.value >= 1 or options.l_jump.value >= 1)) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("Door to Elevator Access A (Ore Processing, Phazon Mines)", None),
                ("Door to Ore Processing (Waste Disposal, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elevator Access A (Ore Processing, Phazon Mines)", (
                ("Door to Research Access (Ore Processing, Phazon Mines)", None),
                ("Door to Storage Depot B (Ore Processing, Phazon Mines)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Constant(True) if ((options.standable_terrain.value >= 1 and options.l_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.bomb_jump.value >= 3 and options.standable_terrain.value >= 2 and options.scan_dash.value >= 4) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.l_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False)]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])]) if (options.wall_boost.value >= 3) else Constant(False), Constant(True) if ((options.l_jump.value >= 1 and options.standable_terrain.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])])]))),
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
                ("Room Center (Mine Security Station, Phazon Mines)", lambda state: (state.has('Mine Security Station Barrier', player))),
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
                ("Door to Security Access A (Mine Security Station, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Mine Security Station Unlock Doors'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])]))),
                ("Door to Security Access B (Mine Security Station, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Mine Security Station Unlock Doors'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])]))),
                ("Door to Storage Depot A (Mine Security Station, Phazon Mines)", lambda state: (state.has('Mine Security Station Barrier', player))),
                ("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)", lambda state: (state.has('Scan Visor', player) and state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Mine Security Station Unlock Doors'), Name('player', Load())], [])), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], []) if (options.combat.value >= 2) else Constant(False)])]))),
            )
            ),
            (
            "Door to Ore Processing (Research Access, Phazon Mines)", (
                ("Door to Elite Research (Research Access, Phazon Mines)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.slope_jump.value >= 2) else Constant(False)]))),
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
                ("Door to Ore Processing (Elevator Access A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]) if (options.bomb_space_jump.value >= 3 and options.standable_terrain.value >= 4) else Constant(False)])]))),
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
                ("Top Floor (Elite Research, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Research Rock Wall'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.clip_through_objects.value >= 1) else Constant(False)]))),
                ("Door to Elite Research (Research Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Security Access B (Elite Research, Phazon Mines)", (
                ("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Invisible Drone'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('phazon_elite_without_dynamo')], [])]), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]))),
                ("Top Floor (Elite Research, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])]))),
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
                ("Top Floor (Elite Research, Phazon Mines)", e(Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []))),
            )
            ),
            (
            "Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)", (
                ("Door to Security Access B (Elite Research, Phazon Mines)", None),
            )
            ),
            (
            "Top Floor (Elite Research, Phazon Mines)", (
                ("Door to Research Access (Elite Research, Phazon Mines)", lambda state: state.has('Elite Research Rock Wall', player)),
                ("Door to Security Access B (Elite Research, Phazon Mines)", e(Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])]))),
                ("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.spinners_without_boost.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])])])]))),
                ("Pickup (Missile) (Elite Research, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Research Rock Wall'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
            )
            ),
            (
            "Door to Elevator Access A (Elevator A, Phazon Mines)", (
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", lambda state: (state.has('Scan Visor', player))),
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
                ("Pickup (Missile) (Elite Control Access, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Damage')], []) if (options.damage_boosting.value >= 4) else Constant(False)])]))),
                ("Door to Elite Control Access (Elevator A, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Elite Control (Elite Control Access, Phazon Mines)", (
                ("Door to Elevator A (Elite Control Access, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])])]))),
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
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", e(Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])]))),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", e(Constant(True) if (((options.standable_terrain.value >= 3 and options.movement.value >= 2))) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Pirate Fight (Elite Control)'), Name('player', Load())], []))),
                ("Door to Elite Control (Elite Control Access, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Elite Control, Phazon Mines)", (
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", lambda state: (logic.has_misc(state, player, 'backwards_lower_mines') and state.has('Scan Visor', player))),
                ("Bottom Floor Center (Elite Control, Phazon Mines)", lambda state: state.has('Elite Control Barriers', player)),
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
                ("Door to Elite Control Access (Elite Control, Phazon Mines)", e(Constant(True) if ((options.standable_terrain.value >= 2 and options.movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Pirate Fight (Elite Control)'), Name('player', Load())], []))),
                ("Door to Ventilation Shaft (Elite Control, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Control Barriers'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Pirate Fight (Elite Control)'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])])]))),
                ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Constant(True) if ((options.standable_terrain.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Elite Pirate Fight (Elite Control)'), Name('player', Load())], [])]))),
                ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)", e(Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])]))),
            )
            ),
            (
            "Door to Elite Control (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Maintenance Tunnel (Elite Control, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", (
                ("Door to Elite Control (Maintenance Tunnel, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Ventilation Shaft, Phazon Mines)", (
                ("Door to Elite Control (Ventilation Shaft, Phazon Mines)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 4) else Constant(False)])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], []))]) if (options.scan_dash.value >= 4 and options.standable_terrain.value >= 2) else Constant(False)]))),
                ("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)", lambda state: (state.has('Scan Visor', player) and state.has('Morph Ball', player) and state.has('Power Bomb', player))),
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
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 2) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []) if (options.bomb_jump.value >= 4 and options.standable_terrain.value >= 4) else Constant(False)])]), BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], [])), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])])])]))),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)]))),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Phazon Processing Center (Maintenance Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(45), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)]), Constant(True) if (options.standable_terrain.value >= 1) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('Phazon')], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []) if (options.bomb_jump.value >= 3 and options.standable_terrain.value >= 3 and options.l_jump.value >= 3) else Constant(False)])]), BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], [])), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])])])]))),
                ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), Constant(True) if (options.invisible_objects.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]), BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], [])), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Processing Item'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])])])]))),
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Phazon Processing Center, Phazon Mines)", (
                ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if ((options.l_jump.value >= 2 or (options.bomb_jump.value >= 2 and options.invisible_objects.value >= 1)) and ((options.complex_bomb_jump.value >= 3 and options.invisible_objects.value >= 1) or (options.scan_dash.value >= 3 and options.standable_terrain.value >= 3 and options.bomb_jump.value >= 3))) else Constant(False)]), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]))),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", None),
            )
            ),
            (
            "Door to Map Station Mines (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Omega Research (Map Station Mines, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Ventilation Shaft (Omega Research, Phazon Mines)", (
                ("Door to Map Station Mines (Omega Research, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", e(Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])]))),
                ("Door to Omega Research (Ventilation Shaft, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Dynamo Access (Omega Research, Phazon Mines)", (
                ("Door to Ventilation Shaft (Omega Research, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Invisible Drone'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])]))),
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Transport Access, Phazon Mines)", (
                ("Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", e(Constant(True) if (options.slope_jump.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]))),
                ("Door to Transport Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns South (Transport Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Transport Access, Phazon Mines)", e(Constant(True) if (options.slope_jump.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]))),
                ("Door to Transport Access (Transport to Magmoor Caverns South, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", (
                ("Door to Elite Quarters (Processing Center Access, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Processing Center Access Barrier'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('backwards_lower_mines')], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)])]))),
                ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Processing Center Access, Phazon Mines)", (
                ("Door to Phazon Processing Center (Processing Center Access, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Processing Center Access Barrier'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(199), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('Phazon')], []) if (options.movement.value >= 2) else Constant(False)])]))),
                ("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)", lambda state: state.has('Scan Visor', player)),
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
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", lambda state: (not state.has('Plasma Beam', player) or state.has('Elite Pirate Fight (Dynamo Access)', player))),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", lambda state: state.has('Plasma Beam', player)),
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Omega Research (Dynamo Access, Phazon Mines)", (
                ("Door to Central Dynamo (Dynamo Access, Phazon Mines)", lambda state: (not state.has('Plasma Beam', player) or state.has('Elite Pirate Fight (Dynamo Access)', player))),
                ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", lambda state: state.has('Plasma Beam', player)),
                ("Door to Dynamo Access (Omega Research, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)", (
                ("Door to Omega Research (Dynamo Access, Phazon Mines)", e(Constant(True) if (options.combat.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])]))),
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
                ("Door to Processing Center Access (Elite Quarters, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Omega Pirate'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 1 and options.bomb_space_jump.value >= 3) else Constant(False)])]))),
                ("Fight Trigger (Elite Quarters, Phazon Mines)", None),
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Processing Center Access (Elite Quarters, Phazon Mines)", (
                ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)", lambda state: (state.has('Omega Pirate', player))),
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
                ("Event - Omega Pirate (Elite Quarters, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 5) else BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Have all Beams'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Super Missile'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(30)], [])])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])]) if (options.combat.value >= 1) else Constant(False), BoolOp(And(), [Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(3)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]) if (options.combat.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], []) if (options.combat.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(500), Constant('Damage')], []) if (options.combat.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(800), Constant('Damage')], []) if (options.combat.value >= 1) else Constant(False)])]))),
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
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(280), Constant('Damage')], [])]) if (options.infinite_speed.value >= 2) else Constant(False))),
                ("Room Bottom (Central Dynamo, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
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
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(680), Constant('Damage')], [])]) if (options.infinite_speed.value >= 2) else Constant(False)])]))),
            )
            ),
            (
            "Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", (
                ("Room Bottom (Central Dynamo, Phazon Mines)", None),
            )
            ),
            (
            "Fight Trigger (Central Dynamo, Phazon Mines)", (
                ("Door to Dynamo Access (Central Dynamo, Phazon Mines)", lambda state: state.has('Invisible Drone', player)),
                ("Event - Security Drone (Central Dynamo, Phazon Mines)", e(Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Damage')], []))),
                ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(280), Constant('Damage')], [])]) if (options.infinite_speed.value >= 2 and options.knowledge.value >= 3) else Constant(False))),
                ("Room Bottom (Central Dynamo, Phazon Mines)", None),
            )
            ),
            (
            "Room Bottom (Central Dynamo, Phazon Mines)", (
                ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Invisible Drone'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Ice Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])])]))),
                ("Door to Save Station Mines B (Central Dynamo, Phazon Mines)", e(Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Invisible Drone'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])]))),
                ("Fight Trigger (Central Dynamo, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4 and options.standable_terrain.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Invisible Drone'), Name('player', Load())], []))])]))),
            )
            ),
            (
            "Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", (
                ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", lambda state: (state.has('Elite Quarters Access Barrier', player))),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", lambda state: (templates['Shoot Plasma Beam'](state))),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters (Elite Quarters Access, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", lambda state: (state.has('Elite Quarters Access Barrier', player))),
                ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)", lambda state: (logic.has_misc(state, player, 'backwards_lower_mines'))),
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
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.l_jump.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], []) if (options.combat.value >= 3) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 4) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4 and options.scan_dash.value >= 4 and options.standable_terrain.value >= 2) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])])]))),
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", e(Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])]))),
                ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", (
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.clip_through_objects.value >= 3) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3 and options.single_room_oob.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3 and options.complex_bomb_jump.value >= 4 and options.standable_terrain.value >= 5 and options.single_room_oob.value >= 4) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])]))),
                ("Door to Elite Quarters Access (Metroid Quarantine B, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.standable_terrain.value >= 1 and options.scan_dash.value >= 1) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(125), Constant('Damage')], [])])]))),
                ("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)", templates['Shoot Super Missile']),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", lambda state: (state.has('Scan Visor', player) and logic.has_misc(state, player, 'backwards_lower_mines'))),
                ("Front of Barrier (Metroid Quarantine B, Phazon Mines)", lambda state: state.has('Metroid Quarantine B Barrier', player)),
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
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('Phazon')], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('Phazon')], []) if (options.slope_jump.value >= 1) else Constant(False)]), Constant(True) if (options.combat.value >= 2) else BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])])]))),
                ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)", lambda state: state.has('Metroid Quarantine B Barrier', player)),
                ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)", lambda state: state.has('Scan Visor', player)),
            )
            ),
            (
            "Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", (
                ("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", lambda state: state.has('Scan Visor', player)),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Metroid Quarantine A Barrier'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 1) else Constant(False)]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4 and options.l_jump.value >= 3) else Constant(False)])]))),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []) if (options.jump_off_enemies.value >= 4 and options.l_jump.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])]) if (options.jump_off_enemies.value >= 3) else Constant(False)]))),
                ("Door to Metroid Quarantine A (Quarantine Access A, Phazon Mines)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Metroid Quarantine A Barrier'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('backwards_lower_mines')], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Phazon')], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('Phazon')], []) if (options.slope_jump.value >= 2) else Constant(False)])]))),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]))),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", e(Constant(True) if (options.scan_dash.value >= 3) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])])]))),
                ("Door to Metroid Quarantine A (Elevator Access B, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 4 and options.standable_terrain.value >= 3) else Constant(False)]))),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", e(Constant(True) if (options.standable_terrain.value >= 1) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]))),
            )
            ),
            (
            "Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", None),
            )
            ),
            (
            "Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Metroid Quarantine A Barrier'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 1) else Constant(False)])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('Phazon')], []) if (options.slope_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(75), Constant('Phazon')], [])]) if (options.bomb_jump.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(55), Constant('Phazon')], []) if (options.standable_terrain.value >= 3) else Constant(False)])]))),
                ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]) if (options.slope_jump.value >= 3 and options.standable_terrain.value >= 3 and options.scan_dash.value >= 3) else Constant(False)])])]))),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 1) else Constant(False)])]))),
                ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.count('Power Bomb', player) >= 2)),
            )
            ),
            (
            "Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)", (
                ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)", lambda state: (state.has('Metroid Quarantine A Barrier', player) or logic.has_misc(state, player, 'backwards_lower_mines'))),
                ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []) if (options.invisible_objects.value >= 1) else Constant(False)]), Constant(True) if (((options.standable_terrain.value >= 1))) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]))),
                ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)", lambda state: (state.has('Morph Ball', player) and state.count('Power Bomb', player) >= 2)),
            )
            ),
            (
            "Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", (
                ("Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('Phazon')], [])]) if (options.bomb_jump.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('Phazon')], [])]) if (options.scan_dash.value >= 1 and options.l_jump.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Phazon')], []) if (options.slope_jump.value >= 3) else Constant(False)]))),
                ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall B (Quarantine Access B, Phazon Mines)", (
                ("Door to Metroid Quarantine B (Quarantine Access B, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(150), Constant('Phazon')], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Phazon')], []) if (options.slope_jump.value >= 1) else Constant(False)]))),
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
                ("Door to Missile Station Mines (Fungal Hall B, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.slope_jump.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], [])]))),
                ("Door to Quarantine Access B (Fungal Hall B, Phazon Mines)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 1) or (options.standable_terrain.value >= 1)) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4) else Constant(False), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], []) if (options.jump_off_enemies.value >= 4) else Constant(False)]))),
                ("Pickup (Missile) (Fungal Hall B, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
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
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", lambda state: (state.has('Scan Visor', player))),
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
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)])]))),
                ("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(1299), Constant('Phazon')], []) if (options.movement.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(1199), Constant('Phazon')], []) if (options.movement.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(1099), Constant('Phazon')], []) if (options.movement.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(999), Constant('Phazon')], []) if (options.movement.value >= 5) else Constant(False)])])])]))),
                ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)])])])]))),
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)", (
                ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Phazon')], []) if (options.movement.value >= 4) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Phazon')], []) if (options.movement.value >= 3) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(400), Constant('Phazon')], []) if (options.movement.value >= 2) else Constant(False)])])])]))),
            )
            ),
            (
            "Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", (
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.standable_terrain.value >= 3 and ((options.bomb_jump.value >= 3) or (options.bomb_space_jump.value >= 3))) else Constant(False)]))),
                ("Pickup (Missile) (Fungal Hall Access, Phazon Mines)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Phazon Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Phazon')], []) if (options.movement.value >= 1) else Constant(False)])]))),
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Door to Elevator B (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", e(BoolOp(Or(), [Constant(True) if (options.movement.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
                ("Door to Fungal Hall Access (Elevator B, Phazon Mines)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile) (Fungal Hall Access, Phazon Mines)", (
                ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)", e(BoolOp(Or(), [Constant(True) if ((options.movement.value >= 5)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
                ("Door to Elevator B (Fungal Hall Access, Phazon Mines)", lambda state: state.has('Space Jump Boots', player)),
            )
            ),
            (
            "Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", (
                ("Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", e(Constant(True) if ((options.slope_jump.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []))),
                ("Door to Fungal Hall A (Phazon Mining Tunnel, Phazon Mines)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Fungal Hall Access (Fungal Hall A, Phazon Mines)", (
                ("Door to Phazon Mining Tunnel (Fungal Hall A, Phazon Mines)", e(BoolOp(And(), [BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.r_jump.value >= 2) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []) if (options.scan_dash.value >= 4) else Constant(False)])]), BoolOp(Or(), [Constant(True) if (options.combat.value >= 4) else BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(4)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Ice Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Plasma Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(599), Constant('Damage')], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(299), Constant('Damage')], [])])]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(299), Constant('Damage')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.combat.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(299), Constant('Damage')], []) if (options.combat.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.combat.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Plasma Beam'), Name('player', Load())], []) if (options.combat.value >= 1) else Constant(False)])]))),
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
                ("Door to Gully (Landing Site, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], [])) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("Door to Canyon Cavern (Landing Site, Tallon Overworld)", None),
                ("Door to Temple Hall (Landing Site, Tallon Overworld)", None),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", None),
                ("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)", lambda state: state.has('Morph Ball', player)),
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
                ("Door to Tallon Canyon (Gully, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
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
                ("Door to Landing Site (Alcove, Tallon Overworld)", e(BoolOp(Or(), [Constant(True) if (options.slope_jump.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
            )
            ),
            (
            "Door to Landing Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Waterfall Cavern (Landing Site, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", (
                ("Door to Landing Site (Waterfall Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
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
                ("Half Pipe (Tallon Canyon, Tallon Overworld)", lambda state: ((state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player) and state.has('Space Jump Boots', player)))),
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
                ("Door to Gully (Tallon Canyon, Tallon Overworld)", lambda state: ((state.has('Morph Ball Bomb', player) and state.has('Morph Ball', player) and state.has('Boost Ball', player)))),
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
                ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 2 and options.standable_terrain.value >= 1 and options.l_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.standable_terrain.value >= 2 and options.scan_dash.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])]))),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.l_jump.value >= 1 or (options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []))]) if (options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3) else Constant(False), Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []) if (options.movement.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []) if (options.standable_terrain.value >= 2 and options.l_jump.value >= 2) else Constant(False)]))),
                ("Door to Frigate Crash Site (Waterfall Cavern, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)", (
                ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)", None),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 3 and options.slope_jump.value >= 3 and options.l_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.wall_boost.value >= 2 and options.movement.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1 and options.l_jump.value >= 2) else Constant(False)]))),
                ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)", (lambda _: True) if (options.standable_terrain.value >= 2 and options.l_jump.value >= 2) else (lambda _: False)),
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
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Overgrown Cavern (Frigate Crash Site, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", (
                ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)", (
                ("Door to Frigate Crash Site (Overgrown Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
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
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.scan_dash.value >= 2) or (options.l_jump.value >= 2 and options.slope_jump.value >= 2 and options.standable_terrain.value >= 2)) else Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]) if (options.standable_terrain.value >= 3 and options.single_room_oob.value >= 3 and (options.movement.value >= 4)) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_space_jump.value >= 3) else Constant(False), Constant(True) if (options.invisible_objects.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])])]))),
                ("Door to Root Cave (Root Tunnel, Tallon Overworld)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Arbor Chamber (Root Cave, Tallon Overworld)", (
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", None),
                ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", e(BoolOp(And(), [Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), Constant(True) if (options.scan_dash.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
                ("Door to Root Cave (Arbor Chamber, Tallon Overworld)", dock_requirements['Plasma Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Root Cave, Tallon Overworld)", (
                ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)", None),
                ("Door to Root Tunnel (Root Cave, Tallon Overworld)", None),
                ("Door to Arbor Chamber (Root Cave, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], [])]))),
            )
            ),
            (
            "Door to Temple Lobby (Artifact Temple, Tallon Overworld)", (
                ("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)", None),
                ("Event - Meta Ridley (Artifact Temple, Tallon Overworld)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Chozo'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Elder'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Lifegiver'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Nature'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Newborn'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Spirit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Strength'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Sun'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Truth'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Warrior'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of Wild'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Artifact of World'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if (options.combat.value >= 4) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(400), Constant('Damage')], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(300), Constant('Damage')], []) if (options.combat.value >= 1) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], []) if (options.combat.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(100), Constant('Damage')], []) if (options.combat.value >= 3) else Constant(False)])]))),
                ("Teleporter to Impact Crater (Artifact Temple, Tallon Overworld)", lambda state: state.has('Meta Ridley', player)),
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
                ("Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False)])]))),
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Frigate Access Tunnel (Main Ventilation Shaft Section C, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section C, Tallon Overworld)", lambda state: state.has('Morph Ball', player)),
                ("Door to Main Ventilation Shaft Section C (Frigate Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Transport Tunnel C (Overgrown Cavern, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport to Chozo Ruins East (Transport Tunnel C, Tallon Overworld)", (
                ("Door to Overgrown Cavern (Transport Tunnel C, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", lambda state: (state.has('Main Ventilation Shaft Section B Conduit', player) or logic.has_misc(state, player, 'backwards_frigate'))),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('backwards_frigate')], []))]) if (options.complex_bomb_jump.value >= 4 and options.single_room_oob.value >= 4) else Constant(False))),
                ("Door to Main Ventilation Shaft Section B (Main Ventilation Shaft Section A, Tallon Overworld)", dock_requirements['Circular Door']),
            )
            ),
            (
            "Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)", (
                ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)", lambda state: state.has('Main Ventilation Shaft Section B Conduit', player)),
                ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]))),
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
                ("Door to Reactor Access (Reactor Core, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Reactor Core Conduits'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])]))),
                ("Door to Main Ventilation Shaft Section A (Reactor Core, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4 and options.gravityless_underwater_movement.value >= 4) else Constant(False)]))),
                ("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 3)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])]))),
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
                ("Door to Cargo Freight Lift to Deck Gamma (Reactor Access, Tallon Overworld)", lambda state: (state.has('Reactor Access Conduits', player))),
                ("Door to Savestation (Reactor Access, Tallon Overworld)", None),
                ("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]))),
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
                ("Door to Deck Beta Transit Hall (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", lambda state: state.has('Cargo Freight Lift to Deck Gamma Conduits', player)),
                ("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", lambda state: (templates['Shoot Any Beam'](state) and (logic.has_missiles(state, player, 1) or state.has('Charge Beam', player)))),
                ("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4) else Constant(False)])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 2 and options.l_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2) else Constant(False), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.slope_jump.value >= 4 and options.gravityless_underwater_movement.value >= 3) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])])])])])]))),
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
                ("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]))),
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
                ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 4 and options.standable_terrain.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1 and options.standable_terrain.value >= 1) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False)]))),
                ("Door to Deck Beta Security Hall (Biohazard Containment, Tallon Overworld)", lambda state: (state.has('Biohazard Containment Conduits', player))),
                ("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)", lambda state: (templates['Shoot Super Missile'](state))),
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
                ("Door to Deck Beta Security Hall (Biotech Research Area 1, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.gravityless_underwater_movement.value >= 1 and (options.slope_jump.value >= 1 or options.standable_terrain.value >= 1)) else Constant(False)]))),
                ("Door to Deck Beta Conduit Hall (Biotech Research Area 1, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Biotech Research Area 1 Conduits'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.gravityless_underwater_movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])])])]))),
                ("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Thermal Visor'), Name('player', Load())], [])]))),
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
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", e(Constant(True) if ((options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
                ("Door to Connection Elevator to Deck Beta (Deck Beta Conduit Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", (
                ("Door to Deck Beta Conduit Hall (Connection Elevator to Deck Beta, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False)])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3 and options.slope_jump.value >= 4) else Constant(False)])]))),
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player) and state.has('Gravity Suit', player))),
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
                ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.gravityless_underwater_movement.value >= 1) else Constant(False)])]))),
                ("Door to Hydro Access Tunnel (Connection Elevator to Deck Beta, Tallon Overworld)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)", (
                ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
            )
            ),
            (
            "Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", e(Constant(True) if ((options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 2)) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]))),
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
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", e(BoolOp(And(), [Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3 and options.scan_dash.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(200), Constant('Damage')], [])]) if (options.bomb_jump.value >= 3 and options.jump_off_enemies.value >= 3) else Constant(False)])]))),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 1) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.standable_terrain.value >= 4 and options.bomb_jump.value >= 5 and options.complex_bomb_jump.value >= 5 and options.movement.value >= 5 and options.scan_dash.value >= 4) else Constant(False)])])]))),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Great Tree Hall Bars Unlocked'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False)]))),
                ("Door to Great Tree Hall (Transport Tunnel D, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", (
                ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)", e(BoolOp(And(), [Constant(True) if (options.invisible_objects.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('X-Ray Visor'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)])]))),
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", None),
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", (
                ("Door to Hydro Access Tunnel (Great Tree Hall, Tallon Overworld)", None),
                ("Next to Spinner (Great Tree Hall, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]) if (options.scan_dash.value >= 5) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 5) else Constant(False)])])]))),
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
                ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Great Tree Hall Bars Unlocked'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3) else Constant(False)]))),
                ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)", None),
                ("Event - Open gate (Great Tree Hall, Tallon Overworld)", lambda state: (state.has('Morph Ball', player) and state.has('Boost Ball', player))),
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
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Constant(True) if (options.wall_boost.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False)])]))),
                ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", (
                ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False)])]))),
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Constant(True) if (options.wall_boost.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5) else Constant(False)])]))),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5) else Constant(False)])]))),
            )
            ),
            (
            "Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)", (
                ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 2) else Constant(False)])]))),
                ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
                ("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
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
                ("Front of PB Wall (Life Grove, Tallon Overworld)", lambda state: (state.has('Morph Ball', player))),
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
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", e(BoolOp(And(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 4) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])])])])]))),
                ("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.single_room_oob.value >= 3 and options.standable_terrain.value >= 3) else Constant(False), BoolOp(And(), [Constant(True) if (options.spinners_without_boost.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)]), BoolOp(Or(), [Constant(True) if ((options.l_jump.value >= 3 and options.standable_terrain.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False)])])])]))),
                ("Front of PB Wall (Life Grove, Tallon Overworld)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
            )
            ),
            (
            "Front of PB Wall (Life Grove, Tallon Overworld)", (
                ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.standable_terrain.value >= 1 and options.r_jump.value >= 2) else Constant(False))),
                ("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)", None),
                ("Behind PB Wall (Life Grove, Tallon Overworld)", lambda state: (state.has('Morph Ball', player) and state.has('Power Bomb', player))),
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
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Super Missile'), Load()), [Name('state', Load())], []), Constant(True) if (options.movement.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]))),
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.movement.value >= 1) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo - Fallen Rubble'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 5 and options.damage_boosting.value >= 4) else Constant(False)]))),
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruins Entrance (Main Plaza, Chozo Ruins)", (
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", None),
                ("Door to Ruined Shrine Access (Main Plaza, Chozo Ruins)", None),
                ("Door to Nursery Access (Main Plaza, Chozo Ruins)", None),
                ("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.movement.value >= 4)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 3) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 1) else Constant(False)]))),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", e(Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1) else Constant(False))),
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
                ("Grapple Ledge (Main Plaza, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3) else Constant(False)])]))),
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
                ("Door from Plaza Access (Main Plaza, Chozo Ruins)", lambda state: logic.has_misc(state, player, 'main_plaza_door')),
                ("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)", None),
            )
            ),
            (
            "Grapple Ledge (Main Plaza, Chozo Ruins)", (
                ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)", None),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.movement.value >= 3 or options.standable_terrain.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False)])])]))),
                ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3 and options.movement.value >= 3 and options.single_room_oob.value >= 3) else Constant(False))),
                ("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)", None),
                ("Locked Door Ledge (Main Plaza, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.complex_bomb_jump.value >= 4 and options.l_jump.value >= 5 and options.single_room_oob.value >= 4 and options.standable_terrain.value >= 4) else Constant(False))),
            )
            ),
            (
            "Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Ruined Fountain (Ruined Fountain Access, Chozo Ruins)", (
                ("Door to Main Plaza (Ruined Fountain Access, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
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
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
                ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", (
                ("Morph Ball Door to Main Plaza (Piston Tunnel, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
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
                ("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.standable_terrain.value >= 3 and options.scan_dash.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flaahgra'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 2) else Constant(False)])]))),
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
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", e(Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False))),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)])]))),
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", None),
                ("Door to Ruined Shrine (Tower of Light Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", (
                ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)", e(BoolOp(Or(), [Constant(True) if ((options.standable_terrain.value >= 3 and options.l_jump.value >= 2)) else BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3 and options.standable_terrain.value >= 3) else Constant(False)]))),
                ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.l_jump.value >= 2 and options.standable_terrain.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5) else Constant(False)])]))),
                ("Pit (Ruined Shrine, Chozo Ruins)", None),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", e(Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False))),
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
                ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)", e(BoolOp(Or(), [Constant(True) if ((options.l_jump.value >= 2 and options.standable_terrain.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []), UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Beetle Battle'), Name('player', Load())], []))]) if (options.standable_terrain.value >= 2 and options.scan_dash.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Ruined Shrine Item (Morph Ball)'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False)])])]))),
                ("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
                ("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])])]) if (options.combat.value >= 2) else Constant(False)]))),
                ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Beetle Battle'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 2) else Constant(False)]))),
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
                ("Pickup (Missile Expansion) (Vault, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(3)])]) if (options.standable_terrain.value >= 3 and options.knowledge.value >= 1) else Constant(False)])]))),
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
                ("Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", lambda state: state.has('Training Chamber Exit Tunnel', player)),
                ("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo Ghosts (Training Chamber)'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.bomb_space_jump.value >= 5 and options.complex_bomb_jump.value >= 4 and options.movement.value >= 4 and options.slope_jump.value >= 1 and options.standable_terrain.value >= 2 and options.knowledge.value >= 2) else Constant(False)])]))),
                ("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)", templates['Shoot Power Beam']),
                ("Event - Unlock morph track (Training Chamber, Chozo Ruins)", lambda state: (state.has('Chozo Ghosts (Training Chamber)', player) and state.has('Boost Ball', player) and state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
                ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Piston Tunnel (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", lambda state: state.has('Training Chamber Exit Tunnel', player)),
                ("Morph Ball Door to Training Chamber (Piston Tunnel, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Training Chamber, Chozo Ruins)", (
                ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Constant(True) if ((options.movement.value >= 4)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 2) else Constant(False)]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo Ghosts (Training Chamber)'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]) if (options.bomb_space_jump.value >= 2 and options.standable_terrain.value >= 2 and options.knowledge.value >= 2) else Constant(False)])]))),
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
                ("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.movement.value >= 2) else Constant(False)])])]))),
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
                ("Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Vault Access (Vault, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Vault Access, Chozo Ruins)", (
                ("Door to Vault (Vault Access, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
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
                ("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
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
                ("Front of Gate (Arboretum, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if ((options.bomb_jump.value >= 2)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Arboretum Gate'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.clip_through_objects.value >= 1) else Constant(False)])]))),
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
                ("Front of Gate (Arboretum, Chozo Ruins)", lambda state: ((state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player)) or state.has('Space Jump Boots', player))),
                ("Door to Arboretum (Gathering Hall Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Front of Gate (Arboretum, Chozo Ruins)", (
                ("Door to Sunchamber Lobby (Arboretum, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Constant(True) if ((options.bomb_jump.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Arboretum Gate'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.single_room_oob.value >= 3 and options.standable_terrain.value >= 3 and options.clip_through_objects.value >= 4) else Constant(False)])]))),
                ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)", None),
                ("Event - Open gate (Arboretum, Chozo Ruins)", lambda state: state.has('Scan Visor', player)),
            )
            ),
            (
            "Event - Open gate (Arboretum, Chozo Ruins)", (
                ("Front of Gate (Arboretum, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Training Chamber Access (Magma Pool, Chozo Ruins)", (
                ("Door to Meditation Fountain (Magma Pool, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(70), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)]), BoolOp(Or(), [Constant(True) if (options.standable_terrain.value >= 2) else Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(220), Constant('HeatDamage2')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False)])])]))),
                ("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(60), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])]))),
                ("Door to Magma Pool (Training Chamber Access, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Door to Meditation Fountain (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Use Grapple Beam'), Load()), [Name('state', Load())], []), Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(50), Constant('HeatDamage2')], [])]) if (options.l_jump.value >= 2 and options.standable_terrain.value >= 1) else Constant(False)]), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(99), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)])])]))),
                ("Door to Magma Pool (Meditation Fountain, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)", (
                ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)", e(BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Heat-Resisting Suit'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(35), Constant('HeatDamage1')], []) if (options.heat_runs.value >= 1) else Constant(False)]))),
            )
            ),
            (
            "Door to Tower of Light Access (Tower of Light, Chozo Ruins)", (
                ("Door to Tower Chamber (Tower of Light, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])])])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1) else Constant(False), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 2) else Constant(False)]))),
                ("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)", e(
                    BoolOp(Or(), [
                        BoolOp(And(), [
                            BoolOp(And(), [
                                Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(36)], []),
                                Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])
                            ]),
                            BoolOp(Or(), [
                                Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []),
                                BoolOp(And(), [
                                    Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []),
                                    Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])
                                ]) if (options.bomb_jump.value >= 4)
                                   else Constant(False)
                            ])
                        ]),
                        Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])
                            if (
                                (
                                    (
                                        (options.scan_dash.value >= 2 and options.standable_terrain.value >= 1) or
                                        (options.scan_dash.value >= 2 and options.l_jump.value >= 2 and options.standable_terrain.value >= 2) or
                                        (options.scan_dash.value >= 2 and options.slope_jump.value >= 1 and options.standable_terrain.value >= 3) or
                                        (options.r_jump.value >= 3 and options.standable_terrain.value >= 1)
                                    )
                                )
                            ) else Constant(False)
                    ]))),
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
                ("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)", lambda state: (logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state))),
                ("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
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
                ("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)", lambda state: (state.has('Flaahgra', player))),
                ("Door to Sun Tower (Sun Tower Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Sun Tower Spider Track Unlocked'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 5 and options.movement.value >= 3) else Constant(False), Constant(True) if (options.combat.value >= 5) else BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(4)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])])])])]))),
                ("Event - Unlock spider track (Sun Tower, Chozo Ruins)", lambda state: (templates['Shoot Super Missile'](state) and state.has('Scan Visor', player))),
                ("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player) and state.has('Spider Ball', player) and state.has('Sun Tower Spider Track Unlocked', player) and state.has('Flaahgra', player))),
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
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []) if (options.knowledge.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('Damage')], [])]) if (options.complex_bomb_jump.value >= 2) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.instant_unmorph_jump.value >= 5) else Constant(False)])]))),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", None),
            )
            ),
            (
            "Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)", (
                ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player) and state.has('Spider Ball', player))),
                ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)", None),
            )
            ),
            (
            "Door to Hive Totem (Transport Access North, Chozo Ruins)", (
                ("Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
                ("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)", None),
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Transport to Magmoor Caverns North (Transport Access North, Chozo Ruins)", (
                ("Door to Hive Totem (Transport Access North, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])]))),
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
                ("Door to Sunchamber (Sunchamber Access, Chozo Ruins)", lambda state: (not state.has('Flaahgra', player) or (state.has('Flaahgra', player) and state.has('Chozo Ghosts (Sunchamber)', player)))),
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
                ("Door to East Atrium (Gathering Hall, Chozo Ruins)", e(BoolOp(Or(), [Constant(True) if (options.l_jump.value >= 1) else BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False)]))),
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
                ("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 5 and options.standable_terrain.value >= 5) else Constant(False)])]))),
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
                ("Door to Transport Access North (Hive Totem, Chozo Ruins)", e(BoolOp(Or(), [Constant(True) if ((options.knowledge.value >= 3 and options.movement.value >= 3)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hive Mecha'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.movement.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(30), Constant('RuinsWater')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flaahgra'), Name('player', Load())], [])]) if (options.slope_jump.value >= 2 and options.gravityless_underwater_movement.value >= 1) else Constant(False), UnaryOp(Not(), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('dock_rando')], [])) if (options.scan_dash.value >= 2) else Constant(False)]))),
                ("Event - Hive Mecha (Hive Totem, Chozo Ruins)", templates['Shoot Power Beam']),
                ("Door to Hive Totem (Totem Access, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Transport Access North (Hive Totem, Chozo Ruins)", (
                ("Door to Totem Access (Hive Totem, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Chozo - Fallen Rubble'), Name('player', Load())], [])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.scan_dash.value >= 1) else Constant(False)]))),
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
                ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)", lambda state: (state.has('Flaahgra', player) or state.has('Chozo Ghosts (Sunchamber)', player))),
                ("Door to Sunchamber Access (Sunchamber, Chozo Ruins)", lambda state: state.has('Chozo Ghosts (Sunchamber)', player)),
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], [])])])]), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)]) if (options.combat.value >= 1) else Constant(False)]), BoolOp(Or(), [Constant(True) if ((options.scan_dash.value >= 3 and options.combat.value >= 2)) else BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(10)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1 and options.combat.value >= 1) else Constant(False)])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Wave Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Wavebuster'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(230)], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]) if (options.combat.value >= 3) else Constant(False)]))),
                ("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Sunchamber Chozo Ghosts Layer Activated'), Name('player', Load())], []), Constant(True) if (options.combat.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.l_jump.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])])]))),
            )
            ),
            (
            "Before Fight (Back) (Sunchamber, Chozo Ruins)", (
                ("Event - Flaahgra (Sunchamber, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Compare(Call(Attribute(Name('state', Load()), 'count', Load()), [Constant('Power Bomb'), Name('player', Load())], []), [GtE()], [Constant(4)])])]) if (options.knowledge.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1) else Constant(False)]))),
            )
            ),
            (
            "Door to Gathering Hall (Watery Hall Access, Chozo Ruins)", (
                ("Door to Watery Hall (Watery Hall Access, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('logic', Load()), 'has_missiles', Load()), [Name('state', Load()), Name('player', Load()), Constant(1)], []), Call(Subscript(Name('templates', Load()), Constant('Shoot Any Beam'), Load()), [Name('state', Load())], [])]), BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]) if (options.knowledge.value >= 1) else Constant(False)]))),
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
                ("Behind Gate (Watery Hall, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
                ("Door to Watery Hall (Dynamo Access, Chozo Ruins)", dock_requirements['Missile Blast Shield']),
            )
            ),
            (
            "Door to Watery Hall Access (Watery Hall, Chozo Ruins)", (
                ("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)", e(BoolOp(And(), [BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(57), Constant('RuinsWater')], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Flaahgra'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(25), Constant('RuinsWater')], [])])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(15), Constant('RuinsWater')], [])]) if (options.bomb_jump.value >= 1) else Constant(False), BoolOp(And(), [UnaryOp(Not(), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])), Call(Attribute(Name('logic', Load()), 'has_misc', Load()), [Name('state', Load()), Name('player', Load()), Constant('NoGravity')], [])]) if (options.slope_jump.value >= 3 and options.gravityless_underwater_movement.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Constant(True) if ((options.slope_jump.value >= 1 and options.gravityless_underwater_movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], [])]), BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Gravity Suit'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.wall_boost.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(65), Constant('RuinsWater')], []) if (options.movement.value >= 2) else Constant(False), Call(Attribute(Name('logic', Load()), 'can_sustain_damage', Load()), [Name('state', Load()), Name('player', Load()), Constant(20), Constant('RuinsWater')], []) if (options.movement.value >= 4) else Constant(False)])])])]))),
                ("Event - Open gate (Watery Hall, Chozo Ruins)", lambda state: state.has('Scan Visor', player)),
                ("Behind Gate (Watery Hall, Chozo Ruins)", lambda state: state.has('Watery Hall Gate', player)),
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
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", lambda state: (state.has('Flaahgra', player) or logic.can_sustain_damage(state, player, 42, 'RuinsWater') or (state.has('Gravity Suit', player) and logic.can_sustain_damage(state, player, 25, 'RuinsWater')))),
            )
            ),
            (
            "Event - Open gate (Watery Hall, Chozo Ruins)", (
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", None),
            )
            ),
            (
            "Behind Gate (Watery Hall, Chozo Ruins)", (
                ("Door to Dynamo Access (Watery Hall, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.single_room_oob.value >= 3 and options.clip_through_objects.value >= 4 and options.standable_terrain.value >= 3) else Constant(False), Constant(True) if ((options.movement.value >= 4)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], [])])])]))),
                ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Watery Hall Gate'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.clip_through_objects.value >= 1) else Constant(False)]))),
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
                ("Door to Energy Core Access (Energy Core, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
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
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
                ("Door to West Furnace Access (Energy Core, Chozo Ruins)", lambda state: state.has('West Furnace Access Door Unlocked', player)),
                ("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)", lambda state: (state.has('Morph Ball', player) and state.has('Morph Ball Bomb', player))),
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
                ("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)", lambda state: (logic.has_missiles(state, player, 1) and templates['Shoot Any Beam'](state))),
                ("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False)])]))),
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
                ("Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])]))),
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Morph Ball Door to Energy Core (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
                ("Morph Ball Door to Burn Dome Access (Energy Core, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Spawn Point (Burn Dome Access, Chozo Ruins)", (
                ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
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
                ("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
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
                ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)", lambda state: state.has('Incinerator Drone', player)),
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
                ("Event - Incinerator Drone (Burn Dome, Chozo Ruins)", lambda state: (templates['Shoot Power Beam'](state) or templates['Shoot Wave Beam'](state) or templates['Shoot Ice Beam'](state))),
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
                ("Pickup (Energy Tank) (Furnace, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 2) else Constant(False)])]))),
                ("Under Spider Track (Furnace, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Constant(True) if (options.standable_terrain.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
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
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])]))),
            )
            ),
            (
            "Under Spider Track (Furnace, Chozo Ruins)", (
                ("Door to East Furnace Access (Furnace, Chozo Ruins)", e(BoolOp(Or(), [Constant(True) if (options.l_jump.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
                ("Door to West Furnace Access (Furnace, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 3) else Constant(False)])]))),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", lambda state: state.has('Morph Ball', player)),
                ("Pickup (Missile Expansion) (Furnace, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]), Constant(True) if (options.wall_boost.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 3) else Constant(False)])]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 3) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Constant(True) if ((options.movement.value >= 1)) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])])])])])]))),
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
                ("Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3) else Constant(False)]))),
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", dock_requirements['Wave Door']),
            )
            ),
            (
            "Morph Ball Door to Furnace (Crossway Access West, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 3) else Constant(False)]))),
                ("Morph Ball Door to Crossway Access West (Furnace, Chozo Ruins)", dock_requirements['Morph Ball Door']),
            )
            ),
            (
            "Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", (
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", lambda state: state.has('Scan Visor', player)),
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
                ("Room Center (Hall of the Elders, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Statue'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]) if (options.clip_through_objects.value >= 3) else Constant(False)]))),
                ("Door to Hall of the Elders (Elder Chamber, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", (
                ("Room Center (Hall of the Elders, Chozo Ruins)", lambda state: (state.has('Hall of the Elders Unlock Doors', player) and state.has('Hall of the Elders Bomb Slots', player))),
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
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", lambda state: (state.has('Hall of the Elders Unlock Doors', player))),
                ("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)", lambda state: (state.has('Hall of the Elders Unlock Doors', player) and state.has('Hall of the Elders Bomb Slots', player) and templates['Shoot Ice Beam'](state))),
                ("Event - Statue Moved (Hall of the Elders, Chozo Ruins)", lambda state: (templates['Shoot Plasma Beam'](state) and state.has('Hall of the Elders Bomb Slots', player))),
                ("Room Center (Hall of the Elders, Chozo Ruins)", None),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", lambda state: ((templates['Shoot Wave Beam'](state) and state.has('Hall of the Elders Bomb Slots', player) and state.has('Hall of the Elders Unlock Doors', player)))),
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
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Unlock Doors'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)])]))),
                ("Door to East Furnace Access (Hall of the Elders, Chozo Ruins)", lambda state: (state.has('Hall of the Elders Unlock Doors', player))),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", lambda state: state.has('Hall of the Elders Unlock Doors', player)),
                ("Door to Elder Chamber (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Statue'), Name('player', Load())], []), Constant(True) if (options.knowledge.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Unlock Doors'), Name('player', Load())], [])]))),
                ("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Unlock Doors'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 1) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.bomb_jump.value >= 5 and options.scan_dash.value >= 4 and options.standable_terrain.value >= 1) else Constant(False)])]))),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 1) else Constant(False)]))),
                ("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [Call(Subscript(Name('templates', Load()), Constant('Shoot Power Beam'), Load()), [Name('state', Load())], []), Constant(True) if (options.combat.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Charge Beam'), Name('player', Load())], [])]))),
                ("Behind Barrier (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Unlock Doors'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 4) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Barrier'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.bomb_jump.value >= 1) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.scan_dash.value >= 3 and options.instant_unmorph_jump.value >= 4 and options.movement.value >= 3 and options.standable_terrain.value >= 2 and options.wall_boost.value >= 3) else Constant(False)])])])])])]))),
            )
            ),
            (
            "Behind Barrier (Hall of the Elders, Chozo Ruins)", (
                ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)", None),
                ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Unlock Doors'), Name('player', Load())], [])]), BoolOp(Or(), [Constant(True) if (options.movement.value >= 1) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])]))),
                ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.knowledge.value >= 3 and options.l_jump.value >= 2 and options.standable_terrain.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Barrier'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.movement.value >= 1) else Constant(False)])])]))),
                ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)", lambda state: (state.has('Scan Visor', player))),
                ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Barrier'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.movement.value >= 2) else Constant(False), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])])]))),
                ("Room Center (Hall of the Elders, Chozo Ruins)", e(BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Hall of the Elders Barrier'), Name('player', Load())], []), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 1) else Constant(False)])])]))),
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
                ("Door to Elder Hall Access (Crossway, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if (options.complex_bomb_jump.value >= 4) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1) else Constant(False)]))),
                ("Door to Crossway (Crossway Access West, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Door to Elder Hall Access (Crossway, Chozo Ruins)", (
                ("Door to Crossway Access West (Crossway, Chozo Ruins)", None),
                ("Pickup (Missile Expansion) (Crossway, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Crossway Bomb Slots'), Name('player', Load())], [])]), Constant(True) if (options.movement.value >= 2) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Spider Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.l_jump.value >= 1 and options.standable_terrain.value >= 2) else Constant(False), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], []) if (options.movement.value >= 3 and options.standable_terrain.value >= 3 and options.scan_dash.value >= 4) else Constant(False)]), BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Scan Visor'), Name('player', Load())], [])]) if (options.bomb_jump.value >= 3 and options.standable_terrain.value >= 4 and options.scan_dash.value >= 4 and options.bomb_space_jump.value >= 4) else Constant(False)])]))),
                ("Event - Activate Bomb Slots (Crossway, Chozo Ruins)", lambda state: (templates['Shoot Super Missile'](state) and state.has('Scan Visor', player))),
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
                ("Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
                ("Door to Crossway Access South (Crossway, Chozo Ruins)", dock_requirements['Ice Door']),
            )
            ),
            (
            "Door to Hall of the Elders (Crossway Access South, Chozo Ruins)", (
                ("Door to Crossway (Crossway Access South, Chozo Ruins)", lambda state: (state.has('Morph Ball', player))),
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
                ("Door to Antechamber (Reflecting Pool, Chozo Ruins)", e(BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Reflecting Pool Water Drained'), Name('player', Load())], []), Constant(True) if (options.movement.value >= 3) else Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], [])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []) if ((options.complex_bomb_jump.value >= 4 or options.bomb_space_jump.value >= 4) and options.standable_terrain.value >= 3) else Constant(False)])]), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.slope_jump.value >= 1 and options.standable_terrain.value >= 1) else Constant(False)]))),
                ("Event - Drain water (Reflecting Pool, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Power Bomb'), Name('player', Load())], []) if (options.knowledge.value >= 1) else Constant(False)])]))),
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
                ("Save Station (Save Station 3, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 4) else Constant(False)])]))),
                ("Door to Save Station 3 (Transport to Tallon Overworld East, Chozo Ruins)", dock_requirements['Normal Door']),
            )
            ),
            (
            "Save Station (Save Station 3, Chozo Ruins)", (
                ("Door to Reflecting Pool (Save Station 3, Chozo Ruins)", None),
                ("Door to Transport to Tallon Overworld East (Save Station 3, Chozo Ruins)", e(BoolOp(And(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball'), Name('player', Load())], []), BoolOp(Or(), [Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Morph Ball Bomb'), Name('player', Load())], []), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Space Jump Boots'), Name('player', Load())], []) if (options.standable_terrain.value >= 2 and options.movement.value >= 3) else Constant(False), Call(Attribute(Name('state', Load()), 'has', Load()), [Constant('Boost Ball'), Name('player', Load())], []) if (options.wall_boost.value >= 5) else Constant(False)])]))),
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