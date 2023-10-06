from typing import TYPE_CHECKING, Optional
import orjson
if TYPE_CHECKING:
  from . import Types as DataTypes

HEADER_FILENAME: str = "data/randovania_data/json_data/header.json"

def relative_to_script(script_path: str, rel_path: str) -> str:
    import os.path
    return os.path.join(os.path.dirname(os.path.abspath(script_path)), rel_path)

def _get_header() -> DataTypes.Header:
    with open(relative_to_script(__file__, HEADER_FILENAME), "r") as f:
        return orjson.loads(f.read())

header = _get_header()

items_short_to_long: dict[str, str] = {
    short_name: item["long_name"]
    for short_name, item in header["resource_database"]["items"].items()
    if not short_name in ["LockedPB", "LockedMissile", "Unknown1", "Unknown2", "HealthRefill"]
}

items: list[str] = list(items_short_to_long.values())

events_short_to_long: dict[str, str] = {
  short_name: event["long_name"]
  for short_name, event in header["resource_database"]["events"].items()
}

tricks_short_to_long = {
    short: trick["long_name"]
    for short, trick in header["resource_database"]["tricks"].items()
}

def parse_dock_requirements(dock: DataTypes.DockWeaknessEntry) -> Optional[str]:
    req = parse_connection_data(dock["requirement"])
    if req == "lambda _: False":
        return None
    lock = dock["lock"]
    if lock is None:
        return req
    else:
        lock_req = parse_connection_data(lock["requirement"])
        if lock_req == "lambda _: False":
            return None
        elif req == "None":
            return lock_req
        elif lock_req == "None":
            return req
        else:
            return f"({req}) and ({lock_req})"

dock_requirements: dict[str, Optional[str]] = {
    dock_type: parse_dock_requirements(item)
    for docks in header["dock_weakness_database"]["types"].values()
    for dock_type, item in docks["items"].items()
}