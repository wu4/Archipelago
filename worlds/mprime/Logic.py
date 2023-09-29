from BaseClasses import MultiWorld, CollectionState

from worlds.AutoWorld import LogicMixin
from .Items import events_short_to_long, items_short_to_long
from .Utils import get_underscored
from .data import damage_resistances

from typing import cast, TYPE_CHECKING

if TYPE_CHECKING:
    from .data.Types import ResourceData

# LogicMixin is monkey-patched over CollectionState
# lets avoid polluting the namespace
def get_player_option(multiworld: MultiWorld, player, option_name: str):
    # for example, multiworld.l_jump[player]
    return getattr(multiworld, option_name)[player]


class MetroidPrimeLogic(LogicMixin):
    def metroid_prime_has_energy(self, player: int, amount: int) -> bool:
        self_state = cast(CollectionState, self)
        return 99 + (self_state.count("EnergyTank", player) * 100) > amount

    def metroid_prime_resist_damage(self, player: int, damage: int, damage_type: str) -> int:
        self_state = cast(CollectionState, self)

        multipliers = damage_resistances.get(damage_type)
        if multipliers is None: return damage

        smallest_multiplier = 1.0

        for (suit_name, multiplier) in multipliers.items():
            if multiplier < smallest_multiplier and self_state.has(suit_name, player):
                smallest_multiplier = multiplier

        return int(float(damage) * smallest_multiplier)

    def metroid_prime_has_resource(self, player: int, resource_data: "ResourceData") -> bool:
        self_state = cast(CollectionState, self)

        if resource_data["type"] == "items":
            amount = resource_data["amount"]
            resource_name = items_short_to_long[resource_data["name"]]
            if resource_name == "Missile":
                return self_state.has("Missile Launcher", player) and (self_state.count("Missile", player) * 5 >= amount)
            return self_state.has(resource_name, player, resource_data["amount"])

        elif resource_data["type"] == "tricks":
            value = get_player_option(self_state.multiworld, player, get_underscored(f"metroid_prime_{resource_data['name']}")).value

            return (resource_data["amount"] >= value)

        elif resource_data["type"] == "damage":
            resisted_damage = self.metroid_prime_resist_damage(player, resource_data["amount"], resource_data["name"])

            return self.metroid_prime_has_energy(player, resisted_damage)

        elif resource_data["type"] == "events":
            return self_state.has(events_short_to_long[resource_data["name"]], player)

        elif resource_data["type"] == "misc":
            # not implemented
            return True

        raise NotImplementedError