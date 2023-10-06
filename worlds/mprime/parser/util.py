from inflection import underscore
from typing import Iterable, TypeVar, Callable, TYPE_CHECKING
from . import Types as DataTypes


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

def intersperse(val, sequence):
    first = True
    for item in sequence:
        if not first:
            yield val
        yield item
        first = False

def absolute_location_format(location: DataTypes.AbsoluteLocation) -> str:
    return absolute_node_format(location["node"], location["area"], location["region"])

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