from BaseClasses import Location

class MetroidPrimeLocation(Location):
    game = "Metroid Prime"

    def __init__(self, player: int, name="", code=None, parent=None):
        super(MetroidPrimeLocation, self).__init__(player, name, code, parent)
        self.event = code is None