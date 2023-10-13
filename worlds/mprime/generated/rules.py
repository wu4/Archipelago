from BaseClasses import CollectionState
from worlds.AutoWorld import World
from typing import Callable, Optional, cast

ConnectionRule = Callable[[CollectionState], bool]
ConnectionNameTuple = tuple[str, Optional[ConnectionRule]]
NodeRules = tuple[str, tuple[ConnectionNameTuple, ...]]

def set_rules(self: World):
 from ..options import MetroidPrimeOptions
 from ..logic import can_sustain_damage as l_csd,has_misc as l_hmisc,has_missiles as l_hm
 p=self.player
 o=cast(MetroidPrimeOptions, self.options)
 t: dict[str, ConnectionRule] = {
  "Shoot Super Missile": lambda s:(s.has('Power Beam',p) and l_hm(s, p, 5) and s.has('Charge Beam',p) and s.has('Super Missile',p) and t['Can Use Arm Cannon'](s)),
  "Have all Beams": lambda s:(s.has('Power Beam',p) and s.has('Wave Beam',p) and s.has('Ice Beam',p) and s.has('Plasma Beam',p) and t['Can Use Arm Cannon'](s)),
  "Heat-Resisting Suit": lambda s:(s.has('Gravity Suit',p) or s.has('Varia Suit',p) or s.has('Phazon Suit',p)),
  "Can Use Arm Cannon": lambda s:(s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p)),
  "Shoot Any Beam": lambda s:(t['Can Use Arm Cannon'](s) and (s.has('Power Beam',p) or s.has('Wave Beam',p) or s.has('Ice Beam',p) or s.has('Plasma Beam',p))),
  "Shoot Power Beam": lambda s:(s.has('Power Beam',p) and t['Can Use Arm Cannon'](s)),
  "Shoot Wave Beam": lambda s:(s.has('Wave Beam',p) and t['Can Use Arm Cannon'](s)),
  "Shoot Ice Beam": lambda s:(s.has('Ice Beam',p) and t['Can Use Arm Cannon'](s)),
  "Shoot Plasma Beam": lambda s:(s.has('Plasma Beam',p) and t['Can Use Arm Cannon'](s)),
  "Use Grapple Beam": lambda s:(s.has('Grapple Beam',p) and t['Can Use Arm Cannon'](s)),
  "Open Normal Door": lambda s:(t['Shoot Any Beam'](s) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Scan Visor',p))),
  "Move Past Scatter Bombu": lambda s:(s.has('Morph Ball',p) or (o.movement.value>=1 and l_csd(s,p,12,'Damage')) or o.movement.value>=2 or l_csd(s,p,30,'Damage') or t['Shoot Wave Beam'](s)),
 }
 entrance_rules:tuple[NodeRules,...]=(
("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)",(
 ("Save Station (Crater Entry Point, Impact Crater)",None),
 ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)",None),
 ("Door to Crater Missile Station (Phazon Core, Impact Crater)",lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4 and o.complex_bomb_jump.value>=5 and o.slope_jump.value>=3 and o.standable_terrain.value>=4) or (s.has('Scan Visor',p) and o.l_jump.value>=4 and o.standable_terrain.value>=4 and o.scan_dash.value>=4 and o.slope_jump.value>=4)))),)),
("Save Station (Crater Entry Point, Impact Crater)",(
 ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)",None),)),
("Door to Crater Missile Station (Phazon Core, Impact Crater)",(
 ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Teleporter to Credits (Metroid Prime Lair, Impact Crater)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=5 and (o.l_jump.value>=4 or (s.has('Scan Visor',p) and o.scan_dash.value>=2))) or (o.scan_dash.value>=4 and o.standable_terrain.value>=4 and o.jump_off_enemies.value>=5)) and t['Shoot Plasma Beam'](s) and ((s.has('Space Jump Boots',p) and o.movement.value>=1 and l_csd(s,p,5,'Damage')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (s.has('Spider Ball',p) or (o.bomb_jump.value>=1 and l_csd(s,p,40,'Damage') and o.movement.value>=1)))) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p))) and (t['Shoot Wave Beam'](s) and (s.has('Charge Beam',p) or o.combat.value>=2) and (t['Shoot Power Beam'](s) or (s.has('Plasma Beam',p) and s.has('Flamethrower',p) and l_hm(s, p, 25) and s.has('Charge Beam',p) and o.combat.value>=2 and o.knowledge.value>=2)) and (l_csd(s,p,54,'Damage') or o.combat.value>=1)) and (t['Shoot Ice Beam'](s) and (t['Shoot Power Beam'](s) or (s.has('Plasma Beam',p) and s.has('Charge Beam',p) and l_hm(s, p, 25) and o.combat.value>=2 and o.knowledge.value>=2 and s.has('Flamethrower',p))) and (l_csd(s,p,76,'Damage') or s.has('Morph Ball',p) or o.combat.value>=1) and (l_csd(s,p,119,'Damage') or o.combat.value>=1)) and ((t['Shoot Power Beam'](s) or (s.has('Charge Beam',p) and l_hm(s, p, 25) and s.has('Flamethrower',p) and o.combat.value>=2 and o.knowledge.value>=2)) and (l_csd(s,p,179,'Damage') or o.combat.value>=1)) and ((t['Have all Beams'](s) or (t['Shoot Any Beam'](s) and o.combat.value>=3)) and ((s.has('Morph Ball',p) or l_csd(s,p,99,'Damage') or o.combat.value>=1) and ((l_csd(s,p,239,'Damage') or o.combat.value>=2) or (l_csd(s,p,149,'Damage') and o.combat.value>=1)))) and (s.has('Phazon Suit',p) and ((s.has('X-Ray Visor',p) and s.has('Thermal Visor',p)) or o.invisible_objects.value>=3) and (s.has('Charge Beam',p) or o.combat.value>=1) and (s.has('Space Jump Boots',p) or o.combat.value>=3) and ((s.has('Morph Ball',p) and s.has('Power Bomb',p,2)) or l_hm(s, p, 5) or o.combat.value>=3) and (o.combat.value>=5 or (o.combat.value>=4 and l_csd(s,p,99,'Damage')) or (o.combat.value>=3 and l_csd(s,p,149,'Damage')) or (o.combat.value>=2 and l_csd(s,p,199,'Damage')) or (o.combat.value>=1 and l_csd(s,p,249,'Damage')) or l_csd(s,p,299,'Damage')) and t['Shoot Any Beam'](s)))),
 ("Missile Station (Crater Missile Station, Impact Crater)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Teleporter to Credits (Metroid Prime Lair, Impact Crater)",(
 ("Event - Credits (Credits, End of Game)",None),)),
("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=3) or o.scan_dash.value>=4)),
 ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4))),
 ("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Save Station (Save Station B, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),
 ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (s.has('Charge Beam',p) or l_hm(s, p, 1) or s.has('Plasma Beam',p)) and t['Move Past Scatter Bombu'](s)) and (s.has('Scan Visor',p) and l_hm(s, p, 1)))),
 ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (s.has('Charge Beam',p) or l_hm(s, p, 3))))),)),
("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",None),
 ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)",lambda s:(t['Shoot Super Missile'](s) and s.has('Scan Visor',p) and s.has('Morph Ball',p) and s.has('Spider Ball',p))),
 ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (l_hm(s, p, 1) or s.has('Plasma Beam',p) or (s.has('Charge Beam',p) and (s.has('Power Beam',p) or s.has('Wave Beam',p)))) and t['Move Past Scatter Bombu'](s)) and (s.has('Space Jump Boots',p) or ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (o.jump_off_enemies.value>=3 and o.movement.value>=3 and o.scan_dash.value>=4 and o.l_jump.value>=2 and l_csd(s,p,50,'Damage')))))),)),
("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",None),
 ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)",lambda s:(o.scan_dash.value>=2 and (s.has('Scan Visor',p) or s.has('X-Ray Visor',p)))),
 ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)",None),
 ("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and o.single_room_oob.value>=3 and o.standable_terrain.value>=3 and s.has('Space Jump Boots',p) and s.has('Boost Ball',p) and t['Shoot Super Missile'](s) and s.has('Scan Visor',p) and o.scan_dash.value>=2 and o.movement.value>=3 and not l_hmisc(s,p,'dock_rando'))),
 ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",None),
 ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)",None),
 ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Behind Ice) (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",None),)),
("Pickup (Spider Track Missile) (Phendrana Shorelines, Phendrana Drifts)",(
 ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)",None),)),
("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)",(
 ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",None),)),
("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",(
 ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",None),)),
("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",(
 ("Pickup (Artifact of Sun) (Chozo Ice Temple, Phendrana Drifts)",lambda s:(t['Shoot Plasma Beam'](s) and s.has('Morph Ball',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2) or (o.scan_dash.value>=3 and o.standable_terrain.value>=1 and not s.has('Chozo Ice Temple Bomb Slot',p)) or (s.has('Chozo Ice Temple Bomb Slot',p) and o.standable_terrain.value>=3 and o.l_jump.value>=2)))),
 ("Event - Chozo Ice Temple Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and l_hm(s, p, 1) and t['Shoot Any Beam'](s) and s.has('Morph Ball Bomb',p))),
 ("Door to Temple Entryway (Phendrana Shorelines, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (s.has('Plasma Beam',p) or l_hm(s, p, 1) or (s.has('Charge Beam',p) and (s.has('Power Beam',p) or s.has('Wave Beam',p)))) and t['Move Past Scatter Bombu'](s)))),
 ("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)",lambda s:(s.has('Chozo Ice Temple Bomb Slot',p) and t['Open Normal Door'](s) and (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p)) and ((t['Shoot Any Beam'](s) and l_hm(s, p, 25)) or ((s.has('Power Bomb',p) and o.combat.value>=1) and t['Shoot Any Beam'](s)) or (l_hm(s, p, 17) and t['Shoot Any Beam'](s) and o.combat.value>=1) or (o.combat.value>=3 and s.has('Power Bomb',p,4) and l_csd(s,p,100,'Damage'))))),)),
("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and o.slope_jump.value>=1) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=3))),
 ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and ((l_hm(s, p, 1) and t['Shoot Any Beam'](s) and o.l_jump.value>=1) or (not s.has('Research Core Power Outage',p) and ((l_hm(s, p, 1) and t['Shoot Any Beam'](s) and o.scan_dash.value>=1) or o.scan_dash.value>=2)) or (s.has('Research Core Power Outage',p) and ((l_hm(s, p, 1) and t['Shoot Any Beam'](s) and s.has('Scan Visor',p) and o.scan_dash.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=2))))) or (s.has('Space Jump Boots',p) and ((t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or (o.jump_off_enemies.value>=1 and not s.has('Research Core Power Outage',p) and l_csd(s,p,10,'Damage')) or (o.jump_off_enemies.value>=2 and s.has('Research Core Power Outage',p)) or o.slope_jump.value>=1)) or (o.jump_off_enemies.value>=5 and not s.has('Research Core Power Outage',p) and o.l_jump.value>=1 and l_csd(s,p,10,'Damage') and o.damage_boosting.value>=3))),
 ("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Move Past Scatter Bombu'](s) and t['Open Normal Door'](s) and (s.has('Space Jump Boots',p) or s.has('Scan Visor',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.movement.value>=4)))),
 ("Door to Ruins Entryway (Phendrana Shorelines, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)",(
 ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)",None),
 ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)",lambda s:s.has('Space Jump Boots',p)),
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and t['Shoot Wave Beam'](s))),)),
("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)",(
 ("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2))),)),
("Middle-Left Rooftop (Ice Ruins West, Phendrana Drifts)",(
 ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)",None),
 ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (o.scan_dash.value>=1 and not s.has('Research Core Power Outage',p)))),
 ("Pickup (Power Bomb) (Ice Ruins West, Phendrana Drifts)",lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Space Jump Boots',p) or (o.standable_terrain.value>=1 or o.l_jump.value>=1) or ((not s.has('Research Core Power Outage',p) and o.scan_dash.value>=1) or (s.has('Research Core Power Outage',p) and s.has('Scan Visor',p) and o.scan_dash.value>=1))))),)),
("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)",(
 ("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (s.has('Spider Ball',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4)))),
 ("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Door to Plaza Walkway (Phendrana Shorelines, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (s.has('Charge Beam',p) or s.has('Plasma Beam',p) or l_hm(s, p, 1)) and t['Move Past Scatter Bombu'](s)))),)),
("Pickup (Spider Track Missile Expansion) (Ice Ruins East, Phendrana Drifts)",(
 ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)",None),)),
("Pickup (Missile Expansion Behind Ice) (Ice Ruins East, Phendrana Drifts)",(
 ("Door to Ice Ruins Access (Ice Ruins East, Phendrana Drifts)",None),)),
("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and s.has('Spider Ball',p) and (s.has('Space Jump Boots',p) or (o.bomb_jump.value>=1 and s.has('Morph Ball Bomb',p)) or o.slope_jump.value>=3))),
 ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (o.standable_terrain.value>=2 or o.r_jump.value>=2)) or (s.has('Morph Ball',p) and ((s.has('Scan Visor',p) and o.bomb_jump.value>=3 and o.scan_dash.value>=3 and o.standable_terrain.value>=3) or (s.has('Boost Ball',p) and o.bomb_jump.value>=2) or (s.has('Boost Ball',p) and s.has('Space Jump Boots',p))) and s.has('Morph Ball Bomb',p)))),
 ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (s.has('Boost Ball',p) or (s.has('Scan Visor',p) and o.bomb_jump.value>=3 and o.scan_dash.value>=2 and o.standable_terrain.value>=2))) or (s.has('Space Jump Boots',p) and (o.standable_terrain.value>=2 or o.r_jump.value>=2)))),
 ("Door to Courtyard Entryway (Ice Ruins West, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),
 ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Scan Visor',p) and o.scan_dash.value>=2))),
 ("Save Station (Save Station A, Phendrana Drifts)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),
 ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or o.l_jump.value>=2)),
 ("Door to Map Station (Research Entrance, Phendrana Drifts)",lambda s:(((s.has('Charge Beam',p) or o.combat.value>=2 or s.has('Plasma Beam',p) or l_csd(s,p,300,'Damage')) and (t['Shoot Any Beam'](s) or (s.has('Morph Ball',p) and o.combat.value>=2 and (s.has('Morph Ball Bomb',p) or s.has('Power Bomb',p,4))))) and t['Shoot Wave Beam'](s))),)),
("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),
 ("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)",None),
 ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p) and t['Shoot Wave Beam'](s))),)),
("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),)),
("Top Middle Platform (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),
 ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Scan Visor',p) and o.scan_dash.value>=3))),
 ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or o.l_jump.value>=2)),
 ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)",lambda s:(t['Shoot Super Missile'](s) and t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))),
 ("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and o.movement.value>=2))),)),
("Front of Tunnel (Ruined Courtyard, Phendrana Drifts)",(
 ("Door to Courtyard Entryway (Ruined Courtyard, Phendrana Drifts)",None),
 ("Pickup (Energy Tank) (Ruined Courtyard, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or o.standable_terrain.value>=1))),)),
("Door to Map Station (Research Entrance, Phendrana Drifts)",(
 ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s))),
 ("Door to Specimen Storage (Ruined Courtyard, Phendrana Drifts)",lambda s:(((s.has('Charge Beam',p) or o.combat.value>=2 or s.has('Plasma Beam',p) or l_csd(s,p,300,'Damage')) and (t['Shoot Any Beam'](s) or (s.has('Morph Ball',p) and o.combat.value>=2 and (s.has('Morph Ball Bomb',p) or s.has('Power Bomb',p,4))))) and t['Shoot Wave Beam'](s))),
 ("Map Station (Map Station, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",(
 ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) and o.slope_jump.value>=5 and o.r_jump.value>=3 and o.standable_terrain.value>=3)),
 ("Room Center (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Scan Visor',p) and s.has('Space Jump Boots',p) and o.scan_dash.value>=2 and o.knowledge.value>=2)),
 ("Fight Trigger (Quarantine Cave, Phendrana Drifts)",None),
 ("Door to Quarantine Access (Ruined Courtyard, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",(
 ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.l_jump.value>=2 and ((s.has('Scan Visor',p) and o.scan_dash.value>=3) or o.r_jump.value>=3))),
 ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and s.has('Scan Visor',p) and o.scan_dash.value>=2) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.r_jump.value>=4)))),
 ("Room Center (Quarantine Cave, Phendrana Drifts)",None),
 ("Fight Trigger (Quarantine Cave, Phendrana Drifts)",None),
 ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)",(
 ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.l_jump.value>=2 and (o.r_jump.value>=4 or (s.has('Scan Visor',p) and o.scan_dash.value>=3)))),
 ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and s.has('Scan Visor',p) and o.scan_dash.value>=3) or (s.has('Space Jump Boots',p) and o.r_jump.value>=4 and o.standable_terrain.value>=3)))),
 ("Room Center (Quarantine Cave, Phendrana Drifts)",lambda s:s.has('Morph Ball',p)),
 ("Fight Trigger (Quarantine Cave, Phendrana Drifts)",lambda s:s.has('Morph Ball',p)),
 ("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Event - Thardus (Quarantine Cave, Phendrana Drifts)",(
 ("Room Center (Quarantine Cave, Phendrana Drifts)",None),)),
("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)",(
 ("Room Center (Quarantine Cave, Phendrana Drifts)",None),)),
("Room Center (Quarantine Cave, Phendrana Drifts)",(
 ("Door to North Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:((s.has('Thardus',p) and ((s.has('Morph Ball',p) and s.has('Spider Ball',p)) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=3))) or (o.jump_off_enemies.value>=5 and (o.damage_boosting.value>=5 or (s.has('Space Jump Boots',p) and o.damage_boosting.value>=4)) and l_csd(s,p,30,'Damage') and not s.has('Thardus',p)) or (s.has('Spider Ball',p) and s.has('Morph Ball',p) and s.has('Space Jump Boots',p) and (o.movement.value>=2 or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1)) and o.standable_terrain.value>=2 and o.l_jump.value>=2 and (o.knowledge.value>=2 or s.has('Thardus',p))))),
 ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and s.has('Spider Ball',p)) or (t['Use Grapple Beam'](s) and (s.has('Space Jump Boots',p) or o.movement.value>=3)))),
 ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and ((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.slope_jump.value>=4)) or (t['Use Grapple Beam'](s) and o.movement.value>=2) or (s.has('Spider Ball',p) and (o.movement.value>=2 or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2)) and ((s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and ((s.has('Scan Visor',p) and o.scan_dash.value>=3) or o.r_jump.value>=3)) or (s.has('Scan Visor',p) and o.standable_terrain.value>=4 and o.scan_dash.value>=4)) and (o.knowledge.value>=2 or s.has('Thardus',p)))))),
 ("Pickup (Spider Ball) (Quarantine Cave, Phendrana Drifts)",lambda s:s.has('Thardus',p)),
 ("Fight Trigger (Quarantine Cave, Phendrana Drifts)",None),)),
("Fight Trigger (Quarantine Cave, Phendrana Drifts)",(
 ("Event - Thardus (Quarantine Cave, Phendrana Drifts)",lambda s:(((s.has('Thermal Visor',p) or o.invisible_objects.value>=1 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.combat.value>=1)) and (s.has('Combat Visor',p) or s.has('X-Ray Visor',p) or ((s.has('Thermal Visor',p) and o.invisible_objects.value>=5) or (s.has('Power Bomb',p,2) and s.has('Morph Ball',p) and s.has('Thermal Visor',p) and o.invisible_objects.value>=4 and o.combat.value>=2)))) and ((((s.has('Power Beam',p) or s.has('Wave Beam',p)) and (s.has('Charge Beam',p) or o.combat.value>=3 or (s.has('Power Bomb',p,2) and o.combat.value>=2 and s.has('Morph Ball',p)))) or (s.has('Plasma Beam',p) and (s.has('Charge Beam',p) or o.combat.value>=1))) or (t['Shoot Any Beam'](s) and (l_hm(s, p, 80) or (l_hm(s, p, 5) and o.combat.value>=3) or (l_hm(s, p, 40) and s.has('Power Bomb',p,2) and s.has('Morph Ball',p) and o.combat.value>=2)))) and (o.combat.value>=2 or l_csd(s,p,200,'Damage') or (s.has('Morph Ball',p) and (s.has('Boost Ball',p) or o.combat.value>=1))))),
 ("Room Center (Quarantine Cave, Phendrana Drifts)",lambda s:s.has('Thardus',p)),)),
