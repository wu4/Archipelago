from typing import TypeAlias, Literal

TempItem: TypeAlias = Literal[
    "Apple",
    "Medicine",
    "Bubble Conch",
    "Sage's Gloves",
    "Lady Opal's Head",
    "Shelnert's Fish",
    "Mr. Kerrington's Wings",

    "Jester Boots"
]

MaybeTempItem: TypeAlias = TempItem | None
