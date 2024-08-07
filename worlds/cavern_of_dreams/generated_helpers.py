from typing import TYPE_CHECKING, Callable

if TYPE_CHECKING:
    from BaseClasses import CollectionState

def construct_rule(player: int, rules: tuple[tuple[bool, str]], should_print: bool = False) -> "Callable[[CollectionState], bool]":
    rules_str = " or ".join(f"({rule_str})" for condition, rule_str in rules if condition)

    if rules_str == "":
        rules_str = "False"

    if should_print:
        print(rules_str)

    return eval(f"lambda s:{rules_str}", {"p": player})
