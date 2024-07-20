from worlds.generic.Rules import ItemRule
from .ap_generated.data import item_group_sets

_shrooms = item_group_sets["Shroom"]
is_shroom: ItemRule = lambda item: item.name in _shrooms

_events = item_group_sets["Event"]
is_event: ItemRule = lambda item: item.name in _events

_eggs = item_group_sets["Egg"]
is_egg: ItemRule = lambda item: item.name in _eggs
