from BaseClasses import Item, ItemClassification
from .ap_generated.data import item_group_sets

# item_groups and item_group_sets are identical aside from being lists and sets
# we use lists for calculating progressive shrooms to keep things deterministic
# sets otherwise for performance

def get_shroom_groups():
    from .ap_generated.data import item_groups
    shrooms = item_groups["Shroom"]
    return set(shrooms[:281]), set(shrooms[281:])

progressive_shrooms, non_progressive_shrooms = get_shroom_groups()

class CavernOfDreamsItem(Item):
    game = "Cavern of Dreams"

    @staticmethod
    def get_classification(name: str) -> ItemClassification:
        if name in item_group_sets["Card"]:
            return ItemClassification.filler
        elif name in item_group_sets["Egg"] or name in progressive_shrooms:
            return ItemClassification.progression_skip_balancing
        elif name in non_progressive_shrooms:
            return ItemClassification.filler
        else:
            return ItemClassification.progression

    def __init__(self, name: str, code: int, player: int):
        super().__init__(name, CavernOfDreamsItem.get_classification(name), code, player)


class CavernOfDreamsEvent(Item):
    game = "Cavern of Dreams"

    def __init__(self, name: str, player: int, skippable: bool = False):
        super().__init__(
            name,
            ItemClassification.progression if not skippable else ItemClassification.useful,
            None,
            player
        )
