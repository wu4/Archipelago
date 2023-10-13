from BaseClasses import Item, ItemClassification

class MetroidPrimeItem(Item):
    game = "Metroid Prime"
    @staticmethod
    def get_classification(name: str) -> ItemClassification:
        # if name in ["Nothing"]:
        #     return ItemClassification.filler
        # return ItemClassification.progression
        if name in ["Nothing", "Health Refill"]:
            return ItemClassification.filler
        # elif name in ["Missile", "Energy Tank", "Power Bomb"]:
        #     return ItemClassification.useful
        else:
            return ItemClassification.progression

    def __init__(self, name: str, code: int, player: int):
        super().__init__(name, MetroidPrimeItem.get_classification(name), code, player)
        
class MetroidPrimeEvent(Item):
    game = "Metroid Prime"
    
    def __init__(self, name: str, player: int, skippable: bool = False):
        super().__init__(name, ItemClassification.progression if not skippable else ItemClassification.useful, None, player)