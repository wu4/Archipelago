from inflection import underscore

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

import re
link_re = re.compile(r"<a href='([^']+)'>([^<]+)</a>")

def parse_trick_desc(trick_desc: str) -> str:
    links_replaced = link_re.sub(lambda match: f"{match.group(2)} ({match.group(1)})", trick_desc)
    return links_replaced.replace("<br />", "\\n")