("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)",(
 ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)",lambda s:s.has('Research Lab Hydra Barrier',p)),
 ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)",lambda s:s.has('Scan Visor',p)),
 ("Door to Map Station (Research Entrance, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s))),)),
("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)",(
 ("Door to Hydra Lab Entryway (Research Lab Hydra, Phendrana Drifts)",lambda s:s.has('Research Lab Hydra Barrier',p)),
 ("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)",lambda s:(s.has('Scan Visor',p) and l_hmisc(s,p,'backwards_labs'))),
 ("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)",lambda s:t['Shoot Super Missile'](s)),
 ("Door to Observatory Access (Observatory, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Event - Research Lab Hydra Barrier Lowered (Research Lab Hydra, Phendrana Drifts)",(
 ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)",None),)),
("Pickup (Missile) (Research Lab Hydra, Phendrana Drifts)",(
 ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)",None),)),
("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)",(
 ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)",None),
 ("Door to Frozen Pike (Transport Access, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and ((o.slope_jump.value>=4 and o.standable_terrain.value>=4 and ((s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4) or (s.has('Scan Visor',p) and o.scan_dash.value>=4))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or s.has('Spider Ball',p) or (s.has('Morph Ball Bomb',p) and o.bomb_space_jump.value>=3 and o.standable_terrain.value>=3 and o.l_jump.value>=1))) and t['Shoot Ice Beam'](s))),
 ("Door to South Quarantine Tunnel (Quarantine Cave, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Door to Observatory Access (Observatory, Phendrana Drifts)",(
 ("Door to Save Station D (Observatory, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) and (s.has('Observatory Activated',p) or (s.has('Scan Visor',p) and o.scan_dash.value>=3) or o.r_jump.value>=3))),
 ("Event - Observatory Activated (Observatory, Phendrana Drifts)",lambda s:(s.has('Scan Visor',p) and s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Boost Ball',p) and not s.has('Research Core Power Outage',p) and (s.has('Space Jump Boots',p) or o.bomb_jump.value>=3))),
 ("Door to Observatory Access (Research Lab Hydra, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Door to West Tower Entrance (Observatory, Phendrana Drifts)",(
 ("Door to Observatory Access (Observatory, Phendrana Drifts)",None),
 ("Door to Save Station D (Observatory, Phendrana Drifts)",lambda s:(s.has('Observatory Activated',p) or (s.has('Space Jump Boots',p) and ((s.has('Scan Visor',p) and o.scan_dash.value>=2) or o.r_jump.value>=2)) or (s.has('Scan Visor',p) and o.scan_dash.value>=3))),
 ("Pickup (Super Missile) (Observatory, Phendrana Drifts)",lambda s:(s.has('Observatory Activated',p) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=2) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Scan Visor',p) and o.complex_bomb_jump.value>=4 and o.scan_dash.value>=3 and o.standable_terrain.value>=4))),
 ("Door to West Tower (Control Tower, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Scan Visor',p) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Move Past Scatter Bombu'](s))),)),
("Door to Save Station D (Observatory, Phendrana Drifts)",(
 ("Door to Observatory Access (Observatory, Phendrana Drifts)",None),
 ("Door to West Tower Entrance (Observatory, Phendrana Drifts)",lambda s:(s.has('Observatory Activated',p) or (s.has('Space Jump Boots',p) and ((s.has('Scan Visor',p) and o.scan_dash.value>=2) or o.r_jump.value>=1)) or (s.has('Scan Visor',p) and o.scan_dash.value>=3))),
 ("Pickup (Super Missile) (Observatory, Phendrana Drifts)",lambda s:(s.has('Observatory Activated',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Space Jump Boots',p) and o.bomb_space_jump.value>=3 and o.standable_terrain.value>=3 and o.l_jump.value>=2))),
 ("Save Station (Save Station D, Phendrana Drifts)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Event - Observatory Activated (Observatory, Phendrana Drifts)",(
 ("Door to Observatory Access (Observatory, Phendrana Drifts)",None),
 ("Door to Save Station D (Observatory, Phendrana Drifts)",lambda s:s.has('Space Jump Boots',p)),)),
("Pickup (Super Missile) (Observatory, Phendrana Drifts)",(
 ("Door to Observatory Access (Observatory, Phendrana Drifts)",None),
 ("Door to West Tower Entrance (Observatory, Phendrana Drifts)",lambda s:s.has('Observatory Activated',p)),
 ("Door to Save Station D (Observatory, Phendrana Drifts)",lambda s:s.has('Observatory Activated',p)),)),
("Door to Frozen Pike (Transport Access, Phendrana Drifts)",(
 ("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)",lambda s:(t['Shoot Plasma Beam'](s) or (s.has('Space Jump Boots',p) and s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.clip_through_objects.value>=3 and o.standable_terrain.value>=3 and o.single_room_oob.value>=5 and o.jump_off_enemies.value>=5 and l_csd(s,p,125,'Damage') and s.has('Charge Beam',p) and t['Shoot Any Beam'](s)))),
 ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and t['Shoot Ice Beam'](s))),
 ("Door to Pike Access (Frozen Pike, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Energy Tank) (Transport Access, Phendrana Drifts)",(
 ("Door to Frozen Pike (Transport Access, Phendrana Drifts)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Door to Pike Access (Frozen Pike, Phendrana Drifts)",(
 ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)",None),
 ("Door to Frozen Pike (Transport Access, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and ((s.has('Space Jump Boots',p) and (o.standable_terrain.value>=2 or (s.has('Scan Visor',p) and o.scan_dash.value>=2) or (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=2))) or o.r_jump.value>=3)) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4)))),
 ("Door to Pike Access (Research Core, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)",(
 ("Door to Pike Access (Frozen Pike, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Scan Visor',p) and o.scan_dash.value>=2 and o.bomb_jump.value>=3) or (o.slope_jump.value>=2 and o.standable_terrain.value>=3 and ((not s.has('Gravity Chamber Item (Lower)',p) and s.has('X-Ray Visor',p)) or (s.has('Gravity Chamber Item (Lower)',p) and t['Shoot Ice Beam'](s))) and o.scan_dash.value>=4))),
 ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)",lambda s:(((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))) or ((not s.has('Gravity Suit',p) and o.slope_jump.value>=3 and l_hmisc(s,p,'NoGravity') and o.gravityless_underwater_movement.value>=3) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2))) and t['Shoot Wave Beam'](s))),
 ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Door to West Tower (Control Tower, Phendrana Drifts)",(
 ("Room Center (Control Tower, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_space_jump.value>=1)) and o.knowledge.value>=2 and o.movement.value>=2)),
 ("Fight Trigger (Control Tower, Phendrana Drifts)",None),
 ("Door to West Tower Entrance (Observatory, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Move Past Scatter Bombu'](s))),)),
("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)",(
 ("Room Center (Control Tower, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and ((s.has('Control Tower Tower',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=2))) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=3 and o.single_room_oob.value>=3))) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and (o.single_room_oob.value>=3 or (o.standable_terrain.value>=2 and o.single_room_oob.value>=2))))),
 ("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)",lambda s:(t['Shoot Any Beam'](s) and l_hm(s, p, 1))),)),
("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)",(
 ("Room Center (Control Tower, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or o.standable_terrain.value>=1 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))),)),
("Room Center (Control Tower, Phendrana Drifts)",(
 ("Door to West Tower (Control Tower, Phendrana Drifts)",lambda s:(s.has('Control Tower Fight',p) or s.has('Research Core Power Outage',p) or (o.knowledge.value>=2 and o.movement.value>=2 and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.wall_boost.value>=2))))),
 ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and (s.has('Control Tower Tower',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=5 and o.standable_terrain.value>=3 and o.single_room_oob.value>=4 and (o.bomb_jump.value>=1 or o.slope_jump.value>=1)))) or (s.has('Space Jump Boots',p) and o.single_room_oob.value>=2 and o.standable_terrain.value>=3 and (o.movement.value>=4 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4))))),
 ("Event - Tower (From Room Center) (Control Tower, Phendrana Drifts)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s) and ((s.has('Plasma Beam',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (o.slope_jump.value>=1 and o.standable_terrain.value>=1))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1)))),
 ("Fight Trigger (Control Tower, Phendrana Drifts)",None),
 ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)",lambda s:(((s.has('Scan Visor',p) and t['Shoot Any Beam'](s)) or (s.has('Morph Ball',p) and s.has('Power Bomb',p) and o.knowledge.value>=1) or (t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or (t['Shoot Plasma Beam'](s) and o.knowledge.value>=1)) and t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s) and s.has('Scan Visor',p))),)),
("Event - Tower (From Pickup) (Control Tower, Phendrana Drifts)",(
 ("Pickup (Artifact of Elder) (Control Tower, Phendrana Drifts)",None),)),
("Fight Trigger (Control Tower, Phendrana Drifts)",(
 ("Room Center (Control Tower, Phendrana Drifts)",lambda s:(s.has('Control Tower Fight',p) or s.has('Research Core Power Outage',p))),
 ("Event - Control Tower Fight (Control Tower, Phendrana Drifts)",lambda s:(not s.has('Research Core Power Outage',p) and t['Shoot Any Beam'](s) and (s.has('Charge Beam',p) or l_csd(s,p,300,'Damage') or o.combat.value>=2 or s.has('Plasma Beam',p)) and (o.combat.value>=1 or l_csd(s,p,100,'Damage')) and not s.has('Control Tower Fight',p))),)),
("Event - Control Tower Fight (Control Tower, Phendrana Drifts)",(
 ("Room Center (Control Tower, Phendrana Drifts)",None),)),
("Door to Pike Access (Research Core, Phendrana Drifts)",(
 ("Door to Research Core Access (Research Core, Phendrana Drifts)",lambda s:((s.has('Research Core Power Outage',p) and t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1)) or not s.has('Research Core Power Outage',p))),
 ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)",lambda s:s.has('Scan Visor',p)),
 ("Door to Pike Access (Frozen Pike, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Door to Research Core Access (Research Core, Phendrana Drifts)",(
 ("Door to Pike Access (Research Core, Phendrana Drifts)",None),
 ("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)",lambda s:s.has('Scan Visor',p)),
 ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Thermal Visor) (Research Core, Phendrana Drifts)",(
 ("Event - Research Core Power Outage (Research Core, Phendrana Drifts)",None),)),
("Event - Research Core Power Outage (Research Core, Phendrana Drifts)",(
 ("Door to Pike Access (Research Core, Phendrana Drifts)",None),)),
("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)",(
 ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or (s.has('Scan Visor',p) and o.scan_dash.value>=2))) or (s.has('Scan Visor',p) and o.scan_dash.value>=3))),
 ("Frost Cave Floor (Frost Cave, Phendrana Drifts)",None),
 ("Event - Ice Broken (Frost Cave, Phendrana Drifts)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s) and ((t['Use Grapple Beam'](s) and (s.has('Space Jump Boots',p) or o.slope_jump.value>=1)) or (s.has('Scan Visor',p) and ((s.has('Space Jump Boots',p) and o.scan_dash.value>=2) or (o.scan_dash.value>=3 and o.slope_jump.value>=1))) or (s.has('Space Jump Boots',p) and t['Shoot Ice Beam'](s) and o.jump_off_enemies.value>=3)))),
 ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Morph Ball',p) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.single_room_oob.value>=3)))),)),
("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)",(
 ("Frost Cave Floor (Frost Cave, Phendrana Drifts)",None),
 ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Pickup (Missile) (Frost Cave, Phendrana Drifts)",(
 ("Frost Cave Floor (Frost Cave, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (s.has('Gravity Suit',p) or (o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and ((s.has('Gravity Suit',p) and o.bomb_jump.value>=1) or (o.complex_bomb_jump.value>=4 and o.gravityless_underwater_movement.value>=4))))),)),
("Frost Cave Floor (Frost Cave, Phendrana Drifts)",(
 ("Door to Frost Cave Access (Frost Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (o.slope_jump.value>=2 and t['Use Grapple Beam'](s) and o.l_jump.value>=2))),
 ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and ((t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or (o.slope_jump.value>=2 or o.l_jump.value>=2))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and l_hm(s, p, 1) and t['Shoot Any Beam'](s)))),
 ("Pickup (Missile) (Frost Cave, Phendrana Drifts)",lambda s:s.has('Frost Cave Ice Floor',p)),
 ("Save Station (Save Station C, Phendrana Drifts)",lambda s:(((s.has('Space Jump Boots',p) and ((t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or o.slope_jump.value>=2)) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and l_hm(s, p, 1) and t['Shoot Any Beam'](s) and o.bomb_jump.value>=3)) and t['Shoot Wave Beam'](s))),)),
("Event - Ice Broken (Frost Cave, Phendrana Drifts)",(
 ("Frost Cave Floor (Frost Cave, Phendrana Drifts)",None),)),
("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)",(
 ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or (o.scan_dash.value>=3 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and (s.has('Gravity Suit',p) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2) or o.l_jump.value>=2))))),
 ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)",None),
 ("Door to Frost Cave Access (Frozen Pike, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4 and (s.has('Gravity Suit',p) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2)))) and t['Shoot Wave Beam'](s))),)),
("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)",(
 ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)",lambda s:((t['Use Grapple Beam'](s) and l_hm(s, p, 1) and t['Shoot Any Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or o.slope_jump.value>=2)) or (s.has('Space Jump Boots',p) and (o.scan_dash.value>=2 or o.r_jump.value>=3 or (o.r_jump.value>=2 and o.movement.value>=2))))),
 ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and o.slope_jump.value>=3 and s.has('Gravity Suit',p)) or (l_hm(s, p, 3) and t['Shoot Any Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and o.l_jump.value>=2) or (o.l_jump.value>=2 and o.slope_jump.value>=3))))),
 ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4 and (s.has('Gravity Suit',p) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2))) or ((s.has('Gravity Suit',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.slope_jump.value>=2 and o.wall_boost.value>=2 and o.gravityless_underwater_movement.value>=3)) and o.movement.value>=4 and o.standable_terrain.value>=2 and o.scan_dash.value>=2 and o.slope_jump.value>=3 and o.l_jump.value>=1)))),)),
("Door to Chamber Access (Hunter Cave, Phendrana Drifts)",(
 ("Door to Hunter Cave Access (Hunter Cave, Phendrana Drifts)",None),
 ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)",None),
 ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)",(
 ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or ((s.has('Gravity Suit',p) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2)) and (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2)))),
 ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) and o.slope_jump.value>=2)),
 ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s))),)),
("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)",(
 ("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)",lambda s:((t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or (s.has('Morph Ball',p) and s.has('Power Bomb',p)))),
 ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)",lambda s:(s.has('Scan Visor',p) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (o.standable_terrain.value>=2 and o.l_jump.value>=1))),
 ("Door to Research Core Access (Research Core, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Energy Tank) (Research Lab Aether, Phendrana Drifts)",(
 ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)",None),)),
("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)",(
 ("Lab Catwalk (Research Lab Aether, Phendrana Drifts)",None),)),
("Lab Catwalk (Research Lab Aether, Phendrana Drifts)",(
 ("Door to Research Core Access (Research Lab Aether, Phendrana Drifts)",None),
 ("Pickup (Missile) (Research Lab Aether, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (s.has('Space Jump Boots',p) or o.standable_terrain.value>=1))),
 ("Room Center (Control Tower, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) or (o.standable_terrain.value>=1 and ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=2) or o.l_jump.value>=1))) and t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s))),)),
("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)",(
 ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.standable_terrain.value>=2)) or (s.has('Morph Ball Bomb',p) and ((t['Use Grapple Beam'](s) and o.bomb_jump.value>=4) or (s.has('Scan Visor',p) and o.complex_bomb_jump.value>=5 and o.scan_dash.value>=5 and o.standable_terrain.value>=4 and o.bomb_jump.value>=4)) and s.has('Morph Ball',p)))),
 ("Door to Lower Edge Tunnel (Hunter Cave, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),
 ("Door to Upper Edge Tunnel (Frost Cave, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Morph Ball',p))),)),
("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)",(
 ("Door to Upper Edge Tunnel (Phendrana's Edge, Phendrana Drifts)",None),
 ("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and s.has('Power Bomb',p) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=1)) and t['Shoot Plasma Beam'](s))),
 ("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)",lambda s:((s.has('Morph Ball',p) and ((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.standable_terrain.value>=2 or o.slope_jump.value>=2 or o.r_jump.value>=2 or o.l_jump.value>=2 or (s.has('Scan Visor',p) and o.scan_dash.value>=2))) or (t['Use Grapple Beam'](s) or (s.has('Scan Visor',p) and o.scan_dash.value>=4)))) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))))),)),
("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)",(
 ("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)",lambda s:(s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or (o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1))),
 ("Door to Lake Tunnel (Hunter Cave, Phendrana Drifts)",lambda s:(t['Shoot Wave Beam'](s) and t['Move Past Scatter Bombu'](s))),)),
("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)",(
 ("Door to Lake Tunnel (Gravity Chamber, Phendrana Drifts)",None),
 ("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (o.slope_jump.value>=3 or (s.has('Scan Visor',p) and o.scan_dash.value>=3))) or (t['Shoot Plasma Beam'](s) and t['Use Grapple Beam'](s)) or (s.has('Gravity Chamber Item (Lower)',p) and ((s.has('Charge Beam',p) and ((s.has('Space Jump Boots',p) and o.jump_off_enemies.value>=3) or o.jump_off_enemies.value>=5) and t['Shoot Any Beam'](s)) or ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and o.standable_terrain.value>=3 and o.scan_dash.value>=4) or (s.has('Scan Visor',p) and o.scan_dash.value>=5 and o.standable_terrain.value>=5))) and t['Shoot Wave Beam'](s) and not l_hmisc(s,p,'dock_rando')))),
 ("Door to Chamber Access (Hunter Cave, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)",(
 ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)",lambda s:((s.has('Space Jump Boots',p) and (s.has('Gravity Suit',p) or (o.slope_jump.value>=3 and o.gravityless_underwater_movement.value>=3))) or (s.has('Gravity Suit',p) and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (o.scan_dash.value>=3 and s.has('Boost Ball',p) and o.wall_boost.value>=4 and o.standable_terrain.value>=2)) and s.has('Morph Ball',p)) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.wall_boost.value>=3 and o.slope_jump.value>=4 and o.gravityless_underwater_movement.value>=4 and l_hmisc(s,p,'NoGravity')))),)),
("Pickup (Missile) (Gravity Chamber, Phendrana Drifts)",(
 ("Door to Chamber Access (Gravity Chamber, Phendrana Drifts)",None),)),
("Event - Gravity Suit (Gravity Chamber, Phendrana Drifts)",(
 ("Pickup (Gravity Suit) (Gravity Chamber, Phendrana Drifts)",None),)),
("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)",(
 ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,90,'HeatDamage1')) or (o.heat_runs.value>=2 and o.scan_dash.value>=1 and l_csd(s,p,75,'HeatDamage1'))))),
 ("Save Station (Save Station Magmoor A, Magmoor Caverns)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)",(
 ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)",lambda s:(l_hm(s, p, 2) and t['Shoot Any Beam'](s) and ((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=1) and ((s.has('Space Jump Boots',p) and l_csd(s,p,120,'HeatDamage1')) or (o.standable_terrain.value>=1 and l_csd(s,p,190,'HeatDamage1')) or (o.scan_dash.value>=1 and l_csd(s,p,190,'HeatDamage1'))))))),
 ("Next to Crates (Lava Lake, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and ((l_csd(s,p,140,'HeatDamage1') and l_csd(s,p,20,'HeatDamage2')) or (o.scan_dash.value>=2 and l_csd(s,p,110,'HeatDamage1') and l_csd(s,p,10,'HeatDamage2')) or (s.has('Space Jump Boots',p) and ((o.scan_dash.value>=1 and l_csd(s,p,100,'HeatDamage1')) or (o.r_jump.value>=2 and l_csd(s,p,120,'HeatDamage1')))))))),
 ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,90,'HeatDamage1')) or (o.heat_runs.value>=2 and o.scan_dash.value>=1 and l_csd(s,p,75,'HeatDamage1'))))),)),
("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)",(
 ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and (l_csd(s,p,150,'HeatDamage1') or (s.has('Space Jump Boots',p) and l_csd(s,p,135,'HeatDamage1')) or (l_csd(s,p,120,'HeatDamage1') and (o.scan_dash.value>=2 or (s.has('Space Jump Boots',p) and o.movement.value>=2))))))),
 ("Next to Crates (Lava Lake, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,65,'HeatDamage1') or (o.scan_dash.value>=1 and l_csd(s,p,45,'HeatDamage1')))))),)),
("Next to Crates (Lava Lake, Magmoor Caverns)",(
 ("Door to Lake Tunnel (Lava Lake, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and ((l_csd(s,p,160,'HeatDamage1') and l_csd(s,p,25,'HeatDamage2')) or (o.scan_dash.value>=1 and l_csd(s,p,115,'HeatDamage1') and l_csd(s,p,10,'HeatDamage2')) or (s.has('Space Jump Boots',p) and ((l_csd(s,p,155,'HeatDamage1') and l_csd(s,p,10,'HeatDamage2')) or (o.scan_dash.value>=1 and l_csd(s,p,125,'HeatDamage1')) or (o.r_jump.value>=2 and l_csd(s,p,135,'HeatDamage1')))))))),
 ("Pickup (Artifact of Nature) (Lava Lake, Magmoor Caverns)",lambda s:(l_hm(s, p, 2) and t['Shoot Any Beam'](s) and ((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=1) and ((s.has('Space Jump Boots',p) and l_csd(s,p,80,'HeatDamage1')) or (o.standable_terrain.value>=1 and l_csd(s,p,90,'HeatDamage1')) or (o.scan_dash.value>=1 and l_csd(s,p,90,'HeatDamage1'))))))),
 ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:((s.has('Morph Ball',p) and ((t['Heat-Resisting Suit'](s) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p,2) and o.knowledge.value>=1))) or (o.heat_runs.value>=2 and ((s.has('Morph Ball Bomb',p) and (l_csd(s,p,340,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,265,'HeatDamage1')) or (s.has('Space Jump Boots',p) and (l_csd(s,p,305,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,245,'HeatDamage1')) or (o.r_jump.value>=2 and l_csd(s,p,270,'HeatDamage1')))))) or (s.has('Power Bomb',p,2) and o.knowledge.value>=1 and (l_csd(s,p,360,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,340,'HeatDamage1')) or (s.has('Space Jump Boots',p) and (l_csd(s,p,365,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,320,'HeatDamage1')) or (o.r_jump.value>=2 and l_csd(s,p,340,'HeatDamage1')))))))))) and t['Open Normal Door'](s) and ((t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,90,'HeatDamage1'))) or (s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,99,'HeatDamage1'))))))),)),
