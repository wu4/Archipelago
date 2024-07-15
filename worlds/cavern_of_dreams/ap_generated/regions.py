from BaseClasses import Entrance as E, Location as L
from ..regions import CavernOfDreamsRegion as R
from ..entrance_rando import randomize_entrances
bilinear:list[tuple[str,str]]=[
  ('CAVE.SunCavern.LostleafLobbyTeleport', 'CAVE.LostleafLobby.SunCavernTeleport'),
  ('MONSTER.Sky.GreenDoor', 'MONSTER.Kerrington.SkyFenceDoor'),
  ('GALLERY.WaterLobby.LunaRoomDoor', 'GALLERY.LunaRoom.WaterLobbyDoor'),
  ('GALLERY.EarthLobby.FoyerDoor', 'GALLERY.Foyer.EarthLobbyDoor'),
  ('GALLERY.WaterLobby.SewerDoor', 'CAVE.Sewer.GalleryDoor'),
  ('MONSTER.Sky.WaterDroneDoor', 'MONSTER.WaterDrone.SkyDoor'),
  ('CAVE.SunCavern.DucklingsDoorLower', 'LAKE.LostleafLake.DucklingsDoorLower'),
  ('GALLERY.Chalice.ShortcutDownDoor', 'GALLERY.Chalice.ShortcutUpDoor'),
  ('LAKE.LostleafLake.DucklingsDoorUpper', 'CAVE.SunCavern.DucklingsDoorUpper'),
  ('MONSTER.Heart.KerringtonDoor', 'MONSTER.Kerrington.HeartDoor'),
  ('LAKE.Treehouse.LostleafBackDoor', 'LAKE.LostleafLake.TreehouseBackDoor'),
  ('CAVE.LostleafLobby.SunCavernDoor', 'CAVE.SunCavern.LostleafLobbyDoor'),
  ('LAKE.LostleafLake.CryptDoorFront', 'LAKE.Crypt.LostleafLakeDoorFront'),
  ('CAVE.GalleryLobby.RainbowBench', 'CAVE.Rainbow.WellEntrance'),
  ('GALLERY.EarthLobby.KerringtonCauldron', 'MONSTER.Kerrington.EarthLobbyCauldron'),
  ('PALACE.Sanctum.PalaceDoor', 'PALACE.Palace.SanctumDoor'),
  ('CAVE.Sewer.ArmadaLobbyDoor', 'CAVE.ArmadaLobby.SewerDoor'),
  ('CAVE.Rainbow.WellEntrance', 'CAVE.GalleryLobby.RainbowBench'),
  ('GALLERY.Foyer.GalleryLobbyDoor', 'CAVE.GalleryLobby.FoyerDoor'),
  ('GALLERY.Foyer.EarthLobbyDoor', 'GALLERY.EarthLobby.FoyerDoor'),
  ('CAVE.LostleafLobby.GalleryLobbyDoor', 'CAVE.GalleryLobby.LostleafLobbyDoor'),
  ('MONSTER.EarthDrone.SkyDoor', 'MONSTER.Sky.EarthDroneDoor'),
  ('MONSTER.Kerrington.SkyDogDoor', 'MONSTER.Sky.YellowDoor'),
  ('CAVE.SunCavern.MoonCavernHeartDoor', 'CAVE.MoonCavern.SunCavernDoor'),
  ('MONSTER.Sky.YellowDoor', 'MONSTER.Kerrington.SkyDogDoor'),
  ('PALACE.Sanctum.ValleyDoor', 'PALACE.Valley.SanctumDoor'),
  ('GALLERY.Drown.WaterLobbyDoor', 'GALLERY.WaterLobby.DrownPainting'),
  ('CAVE.ArmadaLobby.SewerDoor', 'CAVE.Sewer.ArmadaLobbyDoor'),
  ('CAVE.GalleryLobby.MoonCavernDoor', 'CAVE.MoonCavern.GalleryLobbyDoor'),
  ('MONSTER.Sky.FireDroneDoor', 'MONSTER.FireDrone.SkyDoor'),
  ('CAVE.PalaceLobby.MoonCavernDoor', 'CAVE.MoonCavern.PalaceLobbyDoor'),
  ('CAVE.SunCavern.PalaceLobbyTeleport', 'CAVE.PalaceLobby.SunCavernTeleport'),
  ('GALLERY.WaterLobby.FoyerDoor', 'GALLERY.Foyer.WaterLobbyDoor'),
  ('PALACE.Valley.SanctumDoor', 'PALACE.Sanctum.ValleyDoor'),
  ('CAVE.SunCavern.DucklingsDoorUpper', 'LAKE.LostleafLake.DucklingsDoorUpper'),
  ('GALLERY.WaterLobby.DrownPainting', 'GALLERY.Drown.WaterLobbyDoor'),
  ('LAKE.LostleafLake.LostleafLobbyDoor', 'CAVE.LostleafLobby.LostleafLakeDoor'),
  ('LAKE.LostleafLake.TreehouseFrontDoor', 'LAKE.Treehouse.LostleafFrontDoor'),
  ('CAVE.PalaceLobby.SunCavernTeleport', 'CAVE.SunCavern.PalaceLobbyTeleport'),
  ('CAVE.ArmadaLobby.SunCavernDoor', 'CAVE.SunCavern.ArmadaLobbyDoor'),
  ('MONSTER.WaterDrone.SkyDoor', 'MONSTER.Sky.WaterDroneDoor'),
  ('CAVE.ArmadaLobby.EarthDroneCannonShot', 'MONSTER.EarthDrone.ArmadaLobbyDoor'),
  ('LAKE.Teepee.FrontDoor', 'LAKE.LostleafLake.TeepeeFrontDoor'),
  ('PALACE.DiningRoom.ValleyDoor', 'PALACE.Valley.DiningRoomDoor'),
  ('CAVE.GalleryLobby.SunCavernTeleport', 'CAVE.SunCavern.GalleryLobbyTeleport'),
  ('CAVE.MoonCavern.SunCavernDoor', 'CAVE.SunCavern.MoonCavernHeartDoor'),
  ('MONSTER.Kerrington.SkyDoorBack', 'MONSTER.Sky.KerringtonDoorBack'),
  ('CAVE.SunCavern.ArmadaLobbyTeleport', 'CAVE.ArmadaLobby.SunCavernTeleport'),
  ('CAVE.SunCavern.ArmadaLobbyDoor', 'CAVE.ArmadaLobby.SunCavernDoor'),
  ('CAVE.MoonCavern.PalaceLobbyDoor', 'CAVE.PalaceLobby.MoonCavernDoor'),
  ('PALACE.Valley.DiningRoomDoor', 'PALACE.DiningRoom.ValleyDoor'),
  ('PALACE.Palace.SanctumDoor', 'PALACE.Sanctum.PalaceDoor'),
  ('MONSTER.Kerrington.EarthLobbyCauldron', 'GALLERY.EarthLobby.KerringtonCauldron'),
  ('GALLERY.LunaRoom.WaterLobbyDoor', 'GALLERY.WaterLobby.LunaRoomDoor'),
  ('LAKE.Treehouse.LostleafFrontDoor', 'LAKE.LostleafLake.TreehouseFrontDoor'),
  ('MONSTER.EarthDrone.ArmadaLobbyDoor', 'CAVE.ArmadaLobby.EarthDroneCannonShot'),
  ('PALACE.Valley.ObservatoryDoor', 'PALACE.Observatory.ValleyDoor'),
  ('LAKE.LostleafLake.DucklingsDoorLower', 'CAVE.SunCavern.DucklingsDoorLower'),
  ('LAKE.Crypt.LostleafLakeDoorBack', 'LAKE.LostleafLake.CryptDoorBack'),
  ('MONSTER.Kerrington.HeartDoor', 'MONSTER.Heart.KerringtonDoor'),
  ('CAVE.PalaceLobby.ValleyDoor', 'PALACE.Valley.PalaceLobbyDoor'),
  ('CAVE.LostleafLobby.SunCavernTeleport', 'CAVE.SunCavern.LostleafLobbyTeleport'),
  ('LAKE.Church.LostleafLakeDoor', 'LAKE.LostleafLake.ChurchDoor'),
  ('GALLERY.Undead.EarthLobbyDoor', 'GALLERY.EarthLobby.UndeadPainting'),
  ('PALACE.Valley.PalaceLobbyDoor', 'CAVE.PalaceLobby.ValleyDoor'),
  ('GALLERY.FireLobby.EarthLobbyDoor', 'GALLERY.EarthLobby.FireLobbyDoor'),
  ('PALACE.Valley.PalaceBasementDoor', 'PALACE.Palace.BasementDoor'),
  ('MONSTER.Sky.EarthDroneDoor', 'MONSTER.EarthDrone.SkyDoor'),
  ('LAKE.LostleafLake.CryptDoorBack', 'LAKE.Crypt.LostleafLakeDoorBack'),
  ('GALLERY.EarthLobby.UndeadPainting', 'GALLERY.Undead.EarthLobbyDoor'),
  ('CAVE.GalleryLobby.LostleafLobbyDoor', 'CAVE.LostleafLobby.GalleryLobbyDoor'),
  ('PALACE.Observatory.ValleyDoor', 'PALACE.Valley.ObservatoryDoor'),
  ('LAKE.LostleafLake.TreehouseBackDoor', 'LAKE.Treehouse.LostleafBackDoor'),
  ('MONSTER.Sky.KerringtonDoorFront', 'MONSTER.Kerrington.SkyDoorFront'),
  ('MONSTER.Kerrington.SkyFenceDoor', 'MONSTER.Sky.GreenDoor'),
  ('GALLERY.EarthLobby.FireLobbyDoor', 'GALLERY.FireLobby.EarthLobbyDoor'),
  ('GALLERY.Foyer.FireLobbyDoor', 'GALLERY.FireLobby.FoyerDoor'),
  ('MONSTER.Sky.KerringtonDoorBack', 'MONSTER.Kerrington.SkyDoorBack'),
  ('PALACE.Valley.ObservatoryShortcutDoorBottom', 'PALACE.Valley.ObservatoryShortcutDoorTop'),
  ('CAVE.MoonCavern.GalleryLobbyDoor', 'CAVE.GalleryLobby.MoonCavernDoor'),
  ('CAVE.Sewer.GalleryDoor', 'GALLERY.WaterLobby.SewerDoor'),
  ('PALACE.Palace.FrontDoor', 'PALACE.Valley.PalaceFrontDoor'),
  ('CAVE.GalleryLobby.FoyerDoor', 'GALLERY.Foyer.GalleryLobbyDoor'),
  ('PALACE.Valley.ObservatoryShortcutDoorTop', 'PALACE.Valley.ObservatoryShortcutDoorBottom'),
  ('LAKE.LostleafLake.ValleyDoor', 'PALACE.Valley.LostleafDoor'),
  ('LAKE.LostleafLake.ChurchDoor', 'LAKE.Church.LostleafLakeDoor'),
  ('PALACE.Valley.PalaceFrontDoor', 'PALACE.Palace.FrontDoor'),
  ('PALACE.Palace.BasementDoor', 'PALACE.Valley.PalaceBasementDoor'),
  ('LAKE.LostleafLake.TeepeeFrontDoor', 'LAKE.Teepee.FrontDoor'),
  ('GALLERY.Foyer.WaterLobbyDoor', 'GALLERY.WaterLobby.FoyerDoor'),
  ('GALLERY.Chalice.ShortcutUpDoor', 'GALLERY.Chalice.ShortcutDownDoor'),
  ('MONSTER.FireDrone.SkyDoor', 'MONSTER.Sky.FireDroneDoor'),
  ('CAVE.SunCavern.GalleryLobbyTeleport', 'CAVE.GalleryLobby.SunCavernTeleport'),
  ('GALLERY.FireLobby.FoyerDoor', 'GALLERY.Foyer.FireLobbyDoor'),
  ('PALACE.Valley.LostleafDoor', 'LAKE.LostleafLake.ValleyDoor'),
  ('CAVE.ArmadaLobby.SunCavernTeleport', 'CAVE.SunCavern.ArmadaLobbyTeleport'),
  ('MONSTER.Kerrington.SkyDoorFront', 'MONSTER.Sky.KerringtonDoorFront'),
  ('CAVE.LostleafLobby.LostleafLakeDoor', 'LAKE.LostleafLake.LostleafLobbyDoor'),
  ('GALLERY.Chalice.FireLobbyDoor', 'GALLERY.FireLobby.ChalicePainting'),
  ('LAKE.Crypt.LostleafLakeDoorFront', 'LAKE.LostleafLake.CryptDoorFront'),
  ('CAVE.SunCavern.LostleafLobbyDoor', 'CAVE.LostleafLobby.SunCavernDoor'),
  ('GALLERY.FireLobby.ChalicePainting', 'GALLERY.Chalice.FireLobbyDoor'),
]
one_way:list[tuple[str,str]]=[
  ('GALLERY.EarthLobby.ToiletDragonHead', 'GALLERY.WaterLobby.FarDrain'),
  ('GALLERY.EarthLobby.ToiletCoffins', 'GALLERY.WaterLobby.GiantDrain'),
  ('GALLERY.Foyer.WaterLobbyHole', 'GALLERY.WaterLobby.FoyerHole'),
  ('GALLERY.EarthLobby.ToiletBridge', 'GALLERY.WaterLobby.CenterDrain'),
  ('GALLERY.EarthLobby.ToiletPainting', 'GALLERY.WaterLobby.EggDrain'),
  ('LAKE.LostleafLake.TeepeeTopside', 'LAKE.Teepee.Topside'),
]
def create_regions(w):
  p=w.player
  o=w.options
  mw=w.multiworld
  r0=R('CAVE.SunCavern.Main',p,mw)
  r1=R('CAVE.SunCavern.ArmadaLobbyRoom',p,mw)
  r2=R('CAVE.ArmadaLobby.Main',p,mw)
  r3=R('CAVE.ArmadaLobby.JesterBootsPlatform',p,mw)
  r4=R('CAVE.ArmadaLobby.ArmadaLobbyBootsWall.WhackableRegion',p,mw)
  r5=R('CAVE.ArmadaLobby.JesterBootsRoom',p,mw)
  r6=R('CAVE.ArmadaLobby.EnterCannon',p,mw)
  r7=R('CAVE.ArmadaLobby.CannonLip',p,mw)
  r8=R('CAVE.ArmadaLobby.EggPlatform',p,mw)
  r9=R('MONSTER.EarthDrone.Main',p,mw)
  r10=R('MONSTER.Sky.Main',p,mw)
  r11=R('MONSTER.Sky.YellowLedge',p,mw)
  r12=R('MONSTER.Sky.YellowDoorway',p,mw)
  r13=R('MONSTER.Kerrington.DogRoom',p,mw)
  r14=R('MONSTER.Sky.Tail',p,mw)
  r15=R('MONSTER.Sky.Topside',p,mw)
  r16=R('MONSTER.Sky.FireDronePlatform',p,mw)
  r17=R('MONSTER.FireDrone.Main',p,mw)
  r18=R('MONSTER.Sky.UpperWings',p,mw)
  r19=R('MONSTER.Sky.WaterDronePlatform',p,mw)
  r20=R('MONSTER.WaterDrone.Main',p,mw)
  r21=R('MONSTER.Kerrington.MedicinePool',p,mw)
  r22=R('MONSTER.Kerrington.Main',p,mw)
  r23=R('MONSTER.Kerrington.Cockpit',p,mw)
  r24=R('MONSTER.Kerrington.HeartEntryway',p,mw)
  r25=R('MONSTER.Kerrington.HeartEntrywayPlatform',p,mw)
  r26=R('MONSTER.Kerrington.HeartEntrywayCardPlatform',p,mw)
  r27=R('MONSTER.Heart.Main',p,mw)
  r28=R('MONSTER.Kerrington.IntoFrontDoor',p,mw)
  r29=R('MONSTER.Kerrington.GreenRoom',p,mw)
  r30=R('MONSTER.Kerrington.GreenFence',p,mw)
  r31=R('MONSTER.Sky.GreenDoorway',p,mw)
  r32=R('MONSTER.Kerrington.LabGreenConnector',p,mw)
  r33=R('MONSTER.Kerrington.GreenBoiler',p,mw)
  r34=R('MONSTER.Kerrington.LowerLabContainers',p,mw)
  r35=R('MONSTER.Kerrington.UpperLabContainers',p,mw)
  r36=R('MONSTER.Kerrington.MedicinePoolSlide',p,mw)
  r37=R('MONSTER.Kerrington.MedicinePoolEggPlatform',p,mw)
  r38=R('CAVE.ArmadaLobby.FlagPlatform',p,mw)
  r39=R('CAVE.ArmadaLobby.SewerConnector',p,mw)
  r40=R('CAVE.Sewer.ArmadaLobbySide',p,mw)
  r41=R('CAVE.Sewer.GallerySide',p,mw)
  r42=R('GALLERY.WaterLobby.LobbySewerUnderwater',p,mw)
  r43=R('GALLERY.WaterLobby.LobbySewerMiddle',p,mw)
  r44=R('GALLERY.WaterLobby.Main',p,mw)
  r45=R('GALLERY.WaterLobby.SpookyWall.WhackableRegion',p,mw)
  r46=R('GALLERY.WaterLobby.Spooky',p,mw)
  r47=R('GALLERY.WaterLobby.LunaHouse',p,mw)
  r48=R('GALLERY.LunaRoom.LunaHouse',p,mw)
  r49=R('GALLERY.WaterLobby.SpookyWaterUpper',p,mw)
  r50=R('GALLERY.WaterLobby.SpookyWaterLower',p,mw)
  r51=R('GALLERY.Foyer.Main',p,mw)
  r52=R('GALLERY.Foyer.SideDoors',p,mw)
  r53=R('GALLERY.FireLobby.Main',p,mw)
  r54=R('GALLERY.FireLobby.ChalicePlatform',p,mw)
  r55=R('GALLERY.FireLobby.FishPlatform',p,mw)
  r56=R('GALLERY.FireLobby.KerringtonPaintingPlatform',p,mw)
  r57=R('GALLERY.Chalice.Main',p,mw)
  r58=R('GALLERY.Chalice.EggPlatform',p,mw)
  r59=R('GALLERY.Chalice.BottomShortcutPlatform',p,mw)
  r60=R('GALLERY.FireLobby.EarthLobbyEntryway',p,mw)
  r61=R('GALLERY.EarthLobby.FireLobbyEntryway',p,mw)
  r62=R('GALLERY.EarthLobby.Coffins',p,mw)
  r63=R('GALLERY.EarthLobby.GrowMainBush',p,mw)
  r64=R('GALLERY.EarthLobby.MainUnderwater',p,mw)
  r65=R('GALLERY.EarthLobby.Main',p,mw)
  r66=R('GALLERY.EarthLobby.InsideCastle',p,mw)
  r67=R('GALLERY.EarthLobby.GrowCastleBushes',p,mw)
  r68=R('GALLERY.EarthLobby.CastleUnderwater',p,mw)
  r69=R('GALLERY.WaterLobby.LobbySewerEgg',p,mw)
  r70=R('GALLERY.EarthLobby.KerringtonCauldronPlatform',p,mw)
  r71=R('GALLERY.EarthLobby.KerringtonCauldronEntryway',p,mw)
  r72=R('MONSTER.Kerrington.CauldronRoom',p,mw)
  r73=R('GALLERY.EarthLobby.CastleWingsPlatform',p,mw)
  r74=R('GALLERY.Undead.Main',p,mw)
  r75=R('GALLERY.EarthLobby.DragonHead',p,mw)
  r76=R('GALLERY.EarthLobby.FoyerEntryPlatform',p,mw)
  r77=R('GALLERY.EarthLobby.CoffinsUnderwater',p,mw)
  r78=R('GALLERY.WaterLobby.LobbySewerGiant',p,mw)
  r79=R('GALLERY.EarthLobby.CoffinsStatuePlatform',p,mw)
  r80=R('GALLERY.FireLobby.ClimbToKerringtonPaintingPlatform',p,mw)
  r81=R('CAVE.GalleryLobby.Main',p,mw)
  r82=R('CAVE.GalleryLobby.OuterWalls',p,mw)
  r83=R('CAVE.GalleryLobby.Maze',p,mw)
  r84=R('CAVE.GalleryLobby.MazeStatue',p,mw)
  r85=R('CAVE.GalleryLobby.LostleafCave',p,mw)
  r86=R('CAVE.LostleafLobby.HiddenDoorway',p,mw)
  r87=R('CAVE.LostleafLobby.BreakHiddenWall',p,mw)
  r88=R('CAVE.LostleafLobby.Main',p,mw)
  r89=R('CAVE.LostleafLobby.Trees',p,mw)
  r90=R('CAVE.SunCavern.MightyWallLedge',p,mw)
  r91=R('LAKE.LostleafLake.Main',p,mw)
  r92=R('LAKE.LostleafLake.OuterRim',p,mw)
  r93=R('LAKE.LostleafLake.TeepeeIsland',p,mw)
  r94=R('LAKE.LostleafLake.Lake',p,mw)
  r95=R('LAKE.LostleafLake.SecretWorld',p,mw)
  r96=R('LAKE.LostleafLake.DucklingsLedge',p,mw)
  r97=R('LAKE.LostleafLake.Ducklings',p,mw)
  r98=R('CAVE.SunCavern.WaterfallLedge',p,mw)
  r99=R('CAVE.SunCavern.DucklingsDoorway',p,mw)
  r100=R('CAVE.SunCavern.DucklingsLedge',p,mw)
  r101=R('CAVE.SunCavern.MoonCavernHeartDoorway',p,mw)
  r102=R('CAVE.MoonCavern.Main',p,mw)
  r103=R('CAVE.MoonCavern.DiveHoles',p,mw)
  r104=R('CAVE.MoonCavern.DiveRoom',p,mw)
  r105=R('CAVE.MoonCavern.DivePuzzleLedge',p,mw)
  r106=R('CAVE.MoonCavern.UpperConnector',p,mw)
  r107=R('CAVE.MoonCavern.Upper',p,mw)
  r108=R('CAVE.PalaceLobby.Main',p,mw)
  r109=R('CAVE.PalaceLobby.Underwater',p,mw)
  r110=R('CAVE.PalaceLobby.PrismicEntryPlatform',p,mw)
  r111=R('CAVE.PalaceLobby.Ledges',p,mw)
  r112=R('CAVE.PalaceLobby.TopLedge',p,mw)
  r113=R('PALACE.Valley.Main',p,mw)
  r114=R('PALACE.Valley.OuterRim',p,mw)
  r115=R('PALACE.Valley.JesterBootsCoveFloatingPoms',p,mw)
  r116=R('PALACE.Valley.JesterBootsCove',p,mw)
  r117=R('PALACE.Valley.LostleafEntryway',p,mw)
  r118=R('PALACE.Valley.JesterBootsCoveLowerPlatforms',p,mw)
  r119=R('PALACE.Valley.JesterBootsCoveCastlePlatform',p,mw)
  r120=R('PALACE.Valley.JesterBootsCoveLowerCastle',p,mw)
  r121=R('PALACE.Valley.JesterBootsCoveMidCastle',p,mw)
  r122=R('PALACE.Valley.JesterBootsCoveUpperCastle',p,mw)
  r123=R('PALACE.Valley.JesterBootsCovePrestonPlatform',p,mw)
  r124=R('PALACE.Valley.EntrancePomLedge',p,mw)
  r125=R('PALACE.Valley.PalaceCardLedge',p,mw)
  r126=R('PALACE.Valley.Spires',p,mw)
  r127=R('PALACE.Valley.PokiPokiCave',p,mw)
  r128=R('PALACE.Valley.ObservatoryPlatform',p,mw)
  r129=R('PALACE.Valley.ObservatoryEntry',p,mw)
  r130=R('PALACE.Observatory.Main',p,mw)
  r131=R('PALACE.Valley.ObservatoryRoof',p,mw)
  r132=R('PALACE.Valley.ObservatorySlideEnd',p,mw)
  r133=R('PALACE.DiningRoom.Main',p,mw)
  r134=R('PALACE.DiningRoom.InitialPlatforms',p,mw)
  r135=R('PALACE.DiningRoom.Chandelier',p,mw)
  r136=R('PALACE.Valley.PalaceTop',p,mw)
  r137=R('PALACE.Sanctum.ValleyEntryway',p,mw)
  r138=R('PALACE.Sanctum.BubbleClimb',p,mw)
  r139=R('PALACE.Sanctum.Main',p,mw)
  r140=R('PALACE.Sanctum.PalaceEntryway',p,mw)
  r141=R('PALACE.Palace.SanctumEntryway',p,mw)
  r142=R('PALACE.Palace.Main',p,mw)
  r143=R('PALACE.Palace.BubbleConchRoom',p,mw)
  r144=R('PALACE.Palace.BubbleConchRoomHighShrooms',p,mw)
  r145=R('PALACE.Palace.SentryControlRoom',p,mw)
  r146=R('PALACE.Valley.UpperWater',p,mw)
  r147=R('PALACE.Valley.GobblerCave',p,mw)
  r148=R('PALACE.Valley.LowerWater',p,mw)
  r149=R('PALACE.Valley.BigstarCave',p,mw)
  r150=R('PALACE.Valley.BreakLowerWaterWall',p,mw)
  r151=R('PALACE.Palace.Basement',p,mw)
  r152=R('PALACE.Palace.BasementEggPlatform',p,mw)
  r153=R('PALACE.Sanctum.RaceStart',p,mw)
  r154=R('PALACE.Valley.ClipIntoIce',p,mw)
  r155=R('PALACE.Valley.PoolCardLedge',p,mw)
  r156=R('PALACE.Valley.Pool',p,mw)
  r157=R('CAVE.MoonCavern.LavaMushroomPlatform',p,mw)
  r158=R('CAVE.MoonCavern.NightmareLobbyDoorway',p,mw)
  r159=R('LAKE.LostleafLake.TreehouseBranches',p,mw)
  r160=R('LAKE.LostleafLake.PrestonLedge',p,mw)
  r161=R('LAKE.LostleafLake.BigAppleLedge',p,mw)
  r162=R('LAKE.LostleafLake.WinkyTreeLedge',p,mw)
  r163=R('LAKE.LostleafLake.TreehouseFrontEntry',p,mw)
  r164=R('LAKE.LostleafLake.TreehouseBackEntry',p,mw)
  r165=R('LAKE.Treehouse.Main',p,mw)
  r166=R('LAKE.LostleafLake.TreehouseRoof',p,mw)
  r167=R('LAKE.LostleafLake.WaterfallCanopy',p,mw)
  r168=R('LAKE.LostleafLake.DeepWoods',p,mw)
  r169=R('LAKE.LostleafLake.DeepWoodsPuzzleEgg',p,mw)
  r170=R('LAKE.LostleafLake.DeepDeepWoods',p,mw)
  r171=R('LAKE.LostleafLake.CryptCanopy',p,mw)
  r172=R('LAKE.LostleafLake.CryptBackLedge',p,mw)
  r173=R('LAKE.LostleafLake.OverCryptBackFence',p,mw)
  r174=R('LAKE.Crypt.BackExit',p,mw)
  r175=R('LAKE.Crypt.LeftPlatform',p,mw)
  r176=R('LAKE.Crypt.Main',p,mw)
  r177=R('LAKE.Crypt.RightPlatform',p,mw)
  r178=R('LAKE.Crypt.EggPlatform',p,mw)
  r179=R('LAKE.Crypt.TimedPlatform',p,mw)
  r180=R('LAKE.LostleafLake.InsideCrypt',p,mw)
  r181=R('LAKE.LostleafLake.BellTower',p,mw)
  r182=R('LAKE.LostleafLake.RingBell',p,mw)
  r183=R('LAKE.LostleafLake.InsideChurch',p,mw)
  r184=R('LAKE.Church.Main',p,mw)
  r185=R('LAKE.Church.Basement',p,mw)
  r186=R('LAKE.LostleafLake.WaterfallEggCave',p,mw)
  r187=R('LAKE.LostleafLake.FallIntoTeepee',p,mw)
  r188=R('LAKE.Teepee.Main',p,mw)
  r189=R('LAKE.LostleafLake.LakeStump',p,mw)
  r190=R('CAVE.Rainbow.Well',p,mw)
  r191=R('CAVE.Rainbow.Main',p,mw)
  r192=R('CAVE.Rainbow.MoonLedges',p,mw)
  r193=R('CAVE.Rainbow.ShroomLedges',p,mw)
  r194=R('CAVE.Rainbow.Topside',p,mw)
  r195=R('GALLERY.Drown.Main',p,mw)
  r196=R('GALLERY.Drown.BubbleConchPipe',p,mw)
  r197=R('CAVE.SunCavern.HighJumpLedge',p,mw)
  r198=R('CAVE.SunCavern.VineLedge',p,mw)
  r199=R('CAVE.SunCavern.TailSpinLedge',p,mw)
  # CAVE.SunCavern.Main -> CAVE.SunCavern.ArmadaLobbyRoom
  r0.connect(r1,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Wings', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('High Jump', p) and (s.has('Sprint', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.HighJumpLedge
  r0.connect(r197,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has_all(['Sprint', 'Roll'], p))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.VineLedge
  r0.connect(r198,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Double Jump', p) and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s.has_any(['High Jump', 'Wings'], p))) or (s.has_all(['High Jump', 'Wings'], p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Double Jump', p) and o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.TailSpinLedge
  r0.connect(r199,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Bubble', 'Wings'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or s.has('Roll', p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.MightyWallLedge
  r0.connect(r90,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s.has('Double Jump', p) and (s.has_any(['High Jump', 'Wings'], p))) or (o.difficulty.value >= 1 and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has_any(['High Jump', 'Double Jump'], p))))))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.WaterfallLedge
  r0.connect(r98,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['High Jump', 'Double Jump', 'Wings'], p) and o.difficulty.value >= 1 and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.DucklingsLedge
  r0.connect(r100,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['Wings', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Roll', p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has('High Jump', p) or o.difficulty.value >= 1))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.DucklingsDoorway
  r0.connect(r99,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Sprint', p) and ((o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (o.difficulty.value >= 1 and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Sprint', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2) or (s.has('Bubble', p) and o.difficulty.value >= 1 and o.bubble_jump.value >= 1) or (s.has('Wings', p) and o.momentum_cancel.value == 1) or (o.difficulty.value >= 1 and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # CAVE.SunCavern.Main -> CAVE.SunCavern.MoonCavernHeartDoorway
  r0.connect(r101,None,lambda s:(s.has('Swim', p) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or s.has('Sprint', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or o.difficulty.value >= 1)))
  # CAVE.SunCavern.ArmadaLobbyRoom -> CAVE.SunCavern.Main
  r1.connect(r0,None,None)
  # CAVE.ArmadaLobby.Main -> CAVE.ArmadaLobby.JesterBootsPlatform
  r2.connect(r3,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Raise Armada Lobby Pipes', 'Wings', 'Double Jump'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has('High Jump', p) or o.difficulty.value >= 1)) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Sprint', 'Horn'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Roll', p) and o.ejection_launch.value == 1)))
  # CAVE.ArmadaLobby.Main -> CAVE.ArmadaLobby.EnterCannon
  r2.connect(r6,None,lambda s:(o.out_of_bounds.value == 1 and not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  # CAVE.ArmadaLobby.Main -> CAVE.ArmadaLobby.CannonLip
  r2.connect(r7,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Activate Armada Lobby Red Pipe Updraft', 'Raise Armada Lobby Pipes', 'Wings'], p)) or (s.has('Double Jump', p) and (s.has_any(['High Jump', 'Wings'], p) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.difficulty.value >= 1)))))
  # CAVE.ArmadaLobby.Main -> CAVE.ArmadaLobby.FlagPlatform
  r2.connect(r38,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has('Double Jump', p) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has_any(['High Jump', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2)))
  # CAVE.ArmadaLobby.JesterBootsPlatform -> CAVE.ArmadaLobby.ArmadaLobbyBootsWall.WhackableRegion
  r3.connect(r4,None,None)
  # CAVE.ArmadaLobby.JesterBootsPlatform -> CAVE.ArmadaLobby.JesterBootsRoom
  r3.connect(r5,None,lambda s:s.has('CAVE.ArmadaLobby.ArmadaLobbyBootsWall', p))
  # CAVE.ArmadaLobby.JesterBootsPlatform -> CAVE.ArmadaLobby.Main
  r3.connect(r2,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'High Jump', 'Sprint', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or s.has('Raise Armada Lobby Pipes', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # CAVE.ArmadaLobby.JesterBootsRoom -> CAVE.ArmadaLobby.ArmadaLobbyBootsWall.WhackableRegion
  r5.connect(r4,None,None)
  # CAVE.ArmadaLobby.JesterBootsRoom -> CAVE.ArmadaLobby.JesterBootsPlatform
  r5.connect(r3,None,lambda s:s.has('CAVE.ArmadaLobby.ArmadaLobbyBootsWall', p))
  # CAVE.ArmadaLobby.EnterCannon -> CAVE.ArmadaLobby.CannonLip
  r6.connect(r7,None,None)
  # CAVE.ArmadaLobby.CannonLip -> CAVE.ArmadaLobby.Main
  r7.connect(r2,None,None)
  # CAVE.ArmadaLobby.CannonLip -> CAVE.ArmadaLobby.EnterCannon
  r7.connect(r6,None,None)
  # CAVE.ArmadaLobby.CannonLip -> CAVE.ArmadaLobby.EggPlatform
  r7.connect(r8,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or o.ability_toggle.value == 1)) or (s.has_all(['Bubble', 'Double Jump'], p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2) or (s.has_all(['Roll', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # CAVE.ArmadaLobby.EggPlatform -> CAVE.ArmadaLobby.CannonLip
  r8.connect(r7,None,None)
  # MONSTER.Sky.Main -> MONSTER.Sky.YellowLedge
  r10.connect(r11,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has_any(['Wings', 'Roll', 'Double Jump', 'Sprint'], p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # MONSTER.Sky.Main -> MONSTER.Sky.GreenDoorway
  r10.connect(r31,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # MONSTER.Sky.Main -> MONSTER.Sky.Topside
  r10.connect(r15,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['Double Jump', 'High Jump', 'Roll'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))))
  # MONSTER.Sky.YellowLedge -> MONSTER.Sky.YellowDoorway
  r11.connect(r12,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # MONSTER.Sky.YellowLedge -> MONSTER.Sky.Main
  r11.connect(r10,None,None)
  # MONSTER.Sky.YellowLedge -> MONSTER.Sky.Tail
  r11.connect(r14,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'Roll', 'Double Jump', 'Sprint'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # MONSTER.Sky.YellowDoorway -> MONSTER.Sky.YellowLedge
  r12.connect(r11,None,None)
  # MONSTER.Sky.Tail -> MONSTER.Sky.Topside
  r14.connect(r15,None,lambda s:(s.has_any(['Wings', 'Sprint', 'Roll', 'High Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # MONSTER.Sky.Topside -> MONSTER.Sky.Main
  r15.connect(r10,None,None)
  # MONSTER.Sky.Topside -> MONSTER.Sky.Tail
  r15.connect(r14,None,None)
  # MONSTER.Sky.Topside -> MONSTER.Sky.YellowLedge
  r15.connect(r11,None,None)
  # MONSTER.Sky.Topside -> MONSTER.Sky.FireDronePlatform
  r15.connect(r16,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))
  # MONSTER.Sky.Topside -> MONSTER.Sky.UpperWings
  r15.connect(r18,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has('Wings', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['Roll', 'High Jump', 'Sprint'], p))) or (s.has('Sprint', p) and (s.has_any(['Roll', 'High Jump'], p)))))
  # MONSTER.Sky.Topside -> MONSTER.Sky.WaterDronePlatform
  r15.connect(r19,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and s.has('Sprint', p)))
  # MONSTER.Sky.FireDronePlatform -> MONSTER.Sky.Main
  r16.connect(r10,None,None)
  # MONSTER.Sky.FireDronePlatform -> MONSTER.Sky.Tail
  r16.connect(r14,None,lambda s:(s.has('Wings', p) or (s.has_all(['Roll', 'Bubble'], p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))) and o.bubble_jump.value >= 1)))
  # MONSTER.Sky.UpperWings -> MONSTER.Sky.Main
  r18.connect(r10,None,None)
  # MONSTER.Sky.WaterDronePlatform -> MONSTER.Sky.Main
  r19.connect(r10,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and s.has('Sprint', p)))
  # MONSTER.Kerrington.MedicinePool -> MONSTER.Kerrington.Main
  r21.connect(r22,None,lambda s:s.has('Open Medicine Pool', p))
  # MONSTER.Kerrington.MedicinePool -> MONSTER.Kerrington.MedicinePoolSlide
  r21.connect(r36,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Sprint', 'Roll'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['Sprint', 'Roll'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.MedicinePool
  r22.connect(r21,None,lambda s:s.has('Open Medicine Pool', p))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.Cockpit
  r22.connect(r23,None,lambda s:(s.has('Open Armada Cockpit', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.HeartEntryway
  r22.connect(r24,None,lambda s:(s.has("Open Kerrington's Heart", p) and (s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Free Armada Buddies', p) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and ((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and ((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Double Jump', p) and (s.has('Sprint', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))) or (s.has('Bubble', p) and o.bubble_jump.value == 2 and o.z_target.value == 1 and ((o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has_all(['Horn', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.IntoFrontDoor
  r22.connect(r28,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p]=='Jester Boots' and s.has('Double Jump', p))))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.GreenRoom
  r22.connect(r29,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p] is None and o.damage_boost.value == 1 and o.momentum_cancel.value == 1) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Roll', 'Sprint'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.LowerLabContainers
  r22.connect(r34,None,lambda s:((s.has('Double Jump', p) and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))))) or (s.has('Free Armada Buddies', p) and (s.has('Swim', p) or o.difficulty.value >= 1) and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Double Jump', 'Wings'], p) or o.difficulty.value >= 1))))))
  # MONSTER.Kerrington.Main -> MONSTER.Kerrington.UpperLabContainers
  r22.connect(r35,None,lambda s:((s.has_all(['Wings', 'Double Jump'], p) and o.ability_toggle.value == 1)))
  # MONSTER.Kerrington.Cockpit -> MONSTER.Kerrington.Main
  r23.connect(r22,None,lambda s:(s.has('Open Armada Cockpit', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # MONSTER.Kerrington.HeartEntryway -> MONSTER.Kerrington.Main
  r24.connect(r22,None,lambda s:s.has("Open Kerrington's Heart", p))
  # MONSTER.Kerrington.HeartEntryway -> MONSTER.Kerrington.HeartEntrywayPlatform
  r24.connect(r25,None,lambda s:(s.has('High Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # MONSTER.Kerrington.HeartEntryway -> MONSTER.Kerrington.HeartEntrywayCardPlatform
  r24.connect(r26,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # MONSTER.Kerrington.HeartEntrywayPlatform -> MONSTER.Kerrington.HeartEntryway
  r25.connect(r24,None,None)
  # MONSTER.Kerrington.HeartEntrywayPlatform -> MONSTER.Kerrington.HeartEntrywayCardPlatform
  r25.connect(r26,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2) or (s.has_all(['Bubble', 'Double Jump'], p) and o.bubble_jump.value >= 1 and (s.has('Sprint', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))))
  # MONSTER.Kerrington.HeartEntrywayCardPlatform -> MONSTER.Kerrington.HeartEntryway
  r26.connect(r24,None,None)
  # MONSTER.Kerrington.IntoFrontDoor -> MONSTER.Kerrington.Main
  r28.connect(r22,None,None)
  # MONSTER.Kerrington.GreenRoom -> MONSTER.Kerrington.Main
  r29.connect(r22,None,None)
  # MONSTER.Kerrington.GreenRoom -> MONSTER.Kerrington.GreenFence
  r29.connect(r30,None,None)
  # MONSTER.Kerrington.GreenRoom -> MONSTER.Kerrington.LabGreenConnector
  r29.connect(r32,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # MONSTER.Kerrington.GreenRoom -> MONSTER.Kerrington.GreenBoiler
  r29.connect(r33,None,lambda s:(s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['High Jump', 'Roll'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Roll', 'Sprint'], p)) or ((o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))
  # MONSTER.Kerrington.GreenFence -> MONSTER.Kerrington.GreenRoom
  r30.connect(r29,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Wings', 'Bubble'], p) and o.bubble_jump.value == 2) or (s.has('Roll', p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Double Jump', p) and (s.has('Wings', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and (s.has_any(['High Jump', 'Sprint'], p)))))
  # MONSTER.Sky.GreenDoorway -> MONSTER.Sky.Main
  r31.connect(r10,None,None)
  # MONSTER.Kerrington.LabGreenConnector -> MONSTER.Kerrington.GreenRoom
  r32.connect(r29,None,None)
  # MONSTER.Kerrington.LabGreenConnector -> MONSTER.Kerrington.GreenBoiler
  r32.connect(r33,None,None)
  # MONSTER.Kerrington.LabGreenConnector -> MONSTER.Kerrington.LowerLabContainers
  r32.connect(r34,None,None)
  # MONSTER.Kerrington.LabGreenConnector -> MONSTER.Kerrington.UpperLabContainers
  r32.connect(r35,None,None)
  # MONSTER.Kerrington.GreenBoiler -> MONSTER.Kerrington.Main
  r33.connect(r22,None,None)
  # MONSTER.Kerrington.LowerLabContainers -> MONSTER.Kerrington.Main
  r34.connect(r22,None,None)
  # MONSTER.Kerrington.LowerLabContainers -> MONSTER.Kerrington.LabGreenConnector
  r34.connect(r32,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Free Armada Buddies', p) and ((s.has('High Jump', p) and (s.has('Double Jump', p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Wings', 'Double Jump'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Roll', p) and o.difficulty.value >= 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # MONSTER.Kerrington.LowerLabContainers -> MONSTER.Kerrington.UpperLabContainers
  r34.connect(r35,None,lambda s:((s.has('Double Jump', p) and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('High Jump', p) and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has('Wings', p) and ((o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))) or (s.has('Free Armada Buddies', p) and ((s.has_all(['Double Jump', 'Wings'], p))))))
  # MONSTER.Kerrington.UpperLabContainers -> MONSTER.Kerrington.Main
  r35.connect(r22,None,None)
  # MONSTER.Kerrington.UpperLabContainers -> MONSTER.Kerrington.LabGreenConnector
  r35.connect(r32,None,lambda s:((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Free Armada Buddies', p) and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # MONSTER.Kerrington.MedicinePoolSlide -> MONSTER.Kerrington.MedicinePoolEggPlatform
  r36.connect(r37,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['High Jump', 'Sprint', 'Double Jump', 'Wings'], p) or o.difficulty.value >= 1 or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # MONSTER.Kerrington.MedicinePoolEggPlatform -> MONSTER.Kerrington.MedicinePool
  r37.connect(r21,None,None)
  # CAVE.ArmadaLobby.FlagPlatform -> CAVE.ArmadaLobby.Main
  r38.connect(r2,None,None)
  # CAVE.ArmadaLobby.FlagPlatform -> CAVE.ArmadaLobby.SewerConnector
  r38.connect(r39,None,lambda s:s.has('Swim', p))
  # CAVE.ArmadaLobby.SewerConnector -> CAVE.ArmadaLobby.FlagPlatform
  r39.connect(r38,None,lambda s:s.has('Swim', p))
  # CAVE.Sewer.ArmadaLobbySide -> CAVE.Sewer.GallerySide
  r40.connect(r41,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and ((o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (o.ability_toggle.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s._cavernofdreams_carrying[p]=='Jester Boots' and s.has('Wings', p)))) or (s.has('Wings', p) and ((o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))) or (s._cavernofdreams_carrying[p]=='Jester Boots' and ((o.difficulty.value >= 1 and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Double Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s._cavernofdreams_carrying[p]=='Jester Boots' and s.has('Bubble', p) and o.difficulty.value >= 2 and o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2)))
  # CAVE.Sewer.GallerySide -> CAVE.Sewer.ArmadaLobbySide
  r41.connect(r40,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Double Jump', p) and (s.has('Wings', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has_all(['High Jump', 'Bubble'], p) and (o.difficulty.value >= 1 or o.z_target.value == 1) and o.bubble_jump.value == 2 and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Sprint', 'Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.difficulty.value >= 2 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.difficulty.value >= 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has('Wings', p) or (s.has_all(['Bubble', 'High Jump'], p)))) or (s.has_all(['Roll', 'Sprint'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.WaterLobby.LobbySewerUnderwater -> GALLERY.WaterLobby.LobbySewerMiddle
  r42.connect(r43,None,None)
  # GALLERY.WaterLobby.LobbySewerUnderwater -> GALLERY.WaterLobby.LobbySewerGiant
  r42.connect(r78,None,None)
  # GALLERY.WaterLobby.LobbySewerMiddle -> GALLERY.WaterLobby.Main
  r43.connect(r44,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Double Jump', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.WaterLobby.LobbySewerMiddle -> GALLERY.WaterLobby.LobbySewerEgg
  r43.connect(r69,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has('Double Jump', p) and (s.has('Wings', p) or (s.has('Bubble', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and o.bubble_jump.value >= 1) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s.has('High Jump', p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and ((s.has_all(['Roll', 'Bubble'], p) and o.bubble_jump.value >= 1) or (s.has_all(['Wings', 'High Jump'], p)))))))
  # GALLERY.WaterLobby.LobbySewerMiddle -> GALLERY.WaterLobby.LobbySewerUnderwater
  r43.connect(r42,None,lambda s:s.has('Swim', p))
  # GALLERY.WaterLobby.Main -> GALLERY.WaterLobby.LobbySewerMiddle
  r44.connect(r43,None,None)
  # GALLERY.WaterLobby.Main -> GALLERY.WaterLobby.SpookyWall.WhackableRegion
  r44.connect(r45,None,None)
  # GALLERY.WaterLobby.Main -> GALLERY.WaterLobby.Spooky
  r44.connect(r46,None,lambda s:s.has('GALLERY.WaterLobby.SpookyWall', p))
  # GALLERY.WaterLobby.Spooky -> GALLERY.WaterLobby.LunaHouse
  r46.connect(r47,None,lambda s:s.has("Open Luna's House", p))
  # GALLERY.WaterLobby.Spooky -> GALLERY.WaterLobby.SpookyWaterUpper
  r46.connect(r49,None,lambda s:s.has('Swim', p))
  # GALLERY.WaterLobby.Spooky -> GALLERY.WaterLobby.SpookyWall.WhackableRegion
  r46.connect(r45,None,None)
  # GALLERY.WaterLobby.Spooky -> GALLERY.WaterLobby.Main
  r46.connect(r44,None,lambda s:s.has('GALLERY.WaterLobby.SpookyWall', p))
  # GALLERY.WaterLobby.LunaHouse -> GALLERY.WaterLobby.Spooky
  r47.connect(r46,None,lambda s:s.has("Open Luna's House", p))
  # GALLERY.WaterLobby.SpookyWaterUpper -> GALLERY.WaterLobby.Spooky
  r49.connect(r46,None,None)
  # GALLERY.WaterLobby.SpookyWaterUpper -> GALLERY.WaterLobby.SpookyWaterLower
  r49.connect(r50,None,lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  # GALLERY.WaterLobby.SpookyWaterLower -> GALLERY.WaterLobby.SpookyWaterUpper
  r50.connect(r49,None,None)
  # GALLERY.Foyer.Main -> GALLERY.Foyer.SideDoors
  r51.connect(r52,None,lambda s:s.has('Open Gallery Doors', p))
  # GALLERY.Foyer.SideDoors -> GALLERY.Foyer.Main
  r52.connect(r51,None,None)
  # GALLERY.FireLobby.Main -> GALLERY.FireLobby.ChalicePlatform
  r53.connect(r54,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p] is None and s.has('Extend Fire Lobby Frying Pans', p))))
  # GALLERY.FireLobby.Main -> GALLERY.FireLobby.FishPlatform
  r53.connect(r55,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Double Jump', 'Wings'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # GALLERY.FireLobby.Main -> GALLERY.FireLobby.EarthLobbyEntryway
  r53.connect(r60,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Extend Fire Lobby Tongue Platform', 'Wings'], p) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and ((o.ejection_launch.value == 1 and (o.difficulty.value >= 2 or (s.has('Bubble', p) and o.difficulty.value >= 1 and o.bubble_jump.value >= 1)))))))
  # GALLERY.FireLobby.Main -> GALLERY.FireLobby.ClimbToKerringtonPaintingPlatform
  r53.connect(r80,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['Double Jump', 'Sprint', 'Roll'], p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # GALLERY.FireLobby.Main -> GALLERY.FireLobby.KerringtonPaintingPlatform
  r53.connect(r56,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"}))
  # GALLERY.FireLobby.ChalicePlatform -> GALLERY.FireLobby.Main
  r54.connect(r53,None,None)
  # GALLERY.FireLobby.ChalicePlatform -> GALLERY.FireLobby.FishPlatform
  r54.connect(r55,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.difficulty.value >= 1) or (s.has('Wings', p) and (s.has('Sprint', p) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))))
  # GALLERY.FireLobby.ChalicePlatform -> GALLERY.FireLobby.KerringtonPaintingPlatform
  r54.connect(r56,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'}))
  # GALLERY.FireLobby.FishPlatform -> GALLERY.FireLobby.Main
  r55.connect(r53,None,None)
  # GALLERY.FireLobby.KerringtonPaintingPlatform -> GALLERY.FireLobby.Main
  r56.connect(r53,None,None)
  # GALLERY.Chalice.Main -> GALLERY.Chalice.EggPlatform
  r57.connect(r58,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Coils of Agony - Open Shortcut', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Wings', p) and (s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (((s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))) and (s.has_any(['Double Jump', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or o.difficulty.value >= 1))))
  # GALLERY.Chalice.Main -> GALLERY.Chalice.BottomShortcutPlatform
  r57.connect(r59,None,lambda s:s.has('GALLERY.Chalice.OpenedLowerSnake', p))
  # GALLERY.Chalice.EggPlatform -> GALLERY.Chalice.Main
  r58.connect(r57,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots', None} or s.has_any(['Coils of Agony - Open Shortcut', 'Wings', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.Chalice.BottomShortcutPlatform -> GALLERY.Chalice.Main
  r59.connect(r57,None,None)
  # GALLERY.FireLobby.EarthLobbyEntryway -> GALLERY.FireLobby.Main
  r60.connect(r53,None,None)
  # GALLERY.EarthLobby.FireLobbyEntryway -> GALLERY.EarthLobby.Coffins
  r61.connect(r62,None,None)
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.GrowMainBush
  r62.connect(r63,None,lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p)))
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.MainUnderwater
  r62.connect(r64,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.CoffinsUnderwater
  r62.connect(r77,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.CoffinsStatuePlatform
  r62.connect(r79,None,lambda s:(s.has_any(['Wings', 'Double Jump'], p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.FireLobbyEntryway
  r62.connect(r61,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('High Jump', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.difficulty.value >= 1) or (s.has('Double Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s.has('High Jump', p) or o.difficulty.value >= 1)) or (s.has_all(['Double Jump', 'High Jump'], p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.EarthLobby.Coffins -> GALLERY.EarthLobby.Main
  r62.connect(r65,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['GALLERY.EarthLobby.GrewMainBush', 'Double Jump', 'Wings', 'Sprint'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Roll', 'Horn'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # GALLERY.EarthLobby.MainUnderwater -> GALLERY.EarthLobby.Main
  r64.connect(r65,None,None)
  # GALLERY.EarthLobby.MainUnderwater -> GALLERY.EarthLobby.Coffins
  r64.connect(r62,None,None)
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.MainUnderwater
  r65.connect(r64,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.InsideCastle
  r65.connect(r66,None,lambda s:s.has('Open Gallery of Nightmares Swamp Door', p))
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.GrowMainBush
  r65.connect(r63,None,lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p)))
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.DragonHead
  r65.connect(r75,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has_any(['Double Jump', 'Wings'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and (s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))) and o.bubble_jump.value >= 1)))
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.Coffins
  r65.connect(r62,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['GALLERY.EarthLobby.GrewMainBush', 'Double Jump', 'Wings'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.EarthLobby.Main -> GALLERY.EarthLobby.FoyerEntryPlatform
  r65.connect(r76,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and s.has_all(['High Jump', 'Double Jump', 'Sprint'], p)) or (s.has_all(['Bubble', 'Horn', 'Double Jump'], p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2 and o.ability_toggle.value == 1 and o.z_target.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.EarthLobby.GrowCastleBushes
  r66.connect(r67,None,lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p)))
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.EarthLobby.Main
  r66.connect(r65,None,lambda s:s.has('Open Gallery of Nightmares Swamp Door', p))
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.EarthLobby.CastleUnderwater
  r66.connect(r68,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.EarthLobby.KerringtonCauldronPlatform
  r66.connect(r70,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Wings', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.EarthLobby.CastleWingsPlatform
  r66.connect(r73,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['GALLERY.EarthLobby.GrewCastleBushes', 'Wings', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # GALLERY.EarthLobby.CastleUnderwater -> GALLERY.EarthLobby.InsideCastle
  r68.connect(r66,None,None)
  # GALLERY.WaterLobby.LobbySewerEgg -> GALLERY.WaterLobby.LobbySewerMiddle
  r69.connect(r43,None,None)
  # GALLERY.EarthLobby.KerringtonCauldronPlatform -> GALLERY.EarthLobby.InsideCastle
  r70.connect(r66,None,None)
  # GALLERY.EarthLobby.KerringtonCauldronPlatform -> GALLERY.EarthLobby.KerringtonCauldronEntryway
  r70.connect(r71,None,lambda s:s.has('Open Gallery-Armada Connector', p))
  # GALLERY.EarthLobby.KerringtonCauldronEntryway -> GALLERY.EarthLobby.KerringtonCauldronPlatform
  r71.connect(r70,None,lambda s:s.has('Open Gallery-Armada Connector', p))
  # MONSTER.Kerrington.CauldronRoom -> MONSTER.Kerrington.Main
  r72.connect(r22,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # GALLERY.EarthLobby.CastleWingsPlatform -> GALLERY.EarthLobby.InsideCastle
  r73.connect(r66,None,None)
  # GALLERY.EarthLobby.DragonHead -> GALLERY.EarthLobby.MainUnderwater
  r75.connect(r64,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.DragonHead -> GALLERY.EarthLobby.Main
  r75.connect(r65,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has_any(['Double Jump', 'Wings'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and (s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))) and o.bubble_jump.value >= 1)))
  # GALLERY.EarthLobby.FoyerEntryPlatform -> GALLERY.EarthLobby.Main
  r76.connect(r65,None,None)
  # GALLERY.EarthLobby.CoffinsUnderwater -> GALLERY.EarthLobby.Coffins
  r77.connect(r62,None,None)
  # GALLERY.WaterLobby.LobbySewerGiant -> GALLERY.WaterLobby.LobbySewerUnderwater
  r78.connect(r42,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.CoffinsStatuePlatform -> GALLERY.EarthLobby.CoffinsUnderwater
  r79.connect(r77,None,lambda s:s.has('Swim', p))
  # GALLERY.EarthLobby.CoffinsStatuePlatform -> GALLERY.EarthLobby.Coffins
  r79.connect(r62,None,lambda s:(s.has_any(['Wings', 'Double Jump'], p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # GALLERY.FireLobby.ClimbToKerringtonPaintingPlatform -> GALLERY.FireLobby.KerringtonPaintingPlatform
  r80.connect(r56,None,lambda s:(s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  # CAVE.GalleryLobby.Main -> CAVE.GalleryLobby.OuterWalls
  r81.connect(r82,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has_all(['Double Jump', 'Roll'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Roll', 'Sprint'], p) and o.difficulty.value >= 1)))
  # CAVE.GalleryLobby.Main -> CAVE.GalleryLobby.LostleafCave
  r81.connect(r85,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # CAVE.GalleryLobby.Main -> CAVE.GalleryLobby.Maze
  r81.connect(r83,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Open Gallery Lobby Hedge Maze', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['High Jump', 'Double Jump'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Wings', 'Double Jump'], p)) or (s.has_all(['Roll', 'Wings'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # CAVE.GalleryLobby.Main -> CAVE.GalleryLobby.MazeStatue
  r81.connect(r84,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots'))
  # CAVE.GalleryLobby.OuterWalls -> CAVE.GalleryLobby.Main
  r82.connect(r81,None,None)
  # CAVE.GalleryLobby.OuterWalls -> CAVE.GalleryLobby.Maze
  r82.connect(r83,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or o.momentum_cancel.value == 1))))
  # CAVE.GalleryLobby.OuterWalls -> CAVE.GalleryLobby.LostleafCave
  r82.connect(r85,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or o.momentum_cancel.value == 1))
  # CAVE.GalleryLobby.Maze -> CAVE.GalleryLobby.Main
  r83.connect(r81,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Open Gallery Lobby Hedge Maze', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # CAVE.GalleryLobby.Maze -> CAVE.GalleryLobby.MazeStatue
  r83.connect(r84,None,lambda s:(s.has('Open Gallery Lobby Door', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=='Jester Boots' and (s.has('Double Jump', p) or o.out_of_bounds.value == 1 or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Bubble', p) and (s.has('Double Jump', p) or o.ejection_launch.value == 1 or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Double Jump', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['High Jump', 'Wings'], p)) or (s.has('High Jump', p) and o.difficulty.value >= 1 and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # CAVE.GalleryLobby.MazeStatue -> CAVE.GalleryLobby.Maze
  r84.connect(r83,None,lambda s:(s.has('Open Gallery Lobby Door', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Double Jump', 'Wings', 'High Jump'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # CAVE.GalleryLobby.LostleafCave -> CAVE.GalleryLobby.Main
  r85.connect(r81,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['CAVE.GalleryLobby.GalleryLobbySoil', 'Climb', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # CAVE.LostleafLobby.HiddenDoorway -> CAVE.LostleafLobby.BreakHiddenWall
  r86.connect(r87,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # CAVE.LostleafLobby.HiddenDoorway -> CAVE.LostleafLobby.Main
  r86.connect(r88,None,lambda s:s.has('CAVE.LostleafLobby.BrokeHiddenWall', p))
  # CAVE.LostleafLobby.Main -> CAVE.LostleafLobby.BreakHiddenWall
  r88.connect(r87,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # CAVE.LostleafLobby.Main -> CAVE.LostleafLobby.HiddenDoorway
  r88.connect(r86,None,lambda s:s.has('CAVE.LostleafLobby.BrokeHiddenWall', p))
  # CAVE.LostleafLobby.Main -> CAVE.LostleafLobby.Trees
  r88.connect(r89,None,None)
  # CAVE.LostleafLobby.Trees -> CAVE.LostleafLobby.Main
  r89.connect(r88,None,None)
  # CAVE.SunCavern.MightyWallLedge -> CAVE.SunCavern.Main
  r90.connect(r0,None,None)
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.OuterRim
  r91.connect(r92,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Roll', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.ability_toggle.value == 1) or (s.has_all(['High Jump', 'Double Jump', 'Wings'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1)))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.Lake
  r91.connect(r94,None,lambda s:s.has('Swim', p))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.LakeStump
  r91.connect(r189,None,lambda s:(s.has('Double Jump', p) or (o.difficulty.value >= 1 and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['Wings', 'Sprint'], p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.WaterfallEggCave
  r91.connect(r186,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.DeepWoods
  r91.connect(r168,None,lambda s:s.has('Open Deep Woods', p))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.BellTower
  r91.connect(r181,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['LAKE.LostleafLake.BellTowerSoil', 'Climb'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.RingBell
  r91.connect(r182,None,lambda s:(s.has('Bubble', p) or (s._cavernofdreams_carrying[p]=='Bubble Conch' and s.has('Swim', p))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.TreehouseBranches
  r91.connect(r159,None,lambda s:(s.has('Raise Lake Swings', p) or (s.has_all(['Horn', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.PrestonLedge
  r91.connect(r160,None,lambda s:(s.has('Raise Lake Swings', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['LAKE.LostleafLake.WinkyTreeSoil', 'Climb'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))))
  # LAKE.LostleafLake.Main -> LAKE.LostleafLake.WinkyTreeLedge
  r91.connect(r162,None,lambda s:(s.has('Double Jump', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # LAKE.LostleafLake.OuterRim -> LAKE.LostleafLake.TeepeeIsland
  r92.connect(r93,None,None)
  # LAKE.LostleafLake.OuterRim -> LAKE.LostleafLake.Main
  r92.connect(r91,None,None)
  # LAKE.LostleafLake.OuterRim -> LAKE.LostleafLake.FallIntoTeepee
  r92.connect(r187,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # LAKE.LostleafLake.OuterRim -> LAKE.LostleafLake.PrestonLedge
  r92.connect(r160,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch', 'Jester Boots'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('High Jump', p) and o.difficulty.value >= 2)) and (s.has('Wings', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # LAKE.LostleafLake.OuterRim -> LAKE.LostleafLake.BellTower
  r92.connect(r181,None,lambda s:((s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value == 2) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Roll', p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.LostleafLake.Lake
  r93.connect(r94,None,lambda s:s.has('Swim', p))
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.LostleafLake.FallIntoTeepee
  r93.connect(r187,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Double Jump', 'High Jump', 'Wings'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.LostleafLake.InsideCrypt
  r93.connect(r180,None,lambda s:s.has('Open Crypt', p))
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.LostleafLake.Main
  r93.connect(r91,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has('Wings', p) and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.z_target.value == 1 and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Double Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))))
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.LostleafLake.OuterRim
  r93.connect(r92,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Double Jump', 'Wings', 'High Jump'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.ejection_launch.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['High Jump', 'Double Jump', 'Wings'], p) or (s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has('Sprint', p) and o.difficulty.value >= 2) or (s.has('Bubble', p) and o.difficulty.value >= 1 and o.bubble_jump.value >= 1)) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))))
  # LAKE.LostleafLake.Lake -> LAKE.LostleafLake.SecretWorld
  r94.connect(r95,None,lambda s:(o.out_of_bounds.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  # LAKE.LostleafLake.Lake -> LAKE.LostleafLake.OuterRim
  r94.connect(r92,None,lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"}))
  # LAKE.LostleafLake.Lake -> LAKE.LostleafLake.Main
  r94.connect(r91,None,None)
  # LAKE.LostleafLake.Lake -> LAKE.LostleafLake.InsideChurch
  r94.connect(r183,None,lambda s:(s.has('Open Church', p)))
  # LAKE.LostleafLake.Lake -> LAKE.LostleafLake.TeepeeIsland
  r94.connect(r93,None,None)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.Main
  r95.connect(r91,None,None)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.DucklingsLedge
  r95.connect(r96,None,lambda s:o.ejection_launch.value == 1)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.WaterfallCanopy
  r95.connect(r167,None,lambda s:o.ejection_launch.value == 1)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.BellTower
  r95.connect(r181,None,lambda s:o.ejection_launch.value == 1)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.DeepWoods
  r95.connect(r168,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Air Swim', p) or (s.has_all(['Double Jump', 'Wings', 'Sprint'], p) and o.difficulty.value >= 2)))
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.DeepDeepWoods
  r95.connect(r170,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Air Swim', p)))
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.InsideCrypt
  r95.connect(r180,None,None)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.BigAppleLedge
  r95.connect(r161,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has_any(['Wings', 'Air Swim'], p)))
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.InsideChurch
  r95.connect(r183,None,None)
  # LAKE.LostleafLake.SecretWorld -> LAKE.LostleafLake.WaterfallEggCave
  r95.connect(r186,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Air Swim', p) or (s.has_all(['Double Jump', 'Sprint'], p) and o.difficulty.value >= 2)))
  # LAKE.LostleafLake.DucklingsLedge -> LAKE.LostleafLake.Ducklings
  r96.connect(r97,None,None)
  # LAKE.LostleafLake.DucklingsLedge -> LAKE.LostleafLake.TreehouseBranches
  r96.connect(r159,None,None)
  # LAKE.LostleafLake.DucklingsLedge -> LAKE.LostleafLake.PrestonLedge
  r96.connect(r160,None,None)
  # LAKE.LostleafLake.DucklingsLedge -> LAKE.LostleafLake.WaterfallCanopy
  r96.connect(r167,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.ejection_launch.value == 1 and (s.has('Wings', p) or o.difficulty.value >= 2 or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # LAKE.LostleafLake.Ducklings -> LAKE.LostleafLake.DucklingsLedge
  r97.connect(r96,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Wings', 'Bubble'], p) and o.bubble_jump.value == 2) or (s.has('Double Jump', p) and (s.has('High Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))))
  # CAVE.SunCavern.WaterfallLedge -> CAVE.SunCavern.Main
  r98.connect(r0,None,None)
  # CAVE.SunCavern.WaterfallLedge -> CAVE.SunCavern.DucklingsDoorway
  r98.connect(r99,None,lambda s:((s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # CAVE.SunCavern.WaterfallLedge -> CAVE.SunCavern.MoonCavernHeartDoorway
  r98.connect(r101,None,lambda s:s.has('Swim', p))
  # CAVE.SunCavern.DucklingsDoorway -> CAVE.SunCavern.DucklingsLedge
  r99.connect(r100,None,None)
  # CAVE.SunCavern.DucklingsLedge -> CAVE.SunCavern.Main
  r100.connect(r0,None,None)
  # CAVE.SunCavern.DucklingsLedge -> CAVE.SunCavern.DucklingsDoorway
  r100.connect(r99,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # CAVE.SunCavern.MoonCavernHeartDoorway -> CAVE.SunCavern.Main
  r101.connect(r0,None,lambda s:s.has('Swim', p))
  # CAVE.SunCavern.MoonCavernHeartDoorway -> CAVE.SunCavern.DucklingsDoorway
  r101.connect(r99,None,lambda s:s.has('Swim', p))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.DiveHoles
  r102.connect(r103,None,lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.DiveRoom
  r102.connect(r104,None,lambda s:((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.DivePuzzleLedge
  r102.connect(r105,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or s.has('Bubble', p) or (s.has('Double Jump', p) and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has_all(['Wings', 'Double Jump'], p)) or (s.has('High Jump', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.UpperConnector
  r102.connect(r106,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p] is None and o.damage_boost.value == 1) or (s.has('Bubble', p) and o.z_target.value == 1 and o.bubble_jump.value >= 1) or s.has('Wings', p)))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.Upper
  r102.connect(r107,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or s.has('Wings', p) or (s._cavernofdreams_carrying[p] is None and s.has('Bubble', p) and o.damage_boost.value == 1 and o.bubble_jump.value >= 1)))
  # CAVE.MoonCavern.Main -> CAVE.MoonCavern.LavaMushroomPlatform
  r102.connect(r157,None,None)
  # CAVE.MoonCavern.DiveHoles -> CAVE.MoonCavern.Main
  r103.connect(r102,None,None)
  # CAVE.MoonCavern.DiveRoom -> CAVE.MoonCavern.Main
  r104.connect(r102,None,lambda s:(s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  # CAVE.MoonCavern.DivePuzzleLedge -> CAVE.MoonCavern.Main
  r105.connect(r102,None,None)
  # CAVE.MoonCavern.UpperConnector -> CAVE.MoonCavern.Main
  r106.connect(r102,None,None)
  # CAVE.MoonCavern.UpperConnector -> CAVE.MoonCavern.Upper
  r106.connect(r107,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # CAVE.MoonCavern.Upper -> CAVE.MoonCavern.UpperConnector
  r107.connect(r106,None,None)
  # CAVE.PalaceLobby.Main -> CAVE.PalaceLobby.Underwater
  r108.connect(r109,None,lambda s:s.has('Swim', p))
  # CAVE.PalaceLobby.Main -> CAVE.PalaceLobby.Ledges
  r108.connect(r111,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and ((s.has('Bubble', p) and o.bubble_jump.value == 2 and o.z_target.value == 1) or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))))) or (s.has('High Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has_all(['Double Jump', 'Wings'], p)) or s.has('Activate Palace Lobby Whirlpool', p)))
  # CAVE.PalaceLobby.Underwater -> CAVE.PalaceLobby.Main
  r109.connect(r108,None,None)
  # CAVE.PalaceLobby.Underwater -> CAVE.PalaceLobby.PrismicEntryPlatform
  r109.connect(r110,None,lambda s:(s._cavernofdreams_carrying[p] in {"Shelnert's Fish", 'Bubble Conch'} or s.has_any(['Sprint', 'Air Swim'], p)))
  # CAVE.PalaceLobby.Underwater -> CAVE.PalaceLobby.TopLedge
  r109.connect(r112,None,lambda s:(s._cavernofdreams_carrying[p] in {"Shelnert's Fish", 'Bubble Conch'} or s.has('Air Swim', p)))
  # CAVE.PalaceLobby.PrismicEntryPlatform -> CAVE.PalaceLobby.Ledges
  r110.connect(r111,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['Activate Palace Lobby Whirlpool', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Sprint', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has_all(['Bubble', 'High Jump'], p) and o.bubble_jump.value == 2) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # CAVE.PalaceLobby.PrismicEntryPlatform -> CAVE.PalaceLobby.TopLedge
  r110.connect(r112,None,lambda s:((s.has_all(['Horn', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and (s.has_any(['High Jump', 'Double Jump'], p) or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))))) or (s.has_all(['Double Jump', 'High Jump'], p) and (s.has('Wings', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Bubble', p) and o.bubble_jump.value == 2 and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and (s.has_any(['Double Jump', 'High Jump'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))))
  # CAVE.PalaceLobby.Ledges -> CAVE.PalaceLobby.Main
  r111.connect(r108,None,lambda s:(s.has('Wings', p) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['High Jump', 'Sprint'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # CAVE.PalaceLobby.Ledges -> CAVE.PalaceLobby.PrismicEntryPlatform
  r111.connect(r110,None,lambda s:(s.has('Run Palace Lobby Faucet', p) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('High Jump', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Activate Palace Lobby Whirlpool', p) and ((s.has('Horn', p) and o.difficulty.value >= 2 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or o.ejection_launch.value == 1))))
  # CAVE.PalaceLobby.TopLedge -> CAVE.PalaceLobby.Main
  r112.connect(r108,None,None)
  # CAVE.PalaceLobby.TopLedge -> CAVE.PalaceLobby.PrismicEntryPlatform
  r112.connect(r110,None,None)
  # CAVE.PalaceLobby.TopLedge -> CAVE.PalaceLobby.Ledges
  r112.connect(r111,None,None)
  # PALACE.Valley.Main -> PALACE.Valley.OuterRim
  r113.connect(r114,None,lambda s:(s.has('PALACE.Valley.AirSwimFromLostleafEntryway', p) or (s.has_all(['Unfreeze Prismic Palace', 'Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1)))
  # PALACE.Valley.Main -> PALACE.Valley.UpperWater
  r113.connect(r146,None,lambda s:(s.has_all(['Unfreeze Prismic Palace', 'Swim'], p)))
  # PALACE.Valley.Main -> PALACE.Valley.ClipIntoIce
  r113.connect(r154,None,lambda s:(s.has('Swim', p) and o.out_of_bounds.value == 1))
  # PALACE.Valley.Main -> PALACE.Valley.Spires
  r113.connect(r126,None,lambda s:(s.has('PALACE.Valley.AirSwimFromLostleafEntryway', p) or (s.has_all(['Unfreeze Prismic Palace', 'Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # PALACE.Valley.Main -> PALACE.Valley.PoolCardLedge
  r113.connect(r155,None,lambda s:(s.has('PALACE.Valley.AirSwimFromLostleafEntryway', p) or (s.has_all(['Unfreeze Prismic Palace', 'Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.Main -> PALACE.Valley.Pool
  r113.connect(r156,None,lambda s:(s.has('Swim', p) and (s.has('Unfreeze Prismic Palace', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))
  # PALACE.Valley.Main -> PALACE.Valley.EntrancePomLedge
  r113.connect(r124,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Double Jump', p) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has('High Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # PALACE.Valley.Main -> PALACE.Valley.PokiPokiCave
  r113.connect(r127,None,lambda s:(s.has('Double Jump', p) or o.difficulty.value >= 1 or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and ((o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))))
  # PALACE.Valley.OuterRim -> PALACE.Valley.Main
  r114.connect(r113,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.JesterBootsCoveFloatingPoms
  r114.connect(r115,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.JesterBootsCoveUpperCastle
  r114.connect(r122,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.EntrancePomLedge
  r114.connect(r124,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.PalaceCardLedge
  r114.connect(r125,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.PokiPokiCave
  r114.connect(r127,None,None)
  # PALACE.Valley.OuterRim -> PALACE.Valley.ObservatoryPlatform
  r114.connect(r128,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Wings', p) or (s.has_all(['Sprint', 'Roll'], p))))
  # PALACE.Valley.OuterRim -> PALACE.Valley.PalaceTop
  r114.connect(r136,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has('Wings', p) or o.difficulty.value >= 2 or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.JesterBootsCoveFloatingPoms -> PALACE.Valley.JesterBootsCove
  r115.connect(r116,None,None)
  # PALACE.Valley.JesterBootsCoveFloatingPoms -> PALACE.Valley.OuterRim
  r115.connect(r114,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' and s.has('Roll', p) and o.ejection_launch.value == 1))
  # PALACE.Valley.JesterBootsCoveFloatingPoms -> PALACE.Valley.JesterBootsCovePrestonPlatform
  r115.connect(r123,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has_all(['Wings', 'Horn'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)) and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # PALACE.Valley.JesterBootsCove -> PALACE.Valley.LostleafEntryway
  r116.connect(r117,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has('Open Palace-Lostleaf Connector', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and (s.has_any(['Wings', 'High Jump'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('High Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and o.z_target.value == 1)))
  # PALACE.Valley.JesterBootsCove -> PALACE.Valley.JesterBootsCoveLowerPlatforms
  r116.connect(r118,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2)))
  # PALACE.Valley.LostleafEntryway -> PALACE.Valley.JesterBootsCove
  r117.connect(r116,None,lambda s:(s.has('PALACE.Valley.AirSwimFromLostleafEntryway', p)))
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.JesterBootsCove
  r118.connect(r116,None,None)
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.Main
  r118.connect(r113,None,None)
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.JesterBootsCoveCastlePlatform
  r118.connect(r119,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Double Jump'], p) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2 and o.z_target.value == 1)))
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.JesterBootsCoveLowerCastle
  r118.connect(r120,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.LostleafEntryway
  r118.connect(r117,None,lambda s:((s.has_all(['Roll', 'Bubble'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.bubble_jump.value >= 1)))
  # PALACE.Valley.JesterBootsCoveLowerPlatforms -> PALACE.Valley.JesterBootsCoveFloatingPoms
  r118.connect(r115,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.JesterBootsCoveCastlePlatform -> PALACE.Valley.JesterBootsCoveLowerPlatforms
  r119.connect(r118,None,None)
  # PALACE.Valley.JesterBootsCoveCastlePlatform -> PALACE.Valley.JesterBootsCoveLowerCastle
  r119.connect(r120,None,None)
  # PALACE.Valley.JesterBootsCoveCastlePlatform -> PALACE.Valley.JesterBootsCoveMidCastle
  r119.connect(r121,None,None)
  # PALACE.Valley.JesterBootsCoveLowerCastle -> PALACE.Valley.JesterBootsCove
  r120.connect(r116,None,None)
  # PALACE.Valley.JesterBootsCoveLowerCastle -> PALACE.Valley.LostleafEntryway
  r120.connect(r117,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"}))
  # PALACE.Valley.JesterBootsCoveMidCastle -> PALACE.Valley.JesterBootsCoveUpperCastle
  r121.connect(r122,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Double Jump'], p) or o.difficulty.value >= 1 or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.JesterBootsCoveMidCastle -> PALACE.Valley.LostleafEntryway
  r121.connect(r117,None,lambda s:s.has('Wings', p))
  # PALACE.Valley.JesterBootsCoveMidCastle -> PALACE.Valley.JesterBootsCoveLowerCastle
  r121.connect(r120,None,None)
  # PALACE.Valley.JesterBootsCoveMidCastle -> PALACE.Valley.JesterBootsCoveCastlePlatform
  r121.connect(r119,None,None)
  # PALACE.Valley.JesterBootsCoveMidCastle -> PALACE.Valley.JesterBootsCove
  r121.connect(r116,None,None)
  # PALACE.Valley.JesterBootsCoveUpperCastle -> PALACE.Valley.JesterBootsCoveLowerCastle
  r122.connect(r120,None,None)
  # PALACE.Valley.JesterBootsCoveUpperCastle -> PALACE.Valley.JesterBootsCoveFloatingPoms
  r122.connect(r115,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2 and o.z_target.value == 1) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has_all(['Roll', 'Bubble'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.bubble_jump.value >= 1)))
  # PALACE.Valley.JesterBootsCovePrestonPlatform -> PALACE.Valley.JesterBootsCove
  r123.connect(r116,None,None)
  # PALACE.Valley.JesterBootsCovePrestonPlatform -> PALACE.Valley.JesterBootsCoveFloatingPoms
  r123.connect(r115,None,None)
  # PALACE.Valley.EntrancePomLedge -> PALACE.Valley.Main
  r124.connect(r113,None,None)
  # PALACE.Valley.PalaceCardLedge -> PALACE.Valley.Main
  r125.connect(r113,None,None)
  # PALACE.Valley.PalaceCardLedge -> PALACE.Valley.OuterRim
  r125.connect(r114,None,lambda s:(s.has('Wings', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (s.has('Double Jump', p) and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.momentum_cancel.value == 1) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Sprint', 'Double Jump'], p))))
  # PALACE.Valley.PalaceCardLedge -> PALACE.Valley.Spires
  r125.connect(r126,None,None)
  # PALACE.Valley.PalaceCardLedge -> PALACE.Valley.PokiPokiCave
  r125.connect(r127,None,None)
  # PALACE.Valley.Spires -> PALACE.Valley.Main
  r126.connect(r113,None,None)
  # PALACE.Valley.Spires -> PALACE.Valley.PokiPokiCave
  r126.connect(r127,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.Spires -> PALACE.Valley.ObservatoryPlatform
  r126.connect(r128,None,lambda s:(s.has_any(['Double Jump', 'High Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # PALACE.Valley.PokiPokiCave -> PALACE.Valley.Main
  r127.connect(r113,None,None)
  # PALACE.Valley.PokiPokiCave -> PALACE.Valley.Spires
  r127.connect(r126,None,None)
  # PALACE.Valley.ObservatoryPlatform -> PALACE.Valley.ObservatoryEntry
  r128.connect(r129,None,lambda s:s.has('Unfreeze Prismic Palace', p))
  # PALACE.Valley.ObservatoryPlatform -> PALACE.Valley.ObservatoryRoof
  r128.connect(r131,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # PALACE.Valley.ObservatoryPlatform -> PALACE.Valley.ObservatorySlideEnd
  r128.connect(r132,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has('Roll', p) and (s.has_any(['Sprint', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # PALACE.Valley.ObservatoryPlatform -> PALACE.Valley.OuterRim
  r128.connect(r114,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.momentum_cancel.value == 1) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Wings', 'Double Jump'], p)) or (s.has('Sprint', p) and ((s.has_all(['Double Jump', 'Bubble'], p) and o.bubble_jump.value >= 1))) or (s.has('Roll', p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))) and (s.has_any(['Double Jump', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # PALACE.Valley.ObservatoryEntry -> PALACE.Valley.ObservatoryPlatform
  r129.connect(r128,None,None)
  # PALACE.Valley.ObservatoryRoof -> PALACE.Valley.ObservatoryPlatform
  r131.connect(r128,None,None)
  # PALACE.Valley.ObservatoryRoof -> PALACE.Valley.ObservatoryEntry
  r131.connect(r129,None,lambda s:(s.has('Roll', p) and o.roll_disjoint.value == 1 and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))
  # PALACE.Valley.ObservatoryRoof -> PALACE.Valley.ObservatorySlideEnd
  r131.connect(r132,None,lambda s:s.has('Wings', p))
  # PALACE.Valley.ObservatoryRoof -> PALACE.Valley.OuterRim
  r131.connect(r114,None,lambda s:(s.has('Wings', p) or (s.has_all(['Bubble', 'Double Jump'], p) and o.bubble_jump.value >= 1)))
  # PALACE.Valley.ObservatorySlideEnd -> PALACE.Valley.ObservatoryPlatform
  r132.connect(r128,None,None)
  # PALACE.DiningRoom.Main -> PALACE.DiningRoom.InitialPlatforms
  r133.connect(r134,None,lambda s:(s.has('Raise Dining Room Platform', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Wings', 'Bubble'], p) and o.bubble_jump.value == 2)))))
  # PALACE.DiningRoom.InitialPlatforms -> PALACE.DiningRoom.Chandelier
  r134.connect(r135,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'Sprint'], p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # PALACE.DiningRoom.Chandelier -> PALACE.DiningRoom.Main
  r135.connect(r133,None,None)
  # PALACE.Valley.PalaceTop -> PALACE.Valley.OuterRim
  r136.connect(r114,None,lambda s:(s.has_any(['Wings', 'Double Jump', 'Sprint'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # PALACE.Sanctum.ValleyEntryway -> PALACE.Sanctum.BubbleClimb
  r137.connect(r138,None,None)
  # PALACE.Sanctum.BubbleClimb -> PALACE.Sanctum.Main
  r138.connect(r139,None,lambda s:s.has("Open Heaven's Path Exit", p))
  # PALACE.Sanctum.BubbleClimb -> PALACE.Sanctum.ValleyEntryway
  r138.connect(r137,None,lambda s:(s.has('Swim', p) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish", "Mr. Kerrington's Wings"} or s.has_any(['Sprint', 'Double Jump', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))))
  # PALACE.Sanctum.Main -> PALACE.Sanctum.BubbleClimb
  r139.connect(r138,None,lambda s:s.has("Open Heaven's Path Exit", p))
  # PALACE.Sanctum.Main -> PALACE.Sanctum.PalaceEntryway
  r139.connect(r140,None,lambda s:s.has('Swim', p))
  # PALACE.Sanctum.Main -> PALACE.Sanctum.RaceStart
  r139.connect(r153,None,lambda s:(s.has_all(["Open Heaven's Path Race Entrance", 'Swim'], p) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or s.has('Sprint', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['High Jump', 'Wings', 'Double Jump'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and o.ability_toggle.value == 1))))
  # PALACE.Sanctum.PalaceEntryway -> PALACE.Sanctum.Main
  r140.connect(r139,None,None)
  # PALACE.Palace.SanctumEntryway -> PALACE.Palace.Main
  r141.connect(r142,None,lambda s:s.has('Disable Prismic Palace Seedragons', p))
  # PALACE.Palace.Main -> PALACE.Palace.BubbleConchRoom
  r142.connect(r143,None,lambda s:s.has('Open Bubble Conch Room', p))
  # PALACE.Palace.Main -> PALACE.Palace.SanctumEntryway
  r142.connect(r141,None,lambda s:s.has('Disable Prismic Palace Seedragons', p))
  # PALACE.Palace.Main -> PALACE.Palace.SentryControlRoom
  r142.connect(r145,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', 'Bubble Conch', "Shelnert's Fish"} or s.has_any(['Disable Prismic Palace Seedragons', 'Sprint'], p)))
  # PALACE.Palace.BubbleConchRoom -> PALACE.Palace.BubbleConchRoomHighShrooms
  r143.connect(r144,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings", 'Bubble Conch', "Shelnert's Fish"} or s.has_any(['Sprint', 'Double Jump', 'Wings', 'Air Swim'], p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # PALACE.Palace.BubbleConchRoom -> PALACE.Palace.Main
  r143.connect(r142,None,lambda s:s.has('Open Bubble Conch Room', p))
  # PALACE.Palace.BubbleConchRoomHighShrooms -> PALACE.Palace.BubbleConchRoom
  r144.connect(r143,None,None)
  # PALACE.Palace.SentryControlRoom -> PALACE.Palace.Main
  r145.connect(r142,None,lambda s:(s._cavernofdreams_carrying[p]=='Bubble Conch' or s.has_any(['Disable Prismic Palace Seedragons', 'Sprint'], p)))
  # PALACE.Valley.UpperWater -> PALACE.Valley.Main
  r146.connect(r113,None,lambda s:s.has('Unfreeze Prismic Palace', p))
  # PALACE.Valley.UpperWater -> PALACE.Valley.GobblerCave
  r146.connect(r147,None,lambda s:s.has('Snooze Gobbler', p))
  # PALACE.Valley.UpperWater -> PALACE.Valley.JesterBootsCove
  r146.connect(r116,None,lambda s:s.has('Unfreeze Prismic Palace', p))
  # PALACE.Valley.UpperWater -> PALACE.Valley.JesterBootsCoveLowerPlatforms
  r146.connect(r118,None,lambda s:(s.has('Unfreeze Prismic Palace', p) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or s.has('Sprint', p))))
  # PALACE.Valley.UpperWater -> PALACE.Valley.JesterBootsCoveFloatingPoms
  r146.connect(r115,None,lambda s:(s._cavernofdreams_carrying[p]=='Bubble Conch' and s.has('Unfreeze Prismic Palace', p)))
  # PALACE.Valley.UpperWater -> PALACE.Valley.BreakLowerWaterWall
  r146.connect(r150,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or (s.has('Roll', p) and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # PALACE.Valley.UpperWater -> PALACE.Valley.LowerWater
  r146.connect(r148,None,lambda s:(s.has_any(['PALACE.Valley.BrokeLowerWaterWall', 'Open Palace-Lostleaf Connector'], p)))
  # PALACE.Valley.GobblerCave -> PALACE.Valley.UpperWater
  r147.connect(r146,None,lambda s:s.has('Snooze Gobbler', p))
  # PALACE.Valley.GobblerCave -> PALACE.Valley.LowerWater
  r147.connect(r148,None,lambda s:s.has('Open Gobbler Cave', p))
  # PALACE.Valley.LowerWater -> PALACE.Valley.UpperWater
  r148.connect(r146,None,lambda s:(s.has_any(['PALACE.Valley.BrokeLowerWaterWall', 'Open Palace-Lostleaf Connector'], p)))
  # PALACE.Valley.LowerWater -> PALACE.Valley.BigstarCave
  r148.connect(r149,None,lambda s:s.has('Open Bigstar Cave', p))
  # PALACE.Valley.LowerWater -> PALACE.Valley.GobblerCave
  r148.connect(r147,None,lambda s:s.has('Open Gobbler Cave', p))
  # PALACE.Valley.LowerWater -> PALACE.Valley.BreakLowerWaterWall
  r148.connect(r150,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # PALACE.Valley.BigstarCave -> PALACE.Valley.UpperWater
  r149.connect(r146,None,lambda s:s.has('PALACE.Valley.UnstuckBigstar', p))
  # PALACE.Valley.BigstarCave -> PALACE.Valley.LowerWater
  r149.connect(r148,None,lambda s:s.has('Open Bigstar Cave', p))
  # PALACE.Palace.Basement -> PALACE.Palace.BasementEggPlatform
  r151.connect(r152,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has('PALACE.Palace.KnockedPillarsDown', p) and (s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and (s.has('Wings', p) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Horn', 'Bubble'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and o.z_target.value == 1 and o.bubble_jump.value == 2) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and ((o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Bubble', p) and o.bubble_jump.value == 2 and o.z_target.value == 1))) or (s.has('Wings', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # PALACE.Palace.BasementEggPlatform -> PALACE.Palace.Basement
  r152.connect(r151,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has('PALACE.Palace.KnockedPillarsDown', p) and (s.has('Double Jump', p) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and ((s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Horn', 'Bubble'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and o.z_target.value == 1 and o.bubble_jump.value == 2) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and ((o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Wings', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or o.ability_toggle.value == 1))))))
  # PALACE.Sanctum.RaceStart -> PALACE.Sanctum.Main
  r153.connect(r139,None,None)
  # PALACE.Valley.ClipIntoIce -> PALACE.Valley.PalaceTop
  r154.connect(r136,None,lambda s:o.ejection_launch.value == 1)
  # PALACE.Valley.ClipIntoIce -> PALACE.Valley.OuterRim
  r154.connect(r114,None,lambda s:o.ejection_launch.value == 1)
  # PALACE.Valley.ClipIntoIce -> PALACE.Valley.UpperWater
  r154.connect(r146,None,None)
  # PALACE.Valley.PoolCardLedge -> PALACE.Valley.Main
  r155.connect(r113,None,None)
  # PALACE.Valley.Pool -> PALACE.Valley.Main
  r156.connect(r113,None,None)
  # PALACE.Valley.Pool -> PALACE.Valley.PoolCardLedge
  r156.connect(r155,None,lambda s:((s.has('Unfreeze Prismic Palace', p) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or (s.has_all(['Sprint', 'Double Jump'], p)))) or (s.has_all(['Sprint', 'Double Jump', 'Wings'], p)) or ((s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"}) and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # CAVE.MoonCavern.LavaMushroomPlatform -> CAVE.MoonCavern.NightmareLobbyDoorway
  r157.connect(r158,None,None)
  # CAVE.MoonCavern.LavaMushroomPlatform -> CAVE.MoonCavern.Main
  r157.connect(r102,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['High Jump', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value == 2 and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s._cavernofdreams_carrying[p] is None and o.damage_boost.value == 1 and (o.difficulty.value >= 2 or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))))
  # CAVE.MoonCavern.NightmareLobbyDoorway -> CAVE.MoonCavern.LavaMushroomPlatform
  r158.connect(r157,None,None)
  # LAKE.LostleafLake.TreehouseBranches -> LAKE.LostleafLake.Main
  r159.connect(r91,None,None)
  # LAKE.LostleafLake.TreehouseBranches -> LAKE.LostleafLake.PrestonLedge
  r159.connect(r160,None,None)
  # LAKE.LostleafLake.TreehouseBranches -> LAKE.LostleafLake.BigAppleLedge
  r159.connect(r161,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # LAKE.LostleafLake.TreehouseBranches -> LAKE.LostleafLake.TreehouseFrontEntry
  r159.connect(r163,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and s.has('High Jump', p)) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Double Jump', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # LAKE.LostleafLake.PrestonLedge -> LAKE.LostleafLake.Main
  r160.connect(r91,None,None)
  # LAKE.LostleafLake.PrestonLedge -> LAKE.LostleafLake.TreehouseBranches
  r160.connect(r159,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or o.ejection_launch.value == 1))
  # LAKE.LostleafLake.BigAppleLedge -> LAKE.LostleafLake.TreehouseBranches
  r161.connect(r159,None,None)
  # LAKE.LostleafLake.BigAppleLedge -> LAKE.LostleafLake.WinkyTreeLedge
  r161.connect(r162,None,None)
  # LAKE.LostleafLake.BigAppleLedge -> LAKE.LostleafLake.TreehouseFrontEntry
  r161.connect(r163,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or (s.has('Wings', p) and (s.has('Sprint', p) or (s.has('Bubble', p) and o.bubble_jump.value == 2)))))
  # LAKE.LostleafLake.BigAppleLedge -> LAKE.LostleafLake.WaterfallCanopy
  r161.connect(r167,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # LAKE.LostleafLake.BigAppleLedge -> LAKE.LostleafLake.CryptCanopy
  r161.connect(r171,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['LAKE.LostleafLake.BigAppleLedgeSoil', 'Climb', 'Double Jump', 'Wings'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # LAKE.LostleafLake.WinkyTreeLedge -> LAKE.LostleafLake.Main
  r162.connect(r91,None,None)
  # LAKE.LostleafLake.WinkyTreeLedge -> LAKE.LostleafLake.BigAppleLedge
  r162.connect(r161,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('High Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Double Jump', p) and (s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # LAKE.LostleafLake.TreehouseFrontEntry -> LAKE.LostleafLake.TreehouseBranches
  r163.connect(r159,None,None)
  # LAKE.LostleafLake.TreehouseFrontEntry -> LAKE.LostleafLake.TreehouseBackEntry
  r163.connect(r164,None,lambda s:s._cavernofdreams_carrying[p]=='Jester Boots')
  # LAKE.LostleafLake.TreehouseFrontEntry -> LAKE.LostleafLake.TreehouseRoof
  r163.connect(r166,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or o.ejection_launch.value == 1 or (s.has_all(['Horn', 'Double Jump', 'Wings'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.difficulty.value >= 1 and ((s.has_all(['High Jump', 'Double Jump'], p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))))
  # LAKE.LostleafLake.TreehouseBackEntry -> LAKE.LostleafLake.Main
  r164.connect(r91,None,None)
  # LAKE.LostleafLake.TreehouseBackEntry -> LAKE.LostleafLake.TreehouseFrontEntry
  r164.connect(r163,None,lambda s:s._cavernofdreams_carrying[p]=='Jester Boots')
  # LAKE.LostleafLake.TreehouseBackEntry -> LAKE.LostleafLake.BigAppleLedge
  r164.connect(r161,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots'))
  # LAKE.LostleafLake.TreehouseBackEntry -> LAKE.LostleafLake.TreehouseBranches
  r164.connect(r159,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Wings', p)))
  # LAKE.LostleafLake.TreehouseRoof -> LAKE.LostleafLake.TreehouseFrontEntry
  r166.connect(r163,None,None)
  # LAKE.LostleafLake.TreehouseRoof -> LAKE.LostleafLake.TreehouseBackEntry
  r166.connect(r164,None,None)
  # LAKE.LostleafLake.TreehouseRoof -> LAKE.LostleafLake.BigAppleLedge
  r166.connect(r161,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has('Wings', p)))
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.DeepWoods
  r167.connect(r168,None,None)
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.DeepWoodsPuzzleEgg
  r167.connect(r169,None,None)
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.OuterRim
  r167.connect(r92,None,None)
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.DucklingsLedge
  r167.connect(r96,None,None)
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.Main
  r167.connect(r91,None,None)
  # LAKE.LostleafLake.WaterfallCanopy -> LAKE.LostleafLake.CryptCanopy
  r167.connect(r171,None,lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p) or (o.difficulty.value >= 2 and ((s.has_all(['Roll', 'Double Jump'], p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))) or (s.has_all(['Roll', 'Sprint', 'Bubble'], p) and o.bubble_jump.value >= 1)))
  # LAKE.LostleafLake.DeepWoods -> LAKE.LostleafLake.Main
  r168.connect(r91,None,lambda s:s.has('Open Deep Woods', p))
  # LAKE.LostleafLake.DeepWoods -> LAKE.LostleafLake.DeepWoodsPuzzleEgg
  r168.connect(r169,None,lambda s:s.has('Lower Deep Woods Egg', p))
  # LAKE.LostleafLake.DeepWoods -> LAKE.LostleafLake.DeepDeepWoods
  r168.connect(r170,None,lambda s:not (s._cavernofdreams_carrying[p]=='Jester Boots'))
  # LAKE.LostleafLake.DeepWoodsPuzzleEgg -> LAKE.LostleafLake.DeepWoods
  r169.connect(r168,None,None)
  # LAKE.LostleafLake.DeepDeepWoods -> LAKE.LostleafLake.DeepWoods
  r170.connect(r168,None,lambda s:not (s._cavernofdreams_carrying[p]=='Jester Boots'))
  # LAKE.LostleafLake.CryptCanopy -> LAKE.LostleafLake.BigAppleLedge
  r171.connect(r161,None,None)
  # LAKE.LostleafLake.CryptCanopy -> LAKE.LostleafLake.OuterRim
  r171.connect(r92,None,None)
  # LAKE.LostleafLake.CryptCanopy -> LAKE.LostleafLake.CryptBackLedge
  r171.connect(r172,None,None)
  # LAKE.LostleafLake.CryptBackLedge -> LAKE.LostleafLake.OverCryptBackFence
  r172.connect(r173,None,lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has_all(['LAKE.LostleafLake.CryptSoil', 'Climb'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # LAKE.LostleafLake.OverCryptBackFence -> LAKE.LostleafLake.CryptCanopy
  r173.connect(r171,None,lambda s:(o.out_of_bounds.value == 1 and o.ejection_launch.value == 1 and (s.has('Wings', p) or o.difficulty.value >= 1 or (s.has('Bubble', p) and o.bubble_jump.value >= 1))))
  # LAKE.LostleafLake.OverCryptBackFence -> LAKE.LostleafLake.OuterRim
  r173.connect(r92,None,lambda s:(o.out_of_bounds.value == 1 and (s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.z_target.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s.has_any(['Swim', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))))))
  # LAKE.Crypt.BackExit -> LAKE.Crypt.LeftPlatform
  r174.connect(r175,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or s.has('LAKE.Crypt.BrokeBackExitWithHorn', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # LAKE.Crypt.LeftPlatform -> LAKE.Crypt.Main
  r175.connect(r176,None,None)
  # LAKE.Crypt.LeftPlatform -> LAKE.Crypt.BackExit
  r175.connect(r174,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or s.has('LAKE.Crypt.BrokeBackExitWithHorn', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # LAKE.Crypt.LeftPlatform -> LAKE.Crypt.EggPlatform
  r175.connect(r178,None,lambda s:(s.has_any(['Wings', 'Double Jump', 'Roll', 'Sprint'], p) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # LAKE.Crypt.LeftPlatform -> LAKE.Crypt.TimedPlatform
  r175.connect(r179,None,lambda s:s.has('LAKE.Crypt.PrestonAccess', p))
  # LAKE.Crypt.Main -> LAKE.Crypt.RightPlatform
  r176.connect(r177,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('Double Jump', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('High Jump', p) and (s.has('Wings', p) or o.difficulty.value >= 1 or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (o.wing_storage.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))))
  # LAKE.Crypt.Main -> LAKE.Crypt.LeftPlatform
  r176.connect(r175,None,lambda s:((s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has_all(['Wings', 'Bubble'], p) and o.bubble_jump.value == 2) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Double Jump', p) and (s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has('Bubble', p) and (s.has_any(['Double Jump', 'High Jump'], p)) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # LAKE.Crypt.RightPlatform -> LAKE.Crypt.EggPlatform
  r177.connect(r178,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # LAKE.Crypt.RightPlatform -> LAKE.Crypt.TimedPlatform
  r177.connect(r179,None,lambda s:(s.has('LAKE.Crypt.PrestonAccess', p) and (s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['High Jump', 'Double Jump'], p)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))
  # LAKE.Crypt.EggPlatform -> LAKE.Crypt.TimedPlatform
  r178.connect(r179,None,lambda s:s.has('LAKE.Crypt.PrestonAccess', p))
  # LAKE.Crypt.EggPlatform -> LAKE.Crypt.LeftPlatform
  r178.connect(r175,None,lambda s:(s.has_any(['Wings', 'Double Jump', 'Sprint'], p) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)))
  # LAKE.Crypt.EggPlatform -> LAKE.Crypt.BackExit
  r178.connect(r174,None,lambda s:(s._cavernofdreams_carrying[p] is None and o.out_of_bounds.value == 1 and o.ejection_launch.value == 1 and o.damage_boost.value == 1 and o.z_target.value == 1 and ((s.has('Double Jump', p) and o.difficulty.value >= 1 and o.momentum_cancel.value == 1 and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (o.difficulty.value >= 2 and (s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))))
  # LAKE.Crypt.TimedPlatform -> LAKE.Crypt.EggPlatform
  r179.connect(r178,None,None)
  # LAKE.Crypt.TimedPlatform -> LAKE.Crypt.LeftPlatform
  r179.connect(r175,None,None)
  # LAKE.Crypt.TimedPlatform -> LAKE.Crypt.RightPlatform
  r179.connect(r177,None,None)
  # LAKE.Crypt.TimedPlatform -> LAKE.Crypt.Main
  r179.connect(r176,None,None)
  # LAKE.LostleafLake.InsideCrypt -> LAKE.LostleafLake.TeepeeIsland
  r180.connect(r93,None,lambda s:s.has('Open Crypt', p))
  # LAKE.LostleafLake.BellTower -> LAKE.LostleafLake.OuterRim
  r181.connect(r92,None,lambda s:((s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value == 2) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  # LAKE.LostleafLake.BellTower -> LAKE.LostleafLake.RingBell
  r181.connect(r182,None,lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # LAKE.LostleafLake.BellTower -> LAKE.LostleafLake.Main
  r181.connect(r91,None,None)
  # LAKE.LostleafLake.InsideChurch -> LAKE.LostleafLake.Lake
  r183.connect(r94,None,lambda s:s.has('Swim', p))
  # LAKE.Church.Main -> LAKE.Church.Basement
  r184.connect(r185,None,lambda s:s.has('Open Church Basement', p))
  # LAKE.Church.Basement -> LAKE.Church.Main
  r185.connect(r184,None,None)
  # LAKE.LostleafLake.WaterfallEggCave -> LAKE.LostleafLake.Main
  r186.connect(r91,None,None)
  # LAKE.LostleafLake.LakeStump -> LAKE.LostleafLake.Main
  r189.connect(r91,None,None)
  # LAKE.LostleafLake.LakeStump -> LAKE.LostleafLake.TeepeeIsland
  r189.connect(r93,None,lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (o.difficulty.value >= 1 and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has('Double Jump', p) or (o.momentum_cancel.value == 1 and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))))) or (o.difficulty.value >= 2 and ((s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))))
  # CAVE.Rainbow.Well -> CAVE.Rainbow.Main
  r190.connect(r191,None,None)
  # CAVE.Rainbow.Main -> CAVE.Rainbow.MoonLedges
  r191.connect(r192,None,lambda s:((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Double Jump', p) and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  # CAVE.Rainbow.Main -> CAVE.Rainbow.Well
  r191.connect(r190,None,lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has('Double Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Sprint', 'Roll'], p)) or (s.has('High Jump', p) and o.momentum_cancel.value == 1)))
  # CAVE.Rainbow.MoonLedges -> CAVE.Rainbow.Main
  r192.connect(r191,None,None)
  # CAVE.Rainbow.MoonLedges -> CAVE.Rainbow.Well
  r192.connect(r190,None,None)
  # CAVE.Rainbow.MoonLedges -> CAVE.Rainbow.ShroomLedges
  r192.connect(r193,None,lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['Bubble', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and (s.has_any(['Sprint', 'Double Jump'], p) or (s.has('High Jump', p) and o.momentum_cancel.value == 1))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.difficulty.value >= 2) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has('Wings', p) or o.momentum_cancel.value == 1))))
  # CAVE.Rainbow.ShroomLedges -> CAVE.Rainbow.Main
  r193.connect(r191,None,None)
  # CAVE.Rainbow.ShroomLedges -> CAVE.Rainbow.Topside
  r193.connect(r194,None,lambda s:((s._cavernofdreams_carrying[p]=='Jester Boots' and o.difficulty.value >= 2) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or s.has('Double Jump', p) or (s.has_all(['High Jump', 'Double Jump'], p) and o.momentum_cancel.value == 1) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Bubble', p) and o.z_target.value == 1 and o.bubble_jump.value >= 1)))
  # CAVE.Rainbow.Topside -> CAVE.Rainbow.Main
  r194.connect(r191,None,None)
  # GALLERY.Drown.Main -> GALLERY.Drown.BubbleConchPipe
  r195.connect(r196,None,lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', 'Apple'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  # GALLERY.Drown.BubbleConchPipe -> GALLERY.Drown.Main
  r196.connect(r195,None,None)
  # CAVE.SunCavern.HighJumpLedge -> CAVE.SunCavern.Main
  r197.connect(r0,None,None)
  # CAVE.SunCavern.VineLedge -> CAVE.SunCavern.Main
  r198.connect(r0,None,None)
  # CAVE.SunCavern.VineLedge -> CAVE.SunCavern.HighJumpLedge
  r198.connect(r197,None,lambda s:((o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))) or (s.has('Roll', p) and (s.has('Sprint', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))))
  # CAVE.SunCavern.TailSpinLedge -> CAVE.SunCavern.Main
  r199.connect(r0,None,None)
  l=L(p,'Fed Lostleaf Lake Fella',None,r0)
  l.access_rule=lambda s:(s._cavernofdreams_has_shrooms_for(p,'Lake') and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  r0.locations.append(l)
  l=L(p,'Fed Airborne Armada Fella',None,r0)
  l.access_rule=lambda s:(s._cavernofdreams_has_shrooms_for(p,'Monster') and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  r0.locations.append(l)
  l=L(p,'Fed Prismic Palace Fella',None,r0)
  l.access_rule=lambda s:(s._cavernofdreams_has_shrooms_for(p,'Palace') and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  r0.locations.append(l)
  l=L(p,'Fed Gallery of Nightmares Fella',None,r0)
  l.access_rule=lambda s:(s._cavernofdreams_has_shrooms_for(p,'Gallery') and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  r0.locations.append(l)
  l=L(p,'Whack Mighty Wall',None,r90)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  r90.locations.append(l)
  l=L(p,'Armada Lobby Purple Valve',None,r2)
  l.access_rule=lambda s:(((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r2.locations.append(l)
  l=L(p,'Armada Lobby Green Valve',None,r2)
  l.access_rule=lambda s:(((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r2.locations.append(l)
  l=L(p,'Palace Lobby Faucet Preston',None,r110)
  r110.locations.append(l)
  l=L(p,'Palace Lobby Whirlpool Preston',None,r109)
  r109.locations.append(l)
  l=L(p,'Gallery Lobby - Extinguish Torches',None,r81)
  l.access_rule=lambda s:s.has('Bubble', p)
  r81.locations.append(l)
  l=L(p,'Gallery Lobby - Hedge Maze Preston',None,r84)
  r84.locations.append(l)
  l=L(p,'Lostleaf Lake - Winky Tree Target',None,r91)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and (s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('High Jump', p) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (s.has_all(['Double Jump', 'Horn'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r91.locations.append(l)
  l=L(p,'Lostleaf Lake - Help Shelnert',None,r91)
  l.access_rule=lambda s:s.has('Fish Food', p)
  r91.locations.append(l)
  l=L(p,'Lostleaf Lake - Back of the Headstone',None,r94)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r94.locations.append(l)
  l=L(p,'Lostleaf Lake - Ring Bell',None,r182)
  r182.locations.append(l)
  l=L(p,'Church - Angel Statue Puzzle',None,r184)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  r184.locations.append(l)
  l=L(p,'Lostleaf Lake - Treehouse Preston',None,r160)
  r160.locations.append(l)
  l=L(p,'Lostleaf Lake - Tree Puzzle',None,r168)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r168.locations.append(l)
  l=L(p,"Kerrington - Soothe Mr. Kerrington's Boils",None,r22)
  l.access_rule=lambda s:(s.has_all(['MONSTER.Kerrington.MainBoils', 'MONSTER.Kerrington.GreenBoil'], p))
  r22.locations.append(l)
  l=L(p,'Kerrington - Generators Puzzle',None,r22)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Horn', 'MONSTER.Kerrington.HornOnAnnoyingGenerator'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r22.locations.append(l)
  l=L(p,'Heart - Generators Puzzle',None,r27)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has_all(['Horn', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r27.locations.append(l)
  l=L(p,'Kerrington - Race',None,r22)
  l.access_rule=lambda s:(s.has('Free Armada Buddies', p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))
  r22.locations.append(l)
  l=L(p,'Kerrington - Medicine Pool Preston',None,r21)
  r21.locations.append(l)
  l=L(p,'Prismic Palace - Basement Star Hoops',None,r148)
  r148.locations.append(l)
  l=L(p,'Palace-Lostleaf Connector - Preston',None,r148)
  r148.locations.append(l)
  l=L(p,'Prismic Palace - Angel Statue Puzzle',None,r146)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r146.locations.append(l)
  l=L(p,'Prismic Palace - Help Lady Opal',None,r113)
  l.access_rule=lambda s:(s.has_all(["Lady Opal's Egg 1", "Lady Opal's Egg 2", "Lady Opal's Egg 3"], p))
  r113.locations.append(l)
  l=L(p,'Prismic Palace - Snowcastle Preston',None,r123)
  r123.locations.append(l)
  l=L(p,'Prismic Palace - Observatory Preston',None,r128)
  r128.locations.append(l)
  l=L(p,'Prismic Palace - Bigstar Preston',None,r149)
  r149.locations.append(l)
  l=L(p,'Prismic Palace - Gobbler Preston',None,r147)
  r147.locations.append(l)
  l=L(p,'Prismic Palace - Feed Gobbler',None,r146)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  r146.locations.append(l)
  l=L(p,'Palace Interior - Sentry Control Preston',None,r145)
  r145.locations.append(l)
  l=L(p,'Palace Interior - Seastar Puzzle',None,r142)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  r142.locations.append(l)
  l=L(p,"Heaven's Path - Finished Race",None,r153)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Bubble Conch' or s.has('Sprint', p))
  r153.locations.append(l)
  l=L(p,"Heaven's Path - Bottom Preston",None,r139)
  l.access_rule=lambda s:s.has('Swim', p)
  r139.locations.append(l)
  l=L(p,'Palace Dining Room - Preston',None,r133)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  r133.locations.append(l)
  l=L(p,'Observatory - Telescope Puzzle',None,r130)
  r130.locations.append(l)
  l=L(p,"Gallery of Nightmares - Sage's Painting",None,r51)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=="Sage's Gloves"
  r51.locations.append(l)
  l=L(p,"Gallery of Nightmares - Mr. Kerrington's Painting",None,r56)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings"
  r56.locations.append(l)
  l=L(p,"Gallery of Nightmares - Shelnert's Painting",None,r65)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=="Shelnert's Fish"
  r65.locations.append(l)
  l=L(p,'Gallery-Armada Connector - Preston',None,r70)
  r70.locations.append(l)
  l=L(p,'Gallery of Nightmares - Swamp Angel Statue Puzzle',None,r65)
  l.access_rule=lambda s:(s.has_all(['GALLERY.EarthLobby.RealignMainStatue', 'GALLERY.EarthLobby.RealignDragonHeadStatue', 'GALLERY.EarthLobby.RealignCoffinsStatue'], p))
  r65.locations.append(l)
  l=L(p,'Gallery of Nightmares - Sewer Angel Statue Puzzle',None,r46)
  l.access_rule=lambda s:((s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['GALLERY.WaterLobby.AirSwimFromSpooky', 'GALLERY.WaterLobby.AirSwimFromMain', 'High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))) and (s._cavernofdreams_carrying[p] in {'Bubble Conch', 'Apple'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  r46.locations.append(l)
  l=L(p,"Gallery of Nightmares - Lady Opal's Painting",None,r49)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=="Lady Opal's Head"
  r49.locations.append(l)
  l=L(p,'Gallery of Nightmares - Helped Sniffles',None,r78)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p))
  r78.locations.append(l)
  l=L(p,'Gallery of Nightmares - Fire Lobby Preston',None,r60)
  r60.locations.append(l)
  l=L(p,'Gallery of Nightmares - Fire Lobby Hoops',None,r53)
  l.access_rule=lambda s:(s.has('GALLERY.FireLobby.DouseRaceFlame', p) and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)))
  r53.locations.append(l)
  l=L(p,'Coils of Agony - Hidden Pillar',None,r57)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', 'Apple'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r57.locations.append(l)
  l=L(p,'Gallery of Nightmares - Moisten Wastes of Eternity Painting',None,r66)
  l.access_rule=lambda s:s.has('Bubble', p)
  r66.locations.append(l)
  l=L(p,'Egg: Sun Cavern - Mighty Wall',None,r90)
  r90.locations.append(l)
  l=L(p,'Egg: Sun Cavern - Waterfall',None,r98)
  r98.locations.append(l)
  l=L(p,'Egg: Moon Cavern - Dive Puzzle',None,r104)
  l.access_rule=lambda s:s.has('CAVE.MoonCavern.SolvedDivePuzzle', p)
  r104.locations.append(l)
  l=L(p,'Egg: Moon Cavern - Keehee Climb',None,r107)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has_all(['Climb', 'Wings'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has('High Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))
  r107.locations.append(l)
  l=L(p,'Egg: Lostleaf Lobby - Branches',None,r89)
  r89.locations.append(l)
  l=L(p,'Egg: Armada Lobby - Cannon',None,r8)
  r8.locations.append(l)
  l=L(p,'Egg: Palace Lobby - Submerged',None,r109)
  r109.locations.append(l)
  l=L(p,'Egg: Gallery Lobby - Lostleaf Lobby Entryway',None,r85)
  r85.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Entry Stump',None,r91)
  r91.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Jester Boots',None,r170)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or (s.has('LAKE.LostleafLake.DeepDeepWoodsSoil', p) and (s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))))
  r170.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Lake Log',None,r94)
  r94.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Waterfall',None,r186)
  r186.locations.append(l)
  l=L(p,"Egg: Crypt - Shelwart's Gravestone",None,r178)
  l.access_rule=lambda s:(((s.has('Bubble', p) or o.difficulty.value >= 1) and (s.has_any(['Double Jump', 'High Jump'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and (s.has('Double Jump', p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r178.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Deep Woods Puzzle',None,r169)
  r169.locations.append(l)
  l=L(p,'Egg: Lostleaf Lake - Near the Treehouse',None,r159)
  r159.locations.append(l)
  l=L(p,'Egg: Church - Below the Angel Statues',None,r185)
  r185.locations.append(l)
  l=L(p,"Egg: Airborne Armada - Mr. Kerrington's Tail",None,r14)
  r14.locations.append(l)
  l=L(p,'Egg: Fire Drone',None,r17)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p))
  r17.locations.append(l)
  l=L(p,'Egg: Kerrington - Slide',None,r37)
  r37.locations.append(l)
  l=L(p,'Egg: Kerrington - Dog Food',None,r13)
  r13.locations.append(l)
  l=L(p,'Egg: Kerrington - Boiler',None,r33)
  l.access_rule=lambda s:s.has('Swim', p)
  r33.locations.append(l)
  l=L(p,'Egg: Kerrington - Pipe',None,r22)
  r22.locations.append(l)
  l=L(p,"Egg: Mr. Kerrington's Heart",None,r27)
  l.access_rule=lambda s:(s.has("Unclog Kerrington's Heart", p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))
  r27.locations.append(l)
  l=L(p,'Egg: Kerrington - Dumpling',None,r34)
  l.access_rule=lambda s:(s.has_all(['Free Armada Buddies', 'Swim'], p))
  r34.locations.append(l)
  l=L(p,'Egg: Prismic Palace - Snowcastle',None,r116)
  l.access_rule=lambda s:s.has('Open Prismic Palace Snowcastle', p)
  r116.locations.append(l)
  l=L(p,'Egg: Palace Dining Room',None,r135)
  r135.locations.append(l)
  l=L(p,'Egg: Observatory',None,r130)
  l.access_rule=lambda s:s.has('Reveal Observatory Item', p)
  r130.locations.append(l)
  l=L(p,'Egg: Prismic Palace - Observatory Slide',None,r132)
  r132.locations.append(l)
  l=L(p,'Egg: Prismic Palace - Bigstar',None,r149)
  r149.locations.append(l)
  l=L(p,'Egg: Prismic Palace - Top of the Palace',None,r136)
  r136.locations.append(l)
  l=L(p,'Egg: Palace Interior - Basement',None,r152)
  r152.locations.append(l)
  l=L(p,'Egg: Prismic Palace - Gobbler',None,r147)
  r147.locations.append(l)
  l=L(p,'Egg: Coils of Agony',None,r58)
  r58.locations.append(l)
  l=L(p,'Egg: Pits of Despair',None,r195)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  r195.locations.append(l)
  l=L(p,'Egg: Wastes of Eternity',None,r74)
  r74.locations.append(l)
  l=L(p,'Egg: Gallery of Nightmares - Matryoshka Egg',None,r51)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r51.locations.append(l)
  l=L(p,"Egg: Gallery of Nightmares - Skull's Eye",None,r65)
  l.access_rule=lambda s:s.has("Open Skull's Diamond Eye", p)
  r65.locations.append(l)
  l=L(p,'Egg: Gallery of Nightmares - Mr. Kerrington Painting',None,r56)
  l.access_rule=lambda s:s.has('Open Mr. Kerrington Painting Gate', p)
  r56.locations.append(l)
  l=L(p,'Egg: Gallery of Nightmares - Sewer',None,r69)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['High Jump', 'Double Jump', 'Wings'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))
  r69.locations.append(l)
  l=L(p,'Egg: Gallery of Nightmares - Deepest Darkness',None,r50)
  r50.locations.append(l)
  l=L(p,"Sun Cavern - Sage's Blessing 1",None,r0)
  l.access_rule=lambda s:s.has_group('Egg', p, 1)
  r0.locations.append(l)
  l=L(p,"Sun Cavern - Sage's Blessing 2",None,r0)
  l.access_rule=lambda s:s.has_group('Egg', p, 6)
  r0.locations.append(l)
  l=L(p,"Sun Cavern - Sage's Blessing 3",None,r0)
  l.access_rule=lambda s:s.has_group('Egg', p, 12)
  r0.locations.append(l)
  l=L(p,"Sun Cavern - Sage's Blessing 4",None,r0)
  l.access_rule=lambda s:s.has_group('Egg', p, 24)
  r0.locations.append(l)
  l=L(p,"Sun Cavern - Sage's Blessing 5",None,r0)
  l.access_rule=lambda s:s.has_group('Egg', p, 40)
  r0.locations.append(l)
  l=L(p,'Treehouse - Fish Food',None,r165)
  r165.locations.append(l)
  l=L(p,"Lady Opal's Egg: Castle",None,r126)
  r126.locations.append(l)
  l=L(p,"Lady Opal's Egg: Pool",None,r156)
  r156.locations.append(l)
  l=L(p,"Lady Opal's Egg: Poki-Poki",None,r127)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('PALACE.Valley.AirSwimFromLostleafEntryway', p) or (s.has_all(['Unfreeze Prismic Palace', 'Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1) or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2 and o.z_target.value == 1) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and (s.has_any(['Sprint', 'Double Jump', 'High Jump'], p) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p))))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Climb', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (s.has('Double Jump', p) and ((s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('High Jump', p) and o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))))
  r127.locations.append(l)
  l=L(p,'Card: Sun Cavern - Air Vent',None,r0)
  r0.locations.append(l)
  l=L(p,'Card: Lostleaf Lobby - Branches',None,r89)
  r89.locations.append(l)
  l=L(p,'Card: Moon Cavern - Statue',None,r107)
  r107.locations.append(l)
  l=L(p,'Card: Armada Lobby - Jester Boots',None,r2)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or (s.has('Bubble', p) and o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and o.bubble_jump.value == 2) or (s.has('Double Jump', p) and ((s.has('Wings', p) and o.ability_toggle.value == 1) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))) or (s.has('Bubble', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)) and o.z_target.value == 1 and o.bubble_jump.value >= 1 and ((s.has('Double Jump', p) and o.difficulty.value >= 1) or o.difficulty.value >= 2)))
  r2.locations.append(l)
  l=L(p,'Card: Moon Cavern - Dive',None,r102)
  l.access_rule=lambda s:(s.has_all(['Swim', 'Horn'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  r102.locations.append(l)
  l=L(p,'Card: Gallery Lobby - Hedge Maze',None,r83)
  r83.locations.append(l)
  l=L(p,'Card: Lostleaf Lake - Teepee',None,r93)
  r93.locations.append(l)
  l=L(p,'Card: Lostleaf Lake - Apple Tree',None,r91)
  r91.locations.append(l)
  l=L(p,'Card: Lostleaf Lake - Lake Stump',None,r189)
  r189.locations.append(l)
  l=L(p,'Card: Church - Top',None,r184)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or s.has('Sprint', p) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value == 2))) or (s._cavernofdreams_carrying[p]=='Jester Boots' and s.has_all(['Super Bubble Jump', 'Roll', 'Bubble', 'Roll'], p)))
  r184.locations.append(l)
  l=L(p,'Card: Lostleaf Lake - Entry',None,r91)
  r91.locations.append(l)
  l=L(p,'Card: Treehouse - Top',None,r165)
  r165.locations.append(l)
  l=L(p,'Card: Kerrington - Slide',None,r21)
  l.access_rule=lambda s:((o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and (s.has('High Jump', p) or (s.has('Bubble', p) and o.bubble_jump.value == 2))) or (s.has_all(['Horn', 'Double Jump'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and (s.has_any(['Double Jump', 'Wings'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1))) or (s.has('Wings', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))
  r21.locations.append(l)
  l=L(p,'Card: Kerrington - Pipe',None,r22)
  r22.locations.append(l)
  l=L(p,'Card: Airborne Armada - Broken Wing',None,r18)
  r18.locations.append(l)
  l=L(p,'Card: Airborne Armada - Behind Entry Drone',None,r10)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))
  r10.locations.append(l)
  l=L(p,'Card: Kerrington - Hammocks',None,r22)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Double Jump', 'Wings'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  r22.locations.append(l)
  l=L(p,"Card: Kerrington - Near Mr. Kerrington's Heart",None,r26)
  r26.locations.append(l)
  l=L(p,'Card: Observatory',None,r130)
  r130.locations.append(l)
  l=L(p,'Card: Prismic Palace - Top of Observatory',None,r131)
  r131.locations.append(l)
  l=L(p,'Card: Prismic Palace - Snowcastle',None,r116)
  r116.locations.append(l)
  l=L(p,'Card: Prismic Palace - Top of Palace',None,r125)
  r125.locations.append(l)
  l=L(p,'Card: Prismic Palace - Above Pool',None,r155)
  r155.locations.append(l)
  l=L(p,'Card: Prismic Palace - Inside Palace',None,r142)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', "Shelnert's Fish"} or (s.has('Sprint', p) and (s.has('Double Jump', p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))
  r142.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Swamp Castle',None,r65)
  r65.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Sewer Bottom',None,r42)
  r42.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Basement Entrance',None,r51)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {"Mr. Kerrington's Wings", 'Jester Boots'} or s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1 and (s.has_any(['Roll', 'High Jump', 'Sprint'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  r51.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Swamp',None,r64)
  r64.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Frying Pans',None,r53)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or ((s._cavernofdreams_carrying[p] is None or s.has('Bubble', p)) and ((s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))) or (s.has_all(['Horn', 'Bubble'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (s._cavernofdreams_carrying[p] is None and s.has('Bubble', p) and o.bubble_jump.value >= 1 and o.momentum_cancel.value == 1) or (s.has('Wings', p) and (s._cavernofdreams_carrying[p] in {'Medicine', None} or s.has('Bubble', p))))
  r53.locations.append(l)
  l=L(p,'Card: Gallery of Nightmares - Above Pits of Despair Painting',None,r44)
  l.access_rule=lambda s:(s.has('GALLERY.WaterLobby.AirSwimFromMain', p) or (s._cavernofdreams_carrying[p]=='Jester Boots' and (s.has_any(['High Jump', 'Double Jump'], p) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))))
  r44.locations.append(l)
  l=L(p,'Card: Sewer - Armada Lobby Side',None,r40)
  r40.locations.append(l)
  l=L(p,'Card: Sewer - Gallery of Nightmares Side',None,r41)
  r41.locations.append(l)
  l=L(p,'Card: Dream',None,r194)
  l.access_rule=lambda s:(s.has_any(['High Jump', 'Double Jump'], p) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})))
  r194.locations.append(l)
  l=L(p,'Card: Gallery Lobby - Behind the Gallery',None,r81)
  r81.locations.append(l)
  l=L(p,'Card: Palace Dining Room - Top',None,r135)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Jester Boots', "Mr. Kerrington's Wings"} or s.has_any(['Wings', 'Double Jump'], p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Roll', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)) and o.difficulty.value >= 2) or (s.has('Sprint', p) and o.difficulty.value >= 2))
  r135.locations.append(l)
  l=L(p,'Card: Palace Lobby - Top',None,r112)
  r112.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Ground 1',None,r0)
  r0.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Ground 2',None,r0)
  r0.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Ground 3',None,r0)
  r0.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Ground 4',None,r0)
  r0.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Egg Ledge 1',None,r90)
  r90.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Egg Ledge 2',None,r90)
  r90.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Mighty Wall Egg Ledge 3',None,r90)
  r90.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - High Jump Ledge 1',None,r197)
  r197.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - High Jump Ledge 2',None,r197)
  r197.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Tail Spin Ledge 1',None,r199)
  r199.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Tail Spin Ledge 2',None,r199)
  r199.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Ducklings Ledge 1',None,r100)
  r100.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Ducklings Ledge 2',None,r100)
  r100.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Armada Entrance 1',None,r1)
  r1.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Armada Entrance 2',None,r1)
  r1.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Armada Entrance 3',None,r1)
  r1.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Vine Ledge 1',None,r198)
  r198.locations.append(l)
  l=L(p,'Shroom: Sun Cavern - Vine Ledge 2',None,r198)
  r198.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 1',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 2',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 3',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 4',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 5',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Holes 6',None,r103)
  r103.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Puzzle 1',None,r105)
  r105.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Puzzle 2',None,r105)
  r105.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Dive Puzzle 3',None,r105)
  r105.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Potionfall',None,r102)
  r102.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lonely Shroom',None,r106)
  r106.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Pathway 2',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Pathway 1',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Pathway 3',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Statue 1',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Statue 2',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Entryway 1',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Entryway 2',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Palace Lobby Entryway 3',None,r107)
  r107.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Platforms 1',None,r102)
  r102.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Platforms 2',None,r102)
  r102.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Platforms 3',None,r102)
  r102.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Platforms 4',None,r102)
  r102.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Mushroom Platform 1',None,r157)
  r157.locations.append(l)
  l=L(p,'Shroom: Moon Cavern - Lava Mushroom Platform 2',None,r157)
  r157.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Bridge 2',None,r88)
  r88.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Bridge 3',None,r88)
  r88.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Bridge 1',None,r88)
  r88.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Trees 1',None,r89)
  r89.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Trees 2',None,r89)
  r89.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lobby - Trees 3',None,r89)
  r89.locations.append(l)
  l=L(p,'Shroom: Armada Lobby - Cliffside 1',None,r2)
  r2.locations.append(l)
  l=L(p,'Shroom: Armada Lobby - Cliffside 2',None,r2)
  r2.locations.append(l)
  l=L(p,'Shroom: Armada Lobby - Cliffside 4',None,r2)
  r2.locations.append(l)
  l=L(p,'Shroom: Armada Lobby - Cliffside 5',None,r2)
  r2.locations.append(l)
  l=L(p,'Shroom: Armada Lobby - Cliffside 3',None,r2)
  r2.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 1',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 6',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 5',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 3',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 2',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Ledges 4',None,r111)
  r111.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 1',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 2',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 3',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 5',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 6',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Palace Lobby - Underwater 4',None,r109)
  r109.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Fountain 1',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Fountain 2',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Fountain 3',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Fountain 4',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Castle Hill 3',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Castle Hill 5',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Castle Hill 4',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Castle Hill 1',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Castle Hill 2',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Entryway 1',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Entryway 4',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Entryway 5',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Entryway 3',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Gallery Lobby - Entryway 2',None,r81)
  r81.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 4',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 3',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 1',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 2',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 6',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Treehouse Branches 5',None,r159)
  r159.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 2',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 1',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 3',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 6',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 4',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods 5',None,r170)
  r170.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Behind Church 3',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Behind Church 1',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Behind Church 2',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Teepee 1',None,r93)
  r93.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Teepee 3',None,r93)
  r93.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Teepee 2',None,r93)
  r93.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Waterfall Logs 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Waterfall Logs 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Waterfall Logs 4',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Waterfall Logs 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Logs 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Logs 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Logs 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Logs 4',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Bouncy Mushroom 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Bouncy Mushroom 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Bouncy Mushroom 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Ramp to Winky Tree 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Ramp to Winky Tree 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Ramp to Winky Tree 5',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Ramp to Winky Tree 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Ramp to Winky Tree 4',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods Entryway 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods Entryway 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Deep Woods Entryway 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Gravestone 1',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Gravestone 2',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Lake Gravestone 3',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Bridge 2',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Bridge 1',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Bridge 3',None,r91)
  r91.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Apple Tree 4',None,r162)
  r162.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Apple Tree 3',None,r162)
  r162.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Apple Tree 1',None,r162)
  r162.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Winky Apple Tree 2',None,r162)
  r162.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Church Entryway 3',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Church Entryway 2',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Lostleaf Lake - Church Entryway 1',None,r94)
  r94.locations.append(l)
  l=L(p,'Shroom: Church - Pews 4',None,r184)
  r184.locations.append(l)
  l=L(p,'Shroom: Church - Pews 2',None,r184)
  r184.locations.append(l)
  l=L(p,'Shroom: Church - Pews 1',None,r184)
  r184.locations.append(l)
  l=L(p,'Shroom: Church - Pews 3',None,r184)
  r184.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 4',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 3',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 2',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 1',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 5',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Treehouse - Corners 6',None,r165)
  r165.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Bouncy Shroom 1',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Bouncy Shroom 3',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Bouncy Shroom 2',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Bouncy Shroom 4',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Entry Pathway 5',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Front Entrance 1',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Front Entrance 2',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Front Entrance 3',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Side 1',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Side 2',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Side Yellow Ledge',None,r11)
  r11.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 1',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 2',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 3',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 4',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 6',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Back Entrance 5',None,r14)
  r14.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Topside 1',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Topside 2',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Topside 3',None,r15)
  r15.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Entry Pathway 1',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Entry Pathway 2',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Entry Pathway 3',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Airborne Armada - Entry Pathway 4',None,r10)
  r10.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Entryway 4',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Entryway 3',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Entryway 2',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Hammocks Entryway 2',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Hammocks Entryway 1',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 3',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 2',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 1',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 6',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 5',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Cockpit Entry 4',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Medicine 3',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Medicine 2',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Boiler 1',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Boiler 2',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Boiler 3',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Below Medicine 1',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Plant Base',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Plant 1',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 5',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 6',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 4',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 3',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 2',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Rain Connector 1',None,r32)
  r32.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Entryway 4',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Entryway 3',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Entryway 2',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Lab Entryway 1',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe 5',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe 4',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe 3',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe 2',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe 1',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe Ramp 3',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe Ramp 2',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Pipe Ramp 1',None,r22)
  r22.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Entryway 1',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Slide Entryway 1',None,r21)
  r21.locations.append(l)
  l=L(p,'Shroom: Kerrington - Slide Entryway 2',None,r21)
  r21.locations.append(l)
  l=L(p,'Shroom: Kerrington - Slide Entryway 3',None,r21)
  r21.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Plant 2',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Plant 3',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Plant 4',None,r29)
  r29.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Above Boiler 4',None,r33)
  r33.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Above Boiler 2',None,r33)
  r33.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Above Boiler 1',None,r33)
  r33.locations.append(l)
  l=L(p,'Shroom: Kerrington - Rain Above Boiler 3',None,r33)
  r33.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 6',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 5',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 4',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 3',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 7',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 8',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 1',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Armada Entry Drone - Ledges 2',None,r9)
  r9.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poms 5',None,r127)
  r127.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poms 3',None,r127)
  r127.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poms 4',None,r127)
  r127.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poms 2',None,r127)
  r127.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poms 1',None,r127)
  r127.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry Tree 2',None,r124)
  r124.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry Tree 1',None,r124)
  r124.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry Tree 3',None,r124)
  r124.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry 1',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry 2',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Entry 3',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Jester Boots 1',None,r118)
  r118.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Jester Boots 2',None,r118)
  r118.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Jester Boots 3',None,r118)
  r118.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Jester Boots 4',None,r118)
  r118.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Jester Boots 5',None,r119)
  r119.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pom Spire 1',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pom Spire 2',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pom Spire 3',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pom Spire 4',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pom Spire 5',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Spire 1',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Spire 2',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Spire 3',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Spire 4',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Spire 5',None,r126)
  r126.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Gobbler 2',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Gobbler 3',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Gobbler 1',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 2',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 3',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 1',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 5',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 6',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Plants 4',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Overpass 3',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Overpass 4',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Overpass 5',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Overpass 2',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Overpass 1',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Mushroom Cave 3',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Mushroom Cave 4',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Mushroom Cave 5',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Mushroom Cave 2',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Mushroom Cave 1',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Slide 5',None,r128)
  r128.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Slide 4',None,r128)
  r128.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Slide 3',None,r128)
  r128.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Slide 2',None,r128)
  r128.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Observatory Slide 1',None,r128)
  r128.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poki-Poki Cave 1',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poki-Poki Cave 2',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poki-Poki Cave 3',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poki-Poki Cave 4',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Poki-Poki Cave 5',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool 1',None,r156)
  r156.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool 2',None,r156)
  r156.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool 3',None,r156)
  r156.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool 4',None,r156)
  r156.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool 5',None,r156)
  r156.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 3',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 4',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 5',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 6',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 8',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 7',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 2',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Basement Entry 1',None,r148)
  r148.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Corner 1',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Corner 2',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Corner 3',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Behind 3',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Behind 1',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Lake Behind 2',None,r146)
  r146.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 2',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 3',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 1',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 5',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 4',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Prismic Palace - Pool Bridges 6',None,r113)
  r113.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Star Puzzle 3',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Star Puzzle 1',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Star Puzzle 2',None,r142)
  r142.locations.append(l)
  l=L(p,"Shroom: Palace Interior - Heaven's Path Entry 3",None,r141)
  r141.locations.append(l)
  l=L(p,"Shroom: Palace Interior - Heaven's Path Entry 1",None,r141)
  r141.locations.append(l)
  l=L(p,"Shroom: Palace Interior - Heaven's Path Entry 2",None,r141)
  r141.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Bubble Conch Room 3',None,r143)
  r143.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Bubble Conch Room 1',None,r143)
  r143.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Bubble Conch Room 2',None,r143)
  r143.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Sentry Control Chamber 3',None,r145)
  r145.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Sentry Control Chamber 1',None,r145)
  r145.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Sentry Control Chamber 2',None,r145)
  r145.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 1',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 2',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 3',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 4',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 5',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Palace Back 6',None,r142)
  r142.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Bubble Conch Room 4',None,r144)
  r144.locations.append(l)
  l=L(p,'Shroom: Palace Interior - Bubble Conch Room 5',None,r144)
  r144.locations.append(l)
  l=L(p,'CAVE.ArmadaLobby.ArmadaLobbyBootsWall',None,r4)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', 'Apple'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  e=w.create_event('CAVE.ArmadaLobby.ArmadaLobbyBootsWall')
  l.place_locked_item(e)
  r4.locations.append(l)
  l=L(p,'MONSTER.Kerrington.MainBoils',None,r22)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Medicine'
  e=w.create_event('MONSTER.Kerrington.MainBoils')
  l.place_locked_item(e)
  r22.locations.append(l)
  l=L(p,'MONSTER.Kerrington.CockpitAccess',None,r23)
  e=w.create_event('MONSTER.Kerrington.CockpitAccess')
  l.place_locked_item(e)
  r23.locations.append(l)
  l=L(p,'MONSTER.Kerrington.GreenBoil',None,r29)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Medicine'
  e=w.create_event('MONSTER.Kerrington.GreenBoil')
  l.place_locked_item(e)
  r29.locations.append(l)
  l=L(p,'MONSTER.Kerrington.HornOnAnnoyingGenerator',None,r34)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  e=w.create_event('MONSTER.Kerrington.HornOnAnnoyingGenerator')
  l.place_locked_item(e)
  r34.locations.append(l)
  l=L(p,'GALLERY.WaterLobby.AirSwimFromMain',None,r44)
  l.access_rule=lambda s:(s.has_all(['Swim', 'Air Swim'], p))
  e=w.create_event('GALLERY.WaterLobby.AirSwimFromMain')
  l.place_locked_item(e)
  r44.locations.append(l)
  l=L(p,'GALLERY.WaterLobby.SpookyWall',None,r45)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Bubble Conch', 'Apple'} or s.has('Bubble', p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))))
  e=w.create_event('GALLERY.WaterLobby.SpookyWall')
  l.place_locked_item(e)
  r45.locations.append(l)
  l=L(p,'GALLERY.WaterLobby.AirSwimFromSpooky',None,r46)
  l.access_rule=lambda s:(s.has_all(['Swim', 'Air Swim'], p))
  e=w.create_event('GALLERY.WaterLobby.AirSwimFromSpooky')
  l.place_locked_item(e)
  r46.locations.append(l)
  l=L(p,'GALLERY.FireLobby.DouseRaceFlame',None,r53)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p))
  e=w.create_event('GALLERY.FireLobby.DouseRaceFlame')
  l.place_locked_item(e)
  r53.locations.append(l)
  l=L(p,'GALLERY.Chalice.OpenedLowerSnake',None,r59)
  e=w.create_event('GALLERY.Chalice.OpenedLowerSnake')
  l.place_locked_item(e)
  r59.locations.append(l)
  l=L(p,'GALLERY.EarthLobby.GrewMainBush',None,r63)
  e=w.create_event('GALLERY.EarthLobby.GrewMainBush')
  l.place_locked_item(e)
  r63.locations.append(l)
  l=L(p,'GALLERY.EarthLobby.RealignMainStatue',None,r65)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  e=w.create_event('GALLERY.EarthLobby.RealignMainStatue')
  l.place_locked_item(e)
  r65.locations.append(l)
  l=L(p,'GALLERY.EarthLobby.GrewCastleBushes',None,r67)
  e=w.create_event('GALLERY.EarthLobby.GrewCastleBushes')
  l.place_locked_item(e)
  r67.locations.append(l)
  l=L(p,'GALLERY.EarthLobby.RealignDragonHeadStatue',None,r75)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  e=w.create_event('GALLERY.EarthLobby.RealignDragonHeadStatue')
  l.place_locked_item(e)
  r75.locations.append(l)
  l=L(p,'GALLERY.EarthLobby.RealignCoffinsStatue',None,r79)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))
  e=w.create_event('GALLERY.EarthLobby.RealignCoffinsStatue')
  l.place_locked_item(e)
  r79.locations.append(l)
  l=L(p,'CAVE.GalleryLobby.GalleryLobbySoil',None,r85)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('CAVE.GalleryLobby.GalleryLobbySoil')
  l.place_locked_item(e)
  r85.locations.append(l)
  l=L(p,'CAVE.LostleafLobby.BrokeHiddenWall',None,r87)
  e=w.create_event('CAVE.LostleafLobby.BrokeHiddenWall')
  l.place_locked_item(e)
  r87.locations.append(l)
  l=L(p,'LAKE.LostleafLake.WinkyTreeSoil',None,r91)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('LAKE.LostleafLake.WinkyTreeSoil')
  l.place_locked_item(e)
  r91.locations.append(l)
  l=L(p,'LAKE.LostleafLake.BellTowerSoil',None,r91)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('LAKE.LostleafLake.BellTowerSoil')
  l.place_locked_item(e)
  r91.locations.append(l)
  l=L(p,'CAVE.SunCavern.MoonCavernHeartDoorOpened',None,r101)
  l.access_rule=lambda s:(s.has_group('Gratitude', p, 1) and (((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p)))))
  e=w.create_event('CAVE.SunCavern.MoonCavernHeartDoorOpened')
  l.place_locked_item(e)
  r101.locations.append(l)
  l=L(p,'CAVE.MoonCavern.SolvedDivePuzzle',None,r102)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  e=w.create_event('CAVE.MoonCavern.SolvedDivePuzzle')
  l.place_locked_item(e)
  r102.locations.append(l)
  l=L(p,'PALACE.Valley.AirSwimFromLostleafEntryway',None,r117)
  l.access_rule=lambda s:(s.has_all(['Swim', 'Air Swim'], p) and o.momentum_cancel.value == 1)
  e=w.create_event('PALACE.Valley.AirSwimFromLostleafEntryway')
  l.place_locked_item(e)
  r117.locations.append(l)
  l=L(p,'PALACE.Palace.KnockedPillarsDown',None,r142)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  e=w.create_event('PALACE.Palace.KnockedPillarsDown')
  l.place_locked_item(e)
  r142.locations.append(l)
  l=L(p,'PALACE.Valley.UnstuckBigstar',None,r146)
  l.access_rule=lambda s:(s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))
  e=w.create_event('PALACE.Valley.UnstuckBigstar')
  l.place_locked_item(e)
  r146.locations.append(l)
  l=L(p,'PALACE.Valley.BrokeLowerWaterWall',None,r150)
  e=w.create_event('PALACE.Valley.BrokeLowerWaterWall')
  l.place_locked_item(e)
  r150.locations.append(l)
  l=L(p,'CAVE.MoonCavern.DousedGalleryLobbyFlame',None,r158)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p]=='Medicine' or s.has('Bubble', p))
  e=w.create_event('CAVE.MoonCavern.DousedGalleryLobbyFlame')
  l.place_locked_item(e)
  r158.locations.append(l)
  l=L(p,'LAKE.LostleafLake.BigAppleLedgeSoil',None,r161)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('LAKE.LostleafLake.BigAppleLedgeSoil')
  l.place_locked_item(e)
  r161.locations.append(l)
  l=L(p,'LAKE.LostleafLake.DeepDeepWoodsSoil',None,r170)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('LAKE.LostleafLake.DeepDeepWoodsSoil')
  l.place_locked_item(e)
  r170.locations.append(l)
  l=L(p,'LAKE.LostleafLake.CryptSoil',None,r172)
  l.access_rule=lambda s:s._cavernofdreams_carrying[p]=='Apple'
  e=w.create_event('LAKE.LostleafLake.CryptSoil')
  l.place_locked_item(e)
  r172.locations.append(l)
  l=L(p,'LAKE.Crypt.BrokeBackExitWithHorn',None,r178)
  l.access_rule=lambda s:(s._cavernofdreams_carrying[p] is None and s.has('Horn', p) and o.difficulty.value >= 2 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has('Wings', p) or (s.has('Bubble', p) and o.bubble_jump.value >= 1)) and o.out_of_bounds.value == 1 and o.ejection_launch.value == 1 and o.damage_boost.value == 1 and o.z_target.value == 1)
  e=w.create_event('LAKE.Crypt.BrokeBackExitWithHorn')
  l.place_locked_item(e)
  r178.locations.append(l)
  r=R('CAVE.ArmadaLobby.ArmadaLobbyBoots',p,mw)
  l=L(p,'CAVE.ArmadaLobby.ArmadaLobbyBoots',None,r)
  e=w.create_event('CAVE.ArmadaLobby.ArmadaLobbyBoots')
  l.place_locked_item(e)
  r.locations.append(l)
  r5.connect(r)
  r.connect(r5)
  mw.regions.append(r)
  r=R('MONSTER.Sky.SkyKerringtonWings',p,mw)
  l=L(p,'MONSTER.Sky.SkyKerringtonWings',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('MONSTER.Sky.SkyKerringtonWings')
  l.place_locked_item(e)
  r.locations.append(l)
  r19.connect(r)
  r.connect(r19)
  mw.regions.append(r)
  r=R('MONSTER.Kerrington.MainMedicine',p,mw)
  l=L(p,'MONSTER.Kerrington.MainMedicine',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('MONSTER.Kerrington.MainMedicine')
  l.place_locked_item(e)
  r.locations.append(l)
  r22.connect(r)
  r.connect(r22)
  mw.regions.append(r)
  r=R('MONSTER.Kerrington.GreenMedicine',p,mw)
  l=L(p,'MONSTER.Kerrington.GreenMedicine',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('MONSTER.Kerrington.GreenMedicine')
  l.place_locked_item(e)
  r.locations.append(l)
  r29.connect(r)
  r.connect(r29)
  mw.regions.append(r)
  r=R('GALLERY.WaterLobby.SagesGloves',p,mw)
  l=L(p,'GALLERY.WaterLobby.SagesGloves',None,r)
  l.access_rule=lambda s:(s.has('Carry', p) and (s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  e=w.create_event('GALLERY.WaterLobby.SagesGloves')
  l.place_locked_item(e)
  r.locations.append(l)
  r44.connect(r)
  r.connect(r44)
  mw.regions.append(r)
  r=R('GALLERY.WaterLobby.LadyOpalsHead',p,mw)
  l=L(p,'GALLERY.WaterLobby.LadyOpalsHead',None,r)
  l.access_rule=lambda s:(s.has_all(['Open Gallery of Nightmares Sewer Chest #1', 'Carry'], p))
  e=w.create_event('GALLERY.WaterLobby.LadyOpalsHead')
  l.place_locked_item(e)
  r.locations.append(l)
  r46.connect(r)
  r.connect(r46)
  mw.regions.append(r)
  r=R('GALLERY.WaterLobby.JesterBoots',p,mw)
  l=L(p,'GALLERY.WaterLobby.JesterBoots',None,r)
  l.access_rule=lambda s:s.has('Open Gallery of Nightmares Sewer Chest #2', p)
  e=w.create_event('GALLERY.WaterLobby.JesterBoots')
  l.place_locked_item(e)
  r.locations.append(l)
  r49.connect(r)
  r.connect(r49)
  mw.regions.append(r)
  r=R('GALLERY.FireLobby.ShelnertsFish',p,mw)
  l=L(p,'GALLERY.FireLobby.ShelnertsFish',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('GALLERY.FireLobby.ShelnertsFish')
  l.place_locked_item(e)
  r.locations.append(l)
  r55.connect(r)
  r.connect(r55)
  mw.regions.append(r)
  r=R('GALLERY.EarthLobby.KerringtonWings',p,mw)
  l=L(p,'GALLERY.EarthLobby.KerringtonWings',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('GALLERY.EarthLobby.KerringtonWings')
  l.place_locked_item(e)
  r.locations.append(l)
  r73.connect(r)
  r.connect(r73)
  mw.regions.append(r)
  r=R('LAKE.LostleafLake.LakeAppleTree',p,mw)
  l=L(p,'LAKE.LostleafLake.LakeAppleTree',None,r)
  l.access_rule=lambda s:(s.has('Carry', p) and (s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or o.difficulty.value >= 1 or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p)))))
  e=w.create_event('LAKE.LostleafLake.LakeAppleTree')
  l.place_locked_item(e)
  r.locations.append(l)
  r91.connect(r)
  r.connect(r91)
  mw.regions.append(r)
  r=R('PALACE.Valley.ValleyJesterBoots',p,mw)
  l=L(p,'PALACE.Valley.ValleyJesterBoots',None,r)
  e=w.create_event('PALACE.Valley.ValleyJesterBoots')
  l.place_locked_item(e)
  r.locations.append(l)
  r120.connect(r)
  r.connect(r120)
  mw.regions.append(r)
  r=R('PALACE.Sanctum.BubbleConch',p,mw)
  l=L(p,'PALACE.Sanctum.BubbleConch',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('PALACE.Sanctum.BubbleConch')
  l.place_locked_item(e)
  r.locations.append(l)
  r139.connect(r)
  r.connect(r139)
  mw.regions.append(r)
  r=R('PALACE.Palace.BubbleConch',p,mw)
  l=L(p,'PALACE.Palace.BubbleConch',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('PALACE.Palace.BubbleConch')
  l.place_locked_item(e)
  r.locations.append(l)
  r143.connect(r)
  r.connect(r143)
  mw.regions.append(r)
  r=R('LAKE.LostleafLake.DeepDeepWoodsJesterBoots',p,mw)
  l=L(p,'LAKE.LostleafLake.DeepDeepWoodsJesterBoots',None,r)
  e=w.create_event('LAKE.LostleafLake.DeepDeepWoodsJesterBoots')
  l.place_locked_item(e)
  r.locations.append(l)
  r170.connect(r)
  r.connect(r170)
  mw.regions.append(r)
  r=R('LAKE.LostleafLake.DeepDeepWoodsAppleTree',p,mw)
  l=L(p,'LAKE.LostleafLake.DeepDeepWoodsAppleTree',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('LAKE.LostleafLake.DeepDeepWoodsAppleTree')
  l.place_locked_item(e)
  r.locations.append(l)
  r170.connect(r)
  r.connect(r170)
  mw.regions.append(r)
  r=R('LAKE.LostleafLake.CryptAppleTree',p,mw)
  l=L(p,'LAKE.LostleafLake.CryptAppleTree',None,r)
  l.access_rule=lambda s:(s.has('Carry', p) and (s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or s.has_any(['High Jump', 'Double Jump'], p) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}))))
  e=w.create_event('LAKE.LostleafLake.CryptAppleTree')
  l.place_locked_item(e)
  r.locations.append(l)
  r172.connect(r)
  r.connect(r172)
  mw.regions.append(r)
  r=R('GALLERY.Drown.BubbleConch',p,mw)
  l=L(p,'GALLERY.Drown.BubbleConch',None,r)
  l.access_rule=lambda s:s.has('Carry', p)
  e=w.create_event('GALLERY.Drown.BubbleConch')
  l.place_locked_item(e)
  r.locations.append(l)
  r196.connect(r)
  r.connect(r196)
  mw.regions.append(r)
  # CAVE.SunCavern.ArmadaLobbyRoom -> CAVE.ArmadaLobby.Main
  r1.connect(r2,'CAVE.SunCavern.ArmadaLobbyDoor',None)
  # CAVE.ArmadaLobby.CannonLip -> CAVE.SunCavern.Main
  r7.connect(r0,'CAVE.ArmadaLobby.SunCavernTeleport',lambda s:s.has('Open Armada Lobby Teleport', p))
  # CAVE.ArmadaLobby.EnterCannon -> MONSTER.EarthDrone.Main
  r6.connect(r9,'CAVE.ArmadaLobby.EarthDroneCannonShot',lambda s:not (s._cavernofdreams_carrying[p]=='Jester Boots'))
  # MONSTER.EarthDrone.Main -> CAVE.ArmadaLobby.EnterCannon
  r9.connect(r6,'MONSTER.EarthDrone.ArmadaLobbyDoor',None)
  # MONSTER.EarthDrone.Main -> MONSTER.Sky.Main
  r9.connect(r10,'MONSTER.EarthDrone.SkyDoor',None)
  # MONSTER.Sky.YellowDoorway -> MONSTER.Kerrington.DogRoom
  r12.connect(r13,'MONSTER.Sky.YellowDoor',None)
  # MONSTER.Kerrington.DogRoom -> MONSTER.Sky.YellowDoorway
  r13.connect(r12,'MONSTER.Kerrington.SkyDogDoor',None)
  # MONSTER.Sky.FireDronePlatform -> MONSTER.FireDrone.Main
  r16.connect(r17,'MONSTER.Sky.FireDroneDoor',None)
  # MONSTER.FireDrone.Main -> MONSTER.Sky.FireDronePlatform
  r17.connect(r16,'MONSTER.FireDrone.SkyDoor',None)
  # MONSTER.Sky.WaterDronePlatform -> MONSTER.WaterDrone.Main
  r19.connect(r20,'MONSTER.Sky.WaterDroneDoor',None)
  # MONSTER.WaterDrone.Main -> MONSTER.Sky.WaterDronePlatform
  r20.connect(r19,'MONSTER.WaterDrone.SkyDoor',None)
  # MONSTER.Sky.Tail -> MONSTER.Kerrington.MedicinePool
  r14.connect(r21,'MONSTER.Sky.KerringtonDoorBack',None)
  # MONSTER.Kerrington.HeartEntryway -> MONSTER.Heart.Main
  r24.connect(r27,'MONSTER.Kerrington.HeartDoor',None)
  # MONSTER.Heart.Main -> MONSTER.Kerrington.HeartEntryway
  r27.connect(r24,'MONSTER.Heart.KerringtonDoor',None)
  # MONSTER.Kerrington.IntoFrontDoor -> MONSTER.Sky.Main
  r28.connect(r10,'MONSTER.Kerrington.SkyDoorFront',None)
  # MONSTER.Kerrington.GreenFence -> MONSTER.Sky.GreenDoorway
  r30.connect(r31,'MONSTER.Kerrington.SkyFenceDoor',lambda s:(s._cavernofdreams_carrying[p] in {'Apple', 'Bubble Conch'} or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or ((s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (s.has('Roll', p) and o.roll_disjoint.value == 1)))
  # MONSTER.Sky.GreenDoorway -> MONSTER.Kerrington.GreenFence
  r31.connect(r30,'MONSTER.Sky.GreenDoor',None)
  # MONSTER.Kerrington.MedicinePool -> MONSTER.Sky.Tail
  r21.connect(r14,'MONSTER.Kerrington.SkyDoorBack',lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' and s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p)))
  # MONSTER.Sky.Main -> MONSTER.EarthDrone.Main
  r10.connect(r9,'MONSTER.Sky.EarthDroneDoor',None)
  # MONSTER.Sky.Main -> MONSTER.Kerrington.IntoFrontDoor
  r10.connect(r28,'MONSTER.Sky.KerringtonDoorFront',None)
  # CAVE.ArmadaLobby.SewerConnector -> CAVE.Sewer.ArmadaLobbySide
  r39.connect(r40,'CAVE.ArmadaLobby.SewerDoor',None)
  # CAVE.Sewer.GallerySide -> GALLERY.WaterLobby.LobbySewerUnderwater
  r41.connect(r42,'CAVE.Sewer.GalleryDoor',None)
  # GALLERY.WaterLobby.LunaHouse -> GALLERY.LunaRoom.LunaHouse
  r47.connect(r48,'GALLERY.WaterLobby.LunaRoomDoor',None)
  # GALLERY.LunaRoom.LunaHouse -> GALLERY.WaterLobby.LunaHouse
  r48.connect(r47,'GALLERY.LunaRoom.WaterLobbyDoor',None)
  # GALLERY.WaterLobby.Main -> GALLERY.Foyer.Main
  r44.connect(r51,'GALLERY.WaterLobby.FoyerDoor',None)
  # GALLERY.Foyer.SideDoors -> GALLERY.FireLobby.Main
  r52.connect(r53,'GALLERY.Foyer.FireLobbyDoor',None)
  # GALLERY.FireLobby.ChalicePlatform -> GALLERY.Chalice.Main
  r54.connect(r57,'GALLERY.FireLobby.ChalicePainting',lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has_any(['High Jump', 'Double Jump'], p) or (s.has('Horn', p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'})) or (o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or (o.air_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bounce', 'Roll'], p) and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Aerial Tail', 'Tail'], p))) or (s.has_all(['Super Bubble Jump', 'Roll', 'Bubble'], p))))
  # GALLERY.Chalice.BottomShortcutPlatform -> GALLERY.Chalice.Main
  r59.connect(r57,'GALLERY.Chalice.ShortcutUpDoor',lambda s:s.has('Coils of Agony - Open Shortcut', p))
  # GALLERY.Chalice.Main -> GALLERY.FireLobby.ChalicePlatform
  r57.connect(r54,'GALLERY.Chalice.FireLobbyDoor',None)
  # GALLERY.Chalice.Main -> GALLERY.Chalice.BottomShortcutPlatform
  r57.connect(r59,'GALLERY.Chalice.ShortcutDownDoor',lambda s:s.has('Coils of Agony - Open Shortcut', p))
  # GALLERY.FireLobby.EarthLobbyEntryway -> GALLERY.EarthLobby.FireLobbyEntryway
  r60.connect(r61,'GALLERY.FireLobby.EarthLobbyDoor',None)
  # GALLERY.EarthLobby.CastleUnderwater -> GALLERY.WaterLobby.LobbySewerEgg
  r68.connect(r69,'GALLERY.EarthLobby.ToiletPainting',None)
  # GALLERY.EarthLobby.KerringtonCauldronEntryway -> MONSTER.Kerrington.CauldronRoom
  r71.connect(r72,'GALLERY.EarthLobby.KerringtonCauldron',None)
  # MONSTER.Kerrington.CauldronRoom -> GALLERY.EarthLobby.KerringtonCauldronEntryway
  r72.connect(r71,'MONSTER.Kerrington.EarthLobbyCauldron',None)
  # GALLERY.EarthLobby.InsideCastle -> GALLERY.Undead.Main
  r66.connect(r74,'GALLERY.EarthLobby.UndeadPainting',None)
  # GALLERY.Undead.Main -> GALLERY.EarthLobby.InsideCastle
  r74.connect(r66,'GALLERY.Undead.EarthLobbyDoor',None)
  # GALLERY.EarthLobby.FoyerEntryPlatform -> GALLERY.Foyer.SideDoors
  r76.connect(r52,'GALLERY.EarthLobby.FoyerDoor',None)
  # GALLERY.EarthLobby.MainUnderwater -> GALLERY.WaterLobby.LobbySewerMiddle
  r64.connect(r43,'GALLERY.EarthLobby.ToiletBridge',None)
  # GALLERY.EarthLobby.MainUnderwater -> GALLERY.WaterLobby.LobbySewerMiddle
  r64.connect(r43,'GALLERY.EarthLobby.ToiletDragonHead',None)
  # GALLERY.EarthLobby.CoffinsUnderwater -> GALLERY.WaterLobby.LobbySewerGiant
  r77.connect(r78,'GALLERY.EarthLobby.ToiletCoffins',None)
  # GALLERY.EarthLobby.FireLobbyEntryway -> GALLERY.FireLobby.EarthLobbyEntryway
  r61.connect(r60,'GALLERY.EarthLobby.FireLobbyDoor',None)
  # GALLERY.FireLobby.Main -> GALLERY.Foyer.SideDoors
  r53.connect(r52,'GALLERY.FireLobby.FoyerDoor',None)
  # GALLERY.Foyer.SideDoors -> GALLERY.EarthLobby.FoyerEntryPlatform
  r52.connect(r76,'GALLERY.Foyer.EarthLobbyDoor',None)
  # GALLERY.Foyer.Main -> CAVE.GalleryLobby.Main
  r51.connect(r81,'GALLERY.Foyer.GalleryLobbyDoor',None)
  # CAVE.GalleryLobby.LostleafCave -> CAVE.LostleafLobby.HiddenDoorway
  r85.connect(r86,'CAVE.GalleryLobby.LostleafLobbyDoor',None)
  # CAVE.LostleafLobby.Main -> CAVE.SunCavern.MightyWallLedge
  r88.connect(r90,'CAVE.LostleafLobby.SunCavernDoor',None)
  # CAVE.SunCavern.MightyWallLedge -> CAVE.LostleafLobby.Main
  r90.connect(r88,'CAVE.SunCavern.LostleafLobbyDoor',lambda s:s.has('Topple Mighty Wall', p))
  # CAVE.LostleafLobby.Main -> LAKE.LostleafLake.Main
  r88.connect(r91,'CAVE.LostleafLobby.LostleafLakeDoor',None)
  # LAKE.LostleafLake.Ducklings -> CAVE.SunCavern.WaterfallLedge
  r97.connect(r98,'LAKE.LostleafLake.DucklingsDoorUpper',None)
  # CAVE.SunCavern.DucklingsDoorway -> LAKE.LostleafLake.Ducklings
  r99.connect(r97,'CAVE.SunCavern.DucklingsDoorLower',None)
  # CAVE.SunCavern.MoonCavernHeartDoorway -> CAVE.MoonCavern.Main
  r101.connect(r102,'CAVE.SunCavern.MoonCavernHeartDoor',lambda s:s.has('CAVE.SunCavern.MoonCavernHeartDoorOpened', p))
  # CAVE.MoonCavern.Upper -> CAVE.PalaceLobby.Main
  r107.connect(r108,'CAVE.MoonCavern.PalaceLobbyDoor',None)
  # CAVE.PalaceLobby.PrismicEntryPlatform -> PALACE.Valley.Main
  r110.connect(r113,'CAVE.PalaceLobby.ValleyDoor',None)
  # PALACE.Valley.LostleafEntryway -> LAKE.LostleafLake.OuterRim
  r117.connect(r92,'PALACE.Valley.LostleafDoor',None)
  # PALACE.Valley.ObservatoryEntry -> PALACE.Observatory.Main
  r129.connect(r130,'PALACE.Valley.ObservatoryDoor',None)
  # PALACE.Observatory.Main -> PALACE.Valley.ObservatoryEntry
  r130.connect(r129,'PALACE.Observatory.ValleyDoor',None)
  # PALACE.Valley.ObservatoryPlatform -> PALACE.Valley.Main
  r128.connect(r113,'PALACE.Valley.ObservatoryShortcutDoorTop',lambda s:s.has('Open Observatory Shortcut', p))
  # PALACE.Valley.Spires -> PALACE.DiningRoom.Main
  r126.connect(r133,'PALACE.Valley.DiningRoomDoor',None)
  # PALACE.DiningRoom.Main -> PALACE.Valley.Spires
  r133.connect(r126,'PALACE.DiningRoom.ValleyDoor',None)
  # PALACE.Valley.PalaceTop -> PALACE.Sanctum.ValleyEntryway
  r136.connect(r137,'PALACE.Valley.SanctumDoor',None)
  # PALACE.Sanctum.PalaceEntryway -> PALACE.Palace.SanctumEntryway
  r140.connect(r141,'PALACE.Sanctum.PalaceDoor',None)
  # PALACE.Palace.Main -> PALACE.Valley.UpperWater
  r142.connect(r146,'PALACE.Palace.FrontDoor',None)
  # PALACE.Valley.LowerWater -> PALACE.Palace.Basement
  r148.connect(r151,'PALACE.Valley.PalaceBasementDoor',lambda s:s.has('Open Prismic Palace Basement', p))
  # PALACE.Palace.Basement -> PALACE.Valley.LowerWater
  r151.connect(r148,'PALACE.Palace.BasementDoor',None)
  # PALACE.Valley.UpperWater -> PALACE.Palace.Main
  r146.connect(r142,'PALACE.Valley.PalaceFrontDoor',lambda s:(s.has('Open Prismic Palace Gate', p) or (s.has('Roll', p) and o.roll_disjoint.value == 1)))
  # PALACE.Palace.SanctumEntryway -> PALACE.Sanctum.PalaceEntryway
  r141.connect(r140,'PALACE.Palace.SanctumDoor',None)
  # PALACE.Sanctum.ValleyEntryway -> PALACE.Valley.PalaceTop
  r137.connect(r136,'PALACE.Sanctum.ValleyDoor',None)
  # PALACE.Valley.Main -> CAVE.PalaceLobby.PrismicEntryPlatform
  r113.connect(r110,'PALACE.Valley.PalaceLobbyDoor',None)
  # PALACE.Valley.Main -> PALACE.Valley.ObservatoryPlatform
  r113.connect(r128,'PALACE.Valley.ObservatoryShortcutDoorBottom',lambda s:s.has('Open Observatory Shortcut', p))
  # CAVE.PalaceLobby.PrismicEntryPlatform -> CAVE.SunCavern.Main
  r110.connect(r0,'CAVE.PalaceLobby.SunCavernTeleport',lambda s:s.has('Open Palace Lobby Teleport', p))
  # CAVE.PalaceLobby.Main -> CAVE.MoonCavern.Upper
  r108.connect(r107,'CAVE.PalaceLobby.MoonCavernDoor',None)
  # CAVE.MoonCavern.NightmareLobbyDoorway -> CAVE.GalleryLobby.Main
  r158.connect(r81,'CAVE.MoonCavern.GalleryLobbyDoor',lambda s:(s.has('CAVE.MoonCavern.DousedGalleryLobbyFlame', p) or (s._cavernofdreams_carrying[p] is None and o.difficulty.value >= 2 and o.damage_boost.value == 1 and o.momentum_cancel.value == 1)))
  # CAVE.MoonCavern.Main -> CAVE.SunCavern.MoonCavernHeartDoorway
  r102.connect(r101,'CAVE.MoonCavern.SunCavernDoor',None)
  # CAVE.SunCavern.WaterfallLedge -> LAKE.LostleafLake.Ducklings
  r98.connect(r97,'CAVE.SunCavern.DucklingsDoorUpper',None)
  # LAKE.LostleafLake.Ducklings -> CAVE.SunCavern.DucklingsDoorway
  r97.connect(r99,'LAKE.LostleafLake.DucklingsDoorLower',None)
  # LAKE.LostleafLake.TreehouseBackEntry -> LAKE.Treehouse.Main
  r164.connect(r165,'LAKE.LostleafLake.TreehouseBackDoor',None)
  # LAKE.Treehouse.Main -> LAKE.LostleafLake.TreehouseFrontEntry
  r165.connect(r163,'LAKE.Treehouse.LostleafFrontDoor',lambda s:(s.has('Open Treehouse', p) or (s.has('Roll', p) and o.roll_disjoint.value == 1)))
  # LAKE.Treehouse.Main -> LAKE.LostleafLake.TreehouseBackEntry
  r165.connect(r164,'LAKE.Treehouse.LostleafBackDoor',None)
  # LAKE.LostleafLake.TreehouseFrontEntry -> LAKE.Treehouse.Main
  r163.connect(r165,'LAKE.LostleafLake.TreehouseFrontDoor',lambda s:(s.has('Open Treehouse', p) or (s.has('Roll', p) and o.roll_disjoint.value == 1)))
  # LAKE.LostleafLake.CryptBackLedge -> LAKE.Crypt.BackExit
  r172.connect(r174,'LAKE.LostleafLake.CryptDoorBack',None)
  # LAKE.Crypt.Main -> LAKE.LostleafLake.InsideCrypt
  r176.connect(r180,'LAKE.Crypt.LostleafLakeDoorFront',None)
  # LAKE.LostleafLake.InsideCrypt -> LAKE.Crypt.Main
  r180.connect(r176,'LAKE.LostleafLake.CryptDoorFront',None)
  # LAKE.Crypt.BackExit -> LAKE.LostleafLake.CryptBackLedge
  r174.connect(r172,'LAKE.Crypt.LostleafLakeDoorBack',None)
  # LAKE.LostleafLake.InsideChurch -> LAKE.Church.Main
  r183.connect(r184,'LAKE.LostleafLake.ChurchDoor',None)
  # LAKE.Church.Main -> LAKE.LostleafLake.InsideChurch
  r184.connect(r183,'LAKE.Church.LostleafLakeDoor',None)
  # LAKE.LostleafLake.FallIntoTeepee -> LAKE.Teepee.Main
  r187.connect(r188,'LAKE.LostleafLake.TeepeeTopside',None)
  # LAKE.Teepee.Main -> LAKE.LostleafLake.TeepeeIsland
  r188.connect(r93,'LAKE.Teepee.FrontDoor',None)
  # LAKE.LostleafLake.TeepeeIsland -> LAKE.Teepee.Main
  r93.connect(r188,'LAKE.LostleafLake.TeepeeFrontDoor',None)
  # LAKE.LostleafLake.OuterRim -> PALACE.Valley.LostleafEntryway
  r92.connect(r117,'LAKE.LostleafLake.ValleyDoor',None)
  # LAKE.LostleafLake.Main -> CAVE.LostleafLobby.Main
  r91.connect(r88,'LAKE.LostleafLake.LostleafLobbyDoor',None)
  # CAVE.LostleafLobby.Main -> CAVE.SunCavern.Main
  r88.connect(r0,'CAVE.LostleafLobby.SunCavernTeleport',lambda s:s.has('Open Lake Lobby Teleport', p))
  # CAVE.LostleafLobby.HiddenDoorway -> CAVE.GalleryLobby.LostleafCave
  r86.connect(r85,'CAVE.LostleafLobby.GalleryLobbyDoor',None)
  # CAVE.GalleryLobby.Main -> GALLERY.Foyer.Main
  r81.connect(r51,'CAVE.GalleryLobby.FoyerDoor',lambda s:s.has('Open Gallery Lobby Door', p))
  # CAVE.GalleryLobby.Main -> CAVE.MoonCavern.NightmareLobbyDoorway
  r81.connect(r158,'CAVE.GalleryLobby.MoonCavernDoor',None)
  # CAVE.GalleryLobby.Main -> CAVE.SunCavern.Main
  r81.connect(r0,'CAVE.GalleryLobby.SunCavernTeleport',lambda s:s.has('Open Gallery Lobby Teleport', p))
  # CAVE.GalleryLobby.Main -> CAVE.Rainbow.Well
  r81.connect(r190,'CAVE.GalleryLobby.RainbowBench',None)
  # CAVE.Rainbow.Well -> CAVE.GalleryLobby.Main
  r190.connect(r81,'CAVE.Rainbow.WellEntrance',None)
  # GALLERY.Foyer.Main -> GALLERY.WaterLobby.Main
  r51.connect(r44,'GALLERY.Foyer.WaterLobbyDoor',None)
  # GALLERY.Foyer.Main -> GALLERY.WaterLobby.Main
  r51.connect(r44,'GALLERY.Foyer.WaterLobbyHole',None)
  # GALLERY.WaterLobby.Main -> GALLERY.Drown.Main
  r44.connect(r195,'GALLERY.WaterLobby.DrownPainting',lambda s:(s._cavernofdreams_carrying[p]=='Jester Boots' or s.has('GALLERY.WaterLobby.AirSwimFromMain', p) or (o.wing_jump.value == 1 and (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" or s.has('Wings', p)) and ((s.has_all(['Bubble', 'Double Jump'], p) and o.bubble_jump.value == 2 and o.z_target.value == 1 and o.ground_tail_jump.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))))) or (s._cavernofdreams_carrying[p]=="Mr. Kerrington's Wings" and ((s.has_all(['Sprint', 'Double Jump'], p)) or (s.has('Bubble', p) and o.bubble_jump.value == 2 and o.z_target.value == 1 and (s.has_any(['High Jump', 'Double Jump'], p))) or (s.has('High Jump', p) and (s.has('Sprint', p) or (s.has('Double Jump', p) and o.ability_toggle.value == 1)))))))
  # GALLERY.Drown.Main -> GALLERY.WaterLobby.Main
  r195.connect(r44,'GALLERY.Drown.WaterLobbyDoor',None)
  # GALLERY.WaterLobby.LobbySewerUnderwater -> CAVE.Sewer.GallerySide
  r42.connect(r41,'GALLERY.WaterLobby.SewerDoor',None)
  # CAVE.Sewer.ArmadaLobbySide -> CAVE.ArmadaLobby.SewerConnector
  r40.connect(r39,'CAVE.Sewer.ArmadaLobbyDoor',None)
  # CAVE.ArmadaLobby.Main -> CAVE.SunCavern.ArmadaLobbyRoom
  r2.connect(r1,'CAVE.ArmadaLobby.SunCavernDoor',lambda s:((s.has('Roll', p) and o.roll_disjoint.value == 1 and (s._cavernofdreams_carrying[p] in {None, 'Jester Boots'}) and (s.has_any(['Grounded Tail', 'Tail'], p))) or not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  # CAVE.SunCavern.Main -> CAVE.LostleafLobby.Main
  r0.connect(r88,'CAVE.SunCavern.LostleafLobbyTeleport',lambda s:(s.has('Open Lake Lobby Teleport', p) and not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  # CAVE.SunCavern.Main -> CAVE.ArmadaLobby.CannonLip
  r0.connect(r7,'CAVE.SunCavern.ArmadaLobbyTeleport',lambda s:(s.has('Open Armada Lobby Teleport', p) and not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  # CAVE.SunCavern.Main -> CAVE.PalaceLobby.PrismicEntryPlatform
  r0.connect(r110,'CAVE.SunCavern.PalaceLobbyTeleport',lambda s:(s.has('Open Palace Lobby Teleport', p) and not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  # CAVE.SunCavern.Main -> CAVE.GalleryLobby.Main
  r0.connect(r81,'CAVE.SunCavern.GalleryLobbyTeleport',lambda s:(s.has('Open Gallery Lobby Teleport', p) and not (s._cavernofdreams_carrying[p]=='Jester Boots')))
  M=R('Menu',p,mw)
  # Menu -> CAVE.SunCavern.Main
  M.connect(r0,None,None)
  mw.regions.append(M)
  V=R('Victory',p,mw)
  # Victory -> GALLERY.Foyer.Main
  V.connect(r51,None,None)
  e=w.create_event('Victory')
  l=L(p,'Victory',None,r51)
  l.place_locked_item(e)
  r51.locations.append(l)