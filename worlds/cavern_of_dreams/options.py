from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, Choice, DeathLink

class SuperBounce(Toggle):
  """Considers the ability to super bounce in logic."""
  default = 0

class Movement(Choice):
  """
  Considers the ability to perform various movement tech in logic.
  Beginner: No difficult tech required.
  Intermediate: Involves some tricky jumps or unexpected use of map geometry.
  Expert: Involves very particular jumps that may require strict timing or setup.
  """
  default = 0
  option_beginner = 0
  option_intermediate = 1
  option_expert = 2

class HitlaunchCancels(Toggle):
  """Considers the ability to perform hitlaunch cancels, by pausing immediately after hitlag from receiving damage ends, in logic."""
  default = 0

class JBA(Toggle):
  """Considers use of Jester Boots Anywhere in logic."""
  default = 0

class ShuffleEvents(Toggle):
  """Shuffles events into the pool. For example, healing the Giant is a location with a check."""
  default = 0

class ShuffleHearts(Toggle):
  """Shuffles hearts into the pool. Feeding hatched fellas is now a check."""
  default = 0

class Shroomsanity(Toggle):
  """Shuffles all shrooms into the pool."""
  default = 0

class Cardsanity(Toggle):
  """Shuffles all cards into the pool."""
  default = 0

class ShuffleAbilities(Toggle):
  """Shuffles the abilities the Sage gives you into the pool."""
  default = 0

class ShuffleHighJump(Toggle):
  """Shuffles the ability to High Jump into the pool."""
  default = 0

class ShuffleRoll(Choice):
  """Shuffles the ability to roll into the pool.

  If shuffle_progressive is chosen, two instances of Roll will be shuffled into
  the pool. The first instance you receive will allow you to roll, and the
  second will allow you to build speed while rolling."""
  default = 0
  option_off = 0
  option_shuffle = 1
  option_shuffle_progressive = 2

class ShuffleSwim(Toggle):
  """Shuffles the ability to swim into the pool. If you touch water without the
  ability to swim, you die."""
  default = 0

class DiveWithoutTailwhip(Toggle):
  """Enables the ability to use Dive without Tailwhip."""
  default = 0

class RemoveFlight(Toggle):
  """Removes Flight from the pool. Recommended, else most seeds will risk easily
  becoming trivialized with shuffled abilities."""
  default = 1

@dataclass
class CavernOfDreamsOptions(PerGameCommonOptions):
  super_bounce: SuperBounce
  movement: Movement
  hitlaunch_cancels: HitlaunchCancels
  jester_boots_anywhere: JBA

  shroomsanity: Shroomsanity
  cardsanity: Cardsanity
  shuffle_events: ShuffleEvents
  shuffle_hearts: ShuffleHearts

  shuffle_abilities: ShuffleAbilities

  shuffle_high_jump: ShuffleHighJump
  shuffle_roll: ShuffleRoll
  shuffle_swim: ShuffleSwim

  dive_without_tailwhip: DiveWithoutTailwhip
  remove_flight: RemoveFlight

  death_link: DeathLink