("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)",(
 ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,160,'HeatDamage1')) or (o.heat_runs.value>=3 and ((o.scan_dash.value>=2 and l_csd(s,p,120,'HeatDamage1')) or (s.has('Space Jump Boots',p) and o.r_jump.value>=3 and l_csd(s,p,110,'HeatDamage1')))))),
 ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)",lambda s:((s.has('Charge Beam',p) or l_hm(s, p, 1)) and ((s.has('Space Jump Boots',p) and (((s.has('X-Ray Visor',p) or o.invisible_objects.value>=2) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,280,'HeatDamage1')))) or (o.scan_dash.value>=2 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,155,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,125,'HeatDamage1') and o.r_jump.value>=2))) or (o.standable_terrain.value>=1 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,220,'HeatDamage1')))))) or (o.l_jump.value>=3 and (t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and (s.has('X-Ray Visor',p) and o.invisible_objects.value>=2) and ((o.slope_jump.value>=3 and o.standable_terrain.value>=3 and l_csd(s,p,255,'HeatDamage1')) or (o.scan_dash.value>=4 and l_csd(s,p,225,'HeatDamage1'))))) and t['Shoot Any Beam'](s))),
 ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,145,'HeatDamage1') or (o.r_jump.value>=2 and l_csd(s,p,110,'HeatDamage1') and s.has('Space Jump Boots',p))))))),
 ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,120,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,99,'HeatDamage1'))))),)),
("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,160,'HeatDamage1') or (s.has('Morph Ball',p) and l_csd(s,p,150,'HeatDamage1')) or (s.has('Space Jump Boots',p) and ((o.scan_dash.value>=2 and l_csd(s,p,140,'HeatDamage1')) or (o.r_jump.value>=2 and l_csd(s,p,130,'HeatDamage1')))))))),
 ("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)",lambda s:((s.has('Charge Beam',p) or l_hm(s, p, 1)) and ((s.has('Space Jump Boots',p) and (((s.has('X-Ray Visor',p) or o.invisible_objects.value>=2) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,130,'HeatDamage1')))) or (o.scan_dash.value>=2 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,75,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,60,'HeatDamage1') and o.r_jump.value>=2))) or (o.standable_terrain.value>=1 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,100,'HeatDamage1')))))) or (o.l_jump.value>=3 and (t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=2) and ((o.slope_jump.value>=3 and o.standable_terrain.value>=3 and l_csd(s,p,200,'HeatDamage1')) or (o.scan_dash.value>=4 and l_csd(s,p,180,'HeatDamage1'))))) and t['Shoot Any Beam'](s))),
 ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,95,'HeatDamage1'))))),
 ("Next to Crates (Lava Lake, Magmoor Caverns)",lambda s:((s.has('Morph Ball',p) and ((t['Heat-Resisting Suit'](s) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p,2) and o.knowledge.value>=1))) or (o.heat_runs.value>=2 and ((s.has('Morph Ball Bomb',p) and (l_csd(s,p,285,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,250,'HeatDamage1')) or (s.has('Space Jump Boots',p) and (l_csd(s,p,265,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,255,'HeatDamage1')))))) or (s.has('Power Bomb',p,2) and o.knowledge.value>=1 and (l_csd(s,p,360,'HeatDamage1') or (o.scan_dash.value>=2 and l_csd(s,p,325,'HeatDamage1')))))))) and t['Open Normal Door'](s) and ((t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,95,'HeatDamage1'))) or (s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,99,'HeatDamage1'))))))),)),
("Pickup (Missile Expansion) (Triclops Pit, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,170,'HeatDamage1') or (s.has('Space Jump Boots',p) and (l_csd(s,p,145,'HeatDamage1') or (o.r_jump.value>=2 and l_csd(s,p,110,'HeatDamage1')))))))),
 ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,145,'HeatDamage1') or (s.has('Space Jump Boots',p) and (l_csd(s,p,120,'HeatDamage1') or (o.r_jump.value>=2 and l_csd(s,p,99,'HeatDamage1')))))))),
 ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,95,'HeatDamage1'))))),)),
("Tunnel Entrance (Triclops Pit, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,185,'HeatDamage1') or (s.has('Space Jump Boots',p) and l_csd(s,p,145,'HeatDamage1')))))),
 ("Door to Pit Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,150,'HeatDamage1') or (s.has('Space Jump Boots',p) and l_csd(s,p,130,'HeatDamage1')))))),
 ("Pickup (Missile) (Storage Cavern, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,130,'HeatDamage1') or (s.has('Boost Ball',p) and l_csd(s,p,99,'HeatDamage1'))))) and t['Open Normal Door'](s))),)),
("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)",(
 ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) and o.standable_terrain.value>=2 and o.slope_jump.value>=2 and ((o.heat_runs.value>=2 and l_csd(s,p,235,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,135,'HeatDamage1')) or t['Heat-Resisting Suit'](s))) or (s.has('Scan Visor',p) and l_csd(s,p,135,'HeatDamage1') and l_csd(s,p,15,'Damage') and o.movement.value>=3 and o.scan_dash.value>=3 and o.heat_runs.value>=4))),
 ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)",lambda s:(s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=2 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and (l_csd(s,p,230,'HeatDamage1') or (o.r_jump.value>=2 and l_csd(s,p,199,'HeatDamage1'))))))),
 ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,99,'HeatDamage1')))),
 ("Middle Level (Monitor Station, Magmoor Caverns)",lambda s:(((o.heat_runs.value>=3 or t['Heat-Resisting Suit'](s)) and (t['Shoot Any Beam'](s) and ((l_csd(s,p,255,'HeatDamage1') and l_csd(s,p,85,'HeatDamage2') and o.l_jump.value>=2) or (s.has('Charge Beam',p) and l_csd(s,p,415,'HeatDamage1')) or (l_hm(s, p, 8) and l_csd(s,p,320,'HeatDamage1')) or (o.combat.value>=2 and l_csd(s,p,440,'HeatDamage1'))))) or (o.scan_dash.value>=4 and l_csd(s,p,60,'HeatDamage2') and ((o.heat_runs.value>=4 and l_csd(s,p,315,'HeatDamage1')) or (o.heat_runs.value>=5 and l_csd(s,p,205,'HeatDamage1')))))),
 ("Door to Monitor Tunnel (Triclops Pit, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,120,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,99,'HeatDamage1'))))),)),
("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)",(
 ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((o.scan_dash.value>=2 and l_csd(s,p,99,'HeatDamage1')) or (o.r_jump.value>=2 and o.standable_terrain.value>=2 and l_csd(s,p,135,'HeatDamage1')) or (o.r_jump.value>=3 and l_csd(s,p,199,'HeatDamage1')) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and l_csd(s,p,235,'HeatDamage1')))) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=4) and ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and ((s.has('Boost Ball',p) and o.l_jump.value>=3 and l_csd(s,p,299,'HeatDamage1')) or (o.scan_dash.value>=2 and o.standable_terrain.value>=2 and l_csd(s,p,199,'HeatDamage1')))) or (o.scan_dash.value>=3 and o.standable_terrain.value>=4 and l_csd(s,p,199,'HeatDamage1')))))),
 ("Middle Level (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,45,'HeatDamage1')))),
 ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),)),
("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(o.heat_runs.value>=3 and l_csd(s,p,99,'HeatDamage1') and (o.scan_dash.value>=2 or (s.has('Space Jump Boots',p) and o.r_jump.value>=2)))),
 ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((o.scan_dash.value>=2 and l_csd(s,p,99,'HeatDamage1')) or (s.has('Space Jump Boots',p) and l_csd(s,p,90,'HeatDamage1') and (o.scan_dash.value>=3 or o.r_jump.value>=3))))),
 ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,75,'HeatDamage1')))),
 ("Middle Level (Monitor Station, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((o.l_jump.value>=2 and l_csd(s,p,70,'HeatDamage1')) or (l_csd(s,p,30,'Damage') and l_csd(s,p,120,'HeatDamage1')) or (l_hm(s, p, 2) and t['Shoot Any Beam'](s) and l_csd(s,p,60,'HeatDamage1')) or (l_csd(s,p,75,'HeatDamage1') and (t['Shoot Any Beam'](s) or (s.has('Charge Beam',p) or l_hm(s, p, 1))))))),
 ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,40,'HeatDamage1'))))),)),
("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,99,'HeatDamage1')))),
 ("Middle Level (Monitor Station, Magmoor Caverns)",lambda s:(((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((o.combat.value>=3 and l_csd(s,p,430,'HeatDamage1')) or (l_csd(s,p,255,'HeatDamage1') and l_csd(s,p,65,'HeatDamage2') and o.l_jump.value>=3) or (s.has('Charge Beam',p) and l_csd(s,p,354,'HeatDamage1') and t['Shoot Any Beam'](s)) or (l_hm(s, p, 8) and t['Shoot Any Beam'](s) and l_csd(s,p,300,'HeatDamage1')))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.scan_dash.value>=3 and ((o.heat_runs.value>=3 and l_csd(s,p,205,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,125,'HeatDamage1')))) or (o.scan_dash.value>=4 and l_csd(s,p,35,'HeatDamage2') and ((o.heat_runs.value>=4 and l_csd(s,p,235,'HeatDamage1')) or (o.heat_runs.value>=5 and l_csd(s,p,119,'HeatDamage1')))))),
 ("Room Center (Shore Tunnel, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,55,'HeatDamage1') or (s.has('Morph Ball',p) and (l_csd(s,p,45,'HeatDamage1') or (s.has('Boost Ball',p) and l_csd(s,p,35,'HeatDamage1'))))))))),)),
("Middle Level (Monitor Station, Magmoor Caverns)",(
 ("Door to Monitor Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and ((o.l_jump.value>=2 and l_csd(s,p,55,'HeatDamage1') and l_csd(s,p,40,'HeatDamage2')) or (s.has('Scan Visor',p) and o.scan_dash.value>=2 and l_csd(s,p,45,'HeatDamage1')) or (s.has('Space Jump Boots',p) and o.r_jump.value>=2 and l_csd(s,p,54,'HeatDamage1')))))),
 ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,45,'HeatDamage1')))),
 ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((o.scan_dash.value>=1 and l_csd(s,p,99,'HeatDamage1')) or (o.r_jump.value>=2 and o.standable_terrain.value>=2 and l_csd(s,p,135,'HeatDamage1')) or (o.r_jump.value>=3 and l_csd(s,p,199,'HeatDamage1')) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and l_csd(s,p,235,'HeatDamage1')))) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=4) and ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and ((s.has('Boost Ball',p) and o.l_jump.value>=3 and l_csd(s,p,319,'HeatDamage1')) or (o.scan_dash.value>=2 and o.standable_terrain.value>=2 and l_csd(s,p,219,'HeatDamage1')))) or (o.scan_dash.value>=2 and o.standable_terrain.value>=2 and l_csd(s,p,199,'HeatDamage1')))))),
 ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.l_jump.value>=2 and ((o.heat_runs.value>=2 and l_csd(s,p,154,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,54,'HeatDamage1')))))),)),
("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)",(
 ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,120,'HeatDamage1')))) or (s.has('Boost Ball',p) and o.wall_boost.value>=4 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=4 and l_csd(s,p,250,'HeatDamage1')) or (o.heat_runs.value>=5 and l_csd(s,p,150,'HeatDamage1'))))))),
 ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,185,'HeatDamage1'))))),
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) and (s.has('Charge Beam',p) or l_hm(s, p, 3))))),)),
("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)",(
 ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,99,'HeatDamage1')))) or (s.has('Boost Ball',p) and o.wall_boost.value>=4 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=4 and l_csd(s,p,240,'HeatDamage1')) or (o.heat_runs.value>=5 and l_csd(s,p,140,'HeatDamage1'))))))),
 ("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,135,'HeatDamage1'))))),
 ("Door to Transport Tunnel A (Monitor Station, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Energy Tank) (Transport Tunnel A, Magmoor Caverns)",(
 ("Door to Transport to Phendrana Drifts North (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,80,'HeatDamage1'))))),
 ("Door to Monitor Station (Transport Tunnel A, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,90,'HeatDamage1'))))),)),
("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)",(
 ("Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)",(
 ("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,20,'HeatDamage1')))),)),
("Above Exit Tunnel (Warrior Shrine, Magmoor Caverns)",(
 ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,70,'HeatDamage1'))))),
 ("Pickup (Artifact of Strength) (Warrior Shrine, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,30,'HeatDamage1')))),
 ("Door to Warrior Shrine (Monitor Station, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,80,'HeatDamage1'))))),)),
("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)",(
 ("Room Center (Shore Tunnel, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=2) and ((s.has('Space Jump Boots',p) and l_csd(s,p,35,'HeatDamage1')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and l_csd(s,p,85,'HeatDamage1')) or (l_csd(s,p,65,'HeatDamage1') and o.movement.value>=3)))),)),
("Room Center (Shore Tunnel, Magmoor Caverns)",(
 ("Pickup (Ice Spreader) (Shore Tunnel, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,65,'HeatDamage1'))))),
 ("Door to Shore Tunnel (Monitor Station, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,60,'HeatDamage1'))))),
 ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,65,'HeatDamage1'))) and t['Open Normal Door'](s))),)),
("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)",(
 ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,30,'HeatDamage1')))),
 ("Room Center (Shore Tunnel, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,55,'HeatDamage1') or (s.has('Morph Ball',p) and (l_csd(s,p,45,'HeatDamage1') or (s.has('Boost Ball',p) and l_csd(s,p,35,'HeatDamage1'))))))) and t['Open Normal Door'](s))),)),
("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)",(
 ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((l_csd(s,p,239,'HeatDamage1') and l_csd(s,p,50,'HeatDamage2')) or (o.l_jump.value>=1 and ((o.scan_dash.value>=2 and l_csd(s,p,235,'HeatDamage1') and l_csd(s,p,20,'HeatDamage2')) or (o.scan_dash.value>=4 and l_csd(s,p,189,'HeatDamage1')) or (l_csd(s,p,230,'HeatDamage1') and l_csd(s,p,40,'HeatDamage2')))) or (s.has('Space Jump Boots',p) and ((l_csd(s,p,279,'HeatDamage1') and l_csd(s,p,30,'HeatDamage2')) or (o.r_jump.value>=3 and l_csd(s,p,245,'HeatDamage1') and l_csd(s,p,15,'HeatDamage2'))))) and o.movement.value>=1))),
 ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,245,'HeatDamage1')))) or (o.standable_terrain.value>=1 and s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,270,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,170,'HeatDamage1')))) or (o.standable_terrain.value>=3 and o.scan_dash.value>=3 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,315,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,215,'HeatDamage1')))))),
 ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and ((s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,120,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,99,'HeatDamage1')))) or ((o.movement.value>=1 and l_csd(s,p,45,'HeatDamage2')) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,100,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,65,'HeatDamage1')))) or (o.l_jump.value>=2 and l_csd(s,p,40,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,99,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,59,'HeatDamage1'))))))),)),
("Morph Ball Door to Warrior Shrine (Fiery Shores, Magmoor Caverns)",(
 ("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,25,'HeatDamage1')))),
 ("Morph Ball Door to Fiery Shores (Warrior Shrine, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Pickup (Power Bomb) (Fiery Shores, Magmoor Caverns)",(
 ("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,55,'HeatDamage1')))) or (s.has('Boost Ball',p) and o.wall_boost.value>=3 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,199,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,99,'HeatDamage1'))))))),)),
("Pickup (Missile) (Fiery Shores, Magmoor Caverns)",(
 ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((l_csd(s,p,160,'HeatDamage1') and l_csd(s,p,10,'HeatDamage2')) or (o.l_jump.value>=2 and o.standable_terrain.value>=1 and l_csd(s,p,125,'HeatDamage1'))))),
 ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)",lambda s:((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=2) and ((o.standable_terrain.value>=1 and l_csd(s,p,170,'HeatDamage1')) or (o.scan_dash.value>=2 and l_csd(s,p,20,'HeatDamage2') and l_csd(s,p,199,'HeatDamage1')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (l_csd(s,p,220,'HeatDamage1') or (o.heat_runs.value>=3 and l_csd(s,p,185,'HeatDamage1')))))))),)),
("Below Upper Item Exit Tunnel (Fiery Shores, Magmoor Caverns)",(
 ("Door to Shore Tunnel (Fiery Shores, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,40,'HeatDamage1')))),
 ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)",lambda s:((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,250,'HeatDamage1') and o.l_jump.value>=1))) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((s.has('Space Jump Boots',p) and ((l_csd(s,p,210,'HeatDamage1') and l_csd(s,p,35,'HeatDamage2')) or (o.r_jump.value>=3 and l_csd(s,p,170,'HeatDamage1')) or (o.l_jump.value>=2 and ((l_csd(s,p,175,'HeatDamage1') and l_csd(s,p,20,'HeatDamage2')) or (o.scan_dash.value>=2 and l_csd(s,p,160,'HeatDamage1')))))) or (o.l_jump.value>=2 and ((l_csd(s,p,185,'HeatDamage1') and l_csd(s,p,35,'HeatDamage2')) or (o.scan_dash.value>=2 and l_csd(s,p,170,'HeatDamage1') and l_csd(s,p,20,'HeatDamage2')))) or (l_csd(s,p,215,'HeatDamage1') and l_csd(s,p,50,'HeatDamage2')) or (s.has('Gravity Suit',p) and l_csd(s,p,175,'HeatDamage1') and l_csd(s,p,25,'HeatDamage2'))) and o.movement.value>=1) or ((t['Heat-Resisting Suit'](s) or o.heat_runs.value>=4) and s.has('Space Jump Boots',p) and o.r_jump.value>=3 and o.scan_dash.value>=4 and o.l_jump.value>=2 and l_csd(s,p,25,'HeatDamage2') and (l_csd(s,p,130,'HeatDamage1') or (s.has('Scan Visor',p) and l_csd(s,p,115,'HeatDamage1')))))),
 ("Pickup (Missile) (Fiery Shores, Magmoor Caverns)",lambda s:((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s) and ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p)) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (o.scan_dash.value>=3 and o.standable_terrain.value>=3))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,275,'HeatDamage1') and o.l_jump.value>=1))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1 and o.l_jump.value>=2 and (t['Heat-Resisting Suit'](s) or o.heat_runs.value>=3) and ((l_csd(s,p,170,'HeatDamage1') and l_csd(s,p,15,'HeatDamage2')) or (o.scan_dash.value>=2 and l_csd(s,p,165,'HeatDamage1')) or (o.r_jump.value>=1 and l_csd(s,p,140,'HeatDamage1') and l_csd(s,p,20,'HeatDamage2')))) or (o.l_jump.value>=2 and o.scan_dash.value>=3 and o.standable_terrain.value>=3 and l_csd(s,p,20,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=4 and l_csd(s,p,215,'HeatDamage1')))))),)),
