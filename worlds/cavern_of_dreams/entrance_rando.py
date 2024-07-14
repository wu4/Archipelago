from random import shuffle


def randomize_entrances(
    entrances: list[tuple[str, str]]
) -> list[tuple[str, str]]:
    as_dict = dict(entrances)
    shuffled_values = list(as_dict.values())
    shuffle(shuffled_values)
    return list(zip(as_dict, shuffled_values))
