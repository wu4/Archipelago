from inflection import underscore
from typing import Iterable, TypeVar, Callable
from .types.shared import AbsoluteLocation
import re

def relative_to_file(file_path: str, rel_path: str) -> str:
    import os.path
    return os.path.join(os.path.dirname(os.path.abspath(file_path)), rel_path)

def trick_name_gen(trick_name: str):
    trick_name = underscore(f"{trick_name.replace(' ', '')}")
    if trick_name == "combat/scan_dash":
        return "scan_dash"
    elif trick_name == "spinnerswithout_boost":
        return "spinners_without_boost"
    elif trick_name == "single_room_outof_bounds":
        return "single_room_oob"
    else:
        return trick_name

link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\\n")


def intersperse(val, sequence):
    first = True
    for item in sequence:
        if not first:
            yield val
        yield item
        first = False

LocationTuple = tuple[str, str, str]

def as_location_tuple(location: AbsoluteLocation) -> LocationTuple:
    return (location["node"], location["area"], location["region"])

def absolute_location_tuple_format(location: LocationTuple) -> str:
    return absolute_node_format(location[0], location[1], location[2])

def absolute_node_format(node_name: str, area_name: str, region_name: str) -> str:
    return f"{node_name} ({area_name}, {region_name})"

V = TypeVar("V")
V2 = TypeVar("V2")

def map_dict(func: Callable[[V], V2], dictionary: dict[str, V]) -> dict[str, V2]:
    return dict((k, func(v)) for (k, v) in dictionary.items())

A = TypeVar("A")
def partition(pred: Callable[[A], bool], iterable: Iterable[A]) -> tuple[list[A], list[A]]:
    trues: list[A] = []
    falses: list[A] = []
    for item in iterable:
        if pred(item):
            trues.append(item)
        else:
            falses.append(item)
    return trues, falses