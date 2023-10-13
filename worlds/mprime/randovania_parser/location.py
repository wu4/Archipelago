from .types.shared import AbsoluteLocation
LocationTuple = tuple[str, str, str]

def as_location_tuple(location: AbsoluteLocation) -> LocationTuple:
    return (location["node"], location["area"], location["region"])

def location_tuple_format(location: LocationTuple) -> str:
    return location_format(location[0], location[1], location[2])

def location_format(node_name: str, area_name: str, region_name: str) -> str:
    return f"{node_name} ({area_name}, {region_name})"