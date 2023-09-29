from BaseClasses import Location

from .Utils import region_format
from .data import regions
from .data import PickupNode, Node

locations: list[str] = [
    region_format(node_name, area_name, region_name)
    for region_name, region in regions.items()
    for area_name, area in region.items()
    for node_name, node in area.items()
    if isinstance(node, PickupNode) and "default" in node.layers
]


class MetroidPrimeLocation(Location):
    game = "Metroid Prime"

    # override constructor to automatically mark event locations as such
    def __init__(self, player: int, name="", code=None, parent=None):
        super(MetroidPrimeLocation, self).__init__(player, name, code, parent)
        self.event = code is None