("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)",(
 ("Door to Transport Tunnel B (Fiery Shores, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and ((s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,120,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,99,'HeatDamage1')))) or ((o.movement.value>=1 and l_csd(s,p,45,'HeatDamage2')) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,100,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,65,'HeatDamage1')))) or (o.l_jump.value>=2 and l_csd(s,p,40,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,99,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,59,'HeatDamage1'))))))),
 ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and ((s.has('Morph Ball',p) and ((s.has('Spider Ball',p) and t['Heat-Resisting Suit'](s)) or (s.has('Morph Ball Bomb',p) and ((o.bomb_jump.value>=2 and s.has('Gravity Suit',p) and l_csd(s,p,95,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,125,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,75,'HeatDamage1')))) or (o.bomb_jump.value>=4 and l_csd(s,p,200,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,150,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,99,'HeatDamage1'))) and o.l_jump.value>=3 and o.gravityless_underwater_movement.value>=3))))) or (s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,125,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,85,'HeatDamage1'))) and (o.r_jump.value>=3 or (s.has('Gravity Suit',p) and l_csd(s,p,15,'HeatDamage2') and o.movement.value>=1))) or (s.has('Scan Visor',p) and ((s.has('Space Jump Boots',p) and o.scan_dash.value>=3 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and l_csd(s,p,135,'HeatDamage1')) or (o.heat_runs.value>=3 and l_csd(s,p,85,'HeatDamage1'))) and o.standable_terrain.value>=2) or (o.scan_dash.value>=4 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,145,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,95,'HeatDamage1'))) and o.standable_terrain.value>=3)))) and ((s.has('Space Jump Boots',p) and (o.r_jump.value>=1 or (t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or o.scan_dash.value>=1 or l_csd(s,p,50,'HeatDamage2'))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,285,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or t['Use Grapple Beam'](s) or (l_hm(s, p, 3) and t['Shoot Any Beam'](s) and o.scan_dash.value>=2 and o.l_jump.value>=2) or o.scan_dash.value>=4 or (s.has('Gravity Suit',p) and l_csd(s,p,60,'HeatDamage2'))) and t['Shoot Wave Beam'](s) and (s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,105,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or (l_hm(s, p, 1) and t['Shoot Any Beam'](s) and o.standable_terrain.value>=1) or (o.slope_jump.value>=3 and l_csd(s,p,120,'HeatDamage2') and o.gravityless_underwater_movement.value>=3)))),
 ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)",(
 ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,185,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or l_csd(s,p,230,'HeatDamage2') or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.movement.value>=1 and l_csd(s,p,75,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or (s.has('Gravity Suit',p) and l_csd(s,p,100,'HeatDamage2')) or (s.has('Scan Visor',p) and o.scan_dash.value>=2) or (not s.has('Storage Depot B Item',p) and t['Shoot Any Beam'](s)))),
 ("First Spinner (Geothermal Core, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) and o.l_jump.value>=2 and o.standable_terrain.value>=2) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=5 and o.jump_off_enemies.value>=5 and o.movement.value>=5 and s.has('Boost Ball',p) and s.has('Storage Depot B Item',p)))),
 ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and ((s.has('Space Jump Boots',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,100,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,65,'HeatDamage1'))) and (o.l_jump.value>=2 or l_csd(s,p,50,'HeatDamage2'))) or (s.has('Morph Ball',p) and s.has('Spider Ball',p) and t['Heat-Resisting Suit'](s)) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and l_csd(s,p,60,'HeatDamage2') and o.bomb_jump.value>=1 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,185,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,85,'HeatDamage1'))) and o.gravityless_underwater_movement.value>=1) or (o.scan_dash.value>=4 and o.standable_terrain.value>=3 and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,160,'HeatDamage1')) or (o.heat_runs.value>=4 and l_csd(s,p,80,'HeatDamage1'))) and not l_hmisc(s,p,'dock_rando')) or (s.has('Gravity Suit',p) and l_csd(s,p,40,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=1 and l_csd(s,p,120,'HeatDamage1')) or (o.heat_runs.value>=2 and l_csd(s,p,70,'HeatDamage1')))) or (o.standable_terrain.value>=2 and o.movement.value>=4 and l_csd(s,p,10,'HeatDamage2') and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=3 and l_csd(s,p,110,'HeatDamage1'))))) and ((s.has('Space Jump Boots',p) and (o.r_jump.value>=1 or (t['Shoot Any Beam'](s) and l_hm(s, p, 1)) or o.scan_dash.value>=2 or l_csd(s,p,20,'HeatDamage2'))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,120,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or t['Use Grapple Beam'](s) or (o.scan_dash.value>=3 and l_csd(s,p,60,'HeatDamage2')) or (l_hm(s, p, 3) and t['Shoot Any Beam'](s) and o.scan_dash.value>=2 and o.l_jump.value>=1) or (o.slope_jump.value>=4 and l_csd(s,p,200,'HeatDamage2') and o.l_jump.value>=1 and o.gravityless_underwater_movement.value>=4) or (s.has('Gravity Suit',p) and l_csd(s,p,55,'HeatDamage2') and o.l_jump.value>=1)) and t['Shoot Wave Beam'](s) and (s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,105,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or (l_hm(s, p, 1) and t['Shoot Any Beam'](s) and o.standable_terrain.value>=1) or (o.slope_jump.value>=2 and l_csd(s,p,40,'HeatDamage2') and o.gravityless_underwater_movement.value>=2)))),)),
("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)",(
 ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)",lambda s:(s.has('Geothermal Core Puzzle',p) or o.clip_through_objects.value>=3)),
 ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)",lambda s:t['Shoot Ice Beam'](s)),)),
("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)",(
 ("Door to North Core Tunnel (Geothermal Core, Magmoor Caverns)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,185,'HeatDamage2') and o.gravityless_underwater_movement.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=1) or (o.slope_jump.value>=2 and (l_csd(s,p,300,'HeatDamage2') or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.movement.value>=2 and l_csd(s,p,70,'HeatDamage2'))) and o.gravityless_underwater_movement.value>=2) or (s.has('Gravity Suit',p) and l_csd(s,p,85,'HeatDamage2')) or (not s.has('Storage Depot B Item',p) and t['Shoot Any Beam'](s)))),
 ("First Spinner (Geothermal Core, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or (o.scan_dash.value>=2 and (s.has('Scan Visor',p) or not s.has('Storage Depot B Item',p))))) or (t['Use Grapple Beam'](s) and s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))),
 ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (t['Shoot Any Beam'](s) or s.has('Space Jump Boots',p) or (s.has('Gravity Suit',p) and l_csd(s,p,40,'HeatDamage2')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and l_csd(s,p,100,'HeatDamage2')) or (o.gravityless_underwater_movement.value>=3 and o.slope_jump.value>=3 and l_csd(s,p,80,'HeatDamage2'))) and t['Shoot Wave Beam'](s))),)),
("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)",(
 ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p)) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=2))),)),
("First Spinner (Geothermal Core, Magmoor Caverns)",(
 ("Event - Geothermal Core Opened (Geothermal Core, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and ((s.has('Space Jump Boots',p) and ((o.spinners_without_boost.value>=3 and o.standable_terrain.value>=5 and o.movement.value>=4 and (o.r_jump.value>=4 or (o.scan_dash.value>=4 and (s.has('Scan Visor',p) or s.has('Storage Depot B Item',p))))) or (s.has('Boost Ball',p) and (s.has('Spider Ball',p) or o.slope_jump.value>=1)))) or (s.has('Boost Ball',p) and o.bomb_jump.value>=4 and o.scan_dash.value>=5 and not s.has('Storage Depot B Item',p) and s.has('Spider Ball',p))))),)),
("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)",(
 ("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)",None),
 ("Door to Plasma Processing (Geothermal Core, Magmoor Caverns)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)",(
 ("Door to Geothermal Core (Plasma Processing, Magmoor Caverns)",None),)),
("Event - Plasma Beam (Plasma Processing, Magmoor Caverns)",(
 ("Pickup (Plasma Beam) (Plasma Processing, Magmoor Caverns)",None),)),
("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)",(
 ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=2 and o.slope_jump.value>=1 and o.standable_terrain.value>=1)) and (t['Heat-Resisting Suit'](s) or o.knowledge.value>=1))),
 ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)",lambda s:((t['Heat-Resisting Suit'](s) or o.knowledge.value>=1) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=2 and o.slope_jump.value>=1 and o.standable_terrain.value>=1)))),
 ("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)",lambda s:(s.has('Morph Ball',p) and s.has('Scan Visor',p) and ((s.has('Space Jump Boots',p) and o.scan_dash.value>=3 and o.single_room_oob.value>=4 and o.clip_through_objects.value>=3 and s.has('Boost Ball',p) and l_csd(s,p,75,'HeatDamage2')) or (t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))) and (t['Heat-Resisting Suit'](s) or o.knowledge.value>=1))),
 ("Door to South Core Tunnel (Geothermal Core, Magmoor Caverns)",lambda s:(t['Shoot Wave Beam'](s) and (t['Shoot Any Beam'](s) or s.has('Space Jump Boots',p) or (s.has('Gravity Suit',p) and l_csd(s,p,40,'HeatDamage2')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and l_csd(s,p,100,'HeatDamage2')) or (o.gravityless_underwater_movement.value>=3 and o.slope_jump.value>=2 and l_csd(s,p,80,'HeatDamage2'))) and t['Open Normal Door'](s))),)),
("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)",(
 ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or o.knowledge.value>=1)),
 ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)",lambda s:(o.slope_jump.value>=1 and (t['Heat-Resisting Suit'](s) or o.knowledge.value>=1))),
 ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)",lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball',p) and s.has('Power Bomb',p)) and t['Shoot Ice Beam'](s) and (s.has('Space Jump Boots',p) or t['Use Grapple Beam'](s) or o.slope_jump.value>=1))),)),
("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)",(
 ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:(t['Heat-Resisting Suit'](s) or o.knowledge.value>=1)),
 ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:(o.standable_terrain.value>=1 and (t['Heat-Resisting Suit'](s) or o.knowledge.value>=1))),
 ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Energy Tank) (Magmoor Workstation, Magmoor Caverns)",(
 ("Door to South Core Tunnel (Magmoor Workstation, Magmoor Caverns)",None),)),
