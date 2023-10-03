from BaseClasses import CollectionState

from worlds.AutoWorld import LogicMixin
from .Utils import get_underscored
from .Extracted import damage_resistances

from typing import cast, TYPE_CHECKING


class MetroidPrimeLogic(LogicMixin):
    def metroid_prime_has_energy(self, player: int, amount: int) -> bool:
        self_state = cast(CollectionState, self)
        total_energy = 99 + (self_state.count("Energy Tank", player) * 100)
        return total_energy > amount

    def metroid_prime_resist_damage(self, player: int, damage: int, damage_type: str) -> int:
        self_state = cast(CollectionState, self)

        multipliers = damage_resistances.get(damage_type)
        if multipliers is None: return damage

        smallest_multiplier = 1.0

        for (suit_name, multiplier) in multipliers.items():
            if multiplier < smallest_multiplier and self_state.has(suit_name, player):
                smallest_multiplier = multiplier

        return int(float(damage) * smallest_multiplier)
    
    def metroid_prime_can_sustain_damage(self, player: int, amount: int, damage_type: str) -> bool:
        return self.metroid_prime_has_energy(player, self.metroid_prime_resist_damage(player, amount, damage_type))

    def metroid_prime_has_misc(self, player: int, misc_name: str) -> bool:
        return False
    
    def metroid_prime_has_missiles(self, player: int, amount: int) -> bool:
        self_state = cast(CollectionState, self)
        return self_state.has("Missile Launcher", player) and ((self_state.count("Missile", player) + 1) * 5) >= amount