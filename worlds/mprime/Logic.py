from BaseClasses import CollectionState

from typing import Callable

generation_exports: dict[str, Callable] = {}

def generate_as(name: str):
    def inner(func):
        generation_exports[name] = func
        return func

    return inner

def has_energy(state: CollectionState, player: int, amount: int) -> bool:
    total_energy = 99 + (state.count("Energy Tank", player) * 100)
    return total_energy > amount

def resist_damage(state: CollectionState, player: int, damage: int, damage_type: str) -> int:
    from .generated import damage_resistances

    multipliers = damage_resistances.get(damage_type)
    if multipliers is None: return damage

    smallest_multiplier = min((
        1.0,
        *(
            multiplier
            for suit_name, multiplier in multipliers.items()
            if state.has(suit_name, player)
        )
    ))

    return int(float(damage) * smallest_multiplier)

@generate_as("l_csd")
def can_sustain_damage(state: CollectionState, player: int, damage: int, damage_type: str) -> bool:
    """Returns whether or not `player` can survive `damage` of `damage_type` in `state`."""
    return has_energy(state, player, resist_damage(state, player, damage, damage_type))

@generate_as("l_hmisc")
def has_misc(state: CollectionState, player: int, misc_name: str) -> bool:
    """Returns whether or not `player` has misc option `misc_name` enabled. Stub. Returns False."""
    return False

@generate_as("l_hm")
def has_missiles(state: CollectionState, player: int, amount: int) -> bool:
    """Returns whether or not `player` has defined `amount` of missiles in `state`."""
    return state.has("Missile Launcher", player) and ((state.count("Missile", player) + 1) * 5) >= amount