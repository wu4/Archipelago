from worlds.generic.Rules import ItemRule
from .carryables import CavernOfDreamsCarryable
from .ap_generated.data import item_group_sets

_eggs = item_group_sets["Egg"]
no_eggs: ItemRule = lambda item: item.name not in _eggs

no_carryables: ItemRule = lambda item: not isinstance(item, CavernOfDreamsCarryable)

no_carryables_or_eggs: ItemRule = lambda item: item.name not in _eggs and not isinstance(item, CavernOfDreamsCarryable)
