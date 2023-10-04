from BaseClasses import CollectionState

from worlds.AutoWorld import LogicMixin
from .utils import get_underscored
from .generated import damage_resistances

def has_energy(state: CollectionState, player: int, amount: int) -> bool:
    total_energy = 99 + (state.count("Energy Tank", player) * 100)
    return total_energy > amount

def resist_damage(state: CollectionState, player: int, damage: int, damage_type: str) -> int:
    multipliers = damage_resistances.get(damage_type)
    if multipliers is None: return damage

    smallest_multiplier = 1.0

    for (suit_name, multiplier) in multipliers.items():
        if multiplier < smallest_multiplier and state.has(suit_name, player):
            smallest_multiplier = multiplier

    return int(float(damage) * smallest_multiplier)

def can_sustain_damage(state: CollectionState, player: int, damage: int, damage_type: str) -> bool:
    return has_energy(state, player, resist_damage(state, player, damage, damage_type))

def has_misc(state: CollectionState, player: int, misc_name: str) -> bool:
    return False

def has_missiles(state: CollectionState, player: int, amount: int) -> bool:
    return state.has("Missile Launcher", player) and ((state.count("Missile", player) + 1) * 5) >= amount