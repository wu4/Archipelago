from typing import TypedDict

class AbsoluteLocation(TypedDict):
    region: str
    area: str
    node: str

class Vector3(TypedDict):
    x: float
    y: float
    z: float
