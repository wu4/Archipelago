from typing import TypeVar, Optional, Callable
from inflection import underscore

T = TypeVar("T")
def cached_var(generator: Callable[[], T]) -> Callable[[], T]:
    cached: Optional[T] = None
    return lambda: locals().setdefault("cached", generator()) if cached == None else cached


V = TypeVar("V")
V2 = TypeVar("V2")

def map_dict(func: Callable[[V], V2], dictionary: dict[str, V]) -> dict[str, V2]:
    return dict((k, func(v)) for (k, v) in dictionary.items())


def region_format(node_name: str, area_name: str, region_name: str) -> str:
    return f"{node_name} ({area_name}, {region_name})"


underscored_cache: dict[str, str] = {}
def get_underscored(text: str):
    underscored = underscored_cache.get(text)
    if underscored is None:
        underscored = underscore(text)
        underscored_cache[text] = underscored

    return underscored


def relative_to_script(script_path: str, rel_path: str) -> str:
    import os.path
    return os.path.join(os.path.dirname(os.path.abspath(script_path)), rel_path)