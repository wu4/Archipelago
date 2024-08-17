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


class StartLocation(Choice):
    """
    Where Fynn should start their adventure.

    NOTE: Not all start locations are made equally. In some particular cases,
    Fynn will be given additional items to start with in order to minimize the
    chances of BK (or to make the seed playable).
    """
    default = 0

    option_sun_cavern = 0
    option_moon_cavern = 1

    option_lostleaf_lobby = 2
    option_armada_lobby = 3
    option_prismic_lobby = 4
    option_gallery_lobby = 5

    option_lostleaf_lake = 6
    option_lostleaf_church = 7
    option_lostleaf_treehouse = 8
    option_lostleaf_crypt = 9

    option_armada_outside = 10
    option_armada_inside = 11
    option_armada_earth_drone = 12
    option_armada_fire_drone = 13
    option_armada_water_drone = 14

    option_prismic_valley = 15
    option_prismic_palace = 16
    option_heavens_gate = 17
    option_observatory = 18

    option_gallery_foyer = 19
    option_gallery_earth = 20
    option_gallery_fire = 21
    option_gallery_water = 22

    option_wastes_of_eternity = 23
    option_coils_of_agony = 24
    option_pits_of_despair = 25


class EntranceRando(Toggle):
    """
    Whether or not to randomize entrances.
    """
    default = 0


class SuperBounce(Choice):
    """
    How to treat super bounce, a tech that enables gaining significant height using an aerial tailwhip while rolling.

    Disable (default): Prevents the use of super bounce.
    Enable: Allows the use of super bounce, considering its use in logic.
    Shuffle: Shuffles super bounce into the pool, considering its use in logic.
    """
    default = 0
    option_disable = 0
    option_enable = 1
    option_shuffle = 2


class SuperBubbleJump(Choice):
    """
    How to treat super bubble jump, a tech that enables gaining significant height using bubble shots while rolling.

    Disable (default): Prevents the use of super bubble jump.
    Enable: Allows the use of super bubble jump, considering its use in logic.
    Shuffle: Shuffles super bubble jump into the pool, considering its use in logic.
    """
    default = 0
    option_disable = 0
    option_enable = 1
    option_shuffle = 2


class AirSwim(Choice):
    """
    How to treat air swim, a tech that enables free movement in the air.

    Disable (default): Prevents the use of air swim.
    Enable: Allows the use of air swim, considering its use in logic.
    Shuffle: Shuffles air swim into the pool, considering its use in logic.
    """
    default = 0
    option_disable = 0
    option_enable = 1
    option_shuffle = 2


class Eventsanity(Toggle):
    """Shuffles events into the pool. For example, healing the Giant is a location with a check."""
    default = 0


class Gratitudesanity(Choice):
    """
    How to treat Gratitude, the resource you gain from taking care of your family.

    Disable (default): Gratitude is obtained by feeding hatched fellas, as in the original game.
    Enable: Shuffles gratitude into the pool. Feeding hatched fellas is now a location.
    Split: Shuffles gratitude and the Sun Cavern teleports into the pool separately.
    """
    default = 0
    option_disable = 0
    option_enable = 1
    option_split = 2


class Carryablesanity(Choice):
    """
    How to treat carryable items, like the apples in Lostleaf Lake, Jester
    Boots its various locations, and so on.

    Disable (default): Leave them in their usual spots.
    Kind: Shuffle them into the pool. Entering doorways will cause you to drop
    your carryable, ensuring short pathways.
    Mean: Shuffle them into the pool without mercy. An example scenario is that
    you may have to carry Shelnert's Fish from Shelwart's tombstone through
    Lostleaf Lake, into Sun Cavern, then through Moon Cavern, Gallery Lobby,
    the Foyer, and finally into the Earth Lobby to toss into the painting.
    """
    default = 0
    option_disable = 0
    option_kind = 1
    option_mean = 2


class CarryThroughDoors(Toggle):
    """
    Allows Fynn to carry temporary items through doorways.

    When disabled, Fynn drops anything they're carrying as they move to a new
    area. Forces Carryablesanity to Kind.
    """
    default = 1


class Shroomsanity(Toggle):
    """Shuffles all shrooms into the pool."""
    default = 1


class ShuffleAbilities(Toggle):
    """Shuffles the abilities the Sage gives you into the pool."""
    default = 1


class ShuffleHighJump(Toggle):
    """Shuffles the ability to High Jump into the pool."""
    default = 0


class ShuffleClimb(Toggle):
    """Shuffles the ability to climb into the pool."""
    default = 0


class ShuffleCarry(Toggle):
    """Shuffles the ability to pick up and carry throwables into the pool."""
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


class IncludeDoubleJump(Toggle):
    """Shuffles a brand new ability to double jump into the pool."""
    default = 0


class ExcludeFlight(Toggle):
    """Removes Flight from the pool. Highly recommended."""
    default = 1


class ExcludeWings(Toggle):
    """Removes Wings from the pool. For the brave and bold."""
    default = 0


class SplitTail(Toggle):
    """
    Splits the Tail into grounded and aerial versions, requiring you to obtain both
    to have the full power of the Tail Whip.
    """
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

    Roll disjoints involve canceling roll after attempting to trigger another
    animation, like a Tail Whip, in order to disjoint Fynn's hitbox to touch
    loading zones through walls.
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


class JesterBootsSlopeMovement(Toggle):
    """
    Allows use of the Jester Boots to climb normally unwalkable slopes in
    logic.

    Some slopes can uniquely be climbed while wearing the Jester Boots. For
    example, you can grab the Deep Woods egg location by simply walking up the
    wall with the Jester Boots.
    """
    default = 0


class AllowFun(Toggle):
    """
    Allows making use of some combinations of abilities that are out-of-logic.

    When disabled, the Jester Boots have a distaste for Fynn carrying items,
    and will refuse to allow Fynn to pick items up unless they are taken off
    first. They're only fine with the idea if you are within the boundaries of
    the Deep Woods.
    """
    default = 0


@dataclass
class CavernOfDreamsOptions(PerGameCommonOptions):
    difficulty: Difficulty

    start_location: StartLocation
    entrance_rando: EntranceRando

    shroomsanity: Shroomsanity
    eventsanity: Eventsanity
    gratitudesanity: Gratitudesanity
    carryablesanity: Carryablesanity

    shuffle_abilities: ShuffleAbilities

    shuffle_high_jump: ShuffleHighJump
    shuffle_climb: ShuffleClimb
    shuffle_carry: ShuffleCarry
    shuffle_roll: ShuffleRoll
    shuffle_sprint: ShuffleSprint
    shuffle_swim: ShuffleSwim
    include_double_jump: IncludeDoubleJump
    exclude_flight: ExcludeFlight
    exclude_wings: ExcludeWings
    split_tail: SplitTail

    super_bounce: SuperBounce
    super_bubble_jump: SuperBubbleJump
    air_swim: AirSwim

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

    jester_boots_slope_movement: JesterBootsSlopeMovement

    carry_through_doors: CarryThroughDoors

    allow_fun: AllowFun

    death_link: DeathLink