("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)",(
 ("Door to Transport Tunnel C (Magmoor Workstation, Magmoor Caverns)",lambda s:t['Shoot Wave Beam'](s)),
 ("Door to South Quarantine Tunnel (Transport to Magmoor Caverns South, Phendrana Drifts)",None),
 ("Save Station (Save Station Magmoor B, Magmoor Caverns)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Door to Waste Disposal (Main Quarry, Phazon Mines)",(
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",None),
 ("Crane Platform (Main Quarry, Phazon Mines)",lambda s:t['Use Grapple Beam'](s)),
 ("Door to Waste Disposal (Ore Processing, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p)))),)),
("Door to Quarry Access (Main Quarry, Phazon Mines)",(
 ("Door to Waste Disposal (Main Quarry, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) and t['Use Grapple Beam'](s))),
 ("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)",lambda s:s.has('Scan Visor',p)),
 ("Crane Platform (Main Quarry, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Grapple Beam',p) and o.movement.value>=1) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.wall_boost.value>=4 and o.slope_jump.value>=2))),
 ("Door to Main Quarry (Security Access A, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and s.has('Main Quarry Barrier',p))),
 ("Door to Main Quarry (Save Station Mines A, Phazon Mines)",lambda s:(((s.has('Morph Ball',p) and s.has('Spider Ball',p)) or o.movement.value>=2 or s.has('Space Jump Boots',p) or o.l_jump.value>=1) and t['Shoot Wave Beam'](s))),
 ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Pickup (Missile) (Main Quarry, Phazon Mines)",(
 ("Crane Platform (Main Quarry, Phazon Mines)",None),)),
("Event - Main Quarry Barrier Deactivated (Main Quarry, Phazon Mines)",(
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",None),)),
("Crane Platform (Main Quarry, Phazon Mines)",(
 ("Door to Waste Disposal (Main Quarry, Phazon Mines)",lambda s:(t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and ((o.slope_jump.value>=2 and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=1) or o.r_jump.value>=2)) or (s.has('Scan Visor',p) and o.scan_dash.value>=2) or o.scan_dash.value>=3)),
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",None),
 ("Pickup (Missile) (Main Quarry, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1) and ((s.has('Morph Ball',p) and s.has('Spider Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=2) or (o.knowledge.value>=2 and o.movement.value>=2))) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=1 and (o.scan_dash.value>=2 or o.l_jump.value>=1))))),)),
("Door to Main Quarry (Save Station Mines A, Phazon Mines)",(
 ("Save Station (Save Station Mines A, Phazon Mines)",lambda s:s.has('Phazon Mines Save Station A Barrier',p)),
 ("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)",lambda s:s.has('Scan Visor',p)),
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",lambda s:t['Shoot Wave Beam'](s)),)),
("Save Station (Save Station Mines A, Phazon Mines)",(
 ("Door to Main Quarry (Save Station Mines A, Phazon Mines)",lambda s:s.has('Phazon Mines Save Station A Barrier',p)),)),
("Event - Save Station A Barrier Opened (Save Station Mines A, Phazon Mines)",(
 ("Door to Main Quarry (Save Station Mines A, Phazon Mines)",None),)),
("Door to Main Quarry (Security Access A, Phazon Mines)",(
 ("Pickup (Missile) (Security Access A, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p))),
 ("Door to Security Access A (Mine Security Station, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Main Quarry Barrier',p) or l_hmisc(s,p,'backwards_upper_mines')))),)),
("Pickup (Missile) (Security Access A, Phazon Mines)",(
 ("Door to Main Quarry (Security Access A, Phazon Mines)",None),)),
("Door to Storage Depot B (Ore Processing, Phazon Mines)",(
 ("Door to Waste Disposal (Ore Processing, Phazon Mines)",lambda s:((t['Use Grapple Beam'](s) or o.standable_terrain.value>=1 or (s.has('Space Jump Boots',p) and o.l_jump.value>=1)) and (t['Shoot Wave Beam'](s) or l_csd(s,p,50,'Damage') or o.combat.value>=1))),
 ("Door to Elevator Access A (Ore Processing, Phazon Mines)",None),
 ("Door to Ore Processing (Storage Depot B, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Door to Waste Disposal (Ore Processing, Phazon Mines)",(
 ("Door to Storage Depot B (Ore Processing, Phazon Mines)",lambda s:(t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and (o.r_jump.value>=1 or o.l_jump.value>=1)) or o.standable_terrain.value>=1 or (s.has('Scan Visor',p) and o.scan_dash.value>=2))),
 ("Door to Elevator Access A (Ore Processing, Phazon Mines)",None),
 ("Door to Waste Disposal (Main Quarry, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=4))))),)),
("Door to Elevator Access A (Ore Processing, Phazon Mines)",(
 ("Door to Storage Depot B (Ore Processing, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p) and ((s.has('Power Bomb',p) and (s.has('Space Jump Boots',p) or (o.standable_terrain.value>=1 and o.l_jump.value>=1))) or (s.has('Scan Visor',p) and o.bomb_jump.value>=3 and o.standable_terrain.value>=2 and o.scan_dash.value>=4))) or t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and ((s.has('Power Bomb',p) and o.l_jump.value>=2 and o.standable_terrain.value>=2) or (o.r_jump.value>=2 and o.standable_terrain.value>=3))) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and s.has('Power Bomb',p,4) and o.wall_boost.value>=3 and (s.has('Space Jump Boots',p) or (o.l_jump.value>=1 and o.standable_terrain.value>=1))))),
 ("Door to Elevator A (Elite Control Access, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and s.has('Scan Visor',p))),
 ("Top Floor (Elite Research, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and ((s.has('Morph Ball',p) and s.has('Spider Ball',p)) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.slope_jump.value>=2)) and (s.has('Elite Research Rock Wall',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.clip_through_objects.value>=1)))),)),
("Door to Security Access A (Mine Security Station, Phazon Mines)",(
 ("Room Center (Mine Security Station, Phazon Mines)",None),
 ("Door to Main Quarry (Security Access A, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Door to Security Access B (Mine Security Station, Phazon Mines)",(
 ("Room Center (Mine Security Station, Phazon Mines)",None),
 ("Door to Security Access B (Elite Research, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and t['Shoot Wave Beam'](s))),)),
("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)",(
 ("Room Center (Mine Security Station, Phazon Mines)",None),)),
("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)",(
 ("Door to Security Access A (Mine Security Station, Phazon Mines)",None),
 ("Door to Security Access B (Mine Security Station, Phazon Mines)",None),
 ("Room Center (Mine Security Station, Phazon Mines)",None),)),
("Room Center (Mine Security Station, Phazon Mines)",(
 ("Door to Security Access A (Mine Security Station, Phazon Mines)",lambda s:(s.has('Mine Security Station Unlock Doors',p) and ((t['Shoot Ice Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2))),
 ("Door to Security Access B (Mine Security Station, Phazon Mines)",lambda s:(s.has('Mine Security Station Unlock Doors',p) and ((t['Shoot Ice Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2))),
 ("Event - Mine Security Station Barrier Opened (Mine Security Station, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and s.has('Morph Ball',p) and s.has('Power Bomb',p))),
 ("Event - Mine Security Station Doors Unlocked (Mine Security Station, Phazon Mines)",lambda s:(not s.has('Mine Security Station Unlock Doors',p) and t['Shoot Wave Beam'](s) and (s.has('Charge Beam',p) or o.combat.value>=3 or (o.combat.value>=2 and l_csd(s,p,125,'Damage'))))),
 ("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)",lambda s:(s.has('Mine Security Station Barrier',p) and t['Shoot Plasma Beam'](s))),)),
("Door to Ore Processing (Storage Depot B, Phazon Mines)",(
 ("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)",None),
 ("Door to Storage Depot B (Ore Processing, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)",(
 ("Door to Ore Processing (Storage Depot B, Phazon Mines)",None),)),
("Event - Storage Depot B Item (Storage Depot B, Phazon Mines)",(
 ("Pickup (Grapple Beam) (Storage Depot B, Phazon Mines)",None),)),
("Door to Security Access B (Elite Research, Phazon Mines)",(
 ("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and (s.has('Invisible Drone',p) or l_hmisc(s,p,'phazon_elite_without_dynamo')) and (s.has('Charge Beam',p) or o.combat.value>=1) and t['Shoot Any Beam'](s))),
 ("Top Floor (Elite Research, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2)) and ((t['Shoot Power Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2) and (t['Shoot Any Beam'](s) or l_csd(s,p,200,'Damage')))),
 ("Door to Security Access B (Mine Security Station, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and t['Shoot Wave Beam'](s))),)),
("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)",(
 ("Top Floor (Elite Research, Phazon Mines)",None),)),
("Pickup (Missile) (Elite Research, Phazon Mines)",(
 ("Top Floor (Elite Research, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or o.standable_terrain.value>=1)),)),
("Pickup (Artifact of Warrior) (Elite Research, Phazon Mines)",(
 ("Door to Security Access B (Elite Research, Phazon Mines)",None),)),
("Top Floor (Elite Research, Phazon Mines)",(
 ("Door to Security Access B (Elite Research, Phazon Mines)",lambda s:((t['Shoot Power Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2)),
 ("Event - Rock Wall in Elite Research Destroyed (Elite Research, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and s.has('Morph Ball',p) and ((o.spinners_without_boost.value>=2 and s.has('Morph Ball Bomb',p)) or (s.has('Boost Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))))),
 ("Pickup (Missile) (Elite Research, Phazon Mines)",lambda s:(s.has('Elite Research Rock Wall',p) and (s.has('Space Jump Boots',p) or o.standable_terrain.value>=1))),
 ("Door to Elevator Access A (Ore Processing, Phazon Mines)",lambda s:(((s.has('Morph Ball',p) and s.has('Spider Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and s.has('Power Bomb',p,3) and o.wall_boost.value>=3)) and t['Shoot Power Beam'](s)) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=2 and o.slope_jump.value>=2 and (t['Shoot Power Beam'](s) or o.combat.value>=3))) and t['Shoot Ice Beam'](s) and s.has('Elite Research Rock Wall',p))),)),
("Door to Elevator A (Elite Control Access, Phazon Mines)",(
 ("Door to Elite Control (Elite Control Access, Phazon Mines)",None),
 ("Pickup (Missile) (Elite Control Access, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4) or (o.damage_boosting.value>=4 and l_csd(s,p,100,'Damage'))))),
 ("Door to Elevator Access A (Ore Processing, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Morph Ball',p) and (s.has('Spider Ball',p) or (s.has('Space Jump Boots',p) and s.has('Morph Ball Bomb',p) and t['Shoot Wave Beam'](s) and o.bomb_space_jump.value>=3 and o.standable_terrain.value>=4))))),)),
("Door to Elite Control (Elite Control Access, Phazon Mines)",(
 ("Door to Elevator A (Elite Control Access, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Boost Ball',p) and o.wall_boost.value>=1))))),
 ("Door to Elite Control Access (Elite Control, Phazon Mines)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Missile) (Elite Control Access, Phazon Mines)",(
 ("Door to Elite Control (Elite Control Access, Phazon Mines)",None),)),
("Door to Elite Control Access (Elite Control, Phazon Mines)",(
 ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)",lambda s:(s.has('Charge Beam',p) or o.combat.value>=1 or l_csd(s,p,200,'Damage'))),
 ("Bottom Floor Center (Elite Control, Phazon Mines)",lambda s:(s.has('Elite Pirate Fight (Elite Control)',p) or (o.standable_terrain.value>=3 and o.movement.value>=2))),
 ("Door to Elite Control (Elite Control Access, Phazon Mines)",lambda s:t['Shoot Wave Beam'](s)),)),
("Door to Ventilation Shaft (Elite Control, Phazon Mines)",(
 ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)",lambda s:(l_hmisc(s,p,'backwards_lower_mines') and s.has('Scan Visor',p))),
 ("Bottom Floor Center (Elite Control, Phazon Mines)",lambda s:s.has('Elite Control Barriers',p)),
 ("Door to Omega Research (Ventilation Shaft, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)",(
 ("Bottom Floor Center (Elite Control, Phazon Mines)",None),)),
("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)",(
 ("Bottom Floor Center (Elite Control, Phazon Mines)",None),)),
("Bottom Floor Center (Elite Control, Phazon Mines)",(
 ("Door to Elite Control Access (Elite Control, Phazon Mines)",lambda s:(s.has('Elite Pirate Fight (Elite Control)',p) or (o.standable_terrain.value>=2 and o.movement.value>=1))),
 ("Door to Ventilation Shaft (Elite Control, Phazon Mines)",lambda s:(s.has('Elite Control Barriers',p) and (o.standable_terrain.value>=2 or (s.has('Elite Pirate Fight (Elite Control)',p) and (t['Shoot Ice Beam'](s) or l_csd(s,p,125,'Damage') or o.combat.value>=2))))),
 ("Event - Elite Control Barriers Lowered (Elite Control, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and (s.has('Elite Pirate Fight (Elite Control)',p) or o.standable_terrain.value>=2))),
 ("Event - Elite Pirate Defeated (Elite Control, Phazon Mines)",lambda s:(s.has('Charge Beam',p) or o.combat.value>=1 or l_csd(s,p,200,'Damage'))),
 ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Morph Ball',p) and s.has('Power Bomb',p)))),)),
("Door to Omega Research (Ventilation Shaft, Phazon Mines)",(
 ("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and s.has('Morph Ball',p) and s.has('Power Bomb',p))),
 ("Door to Ventilation Shaft (Omega Research, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),
 ("Door to Ventilation Shaft (Elite Control, Phazon Mines)",lambda s:(((s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and (o.complex_bomb_jump.value>=5 or (s.has('Space Jump Boots',p) and o.complex_bomb_jump.value>=4))))) or (s.has('Space Jump Boots',p) and o.scan_dash.value>=4 and o.standable_terrain.value>=2 and not l_hmisc(s,p,'dock_rando'))) and t['Shoot Ice Beam'](s))),)),
("Pickup (Energy Tank) (Ventilation Shaft, Phazon Mines)",(
 ("Door to Omega Research (Ventilation Shaft, Phazon Mines)",None),)),
("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)",(
 ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)",lambda s:(s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,45,'Phazon')))),
 ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p))),
 ("Door to Workstation Tunnel (Magmoor Workstation, Magmoor Caverns)",lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball',p) and s.has('Power Bomb',p)) and t['Shoot Ice Beam'](s) and (s.has('Space Jump Boots',p) or t['Use Grapple Beam'](s) or o.slope_jump.value>=1) and (((s.has('Space Jump Boots',p) and (o.standable_terrain.value>=2 or s.has('Spider Ball',p))) or (s.has('Morph Ball Bomb',p) and ((s.has('Spider Ball',p) and o.bomb_jump.value>=4 and o.standable_terrain.value>=4) or (o.complex_bomb_jump.value>=5 and o.standable_terrain.value>=5 and o.l_jump.value>=4)))) and (not s.has('Plasma Processing Item',p) or (s.has('Plasma Processing Item',p) and ((t['Shoot Plasma Beam'](s) and t['Shoot Wave Beam'](s) and t['Shoot Power Beam'](s)) or o.combat.value>=2 or l_csd(s,p,200,'Damage'))))))),
 ("Bottom Floor Center (Elite Control, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Morph Ball',p) and s.has('Power Bomb',p)))),)),
("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)",(
 ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)",lambda s:((((s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,45,'Phazon'))) and s.has('Space Jump Boots',p) and (o.standable_terrain.value>=1 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p)))) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and l_csd(s,p,65,'Phazon') and ((s.has('Spider Ball',p) and o.bomb_jump.value>=3 and o.standable_terrain.value>=3 and o.l_jump.value>=3) or (o.bomb_space_jump.value>=4 and o.complex_bomb_jump.value>=4 and o.standable_terrain.value>=3 and o.l_jump.value>=3)))) and (not s.has('Plasma Processing Item',p) or (s.has('Plasma Processing Item',p) and ((t['Shoot Plasma Beam'](s) and t['Shoot Wave Beam'](s) and t['Shoot Power Beam'](s)) or o.combat.value>=2 or l_csd(s,p,125,'Damage')))))),
 ("Pickup (Missile) (Phazon Processing Center, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) and (s.has('X-Ray Visor',p) or s.has('Thermal Visor',p) or o.invisible_objects.value>=1) and s.has('Morph Ball',p) and s.has('Power Bomb',p) and (not s.has('Plasma Processing Item',p) or (s.has('Plasma Processing Item',p) and ((t['Shoot Plasma Beam'](s) and t['Shoot Wave Beam'](s) and t['Shoot Power Beam'](s)) or o.combat.value>=2 or l_csd(s,p,125,'Damage')))))),
 ("Door to Elite Quarters (Processing Center Access, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and ((s.has('Processing Center Access Barrier',p) or l_hmisc(s,p,'backwards_lower_mines')) and (s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,99,'Phazon')))))),)),
("Pickup (Missile) (Phazon Processing Center, Phazon Mines)",(
 ("Door to Maintenance Tunnel (Phazon Processing Center, Phazon Mines)",lambda s:(((s.has('Morph Ball',p) and (o.l_jump.value>=2 or (o.bomb_jump.value>=2 and o.invisible_objects.value>=1)) and ((o.complex_bomb_jump.value>=3 and o.invisible_objects.value>=1) or (o.scan_dash.value>=3 and o.standable_terrain.value>=3 and o.bomb_jump.value>=3)) and s.has('Morph Ball Bomb',p)) or s.has('Space Jump Boots',p)) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=1))),
 ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)",None),)),
("Door to Ventilation Shaft (Omega Research, Phazon Mines)",(
 ("Door to Omega Research (Ventilation Shaft, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),
 ("Door to Omega Research (Dynamo Access, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and ((t['Shoot Power Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2))),
 ("Map Station (Map Station Mines, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Power Bomb',p)) and t['Shoot Ice Beam'](s))),)),
("Door to Elite Quarters (Processing Center Access, Phazon Mines)",(
 ("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)",lambda s:s.has('Scan Visor',p)),
 ("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)",None),
 ("Door to Processing Center Access (Elite Quarters, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Door to Processing Center Access (Phazon Processing Center, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Processing Center Access Barrier',p) and (s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,199,'Phazon')) or (o.movement.value>=2 and l_csd(s,p,99,'Phazon')))))),)),
("Event - Processing Center Access Barrier Opened (Processing Center Access, Phazon Mines)",(
 ("Door to Elite Quarters (Processing Center Access, Phazon Mines)",None),)),
("Pickup (Energy Tank) (Processing Center Access, Phazon Mines)",(
 ("Door to Elite Quarters (Processing Center Access, Phazon Mines)",None),)),
("Door to Central Dynamo (Dynamo Access, Phazon Mines)",(
 ("Door to Omega Research (Dynamo Access, Phazon Mines)",lambda s:(not s.has('Plasma Beam',p) or s.has('Elite Pirate Fight (Dynamo Access)',p))),
 ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)",lambda s:s.has('Plasma Beam',p)),
 ("Fight Trigger (Central Dynamo, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Door to Omega Research (Dynamo Access, Phazon Mines)",(
 ("Door to Central Dynamo (Dynamo Access, Phazon Mines)",lambda s:(not s.has('Plasma Beam',p) or s.has('Elite Pirate Fight (Dynamo Access)',p))),
 ("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)",lambda s:s.has('Plasma Beam',p)),
 ("Door to Ventilation Shaft (Omega Research, Phazon Mines)",lambda s:(t['Shoot Ice Beam'](s) and ((s.has('Scan Visor',p) or s.has('Invisible Drone',p)) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or o.slope_jump.value>=2) and ((t['Shoot Power Beam'](s) and t['Shoot Wave Beam'](s)) or l_csd(s,p,125,'Damage') or o.combat.value>=2)))),)),
("Event - Elite Pirate Fight (Dynamo Access, Phazon Mines)",(
 ("Door to Omega Research (Dynamo Access, Phazon Mines)",lambda s:(s.has('Charge Beam',p) or o.combat.value>=1 or l_csd(s,p,200,'Damage'))),)),
("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)",(
 ("Door to Processing Center Access (Elite Quarters, Phazon Mines)",lambda s:(s.has('Omega Pirate',p) and (s.has('Scan Visor',p) or (s.has('Space Jump Boots',p) and s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=1 and o.bomb_space_jump.value>=3)))),
 ("Fight Trigger (Elite Quarters, Phazon Mines)",None),
 ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Door to Processing Center Access (Elite Quarters, Phazon Mines)",(
 ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)",lambda s:s.has('Omega Pirate',p)),
 ("Fight Trigger (Elite Quarters, Phazon Mines)",None),
 ("Door to Elite Quarters (Processing Center Access, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Event - Omega Pirate (Elite Quarters, Phazon Mines)",(
 ("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)",None),)),
("Pickup (Phazon Suit) (Elite Quarters, Phazon Mines)",(
 ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)",None),)),
("Fight Trigger (Elite Quarters, Phazon Mines)",(
 ("Event - Omega Pirate (Elite Quarters, Phazon Mines)",lambda s:(s.has('X-Ray Visor',p) and ((t['Have all Beams'](s) and s.has('Charge Beam',p) and l_csd(s,p,300,'Damage')) or (s.has('Charge Beam',p) and o.combat.value>=1 and (s.has('Plasma Beam',p) or (t['Shoot Super Missile'](s) and l_hm(s, p, 30))) and l_csd(s,p,200,'Damage')) or (s.has('Power Bomb',p,3) and o.combat.value>=3 and s.has('Morph Ball',p)) or (o.combat.value>=4 and l_csd(s,p,300,'Damage')) or o.combat.value>=5 or (o.combat.value>=2 and l_csd(s,p,500,'Damage')) or (o.combat.value>=1 and l_csd(s,p,800,'Damage'))) and t['Shoot Any Beam'](s))),)),
("Door to Quarantine Access A (Central Dynamo, Phazon Mines)",(
 ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.infinite_speed.value>=2 and (s.has('Power Bomb',p) or s.has('Morph Ball Bomb',p)) and l_csd(s,p,280,'Damage'))),
 ("Room Bottom (Central Dynamo, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p))),
 ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Event - Security Drone (Central Dynamo, Phazon Mines)",(
 ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and s.has('Power Bomb',p) and o.infinite_speed.value>=2 and l_csd(s,p,680,'Damage'))))),)),
("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)",(
 ("Room Bottom (Central Dynamo, Phazon Mines)",None),)),
("Fight Trigger (Central Dynamo, Phazon Mines)",(
 ("Event - Security Drone (Central Dynamo, Phazon Mines)",lambda s:(o.combat.value>=1 or l_csd(s,p,100,'Damage'))),
 ("Pickup (Main Power Bombs) (Central Dynamo, Phazon Mines)",lambda s:(s.has('Boost Ball',p) and s.has('Power Bomb',p) and s.has('Morph Ball',p) and o.infinite_speed.value>=2 and o.knowledge.value>=3 and l_csd(s,p,280,'Damage'))),
 ("Room Bottom (Central Dynamo, Phazon Mines)",None),
 ("Door to Central Dynamo (Dynamo Access, Phazon Mines)",lambda s:(s.has('Invisible Drone',p) and t['Shoot Ice Beam'](s))),)),
("Room Bottom (Central Dynamo, Phazon Mines)",(
 ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and ((s.has('Invisible Drone',p) and (s.has('Ice Beam',p) or o.combat.value>=2 or l_csd(s,p,200,'Damage'))) or o.knowledge.value>=1))),
 ("Fight Trigger (Central Dynamo, Phazon Mines)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4 and o.standable_terrain.value>=2)) and (t['Shoot Ice Beam'](s) or l_csd(s,p,125,'Damage') or o.combat.value>=2 or not s.has('Invisible Drone',p)))),
 ("Save Station (Save Station Mines B, Phazon Mines)",lambda s:((not s.has('Invisible Drone',p) or o.combat.value>=2 or l_csd(s,p,200,'Damage')) and t['Shoot Ice Beam'](s))),)),
("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)",(
 ("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)",lambda s:s.has('Elite Quarters Access Barrier',p)),
 ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and (t['Shoot Wave Beam'](s) or o.combat.value>=2 or l_csd(s,p,125,'Damage')))),)),
("Door to Elite Quarters (Elite Quarters Access, Phazon Mines)",(
 ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)",lambda s:s.has('Elite Quarters Access Barrier',p)),
 ("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)",lambda s:l_hmisc(s,p,'backwards_lower_mines')),
 ("Door to Elite Quarters Access (Elite Quarters, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Event - Elite Quarters Access Barrier Opened (Elite Quarters Access, Phazon Mines)",(
 ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)",None),)),
("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)",(
 ("Front of Barrier (Metroid Quarantine B, Phazon Mines)",lambda s:((s.has('Space Jump Boots',p) and ((o.standable_terrain.value>=2 and o.slope_jump.value>=1 and (t['Use Grapple Beam'](s) or o.l_jump.value>=2)) or o.scan_dash.value>=3) and (t['Shoot Plasma Beam'](s) or (o.combat.value>=3 and l_csd(s,p,125,'Damage')))) or (s.has('Morph Ball',p) and ((s.has('Spider Ball',p) and (t['Use Grapple Beam'](s) or (s.has('Scan Visor',p) and o.scan_dash.value>=4))) or (s.has('Morph Ball Bomb',p) and s.has('Scan Visor',p) and o.complex_bomb_jump.value>=4 and o.scan_dash.value>=4 and o.standable_terrain.value>=2)) and (t['Shoot Plasma Beam'](s) or o.combat.value>=2 or l_csd(s,p,200,'Damage'))))),
 ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and l_csd(s,p,150,'Phazon') and o.bomb_jump.value>=1) or (s.has('X-Ray Visor',p) and o.scan_dash.value>=1 and o.l_jump.value>=1 and l_csd(s,p,150,'Phazon')) or (o.slope_jump.value>=3 and l_csd(s,p,300,'Phazon'))))),)),
("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)",(
 ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.clip_through_objects.value>=3 and ((s.has('Space Jump Boots',p) and o.standable_terrain.value>=3 and o.single_room_oob.value>=3) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and o.complex_bomb_jump.value>=4 and o.standable_terrain.value>=5 and o.single_room_oob.value>=4)) and ((t['Shoot Plasma Beam'](s) and t['Shoot Wave Beam'](s)) or o.combat.value>=2 or l_csd(s,p,200,'Damage')))),
 ("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)",lambda s:t['Shoot Super Missile'](s)),
 ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)",lambda s:(s.has('Scan Visor',p) and l_hmisc(s,p,'backwards_lower_mines'))),
 ("Front of Barrier (Metroid Quarantine B, Phazon Mines)",lambda s:s.has('Metroid Quarantine B Barrier',p)),
 ("Door to Metroid Quarantine B (Elite Quarters Access, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and ((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or o.slope_jump.value>=1 or (s.has('Scan Visor',p) and o.standable_terrain.value>=1 and o.scan_dash.value>=1)) and (t['Shoot Wave Beam'](s) or o.combat.value>=2 or l_csd(s,p,125,'Damage'))))),
 ("Save Station (Save Station Mines C, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Pickup (Missile) (Metroid Quarantine B, Phazon Mines)",(
 ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)",None),)),
("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)",(
 ("Front of Barrier (Metroid Quarantine B, Phazon Mines)",None),)),
("Front of Barrier (Metroid Quarantine B, Phazon Mines)",(
 ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)",lambda s:((s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,150,'Phazon')) or (o.slope_jump.value>=1 and l_csd(s,p,50,'Phazon'))) and (t['Shoot Plasma Beam'](s) or o.combat.value>=2 or l_csd(s,p,200,'Damage')))),
 ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)",lambda s:s.has('Metroid Quarantine B Barrier',p)),
 ("Event - Metroid Quarantine B Barrier Lowered (Metroid Quarantine B, Phazon Mines)",lambda s:s.has('Scan Visor',p)),)),
("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",(
 ("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)",lambda s:s.has('Scan Visor',p)),
 ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Metroid Quarantine A Barrier',p) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=2 or (s.has('Thermal Visor',p) and o.invisible_objects.value>=1)) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4 and o.l_jump.value>=3)))),
 ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)",lambda s:((t['Shoot Ice Beam'](s) and o.jump_off_enemies.value>=4 and o.l_jump.value>=1) or (s.has('Space Jump Boots',p) and o.jump_off_enemies.value>=3 and t['Shoot Ice Beam'](s)))),
 ("Door to Quarantine Access A (Central Dynamo, Phazon Mines)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)",(
 ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",lambda s:((s.has('Metroid Quarantine A Barrier',p) or l_hmisc(s,p,'backwards_lower_mines')) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,200,'Phazon')) or (o.slope_jump.value>=2 and l_csd(s,p,150,'Phazon'))))),
 ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) and o.standable_terrain.value>=2 and ((s.has('Scan Visor',p) and o.scan_dash.value>=3) or (o.r_jump.value>=4 and o.movement.value>=4)))),
 ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Spider Ball',p) and s.has('Morph Ball Bomb',p)) or o.scan_dash.value>=3)),
 ("Door to Elevator B (Fungal Hall Access, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and s.has('Scan Visor',p) and t['Shoot Ice Beam'](s))),)),
("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)",(
 ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)",lambda s:((s.has('Space Jump Boots',p) and o.scan_dash.value>=3 and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=4 and o.standable_terrain.value>=3))),
 ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Spider Ball',p)) or o.standable_terrain.value>=1)),)),
("Event - Metroid Quarantine A Barrier Lowered (Metroid Quarantine A, Phazon Mines)",(
 ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",None),)),
("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)",(
 ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Metroid Quarantine A Barrier',p) and ((s.has('Space Jump Boots',p) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=2 or (s.has('Thermal Visor',p) and o.invisible_objects.value>=1))) or (o.slope_jump.value>=3 and l_csd(s,p,99,'Phazon')) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2 and l_csd(s,p,75,'Phazon')) or (o.standable_terrain.value>=3 and l_csd(s,p,55,'Phazon'))))),
 ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and ((s.has('Spider Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=1))) or (s.has('Scan Visor',p) and (s.has('Space Jump Boots',p) and s.has('Power Bomb',p) and o.slope_jump.value>=3 and o.standable_terrain.value>=3 and o.scan_dash.value>=3))))),
 ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)",lambda s:(((s.has('Morph Ball',p) and s.has('Power Bomb',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=3) or (o.r_jump.value>=4 and o.movement.value>=3)) and s.has('Space Jump Boots',p) and (s.has('X-Ray Visor',p) or ((s.has('Thermal Visor',p) and o.invisible_objects.value>=1) or o.invisible_objects.value>=2)))),
 ("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p,2))),)),
("Front of Spider Track (Bridge) (Metroid Quarantine A, Phazon Mines)",(
 ("Door to Quarantine Access A (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Metroid Quarantine A Barrier',p) or l_hmisc(s,p,'backwards_lower_mines'))),
 ("Pickup (Missile) (Metroid Quarantine A, Phazon Mines)",lambda s:((s.has('X-Ray Visor',p) or (s.has('Thermal Visor',p) and o.invisible_objects.value>=1) or o.invisible_objects.value>=2) and (s.has('Spider Ball',p) or o.standable_terrain.value>=1))),
 ("Front of Spider Track (Wall) (Metroid Quarantine A, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p,2))),)),
("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)",(
 ("Pickup (Missile) (Fungal Hall B, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))),
 ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Door to Quarantine Access B (Metroid Quarantine B, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and l_csd(s,p,150,'Phazon') and o.bomb_jump.value>=1) or (o.slope_jump.value>=1 and l_csd(s,p,100,'Phazon'))) and ((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.slope_jump.value>=1 or (o.scan_dash.value>=2 and s.has('Scan Visor',p)) or o.standable_terrain.value>=1)) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4) or (t['Shoot Ice Beam'](s) and o.jump_off_enemies.value>=4)))),
 ("Missile Station (Missile Station Mines, Phazon Mines)",lambda s:((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.slope_jump.value>=2)) and t['Shoot Plasma Beam'](s))),)),
("Pickup (Missile) (Fungal Hall B, Phazon Mines)",(
 ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)",None),)),
("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)",(
 ("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (s.has('Phazon Suit',p) or (s.has('Boost Ball',p) and ((o.movement.value>=2 and l_csd(s,p,1299,'Phazon')) or (o.movement.value>=3 and l_csd(s,p,1199,'Phazon')) or (o.movement.value>=4 and l_csd(s,p,1099,'Phazon')) or (o.movement.value>=5 and l_csd(s,p,999,'Phazon'))))))),
 ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),
 ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Power Bomb',p) and s.has('Morph Ball Bomb',p) and (s.has('Boost Ball',p) or s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,30,'Phazon')))) and t['Shoot Plasma Beam'](s) and (s.has('Space Jump Boots',p) or o.slope_jump.value>=1) and t['Shoot Ice Beam'](s))),)),
("Pickup (Artifact of Newborn) (Phazon Mining Tunnel, Phazon Mines)",(
 ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (s.has('Phazon Suit',p) or (s.has('Boost Ball',p) and ((o.movement.value>=4 and l_csd(s,p,200,'Phazon')) or (o.movement.value>=3 and l_csd(s,p,300,'Phazon')) or (o.movement.value>=2 and l_csd(s,p,400,'Phazon'))))))),)),
("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)",(
 ("Door to Elevator B (Fungal Hall Access, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.standable_terrain.value>=3 and (o.bomb_jump.value>=3 or o.bomb_space_jump.value>=3)))),
 ("Pickup (Missile) (Fungal Hall Access, Phazon Mines)",lambda s:(s.has('Morph Ball',p) and (s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,100,'Phazon'))))),
 ("Door to Fungal Hall B (Phazon Mining Tunnel, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Power Bomb',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and (s.has('Phazon Suit',p) or (o.movement.value>=1 and l_csd(s,p,30,'Phazon')))))) and t['Shoot Ice Beam'](s) and (((s.has('Space Jump Boots',p) and ((o.r_jump.value>=2 or t['Use Grapple Beam'](s)) or (s.has('Scan Visor',p) and o.scan_dash.value>=2))) or (s.has('Scan Visor',p) and ((o.scan_dash.value>=4 and t['Use Grapple Beam'](s)) or o.scan_dash.value>=5))) and (l_hm(s, p, 4) or s.has('Charge Beam',p) or l_csd(s,p,599,'Damage') or (l_csd(s,p,299,'Damage') and o.combat.value>=1 and s.has('Space Jump Boots',p)) or (l_csd(s,p,299,'Damage') and o.combat.value>=3) or (s.has('Space Jump Boots',p) and o.combat.value>=2) or o.combat.value>=4 or (s.has('Plasma Beam',p) and o.combat.value>=1) or (s.has('Plasma Beam',p) and l_csd(s,p,299,'Damage')))) and t['Shoot Plasma Beam'](s))),)),
("Door to Elevator B (Fungal Hall Access, Phazon Mines)",(
 ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)",lambda s:(o.movement.value>=1 or s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))),
 ("Door to Elevator Access B (Metroid Quarantine A, Phazon Mines)",lambda s:(t['Shoot Plasma Beam'](s) and t['Shoot Ice Beam'](s))),)),
("Pickup (Missile) (Fungal Hall Access, Phazon Mines)",(
 ("Door to Fungal Hall A (Fungal Hall Access, Phazon Mines)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or o.movement.value>=5)),
 ("Door to Elevator B (Fungal Hall Access, Phazon Mines)",lambda s:s.has('Space Jump Boots',p)),)),
("Door to Gully (Landing Site, Tallon Overworld)",(
 ("Door to Alcove (Landing Site, Tallon Overworld)",None),
 ("Ship (Landing Site, Tallon Overworld)",None),
 ("Half Pipe (Tallon Canyon, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and ((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or s.has('Space Jump Boots',p)) and (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Space Jump Boots',p)))),)),
("Door to Alcove (Landing Site, Tallon Overworld)",(
 ("Door to Gully (Landing Site, Tallon Overworld)",None),
 ("Ship (Landing Site, Tallon Overworld)",None),
 ("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)",(
 ("Ship (Landing Site, Tallon Overworld)",None),)),
("Ship (Landing Site, Tallon Overworld)",(
 ("Door to Gully (Landing Site, Tallon Overworld)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4) or (s.has('Scan Visor',p) and o.scan_dash.value>=1) or (o.scan_dash.value>=2 and not l_hmisc(s,p,'dock_rando')))),
 ("Pickup (Missile Expansion) (Landing Site, Tallon Overworld)",lambda s:s.has('Morph Ball',p)),
 ("Half Pipe (Tallon Canyon, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),
 ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and s.has('Morph Ball',p) and t['Open Normal Door'](s))),
 ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)))),)),
("Half Pipe (Tallon Canyon, Tallon Overworld)",(
 ("Door to Gully (Landing Site, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball Bomb',p) and s.has('Morph Ball',p) and s.has('Boost Ball',p)))),
 ("Ship (Landing Site, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Root Tunnel (Root Cave, Tallon Overworld)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Open Normal Door'](s))),)),
("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)",(
 ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)",lambda s:(t['Use Grapple Beam'](s) or (s.has('Space Jump Boots',p) and (s.has('Morph Ball',p) or (s.has('Scan Visor',p) and o.standable_terrain.value>=2 and o.scan_dash.value>=2) or (s.has('Gravity Suit',p) and o.standable_terrain.value>=1) or (o.slope_jump.value>=2 and o.standable_terrain.value>=1 and o.l_jump.value>=1 and o.gravityless_underwater_movement.value>=1))) or (s.has('Morph Ball',p) and (s.has('Gravity Suit',p) or (o.slope_jump.value>=3 and o.gravityless_underwater_movement.value>=3))))),
 ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)",lambda s:((s.has('Space Jump Boots',p) and (s.has('Gravity Suit',p) or o.l_jump.value>=1 or (o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1))) or (s.has('Scan Visor',p) and (o.scan_dash.value>=2 or (s.has('Space Jump Boots',p) and o.scan_dash.value>=1))) or (o.slope_jump.value>=3 and l_hmisc(s,p,'NoGravity') and not s.has('Gravity Suit',p) and o.gravityless_underwater_movement.value>=3) or (t['Use Grapple Beam'](s) and o.movement.value>=1) or (s.has('Gravity Suit',p) and o.standable_terrain.value>=2 and o.l_jump.value>=2))),
 ("Ship (Landing Site, Tallon Overworld)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and s.has('Morph Ball',p) and t['Open Normal Door'](s))),)),
("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)",(
 ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)",None),
 ("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)",lambda s:(o.standable_terrain.value>=2 and o.l_jump.value>=2)),
 ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p) and t['Shoot Ice Beam'](s))),
 ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)",lambda s:(((s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=3 and o.standable_terrain.value>=3 and o.slope_jump.value>=3 and o.l_jump.value>=3) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.wall_boost.value>=2 and o.movement.value>=2) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1 and o.l_jump.value>=2)) and t['Shoot Ice Beam'](s) and s.has('Morph Ball',p))),)),
("Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)",(
 ("Door to Waterfall Cavern (Frigate Crash Site, Tallon Overworld)",None),)),
("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)",(
 ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)",lambda s:(t['Shoot Ice Beam'](s) and s.has('Morph Ball',p))),
 ("Save Station (Save Station 3, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and t['Shoot Ice Beam'](s) and t['Open Normal Door'](s) and (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=4))))),)),
("Door to Transport Tunnel B (Root Cave, Tallon Overworld)",(
 ("Door to Root Tunnel (Root Cave, Tallon Overworld)",None),
 ("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Door to Root Tunnel (Root Cave, Tallon Overworld)",(
 ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)",None),
 ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)",lambda s:((s.has('Space Jump Boots',p) and (t['Use Grapple Beam'](s) or o.scan_dash.value>=2 or (o.l_jump.value>=2 and o.slope_jump.value>=2 and o.standable_terrain.value>=2)) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=1)) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.standable_terrain.value>=3 and o.single_room_oob.value>=3 and s.has('Power Bomb',p) and ((o.instant_unmorph_jump.value>=4 and o.wall_boost.value>=5) or (s.has('Morph Ball Bomb',p) and o.bomb_space_jump.value>=3)) and o.movement.value>=4 and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=2)))),
 ("Half Pipe (Tallon Canyon, Tallon Overworld)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Open Normal Door'](s))),)),
("Door to Arbor Chamber (Root Cave, Tallon Overworld)",(
 ("Door to Root Tunnel (Root Cave, Tallon Overworld)",None),
 ("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)",lambda s:((s.has('X-Ray Visor',p) or o.invisible_objects.value>=1) and (s.has('Space Jump Boots',p) or o.scan_dash.value>=2))),
 ("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Pickup (Missile Expansion) (Root Cave, Tallon Overworld)",(
 ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)",None),
 ("Door to Root Tunnel (Root Cave, Tallon Overworld)",None),
 ("Door to Arbor Chamber (Root Cave, Tallon Overworld)",lambda s:(s.has('Space Jump Boots',p) and (s.has('X-Ray Visor',p) or o.invisible_objects.value>=1))),)),
("Door to Temple Lobby (Artifact Temple, Tallon Overworld)",(
 ("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)",None),
 ("Event - Meta Ridley (Artifact Temple, Tallon Overworld)",lambda s:(s.has('Artifact of Chozo',p) and s.has('Artifact of Elder',p) and s.has('Artifact of Lifegiver',p) and s.has('Artifact of Nature',p) and s.has('Artifact of Newborn',p) and s.has('Artifact of Spirit',p) and s.has('Artifact of Strength',p) and s.has('Artifact of Sun',p) and s.has('Artifact of Truth',p) and s.has('Artifact of Warrior',p) and s.has('Artifact of Wild',p) and s.has('Artifact of World',p) and (s.has('Charge Beam',p) or o.combat.value>=2) and (l_csd(s,p,400,'Damage') or (o.combat.value>=1 and l_csd(s,p,300,'Damage')) or (o.combat.value>=2 and l_csd(s,p,200,'Damage')) or (o.combat.value>=3 and l_csd(s,p,100,'Damage')) or o.combat.value>=4) and t['Shoot Any Beam'](s))),
 ("Ship (Landing Site, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),
 ("Teleporter to Tallon Overworld (Crater Entry Point, Impact Crater)",lambda s:s.has('Meta Ridley',p)),)),
("Pickup (Artifact of Truth) (Artifact Temple, Tallon Overworld)",(
 ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)",None),)),
("Event - Meta Ridley (Artifact Temple, Tallon Overworld)",(
 ("Door to Temple Lobby (Artifact Temple, Tallon Overworld)",None),)),
("Pickup (Missile Expansion) (Transport Tunnel B, Tallon Overworld)",(
 ("Door to Transport Tunnel B (Transport to Tallon Overworld West, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),
 ("Door to Transport Tunnel B (Root Cave, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)",(
 ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:(s.has('Main Ventilation Shaft Section B Conduit',p) or l_hmisc(s,p,'backwards_frigate'))),
 ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and t['Shoot Wave Beam'](s) and o.complex_bomb_jump.value>=4 and o.single_room_oob.value>=4 and not l_hmisc(s,p,'backwards_frigate'))),
 ("Room Bottom (Reactor Core, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)",(
 ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:s.has('Main Ventilation Shaft Section B Conduit',p)),
 ("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))),
 ("Door to Frigate Access Tunnel (Frigate Crash Site, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3))) and t['Shoot Ice Beam'](s))),)),
("Event - Main Ventilation Shaft Section B Conduit Activated (Main Ventilation Shaft Section B, Tallon Overworld)",(
 ("Door to Main Ventilation Shaft Section C (Main Ventilation Shaft Section B, Tallon Overworld)",None),)),
("Room Bottom (Reactor Core, Tallon Overworld)",(
 ("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1) and (s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or o.slope_jump.value>=3))),
 ("Door to Reactor Core (Reactor Access, Tallon Overworld)",lambda s:(s.has('Reactor Core Conduits',p) and (s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or (o.slope_jump.value>=3 and o.gravityless_underwater_movement.value>=3)))),
 ("Door to Main Ventilation Shaft Section A (Main Ventilation Shaft Section B, Tallon Overworld)",lambda s:((s.has('Space Jump Boots',p) or s.has('Gravity Suit',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4 and o.gravityless_underwater_movement.value>=4)) and t['Open Normal Door'](s))),)),
("Event - Reactor Core Conduits Activated (Reactor Core, Tallon Overworld)",(
 ("Room Bottom (Reactor Core, Tallon Overworld)",None),)),
("Door to Reactor Core (Reactor Access, Tallon Overworld)",(
 ("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))),
 ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",lambda s:s.has('Reactor Access Conduits',p)),
 ("Save Station (Savestation, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),
 ("Room Bottom (Reactor Core, Tallon Overworld)",None),)),
("Event - Reactor Access Conduits Activated (Reactor Access, Tallon Overworld)",(
 ("Door to Reactor Core (Reactor Access, Tallon Overworld)",None),)),
("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",(
 ("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",lambda s:(t['Shoot Any Beam'](s) and (l_hm(s, p, 1) or s.has('Charge Beam',p)))),
 ("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1) and ((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4))) or (not s.has('Gravity Suit',p) and ((s.has('Space Jump Boots',p) and o.slope_jump.value>=2 and o.l_jump.value>=2 and o.gravityless_underwater_movement.value>=2) or (s.has('Morph Ball',p) and o.slope_jump.value>=4 and o.gravityless_underwater_movement.value>=3 and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (s.has('Boost Ball',p) and o.wall_boost.value>=1)) and l_hmisc(s,p,'NoGravity'))))))),
 ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and s.has('Cargo Freight Lift to Deck Gamma Conduits',p))),
 ("Door to Reactor Core (Reactor Access, Tallon Overworld)",None),)),
("Pickup (Energy Tank) (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",(
 ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",None),)),
("Event - Conduits Activated (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",(
 ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",None),)),
("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)",(
 ("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))),
 ("Room Bottom (Biohazard Containment, Tallon Overworld)",None),
 ("Door to Reactor Access (Cargo Freight Lift to Deck Gamma, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)",(
 ("Room Bottom (Biohazard Containment, Tallon Overworld)",None),)),
("Event - Biohazard Containment Conduits Activated (Biohazard Containment, Tallon Overworld)",(
 ("Room Bottom (Biohazard Containment, Tallon Overworld)",None),)),
("Room Bottom (Biohazard Containment, Tallon Overworld)",(
 ("Door to Deck Beta Transit Hall (Biohazard Containment, Tallon Overworld)",lambda s:((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and o.standable_terrain.value>=1) or (o.slope_jump.value>=4 and o.standable_terrain.value>=1))) or ((s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (o.slope_jump.value>=4 and o.standable_terrain.value>=3 and o.gravityless_underwater_movement.value>=3)))),
 ("Pickup (Missile Expansion) (Biohazard Containment, Tallon Overworld)",lambda s:t['Shoot Super Missile'](s)),
 ("Room Center (Biotech Research Area 1, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and s.has('Biohazard Containment Conduits',p))),)),
("Room Center (Biotech Research Area 1, Tallon Overworld)",(
 ("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)",lambda s:(t['Shoot Wave Beam'](s) and (s.has('Thermal Visor',p) or o.invisible_objects.value>=1))),
 ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and (s.has('Gravity Suit',p) or s.has('Space Jump Boots',p) or (o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1)) and (s.has('Biotech Research Area 1 Conduits',p) and ((o.l_jump.value>=1 and (s.has('Gravity Suit',p) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2))) or (s.has('Space Jump Boots',p) and (s.has('Gravity Suit',p) or o.gravityless_underwater_movement.value>=1)))))),
 ("Room Bottom (Biohazard Containment, Tallon Overworld)",lambda s:(((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or o.standable_terrain.value>=1)) or (s.has('Space Jump Boots',p) and o.gravityless_underwater_movement.value>=1 and (o.slope_jump.value>=1 or o.standable_terrain.value>=1)) or (o.slope_jump.value>=2 and o.standable_terrain.value>=3 and o.gravityless_underwater_movement.value>=3)) and t['Open Normal Door'](s))),)),
("Event - Conduits Activated (Biotech Research Area 1, Tallon Overworld)",(
 ("Room Center (Biotech Research Area 1, Tallon Overworld)",None),)),
("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)",(
 ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Gravity Suit',p) and s.has('Morph Ball Bomb',p)) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),
 ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Gravity Suit',p))),
 ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)",lambda s:(((o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=2) or s.has('Space Jump Boots',p) or s.has('Gravity Suit',p)) and t['Open Normal Door'](s))),)),
("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)",(
 ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and s.has('Gravity Suit',p)) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),
 ("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Gravity Suit',p) and s.has('Morph Ball Bomb',p)) or (not s.has('Gravity Suit',p) and l_hmisc(s,p,'NoGravity') and o.gravityless_underwater_movement.value>=1)))),
 ("Room Center (Biotech Research Area 1, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and ((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3))) or (o.gravityless_underwater_movement.value>=4 and ((s.has('Space Jump Boots',p) and o.slope_jump.value>=3) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and o.slope_jump.value>=4)))))),)),
("Pickup (Energy Tank) (Hydro Access Tunnel, Tallon Overworld)",(
 ("Door to Connection Elevator to Deck Beta (Hydro Access Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Gravity Suit',p) and s.has('Morph Ball Bomb',p)) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),)),
("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)",(
 ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)",None),
 ("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)",(
 ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)",lambda s:((s.has('X-Ray Visor',p) or o.invisible_objects.value>=1) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and s.has('Scan Visor',p) and o.scan_dash.value>=3) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and o.jump_off_enemies.value>=3 and l_csd(s,p,200,'Damage'))))),
 ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)",lambda s:((s.has('Space Jump Boots',p) and (o.standable_terrain.value>=1 or (s.has('Morph Ball',p) and s.has('Spider Ball',p)))) or (s.has('Morph Ball',p) and ((s.has('Spider Ball',p) and (o.standable_terrain.value>=1 or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2))) or (s.has('Morph Ball Bomb',p) and o.standable_terrain.value>=4 and o.bomb_jump.value>=5 and o.complex_bomb_jump.value>=5 and o.movement.value>=5 and o.scan_dash.value>=4))))),
 ("Next to Spinner (Great Tree Hall, Tallon Overworld)",lambda s:(s.has('Great Tree Hall Bars Unlocked',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3))),
 ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)",lambda s:(t['Shoot Ice Beam'](s) and t['Open Normal Door'](s))),)),
("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)",(
 ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)",lambda s:((s.has('X-Ray Visor',p) or o.invisible_objects.value>=1) and (s.has('Space Jump Boots',p) or (s.has('Scan Visor',p) and o.scan_dash.value>=3)))),
 ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)",None),
 ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)",lambda s:t['Shoot Ice Beam'](s)),)),
("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)",(
 ("Next to Spinner (Great Tree Hall, Tallon Overworld)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Scan Visor',p) and s.has('Morph Ball',p) and o.scan_dash.value>=5 and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (s.has('Boost Ball',p) and o.wall_boost.value>=5))))),
 ("Door to Quarry Access (Main Quarry, Phazon Mines)",lambda s:(t['Shoot Wave Beam'](s) and t['Shoot Ice Beam'](s))),
 ("Door to Great Tree Hall (Hydro Access Tunnel, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Event - Open gate (Great Tree Hall, Tallon Overworld)",(
 ("Next to Spinner (Great Tree Hall, Tallon Overworld)",None),)),
("Next to Spinner (Great Tree Hall, Tallon Overworld)",(
 ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)",lambda s:(s.has('Great Tree Hall Bars Unlocked',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3))),
 ("Door to Transport Tunnel E (Great Tree Hall, Tallon Overworld)",None),
 ("Event - Open gate (Great Tree Hall, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Boost Ball',p))),)),
("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)",(
 ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Boost Ball',p) and (s.has('Morph Ball Bomb',p) or o.wall_boost.value>=2)) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3)) and s.has('Power Bomb',p))),
 ("Door to Life Grove Tunnel (Great Tree Hall, Tallon Overworld)",lambda s:t['Shoot Ice Beam'](s)),)),
("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)",(
 ("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3)))),
 ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)",(
 ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Boost Ball',p) and (s.has('Morph Ball Bomb',p) or o.wall_boost.value>=2)) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=5)) and s.has('Power Bomb',p))),
 ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=5)))),)),
("Top of Half Pipe (Life Grove Tunnel, Tallon Overworld)",(
 ("Door to Great Tree Hall (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=2)))),
 ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)",lambda s:s.has('Morph Ball',p)),
 ("Pickup (Missile Expansion) (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))),)),
("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)",(
 ("Front of PB Wall (Life Grove, Tallon Overworld)",lambda s:s.has('Morph Ball',p)),
 ("Morph Ball Door to Life Grove (Life Grove Tunnel, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)",(
 ("Front of PB Wall (Life Grove, Tallon Overworld)",None),)),
("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)",(
 ("Behind PB Wall (Life Grove, Tallon Overworld)",None),)),
("Behind PB Wall (Life Grove, Tallon Overworld)",(
 ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)",lambda s:(t['Shoot Power Beam'](s) and (s.has('Space Jump Boots',p) or (((s.has('Scan Visor',p) and o.scan_dash.value>=2) or o.scan_dash.value>=4) and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (o.l_jump.value>=3 and o.r_jump.value>=3 and o.standable_terrain.value>=2 and (o.slope_jump.value>=3 or (s.has('Scan Visor',p) and o.scan_dash.value>=4)) and ((s.has('Boost Ball',p) and o.wall_boost.value>=3) or o.movement.value>=4))))) and s.has('Morph Ball',p))),
 ("Pickup (Artifact of Chozo) (Life Grove, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and ((s.has('Space Jump Boots',p) and o.single_room_oob.value>=3 and o.standable_terrain.value>=3) or ((s.has('Boost Ball',p) or o.spinners_without_boost.value>=3) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2) or (o.l_jump.value>=3 and o.standable_terrain.value>=2)))))),
 ("Front of PB Wall (Life Grove, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p))),)),
("Front of PB Wall (Life Grove, Tallon Overworld)",(
 ("Morph Ball Door to Life Grove Tunnel (Life Grove, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Space Jump Boots',p) and o.standable_terrain.value>=1 and o.r_jump.value>=2)),
 ("Pickup (X-Ray Visor) (Life Grove, Tallon Overworld)",None),
 ("Behind PB Wall (Life Grove, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p))),)),
("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),
 ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)",lambda s:(t['Shoot Super Missile'](s) and (s.has('Space Jump Boots',p) or o.movement.value>=1))),
 ("Grapple Ledge (Main Plaza, Chozo Ruins)",lambda s:((t['Use Grapple Beam'](s) and ((s.has('Space Jump Boots',p) and o.movement.value>=1) or o.movement.value>=2)) or (s.has('Space Jump Boots',p) and (o.l_jump.value>=2 or o.r_jump.value>=2 or (s.has('Scan Visor',p) and o.scan_dash.value>=2))) or (o.scan_dash.value>=5 and s.has('Chozo - Fallen Rubble',p) and o.damage_boosting.value>=4 and s.has('Scan Visor',p)))),
 ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p))),)),
("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",(
 ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)",None),
 ("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=3) or o.movement.value>=4)) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=1))),
 ("Locked Door Ledge (Main Plaza, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) and o.l_jump.value>=1)),
 ("Half Pipe (Tallon Canyon, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),
 ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Open Normal Door'](s))),)),
("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),
 ("Grapple Ledge (Main Plaza, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (t['Use Grapple Beam'](s) or (s.has('Scan Visor',p) and ((s.has('Space Jump Boots',p) and o.scan_dash.value>=2) or (o.scan_dash.value>=3 and o.standable_terrain.value>=3))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3)))),
 ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))) and s.has('Training Chamber Exit Tunnel',p))),)),
("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)",(
 ("Locked Door Ledge (Main Plaza, Chozo Ruins)",None),)),
("Pickup (Missile Expansion Half Pipe) (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),)),
("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),)),
("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)",(
 ("Grapple Ledge (Main Plaza, Chozo Ruins)",None),)),
("Locked Door Ledge (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),
 ("Pickup (Energy Tank) (Main Plaza, Chozo Ruins)",None),)),
("Grapple Ledge (Main Plaza, Chozo Ruins)",(
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",None),
 ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((t['Use Grapple Beam'](s) and (s.has('Space Jump Boots',p) or o.movement.value>=3 or o.standable_terrain.value>=2)) or (s.has('Space Jump Boots',p) and ((s.has('Scan Visor',p) and o.scan_dash.value>=1) or o.standable_terrain.value>=3)) or (o.standable_terrain.value>=3 and o.l_jump.value>=2)))),
 ("Pickup (Missile Expansion Tree) (Main Plaza, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Space Jump Boots',p) and o.bomb_jump.value>=3 and o.movement.value>=3 and o.single_room_oob.value>=3)),
 ("Pickup (Missile Expansion Grapple Ledge) (Main Plaza, Chozo Ruins)",None),
 ("Locked Door Ledge (Main Plaza, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4 and o.l_jump.value>=5 and o.single_room_oob.value>=4 and o.standable_terrain.value>=4)),)),
("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Spider Ball',p) and (s.has('Flaahgra',p) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=2) or (o.standable_terrain.value>=3 and o.scan_dash.value>=3)))),
 ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)",lambda s:(((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or (s.has('Space Jump Boots',p) and ((o.standable_terrain.value>=2 and o.l_jump.value>=2 and o.movement.value>=2) or (s.has('Scan Visor',p) and o.scan_dash.value>=3) or (s.has('Gravity Suit',p) and l_csd(s,p,50,'HeatDamage2') and o.l_jump.value>=2 and o.standable_terrain.value>=1)) and (t['Heat-Resisting Suit'](s) or (l_csd(s,p,99,'HeatDamage1') and o.heat_runs.value>=1)))) and t['Open Normal Door'](s))),
 ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)))),
 ("Door to Ruined Fountain Access (Main Plaza, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p))),)),
("Pickup (Missile Expansion) (Ruined Fountain, Chozo Ruins)",(
 ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)",None),)),
("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)",(
 ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Scan Visor',p) and o.scan_dash.value>=2)),
 ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Space Jump Boots',p) and o.l_jump.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=2)))),
 ("Pit (Ruined Shrine, Chozo Ruins)",None),
 ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)",None),
 ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),)),
("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)",(
 ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)",lambda s:((s.has('Boost Ball',p) and s.has('Morph Ball',p) and s.has('Spider Ball',p)) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=3 and o.standable_terrain.value>=3) or (o.standable_terrain.value>=3 and o.l_jump.value>=2))),
 ("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (o.l_jump.value>=2 and o.standable_terrain.value>=3) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=5)))),
 ("Pit (Ruined Shrine, Chozo Ruins)",None),
 ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Scan Visor',p) and o.scan_dash.value>=2)),
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)",(
 ("Pit (Ruined Shrine, Chozo Ruins)",None),)),
("Pickup (Missile Expansion Half Pipe) (Ruined Shrine, Chozo Ruins)",(
 ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)",None),)),
("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)",(
 ("Pit (Ruined Shrine, Chozo Ruins)",None),)),
("Pit (Ruined Shrine, Chozo Ruins)",(
 ("Door to Ruined Shrine Access (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) or (o.standable_terrain.value>=2 and o.scan_dash.value>=2 and (s.has('Scan Visor',p) or not s.has('Beetle Battle',p))) or (o.l_jump.value>=2 and o.standable_terrain.value>=2) or (s.has('Morph Ball',p) and (s.has('Ruined Shrine Item (Morph Ball)',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))))),
 ("Pickup (Missile Expansion Bomb Wall) (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))),
 ("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)",lambda s:(t['Shoot Any Beam'](s) or (o.combat.value>=2 and s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or s.has('Power Bomb',p,4))))),
 ("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or s.has('Beetle Battle',p) or (o.standable_terrain.value>=2 and (o.scan_dash.value>=3 or (s.has('Scan Visor',p) and o.scan_dash.value>=2))))),)),
("Event - Beetle Battle (Ruined Shrine, Chozo Ruins)",(
 ("Pit (Ruined Shrine, Chozo Ruins)",None),)),
("Event - Ruined Shrine Item (Morph Ball) (Ruined Shrine, Chozo Ruins)",(
 ("Pickup (Morph Ball) (Ruined Shrine, Chozo Ruins)",None),)),
("Door to Vault Access (Vault, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Vault, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Space Jump Boots',p) and s.has('Power Bomb',p,3) and o.standable_terrain.value>=3 and o.knowledge.value>=1)))),
 ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p))),
 ("Locked Door Ledge (Main Plaza, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Vault, Chozo Ruins)",(
 ("Door to Vault Access (Vault, Chozo Ruins)",None),)),
("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",(
 ("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Boost Ball',p) and s.has('Spider Ball',p) and (s.has('Chozo Ghosts (Training Chamber)',p) or (s.has('Space Jump Boots',p) and o.bomb_space_jump.value>=5 and o.complex_bomb_jump.value>=4 and o.movement.value>=4 and o.slope_jump.value>=1 and o.standable_terrain.value>=2 and o.knowledge.value>=2)))),
 ("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)",lambda s:t['Shoot Power Beam'](s)),
 ("Event - Unlock morph track (Training Chamber, Chozo Ruins)",lambda s:(s.has('Chozo Ghosts (Training Chamber)',p) and s.has('Boost Ball',p) and s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p))),
 ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),
 ("Morph Ball Door to Piston Tunnel (Main Plaza, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))) and s.has('Training Chamber Exit Tunnel',p))),)),
("Pickup (Energy Tank) (Training Chamber, Chozo Ruins)",(
 ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Spider Ball',p) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=2) or o.movement.value>=4) and (s.has('Chozo Ghosts (Training Chamber)',p) or (s.has('Morph Ball Bomb',p) and s.has('Space Jump Boots',p) and o.bomb_space_jump.value>=2 and o.standable_terrain.value>=2 and o.knowledge.value>=2)))),)),
("Event - Chozo Ghosts (Training Chamber, Chozo Ruins)",(
 ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",None),)),
("Event - Unlock morph track (Training Chamber, Chozo Ruins)",(
 ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",None),)),
("Door to North Atrium (Ruined Nursery, Chozo Ruins)",(
 ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)",None),
 ("Door to North Atrium (Ruined Gallery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Save Station (Save Station 1, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)",(
 ("Door to North Atrium (Ruined Nursery, Chozo Ruins)",None),
 ("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or ((o.standable_terrain.value>=4 or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3)) and (o.movement.value>=4 or (s.has('Boost Ball',p) and o.movement.value>=2)))))),
 ("Door to Ruins Entrance (Main Plaza, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Ruined Nursery, Chozo Ruins)",(
 ("Door to Eyon Tunnel (Ruined Nursery, Chozo Ruins)",None),)),
("Door to Training Chamber (Training Chamber Access, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)",lambda s:s.has('Morph Ball',p)),
 ("Door to Training Chamber Access (Training Chamber, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),
 ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),)),
("Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)",(
 ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)",None),)),
("Door to Gathering Hall Access (Arboretum, Chozo Ruins)",(
 ("Front of Gate (Arboretum, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p)) or s.has('Space Jump Boots',p))),
 ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)))),)),
("Front of Gate (Arboretum, Chozo Ruins)",(
 ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)",None),
 ("Event - Open gate (Arboretum, Chozo Ruins)",lambda s:s.has('Scan Visor',p)),
 ("Before Fight (Front) (Sunchamber, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and (s.has('Arboretum Gate',p) or o.bomb_jump.value>=3)) or (s.has('Space Jump Boots',p) and s.has('Boost Ball',p) and o.single_room_oob.value>=3 and o.standable_terrain.value>=3 and o.clip_through_objects.value>=4))) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Open Normal Door'](s) and (not s.has('Flaahgra',p) or (s.has('Flaahgra',p) and s.has('Chozo Ghosts (Sunchamber)',p))))),)),
("Event - Open gate (Arboretum, Chozo Ruins)",(
 ("Front of Gate (Arboretum, Chozo Ruins)",None),)),
("Door to Training Chamber Access (Magma Pool, Chozo Ruins)",(
 ("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Power Bomb',p) and (t['Heat-Resisting Suit'](s) or (l_csd(s,p,60,'HeatDamage1') and o.heat_runs.value>=1)))),
 ("Door to Training Chamber (Training Chamber Access, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),
 ("Door to Meditation Fountain (Ruined Fountain, Chozo Ruins)",lambda s:(((t['Use Grapple Beam'](s) and t['Heat-Resisting Suit'](s)) or ((t['Heat-Resisting Suit'](s) or (l_csd(s,p,70,'HeatDamage1') and o.heat_runs.value>=1)) and s.has('Space Jump Boots',p) and ((o.movement.value>=2 and (l_csd(s,p,220,'HeatDamage2') or o.standable_terrain.value>=2)) or (s.has('Scan Visor',p) and o.scan_dash.value>=3)))) and t['Open Normal Door'](s))),)),
("Pickup (Power Bomb Expansion) (Magma Pool, Chozo Ruins)",(
 ("Door to Training Chamber Access (Magma Pool, Chozo Ruins)",lambda s:(t['Heat-Resisting Suit'](s) or (l_csd(s,p,35,'HeatDamage1') and o.heat_runs.value>=1))),)),
("Door to Tower of Light Access (Tower of Light, Chozo Ruins)",(
 ("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)",lambda s:((l_hm(s, p, 36) and t['Shoot Any Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=4))) or (s.has('Space Jump Boots',p) and ((o.scan_dash.value>=2 and o.standable_terrain.value>=1) or (o.scan_dash.value>=2 and o.l_jump.value>=2 and o.standable_terrain.value>=2) or (o.scan_dash.value>=2 and o.slope_jump.value>=1 and o.standable_terrain.value>=3) or (o.r_jump.value>=3 and o.standable_terrain.value>=1))))),
 ("Door to Tower of Light Access (Ruined Shrine, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and t['Shoot Wave Beam'](s))),
 ("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)",lambda s:(((s.has('Gravity Suit',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Boost Ball',p) and o.wall_boost.value>=4))))) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1) or (not s.has('Gravity Suit',p) and o.slope_jump.value>=3 and l_hmisc(s,p,'NoGravity') and o.gravityless_underwater_movement.value>=2)) and t['Shoot Wave Beam'](s))),)),
("Pickup (Wavebuster) (Tower of Light, Chozo Ruins)",(
 ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)",None),)),
("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)",(
 ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Vault Access (Vault, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p))),
 ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),
 ("Door to Hive Totem (Transport Access North, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=4))))),)),
("Door to North Atrium (Ruined Gallery, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),
 ("Door to Totem Access (Hive Totem, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Map Station (Map Station, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Door to North Atrium (Ruined Nursery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Ruined Gallery, Chozo Ruins)",(
 ("Door to North Atrium (Ruined Gallery, Chozo Ruins)",None),)),
("Pickup (Missile Expansion 2) (Ruined Gallery, Chozo Ruins)",(
 ("Door to North Atrium (Ruined Gallery, Chozo Ruins)",None),)),
("Door to Sun Tower Access (Sun Tower, Chozo Ruins)",(
 ("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)",lambda s:s.has('Flaahgra',p)),
 ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)",(
 ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p) and (s.has('Sun Tower Spider Track Unlocked',p) or (((s.has('Space Jump Boots',p) and o.complex_bomb_jump.value>=5 and o.movement.value>=3) or (o.complex_bomb_jump.value>=5 and o.movement.value>=5)) and ((l_hm(s, p, 4) and t['Shoot Any Beam'](s)) or o.combat.value>=5))))),
 ("Event - Unlock spider track (Sun Tower, Chozo Ruins)",lambda s:(t['Shoot Super Missile'](s) and s.has('Scan Visor',p))),
 ("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p) and s.has('Sun Tower Spider Track Unlocked',p) and s.has('Flaahgra',p))),
 ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Event - Unlock spider track (Sun Tower, Chozo Ruins)",(
 ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)",None),)),
("Event - Activate Sunchamber Ghosts From Top (Sun Tower, Chozo Ruins)",(
 ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=2 and l_csd(s,p,20,'Damage')) or s.has('Spider Ball',p) or (o.instant_unmorph_jump.value>=5 and s.has('Space Jump Boots',p))) and o.knowledge.value>=2)),
 ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)",None),)),
("Event - Activate Sunchamber Ghosts From Bottom (Sun Tower, Chozo Ruins)",(
 ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and s.has('Spider Ball',p))),
 ("Door to Transport to Magmoor Caverns North (Sun Tower, Chozo Ruins)",None),)),
("Door to Hive Totem (Transport Access North, Chozo Ruins)",(
 ("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)",None),
 ("Door to Transport Access North (Hive Totem, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Door to Transport Access North (Transport to Magmoor Caverns North, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('Morph Ball',p))),)),
("Pickup (Energy Tank) (Transport Access North, Chozo Ruins)",(
 ("Door to Hive Totem (Transport Access North, Chozo Ruins)",None),)),
("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)",(
 ("Door to East Atrium (Gathering Hall, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) or s.has('Space Jump Boots',p) or o.l_jump.value>=1 or (s.has('Scan Visor',p) and o.scan_dash.value>=1))),
 ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Save Station (Save Station 2, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Door to Gathering Hall Access (Arboretum, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to East Atrium (Gathering Hall, Chozo Ruins)",(
 ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)",None),
 ("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Space Jump Boots',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1))) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Power Bomb',p) and o.scan_dash.value>=5 and o.standable_terrain.value>=5 and s.has('Scan Visor',p))))),
 ("Door to Energy Core Access (Energy Core, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)",(
 ("Door to East Atrium (Gathering Hall, Chozo Ruins)",None),)),
("Door to Totem Access (Hive Totem, Chozo Ruins)",(
 ("Door to Transport Access North (Hive Totem, Chozo Ruins)",lambda s:(s.has('Hive Mecha',p) or (s.has('Space Jump Boots',p) and o.movement.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=1) or (o.slope_jump.value>=2 and o.gravityless_underwater_movement.value>=1 and (l_csd(s,p,30,'RuinsWater') or s.has('Flaahgra',p))) or (not l_hmisc(s,p,'dock_rando') and o.scan_dash.value>=2) or (o.knowledge.value>=3 and o.movement.value>=3))),
 ("Event - Hive Mecha (Hive Totem, Chozo Ruins)",lambda s:t['Shoot Power Beam'](s)),
 ("Door to North Atrium (Ruined Gallery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Transport Access North (Hive Totem, Chozo Ruins)",(
 ("Door to Totem Access (Hive Totem, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Scan Visor',p) and o.scan_dash.value>=1) or s.has('Chozo - Fallen Rubble',p))),
 ("Event - Hive Mecha (Hive Totem, Chozo Ruins)",None),
 ("Event - Fallen Rubble (Hive Totem, Chozo Ruins)",None),
 ("Door to Hive Totem (Transport Access North, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)",(
 ("Door to Transport Access North (Hive Totem, Chozo Ruins)",None),)),
("Event - Hive Mecha (Hive Totem, Chozo Ruins)",(
 ("Door to Transport Access North (Hive Totem, Chozo Ruins)",None),)),
("Event - Fallen Rubble (Hive Totem, Chozo Ruins)",(
 ("Pickup (Missile Launcher) (Hive Totem, Chozo Ruins)",None),)),
("Door to Sun Tower Access (Sunchamber, Chozo Ruins)",(
 ("Before Fight (Front) (Sunchamber, Chozo Ruins)",None),
 ("Before Fight (Back) (Sunchamber, Chozo Ruins)",None),
 ("Door to Sun Tower Access (Sun Tower, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)",(
 ("Before Fight (Front) (Sunchamber, Chozo Ruins)",None),)),
("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)",(
 ("Before Fight (Front) (Sunchamber, Chozo Ruins)",None),)),
("Event - Flaahgra (Sunchamber, Chozo Ruins)",(
 ("Pickup (Varia Suit) (Sunchamber, Chozo Ruins)",None),)),
("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)",(
 ("Pickup (Artifact of Wild) (Sunchamber, Chozo Ruins)",None),)),
("Before Fight (Front) (Sunchamber, Chozo Ruins)",(
 ("Door to Sun Tower Access (Sunchamber, Chozo Ruins)",lambda s:(s.has('Flaahgra',p) or s.has('Chozo Ghosts (Sunchamber)',p))),
 ("Event - Flaahgra (Sunchamber, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (o.combat.value>=1 and s.has('Power Bomb',p,4))) and ((l_hm(s, p, 10) and t['Shoot Any Beam'](s)) or t['Shoot Power Beam'](s) or (o.l_jump.value>=1 and s.has('Space Jump Boots',p) and o.combat.value>=1) or (o.scan_dash.value>=3 and o.combat.value>=2)) and (t['Shoot Power Beam'](s) or (t['Shoot Any Beam'](s) and l_hm(s, p, 1)))) or (t['Shoot Wave Beam'](s) and s.has('Wavebuster',p) and l_hm(s, p, 230) and o.combat.value>=3 and s.has('Charge Beam',p)))),
 ("Event - Chozo Ghosts (Sunchamber, Chozo Ruins)",lambda s:((s.has('Sunchamber Chozo Ghosts Layer Activated',p) and (s.has('Charge Beam',p) or o.combat.value>=2)) and (t['Shoot Power Beam'](s) and (s.has('Space Jump Boots',p) or o.l_jump.value>=1)))),
 ("Front of Gate (Arboretum, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and (s.has('Arboretum Gate',p) or (s.has('Boost Ball',p) and o.clip_through_objects.value>=1) or o.bomb_jump.value>=2)) and t['Open Normal Door'](s) and s.has('Chozo Ghosts (Sunchamber)',p))),)),
("Before Fight (Back) (Sunchamber, Chozo Ruins)",(
 ("Event - Flaahgra (Sunchamber, Chozo Ruins)",lambda s:(o.knowledge.value>=1 and s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or s.has('Power Bomb',p,4)) and ((s.has('Space Jump Boots',p) and o.l_jump.value>=1) or o.scan_dash.value>=3))),)),
("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) or (t['Shoot Power Beam'](s) and s.has('Charge Beam',p) and o.knowledge.value>=1))),
 ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Pickup (Missile Expansion) (Watery Hall Access, Chozo Ruins)",(
 ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)",None),)),
("Door to Watery Hall Access (Watery Hall, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)",lambda s:((l_csd(s,p,57,'RuinsWater') or s.has('Flaahgra',p) or (s.has('Gravity Suit',p) and l_csd(s,p,25,'RuinsWater'))) and ((s.has('Gravity Suit',p) and s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1 and l_csd(s,p,15,'RuinsWater')) or (not s.has('Gravity Suit',p) and o.slope_jump.value>=3 and l_hmisc(s,p,'NoGravity') and o.gravityless_underwater_movement.value>=3) or (s.has('Space Jump Boots',p) and (s.has('Gravity Suit',p) or (o.slope_jump.value>=1 and o.gravityless_underwater_movement.value>=1))) or (s.has('Gravity Suit',p) and s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.wall_boost.value>=1 and ((o.movement.value>=2 and l_csd(s,p,65,'RuinsWater')) or (o.movement.value>=4 and l_csd(s,p,20,'RuinsWater'))))))),
 ("Event - Open gate (Watery Hall, Chozo Ruins)",lambda s:s.has('Scan Visor',p)),
 ("Behind Gate (Watery Hall, Chozo Ruins)",lambda s:s.has('Watery Hall Gate',p)),
 ("Door to Gathering Hall (Watery Hall Access, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)",(
 ("Behind Gate (Watery Hall, Chozo Ruins)",None),)),
("Pickup (Missile Expansion) (Watery Hall, Chozo Ruins)",(
 ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)",lambda s:(s.has('Flaahgra',p) or l_csd(s,p,42,'RuinsWater') or (s.has('Gravity Suit',p) and l_csd(s,p,25,'RuinsWater')))),)),
("Event - Open gate (Watery Hall, Chozo Ruins)",(
 ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)",None),)),
("Behind Gate (Watery Hall, Chozo Ruins)",(
 ("Door to Watery Hall Access (Watery Hall, Chozo Ruins)",lambda s:(s.has('Watery Hall Gate',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.clip_through_objects.value>=1))),
 ("Pickup (Charge Beam) (Watery Hall, Chozo Ruins)",None),
 ("Door to Dynamo Access (Dynamo, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1) or (s.has('Boost Ball',p) and o.single_room_oob.value>=3 and o.clip_through_objects.value>=4 and o.standable_terrain.value>=3 and (s.has('Space Jump Boots',p) or o.movement.value>=4)))) and (l_hm(s, p, 1) and t['Shoot Any Beam'](s)))),)),
("Door to Energy Core Access (Energy Core, Chozo Ruins)",(
 ("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p))),
 ("Door to West Furnace Access (Furnace, Chozo Ruins)",lambda s:(t['Open Normal Door'](s) and s.has('West Furnace Access Door Unlocked',p))),
 ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))))),
 ("Door to East Atrium (Gathering Hall, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Event - Unlock West Furnace Access Door (Energy Core, Chozo Ruins)",(
 ("Door to Energy Core Access (Energy Core, Chozo Ruins)",None),)),
("Door to Dynamo Access (Dynamo, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Spider Ball',p) and (s.has('Space Jump Boots',p) or o.standable_terrain.value>=1 or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1)))),
 ("Behind Gate (Watery Hall, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1))) and t['Open Normal Door'](s))),)),
("Pickup (Missile Expansion) (Dynamo, Chozo Ruins)",(
 ("Door to Dynamo Access (Dynamo, Chozo Ruins)",None),)),
("Pickup (Missile Expansion 2) (Dynamo, Chozo Ruins)",(
 ("Door to Dynamo Access (Dynamo, Chozo Ruins)",None),)),
("Door to Burn Dome (Burn Dome Access, Chozo Ruins)",(
 ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),
 ("Door to Energy Core Access (Energy Core, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=4)))),)),
("Spawn Point (Burn Dome Access, Chozo Ruins)",(
 ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)",lambda s:s.has('Morph Ball',p)),)),
("Door to Burn Dome Access (Burn Dome, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))),
 ("Before Fight (Burn Dome, Chozo Ruins)",None),
 ("Door to Burn Dome (Burn Dome Access, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)",(
 ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)",None),)),
("Pickup (Missile Expansion) (Burn Dome, Chozo Ruins)",(
 ("Door to Burn Dome Access (Burn Dome, Chozo Ruins)",lambda s:s.has('Incinerator Drone',p)),
 ("Before Fight (Burn Dome, Chozo Ruins)",None),)),
("Event - Incinerator Drone (Burn Dome, Chozo Ruins)",(
 ("Pickup (Morph Ball Bombs) (Burn Dome, Chozo Ruins)",None),)),
("Before Fight (Burn Dome, Chozo Ruins)",(
 ("Event - Incinerator Drone (Burn Dome, Chozo Ruins)",lambda s:(t['Shoot Power Beam'](s) or t['Shoot Wave Beam'](s) or t['Shoot Ice Beam'](s))),)),
("Door to West Furnace Access (Furnace, Chozo Ruins)",(
 ("Pickup (Energy Tank) (Furnace, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=2)))),
 ("Under Spider Track (Furnace, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Spider Ball',p) or o.standable_terrain.value>=1) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),
 ("Door to Energy Core Access (Energy Core, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Furnace, Chozo Ruins)",(
 ("Under Spider Track (Furnace, Chozo Ruins)",None),)),
("Pickup (Energy Tank) (Furnace, Chozo Ruins)",(
 ("Door to West Furnace Access (Furnace, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=4)))),)),
("Under Spider Track (Furnace, Chozo Ruins)",(
 ("Door to West Furnace Access (Furnace, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=3)))),
 ("Pickup (Missile Expansion) (Furnace, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Spider Ball',p) and ((s.has('Power Bomb',p) and s.has('Boost Ball',p) and (s.has('Morph Ball Bomb',p) or o.wall_boost.value>=2)) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=3))) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1 and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3) or (s.has('Spider Ball',p) and (s.has('Morph Ball Bomb',p) or o.movement.value>=1))))))),
 ("Room Center (Hall of the Elders, Chozo Ruins)",lambda s:(t['Shoot Ice Beam'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or o.l_jump.value>=1))),
 ("Door to Crossway Access West (Crossway, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))) and (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3) and t['Shoot Wave Beam'](s))),)),
("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)",(
 ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)",lambda s:s.has('Scan Visor',p)),
 ("Behind Barrier (Hall of the Elders, Chozo Ruins)",None),
 ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",None),
 ("Door to Elder Hall Access (Crossway, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",None),
 ("Door to Crossway Access West (Crossway, Chozo Ruins)",lambda s:(t['Shoot Ice Beam'](s) and s.has('Morph Ball',p))),)),
("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Unlock Doors',p) and s.has('Hall of the Elders Bomb Slots',p))),)),
("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",None),)),
("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)",(
 ("Behind Barrier (Hall of the Elders, Chozo Ruins)",None),)),
("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)",(
 ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)",lambda s:s.has('Hall of the Elders Unlock Doors',p)),
 ("Pickup (Energy Tank) (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Unlock Doors',p) and s.has('Hall of the Elders Bomb Slots',p) and t['Shoot Ice Beam'](s))),
 ("Event - Statue Moved (Hall of the Elders, Chozo Ruins)",lambda s:(t['Shoot Plasma Beam'](s) and s.has('Hall of the Elders Bomb Slots',p))),
 ("Room Center (Hall of the Elders, Chozo Ruins)",None),
 ("Behind Barrier (Hall of the Elders, Chozo Ruins)",lambda s:(t['Shoot Wave Beam'](s) and s.has('Hall of the Elders Bomb Slots',p) and s.has('Hall of the Elders Unlock Doors',p))),)),
("Event - Statue Moved (Hall of the Elders, Chozo Ruins)",(
 ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)",None),)),
("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",None),)),
("Room Center (Hall of the Elders, Chozo Ruins)",(
 ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Unlock Doors',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1)))),
 ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)",lambda s:s.has('Hall of the Elders Unlock Doors',p)),
 ("Event - Activate bomb slots (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and ((s.has('Spider Ball',p) and s.has('Hall of the Elders Unlock Doors',p)) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=1) or (s.has('Scan Visor',p) and o.bomb_jump.value>=5 and o.scan_dash.value>=4 and o.standable_terrain.value>=1)))),
 ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1))),
 ("Event - Unlock Doors (Hall of the Elders, Chozo Ruins)",lambda s:(t['Shoot Power Beam'](s) and (s.has('Charge Beam',p) or o.combat.value>=1))),
 ("Behind Barrier (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Unlock Doors',p) and ((s.has('Morph Ball Bomb',p) and s.has('Morph Ball',p) and o.bomb_jump.value>=4) or (s.has('Hall of the Elders Barrier',p) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1) or (s.has('Boost Ball',p) and s.has('Scan Visor',p) and o.scan_dash.value>=3 and o.instant_unmorph_jump.value>=4 and o.movement.value>=3 and o.standable_terrain.value>=2 and o.wall_boost.value>=3)))))))),
 ("Under Spider Track (Furnace, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Unlock Doors',p) and t['Shoot Ice Beam'](s))),
 ("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)",lambda s:((s.has('Hall of the Elders Statue',p) and (s.has('Hall of the Elders Unlock Doors',p) or o.knowledge.value>=2)) and t['Shoot Ice Beam'](s))),)),
("Behind Barrier (Hall of the Elders, Chozo Ruins)",(
 ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)",None),
 ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=1) or o.movement.value>=1) and s.has('Hall of the Elders Unlock Doors',p))),
 ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Space Jump Boots',p) and o.knowledge.value>=3 and o.l_jump.value>=2 and o.standable_terrain.value>=2 and (s.has('Hall of the Elders Barrier',p) or (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=1)) and (o.movement.value>=2 or (o.movement.value>=1 and s.has('Boost Ball',p))))))),
 ("Event - Deactivate barrier (Hall of the Elders, Chozo Ruins)",lambda s:s.has('Scan Visor',p)),
 ("Front of Beam Bomb Slots (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Barrier',p) or (s.has('Morph Ball',p) and (o.movement.value>=3 or (s.has('Boost Ball',p) and o.movement.value>=2)) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=1))))),
 ("Room Center (Hall of the Elders, Chozo Ruins)",lambda s:(s.has('Hall of the Elders Barrier',p) or (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Boost Ball',p) and o.wall_boost.value>=1))))),)),
("Door to Crossway Access West (Crossway, Chozo Ruins)",(
 ("Door to Elder Hall Access (Crossway, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Boost Ball',p) or (s.has('Morph Ball Bomb',p) and o.complex_bomb_jump.value>=4))) or (s.has('Space Jump Boots',p) and o.l_jump.value>=1))),
 ("Under Spider Track (Furnace, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))) and (s.has('Space Jump Boots',p) and o.standable_terrain.value>=3) and t['Open Normal Door'](s))),
 ("Door to Crossway Access South (Hall of the Elders, Chozo Ruins)",lambda s:(t['Shoot Ice Beam'](s) and s.has('Morph Ball',p))),)),
("Door to Elder Hall Access (Crossway, Chozo Ruins)",(
 ("Door to Crossway Access West (Crossway, Chozo Ruins)",None),
 ("Pickup (Missile Expansion) (Crossway, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and ((s.has('Morph Ball Bomb',p) and s.has('Boost Ball',p) and s.has('Crossway Bomb Slots',p) and (s.has('Spider Ball',p) or o.movement.value>=2)) or (s.has('Space Jump Boots',p) and o.l_jump.value>=1 and o.standable_terrain.value>=2) or (s.has('Boost Ball',p) and (o.movement.value>=3 or (s.has('Scan Visor',p) and o.movement.value>=3 and o.standable_terrain.value>=3 and o.scan_dash.value>=4))) or (s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=3 and o.standable_terrain.value>=4 and o.scan_dash.value>=4 and s.has('Scan Visor',p) and o.bomb_space_jump.value>=4)))),
 ("Event - Activate Bomb Slots (Crossway, Chozo Ruins)",lambda s:(t['Shoot Super Missile'](s) and s.has('Scan Visor',p))),
 ("Door to Elder Hall Access (Hall of the Elders, Chozo Ruins)",lambda s:((l_hm(s, p, 1) and t['Shoot Any Beam'](s)) and t['Open Normal Door'](s))),)),
("Pickup (Missile Expansion) (Crossway, Chozo Ruins)",(
 ("Door to Crossway Access West (Crossway, Chozo Ruins)",None),)),
("Event - Activate Bomb Slots (Crossway, Chozo Ruins)",(
 ("Door to Elder Hall Access (Crossway, Chozo Ruins)",None),)),
("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)",(
 ("Door to Antechamber (Reflecting Pool, Chozo Ruins)",None),
 ("Save Station (Save Station 3, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),
 ("Door to Transport Tunnel D (Great Tree Hall, Tallon Overworld)",lambda s:(t['Shoot Ice Beam'](s) and t['Open Normal Door'](s))),)),
("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)",(
 ("Door to Antechamber (Reflecting Pool, Chozo Ruins)",lambda s:((s.has('Morph Ball',p) and ((s.has('Reflecting Pool Water Drained',p) and (s.has('Boost Ball',p) or o.movement.value>=3)) or (s.has('Morph Ball Bomb',p) and (o.complex_bomb_jump.value>=4 or o.bomb_space_jump.value>=4) and o.standable_terrain.value>=3))) or (s.has('Space Jump Boots',p) and o.slope_jump.value>=1 and o.standable_terrain.value>=1))),
 ("Event - Drain water (Reflecting Pool, Chozo Ruins)",lambda s:(s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Power Bomb',p) and o.knowledge.value>=1)))),
 ("Door to Reflecting Pool Access (Hall of the Elders, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Door to Antechamber (Reflecting Pool, Chozo Ruins)",(
 ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)",None),
 ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)",None),
 ("Pickup (Ice Beam) (Antechamber, Chozo Ruins)",lambda s:(l_hm(s, p, 1) and t['Shoot Any Beam'](s))),)),
("Event - Drain water (Reflecting Pool, Chozo Ruins)",(
 ("Door to Reflecting Pool Access (Reflecting Pool, Chozo Ruins)",None),)),
("Save Station (Save Station 3, Chozo Ruins)",(
 ("Pickup (Missile Expansion) (Overgrown Cavern, Tallon Overworld)",lambda s:(s.has('Morph Ball',p) and t['Shoot Ice Beam'](s) and t['Open Normal Door'](s) and (s.has('Morph Ball',p) and (s.has('Morph Ball Bomb',p) or (s.has('Space Jump Boots',p) and o.standable_terrain.value>=2 and o.movement.value>=3) or (s.has('Boost Ball',p) and o.wall_boost.value>=5))))),
 ("Door to Save Station 3 (Reflecting Pool, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Space Jump Boots) (Alcove, Tallon Overworld)",(
 ("Door to Alcove (Landing Site, Tallon Overworld)",lambda s:(t['Open Normal Door'](s) and (s.has('Space Jump Boots',p) or o.slope_jump.value>=1 or (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p) and o.bomb_jump.value>=1)))),)),
("Pickup (Missile) (Storage Cavern, Magmoor Caverns)",(
 ("Tunnel Entrance (Triclops Pit, Magmoor Caverns)",lambda s:((s.has('Morph Ball',p) and (t['Heat-Resisting Suit'](s) or (o.heat_runs.value>=2 and (l_csd(s,p,120,'HeatDamage1') or (s.has('Boost Ball',p) and l_csd(s,p,99,'HeatDamage1')))))) and t['Open Normal Door'](s))),)),
("Pickup (Artifact of Spirit) (Storage Cave, Phendrana Drifts)",(
 ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)",lambda s:(((s.has('Morph Ball',p) and s.has('Power Bomb',p)) or o.clip_through_objects.value>=3) and t['Shoot Plasma Beam'](s))),)),
("Pickup (Power Bomb) (Security Cave, Phendrana Drifts)",(
 ("Front of Storage Cave (Phendrana's Edge, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and ((s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p))))),)),
("Save Station (Save Station C, Phendrana Drifts)",(
 ("Frost Cave Floor (Frost Cave, Phendrana Drifts)",lambda s:t['Shoot Wave Beam'](s)),)),
("Save Station (Save Station D, Phendrana Drifts)",(
 ("Door to Save Station D (Observatory, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Save Station (Save Station A, Phendrana Drifts)",(
 ("Door to Save Station A (Ruined Courtyard, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile) (Quarantine Monitor, Phendrana Drifts)",(
 ("Morph Ball Door to Quarantine Monitor (Quarantine Cave, Phendrana Drifts)",lambda s:(s.has('Morph Ball',p) and (s.has('Power Beam',p) or s.has('Ice Beam',p) or s.has('Wave Beam',p) or s.has('Plasma Beam',p)) and (s.has('Combat Visor',p) or s.has('Thermal Visor',p) or s.has('X-Ray Visor',p) or s.has('Scan Visor',p)))),)),
("Pickup (Boost Ball) (Phendrana Canyon, Phendrana Drifts)",(
 ("Door to Ruins Entryway (Ice Ruins West, Phendrana Drifts)",lambda s:(t['Open Normal Door'](s) and t['Move Past Scatter Bombu'](s) and (s.has('Space Jump Boots',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p)) or o.scan_dash.value>=2 or o.standable_terrain.value>=1))),)),
("Pickup (Wave Beam) (Chapel of the Elders, Phendrana Drifts)",(
 ("Front of Bomb Slot (Chozo Ice Temple, Phendrana Drifts)",lambda s:(s.has('Chozo Ice Temple Bomb Slot',p) and t['Open Normal Door'](s) and (s.has('Morph Ball',p) and s.has('Morph Ball Bomb',p)) and t['Shoot Wave Beam'](s) and (s.has('Space Jump Boots',p) or o.bomb_jump.value>=1))),)),
("Save Station (Save Station B, Phendrana Drifts)",(
 ("Door to Shoreline Entrance (Phendrana Shorelines, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Map Station (Map Station, Phendrana Drifts)",(
 ("Door to Map Station (Research Entrance, Phendrana Drifts)",lambda s:t['Open Normal Door'](s)),)),
("Save Station (Save Station Magmoor B, Magmoor Caverns)",(
 ("Door to Save Station Magmoor B (Transport to Phendrana Drifts South, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),)),
("Missile Station (Missile Station Mines, Phazon Mines)",(
 ("Door to Phazon Mining Tunnel (Fungal Hall B, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Save Station (Save Station Mines B, Phazon Mines)",(
 ("Room Bottom (Central Dynamo, Phazon Mines)",lambda s:t['Shoot Ice Beam'](s)),)),
("Map Station (Map Station Mines, Phazon Mines)",(
 ("Door to Ventilation Shaft (Omega Research, Phazon Mines)",lambda s:((s.has('Morph Ball',p) and s.has('Power Bomb',p)) and t['Shoot Ice Beam'](s))),)),
("Save Station (Savestation, Tallon Overworld)",(
 ("Door to Reactor Core (Reactor Access, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Missile Expansion) (Great Tree Chamber, Tallon Overworld)",(
 ("Door to Great Tree Chamber (Great Tree Hall, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Save Station (Save Station 2, Chozo Ruins)",(
 ("Door to Gathering Hall Access (Gathering Hall, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Artifact of World) (Elder Chamber, Chozo Ruins)",(
 ("Room Center (Hall of the Elders, Chozo Ruins)",lambda s:((s.has('Hall of the Elders Statue',p) or (s.has('Morph Ball',p) and s.has('Boost Ball',p) and o.clip_through_objects.value>=3)) and t['Shoot Ice Beam'](s))),)),
("Pickup (Ice Beam) (Antechamber, Chozo Ruins)",(
 ("Door to Antechamber (Reflecting Pool, Chozo Ruins)",lambda s:t['Shoot Ice Beam'](s)),)),
("Pickup (Flamethrower) (Storage Depot A, Phazon Mines)",(
 ("Room Center (Mine Security Station, Phazon Mines)",lambda s:(s.has('Mine Security Station Barrier',p) and t['Shoot Plasma Beam'](s))),)),
("Save Station (Save Station Mines C, Phazon Mines)",(
 ("Door to Save Station Mines C (Metroid Quarantine B, Phazon Mines)",lambda s:t['Shoot Plasma Beam'](s)),)),
("Pickup (Missile Expansion) (Arbor Chamber, Tallon Overworld)",(
 ("Door to Arbor Chamber (Root Cave, Tallon Overworld)",lambda s:t['Open Normal Door'](s)),)),
("Save Station (Save Station Magmoor A, Magmoor Caverns)",(
 ("Door to Save Station Magmoor A (Burning Trail, Magmoor Caverns)",lambda s:t['Open Normal Door'](s)),)),
("Map Station (Map Station, Chozo Ruins)",(
 ("Door to North Atrium (Ruined Gallery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Save Station (Save Station 1, Chozo Ruins)",(
 ("Door to North Atrium (Ruined Nursery, Chozo Ruins)",lambda s:t['Open Normal Door'](s)),)),
("Pickup (Artifact of Lifegiver) (Tower Chamber, Chozo Ruins)",(
 ("Door to Tower of Light Access (Tower of Light, Chozo Ruins)",lambda s:t['Shoot Wave Beam'](s)),)),
("Missile Station (Crater Missile Station, Impact Crater)",(
 ("Door to Crater Missile Station (Phazon Core, Impact Crater)",lambda s:t['Shoot Plasma Beam'](s)),)),)
 get_region = self.multiworld.get_region
 for region_name, exits in entrance_rules:
  connect_to = get_region(region_name,p).connect
  for connecting_region_name, rule in exits:
   connect_to(get_region(connecting_region_name, p), None, rule)