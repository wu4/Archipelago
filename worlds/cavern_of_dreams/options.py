from dataclasses import dataclass

from Options import Toggle, PerGameCommonOptions, Choice, DeathLink

class Difficulty(Choice):
  """
  Considers the ability to perform various movement tech in logic.
  Beginner: No difficult tech required. May still require unexpected use of map geometry.
  Intermediate: Involves some tricky movement that may require a small amount of practice and fast inputs.
  Hard: Involves very particular movement that may require highly strict timing or a large amount of setup.
  """
  default = 0
  option_beginner = 0
  option_intermediate = 1
  option_hard = 2

class SuperBounce(Choice):
  """
  How to treat super bounce, a tech that enables gaining significant height using an aerial tailwhip while rolling.

  Disable (default): Prevents the use of super bounce.
  Enable: Allows the use of super bounce.
  Shuffle: Shuffles super bounce into the pool.
  """
  default = 0
  option_disable = 0
  option_enable = 1
  option_shuffle = 2

class SuperBubbleJump(Choice):
  """
  How to treat super bubble jump, a tech that enables gaining significant height using bubble shots while rolling.

  Disable (default): Prevents the use of super bubble jump.
  Enable: Allows the use of super bubble jump.
  Shuffle: Shuffles super bubble jump into the pool.
  """
  default = 0
  option_disable = 0
  option_enable = 1
  option_shuffle = 2

class JesterBootsAnywhere(Toggle):
  """Considers tech that enables taking the Jester Boots outside of intended rooms in logic."""
  default = 0

class Eventsanity(Toggle):
  """Shuffles events into the pool. For example, healing the Giant is a location with a check."""
  default = 0

class Gratitudesanity(Toggle):
  """Shuffles gratitude into the pool. Feeding hatched fellas is now a check."""
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

class ShuffleSprint(Toggle):
  """Shuffles the ability to build momentum into the pool."""
  default = 0

class ShuffleRoll(Toggle):
  """Shuffles the ability to roll into the pool."""
  default = 0

class ShuffleSwim(Toggle):
  """Shuffles the ability to swim into the pool. If you touch water without the
  ability to swim, you die."""
  default = 0

class EjectionLaunch(Toggle):
  """
  Consider use of ejection launches in logic.

  An example of an ejection launch is clipping into the Pom to launch yourself
  out of the Jester Boots area in Prismic Palace.
  """
  default = 0

class ZTarget(Toggle):
  """
  Consider obscure use of z-targeting in logic.

  An example is using z-targeting to simultaneously move backwards and fire
  Bubbles to build significant speed in the air.
  """
  default = 0

class MomentumCancel(Toggle):
  """
  Consider pausing to cancel momentum in logic.

  An example is repeatedly pausing while using Wings to gain more distance.
  """
  default = 0

class AbilityToggle(Toggle):
  """
  Consider toggling abilities in logic.

  An example is hovering with the Wings, then enabling Double Jump to gain extra height.
  """
  default = 0

class OutOfBounds(Toggle):
  """
  Consider out of bounds movement in logic.

  An example is clipping out of the lake using the tombstone fish in Lostleaf Lake.
  """
  default = 0

class WingJump(Toggle):
  """
  Consider advanced use of the Wings in logic.

  Examples include jumping and immediately activating the Wings to gain more distance, and riding along slopes to gain height.
  """
  default = 0

class WingStorage(Toggle):
  """
  Consider Wing storage in logic.

  Sliding from an unwalkable slope onto walkable terrain while the Wings are activated makes your next airtime trigger Wings without an additional jump press, enabling a significant boost to height and distance.
  """
  default = 0

class BubbleJump(Choice):
  """
  Consider use of Bubble for movement in logic.

  Disable (default): Don't include in logic.
  Enable: Consider floating by holding Bubble in logic.
  With Recoil: Also consider firing Bubbles to launch yourself backwards in logic.
  """
  default = 0
  option_disable = 0
  option_enable = 1
  option_with_recoil = 2

class RollDisjoint(Toggle):
  """
  Consider use of roll disjoints in logic.

  Roll disjoints involve canceling roll while after attempting to trigger
  another animation, like a Tail Whip, in order to disjoint Fynn's hitbox to
  touch loading zones through walls.
  """
  default = 0

class DamageBoost(Toggle):
  """
  Consider use of damage boosts in logic.
  """
  default = 0

class GroundTailJump(Toggle):
  """
  Consider use of grounded Tail Whip jumps in logic.

  If you Tail Whip on the ground and then jump, you are able to jump again once
  the animation ends.
  """
  default = 0

class AirTailJump(Toggle):
  """
  Consider use of aerial Tail Whip jumps in logic.

  If you land while attempting a Tail Whip in the air, you launch yourself
  forward, and are able to jump for a short period of time, gaining a small
  amount of extra height compared to a standard jump.
  """
  default = 0

@dataclass
class CavernOfDreamsOptions(PerGameCommonOptions):
  difficulty: Difficulty

  shroomsanity: Shroomsanity
  cardsanity: Cardsanity
  eventsanity: Eventsanity
  gratitudesanity: Gratitudesanity

  shuffle_abilities: ShuffleAbilities

  shuffle_high_jump: ShuffleHighJump
  shuffle_roll: ShuffleRoll
  shuffle_sprint: ShuffleSprint
  shuffle_swim: ShuffleSwim

  super_bounce: SuperBounce
  super_bubble_jump: SuperBubbleJump

  jester_boots_anywhere: JesterBootsAnywhere

  ejection_launch: EjectionLaunch
  z_target: ZTarget
  momentum_cancel: MomentumCancel
  ability_toggle: AbilityToggle
  out_of_bounds: OutOfBounds

  wing_jump: WingJump
  wing_storage: WingStorage

  bubble_jump: BubbleJump
  roll_disjoint: RollDisjoint
  damage_boost: DamageBoost

  ground_tail_jump: GroundTailJump
  air_tail_jump: AirTailJump

  death_link: DeathLink
