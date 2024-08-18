from BaseClasses import Item, ItemClassification
from .ap_generated.data import item_group_sets

class CavernOfDreamsItem(Item):
    game = "Cavern of Dreams"

    @staticmethod
    def get_classification(name: str) -> ItemClassification:
        if name in item_group_sets["Card"]:
            return ItemClassification.filler
        elif name in item_group_sets["Egg"]:
            return ItemClassification.progression_skip_balancing
        elif name == "Nothing":
            return ItemClassification.filler
        else:
            return ItemClassification.progression

    def __init__(self, name: str, code: int, player: int):
        if name == "Shroom":
            super().__init__("Shroom", ItemClassification.progression_skip_balancing, code, player)
        else:
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
