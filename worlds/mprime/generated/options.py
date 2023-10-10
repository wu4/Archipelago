from dataclasses import dataclass
from Options import Range

Dash=type("Dash",(Range,),{"__doc__":"""By locking onto an enemy or scan point and strafing left or right, Samus' momentum can be maintainted. If this trick is enabled, the player may be expected to abuse this quirk to cross large gaps.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/Dash_Jump_(Prime))""","display_name":"Combat/Scan Dash","range_start":0,"range_end":5,"default":0})
Knowledge=type("Knowledge",(Range,),{"__doc__":"""Some destructible objects have vulnerabilities other than those which the player is informed of. Enabling this trick may require players to apply this knowledge in order to progress.""","display_name":"Knowledge","range_start":0,"range_end":5,"default":0})
Combat=type("Combat",(Range,),{"__doc__":"""If this trick is enabled, the player may be expected to defeat enemies and bosses with fewer items and less health. On Beginner or higher, Charge Beam may be locked behind many of the game's mandatory fights.""","display_name":"Combat","range_start":0,"range_end":5,"default":0})
LJump=type("LJump",(Range,),{"__doc__":"""By holding and releasing the L button at specific points in a jump, Samus can jump further than normal. If this trick is enabled, the player may be expected to cross some gaps in this way.""","display_name":"L-Jump","range_start":0,"range_end":5,"default":0})
InvisibleObjects=type("InvisibleObjects",(Range,),{"__doc__":"""Some objects that normally need visors to be seen, such as Power Conduits or Invisible Platforms, can still be used without the appropriate visor. If enabled, the player may be expected to use these objects even though they cannot see them.""","display_name":"Invisible Objects","range_start":0,"range_end":5,"default":0})
DBoosting=type("DBoosting",(Range,),{"__doc__":"""Some damage sources give Samus extra velocity, which can be used to give her a small boost. Enabling this trick may force players to use this to their advantage.""","display_name":"Damage Boosting","range_start":0,"range_end":5,"default":0})
Movement=type("Movement",(Range,),{"__doc__":"""A broad category for non-obvious movement which can't easily be classified using other tricks. Enabling this will require the player to have a greater understanding of movement and physics in Metroid Prime.""","display_name":"Movement","range_start":0,"range_end":5,"default":0})
SJump=type("SJump",(Range,),{"__doc__":"""By L-Jumping into sloped surfaces in a specific manner, Samus' jumps can gain extra height due to quirks in the game's physics engine. Enabling this trick may require the player to abuse this extra height to reach places which would otherwise be inaccessible.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/Slope_Jump)""","display_name":"Slope Jump","range_start":0,"range_end":5,"default":0})
Standable=type("Standable",(Range,),{"__doc__":"""Samus can maneuver in unexpected ways by standing on small ledges, vines, railings, and other unlikely objects. Enabling this trick may mean that players are expected to climb on the scenery to reach unintended places.""","display_name":"Standable Terrain","range_start":0,"range_end":5,"default":0})
BJ=type("BJ",(Range,),{"__doc__":"""By using the vanilla Bomb Jump mechanic in unexpected locations, Samus can clear jumps normally meant to require the use of other items. Enabling this trick means that the player may be expected to use standard bomb jumps in places other than morph tunnels.""","display_name":"Bomb Jump","range_start":0,"range_end":5,"default":0})
StandEnemies=type("StandEnemies",(Range,),{"__doc__":"""Samus can stand on top of some non-obvious enemies, such as Baby Sheegoths, and jump off of them for extra height. Enabling this trick means that players may be expected to abuse this mechanic to reach uninteded places.""","display_name":"Jump Off Enemies","range_start":0,"range_end":5,"default":0})
ClipThruObjects=type("ClipThruObjects",(Range,),{"__doc__":"""When Samus reaches some in-game barriers from the wrong side, she may be able to clip through with the Boost Ball or a reposition. Enabling this trick will place this in logic.""","display_name":"Clip Through Objects","range_start":0,"range_end":5,"default":0})
RJump=type("RJump",(Range,),{"__doc__":"""This trick allows Samus to jump farther than usual by pressing R in the air. Enabling this trick means that players may be expected to perform R-Jumps to reach areas they otherwise couldn't.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/R-Jumping)""","display_name":"R-Jump","range_start":0,"range_end":5,"default":0})
BSJ=type("BSJ",(Range,),{"__doc__":"""Bomb Jumping and unmorphing forwards from an overhang to get an instant unmorph, then jumping within 2/5 of a second after leaving the ground gives Samus a height boost which can be used to reach higher ledges.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/Bomb_Space_Jump)""","display_name":"Bomb Space Jump","range_start":0,"range_end":5,"default":0})
WallBoost=type("WallBoost",(Range,),{"__doc__":"""Using the Boost Ball, a well placed boost can be used to scale some terrain while morphed. For example, it is possible to leave Burn Dome without Bombs using this method.""","display_name":"Wall Boost","range_start":0,"range_end":5,"default":0})
BoostlessSpiner=type("BoostlessSpiner",(Range,),{"__doc__":"""Some spinners can be turned without the Boost Ball. The exact method required to do this varies. Enabling this trick may require spinners to be turned before obtaining the Boost Ball.""","display_name":"Spinners without Boost","range_start":0,"range_end":5,"default":0})
OoB=type("OoB",(Range,),{"__doc__":"""Samus can travel outside the room's boundaries to gain access to areas/rooms otherwise unreachable given the circumstances. Currently, enabling this trick will only affect single-room traversal.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/Out_of_Bounds)""","display_name":"Single Room Out of Bounds","range_start":0,"range_end":5,"default":0})
HeatRun=type("HeatRun",(Range,),{"__doc__":"""Although Samus takes constant damage in heated rooms, she doesn't necessarily need protection to enter or traverse them. Enabling this trick may require the player to perform Heat Runs, where they are forced to endure heated rooms while still vulnerable to their damage. The logic will provide more Energy Tanks to account for the presence of Heat Runs, but at higher difficulties and with other tricks enabled, players may be expected to perform Heat Runs with less health.""","display_name":"Heat Runs","range_start":0,"range_end":5,"default":0})
CBJ=type("CBJ",(Range,),{"__doc__":"""By abusing the Bomb Refill timer, Samus can reach heights that are normally inaccessible with a standard bomb jump. Enabling this trick allows logic to include High Bomb Jumps, Half Pipe Bomb Jumps, and Uber Bomb Jumps.\nCheck the wiki for more details. (https://wiki.metroidprime.run/wiki/Bomb_Jump)""","display_name":"Complex Bomb Jump","range_start":0,"range_end":5,"default":0})
IS=type("IS",(Range,),{"__doc__":"""Abuse infinite rotational speed to probe the room's collision tree and collect items otherwise out of reach.""","display_name":"Infinite Speed","range_start":0,"range_end":5,"default":0})
UnderwaterMovement=type("UnderwaterMovement",(Range,),{"__doc__":"""Abuse Slope Jumps and/or Bomb Jumps to circumvent the negative effects of being underwater without Gravity Suit.""","display_name":"Gravityless Underwater Movement","range_start":0,"range_end":5,"default":0})
IUJ=type("IUJ",(Range,),{"__doc__":"""Similar to BSJs except you don't use bombs. Obstruct the camera in a way that will let Samus unmorph and be able to jump within 2/5 of a second after leaving the ground.""","display_name":"Instant Unmorph Jump","range_start":0,"range_end":5,"default":0})
@dataclass
class GeneratedOptions:
    scan_dash:Dash
    knowledge:Knowledge
    combat:Combat
    l_jump:LJump
    invisible_objects:InvisibleObjects
    damage_boosting:DBoosting
    movement:Movement
    slope_jump:SJump
    standable_terrain:Standable
    bomb_jump:BJ
    jump_off_enemies:StandEnemies
    clip_through_objects:ClipThruObjects
    r_jump:RJump
    bomb_space_jump:BSJ
    wall_boost:WallBoost
    spinners_without_boost:BoostlessSpiner
    single_room_oob:OoB
    heat_runs:HeatRun
    complex_bomb_jump:CBJ
    infinite_speed:IS
    gravityless_underwater_movement:UnderwaterMovement
    instant_unmorph_jump:IUJ