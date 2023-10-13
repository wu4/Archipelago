from typing import TypedDict, Literal, TypeAlias, Optional

class Template(TypedDict):
    type: Literal["template"]
    data: str


class LogicData(TypedDict):
    comment: Optional[str]
    items: list["Requirement"]


class Logic(TypedDict):
    type: Literal["and", "or"]
    data: LogicData


class ResourceData(TypedDict):
    type: Literal["items", "tricks", "damage", "events", "misc"]
    name: str
    amount: int
    negate: bool


class Resource(TypedDict):
    type: Literal["resource"]
    data: ResourceData


Requirement: TypeAlias = Template | Logic | Resource