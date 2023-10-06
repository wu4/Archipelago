from dataclasses import dataclass
from . import generated
from Options import Toggle, AssembleOptions, PerGameCommonOptions

class ShufflePowerBeam(Toggle):
  """Shuffles the Power Beam into the pool."""
  default = 0
  
class ShuffleCombatVisor(Toggle):
  """Shuffles the Combat Visor into the pool."""
  default = 0
  
class ShuffleScanVisor(Toggle):
  """Shuffles the Scan Visor into the pool."""
  default = 0

class ItemsEveryRoom(Toggle):
  """Adds an item into every room."""
  default = 0

@dataclass
class MetroidPrimeOptions(generated.GeneratedOptions, PerGameCommonOptions):
  shuffle_power_beam: ShufflePowerBeam
  shuffle_combat_visor: ShuffleCombatVisor
  shuffle_scan_visor: ShuffleScanVisor
  items_every_room: ItemsEveryRoom