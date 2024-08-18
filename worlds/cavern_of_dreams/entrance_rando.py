from collections.abc import Generator, Iterable
from typing import TYPE_CHECKING, TypeAlias

from .options import CarryThroughDoors, Carryablesanity
from .regions import CavernOfDreamsEntrance, CavernOfDreamsRegion
from .ap_generated.entrance_rando import parent_regions, create_entrances as generated_create_entrances, bilinear, one_way
if TYPE_CHECKING:
    from .world import CavernOfDreamsWorld

EntranceExitPair: TypeAlias = tuple[str, str]

def _include_flipped(ts: Iterable[EntranceExitPair]) -> Generator[EntranceExitPair, None, None]:
    for t in ts:
        yield t
        yield t[1], t[0]

def _randomize_entrance_pairs(
    world: "CavernOfDreamsWorld",
    entrances: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    as_dict = dict(entrances)
    shuffled_values = list(as_dict.values())
    world.random.shuffle(shuffled_values)
    return list(zip(as_dict, shuffled_values))

def _make_entrance_underwater(entrance: "CavernOfDreamsEntrance"):
    old_access_rule = entrance.access_rule
    entrance.access_rule = lambda state: state.has("Swim", entrance.player) and old_access_rule(state)

def _link_entrances(world: "CavernOfDreamsWorld", entrance_map: list[tuple[str,str]], entrances: dict[str, tuple[CavernOfDreamsEntrance | None, bool]]):

    keep_carryables = world.options.carry_through_doors == CarryThroughDoors.option_true
    for from_entrance_name, to_entrance_name in entrance_map:
        from_entrance, _ = entrances[from_entrance_name]
        if from_entrance is None: continue
        _, to_entrance_underwater = entrances[to_entrance_name]

        if to_entrance_underwater:
            _make_entrance_underwater(from_entrance)

        from_parent_region = parent_regions[from_entrance_name]
        from_entrance.parent_region = world.multiworld.get_region(from_parent_region, world.player)
        from_entrance.parent_region.exits.append(from_entrance)
        to_parent_region_name = parent_regions[to_entrance_name]
        to_parent_region = world.multiworld.get_region(to_parent_region_name, world.player)

        print(f"{from_entrance_name} -> {to_entrance_name}")

        if keep_carryables:
            from_entrance.connect(to_parent_region)
        else:
            # create an intermediate region wherein all carryables are dropped
            intermediate_connection_name = f"{from_entrance_name} -> (dropping carryables) -> {to_entrance_name}"

            intermediate_region = CavernOfDreamsRegion(intermediate_connection_name, world.player, world.multiworld)

            intermediate_entrance = CavernOfDreamsEntrance(world.player, intermediate_connection_name, intermediate_region)
            intermediate_entrance.dont_care_access_rule = lambda s: True
            intermediate_entrance.reject_carryables = True

            intermediate_region.exits.append(intermediate_entrance)
            world.multiworld.regions.append(intermediate_region)

            from_entrance.connect(intermediate_region)
            intermediate_entrance.connect(to_parent_region)


def create_and_link_entrances(world: "CavernOfDreamsWorld") -> list[EntranceExitPair]:
    entrances = generated_create_entrances(world)

    if world.options.entrance_rando:
        rando_bilinear = _randomize_entrance_pairs(world, bilinear)
        rando_one_way = _randomize_entrance_pairs(world, one_way)
        entrance_map = [*rando_one_way, *_include_flipped(rando_bilinear)]
        # print("rando map:")
        # for warp, dest in entrance_map:
        #     print(f"{warp} -> {dest}")
    else:
        entrance_map = [*one_way, *_include_flipped(bilinear)]

    _link_entrances(world, entrance_map, entrances)

    if world.options.entrance_rando:
        return entrance_map
    else:
        # the client doesnt need to fudge with entrances otherwise
        return []
