from BaseClasses import Item, ItemClassification
from .ap_generated import data

class CavernOfDreamsItem(Item):
    game = "Cavern of Dreams"
    @staticmethod
    def get_classification(name: str) -> ItemClassification:
        if name.startswith("Shroom"):
            return ItemClassification.filler
        else:
            return ItemClassification.progression

    def __init__(self, name: str, code: int, player: int):
        super().__init__(name, CavernOfDreamsItem.get_classification(name), code, player)

class CavernOfDreamsEvent(Item):
    game = "Cavern of Dreams"

    def __init__(self, name: str, player: int, skippable: bool = False):
        super().__init__(name, ItemClassification.progression if not skippable else ItemClassification.useful, None, player)
