from BaseClasses import Item
from .data import header

items_short_to_long: dict[str, str] = {
    short_name: item["long_name"]
    for short_name, item in header["resource_database"]["items"].items()
    if not short_name in ["LockedPB", "LockedMissile"]
}

items: list[str] = list(items_short_to_long.values())

events_short_to_long: dict[str, str] = {
  short_name: event["long_name"]
  for short_name, event in header["resource_database"]["events"].items()
}

events_long_to_short: dict[str, str] = {
  event["long_name"]: short_name
  for short_name, event in header["resource_database"]["events"].items()
}

class MetroidPrimeItem(Item):
    game = "Metroid Prime"