from BaseClasses import Entrance, Item, Location, LocationProgressType, MultiWorld, Region, CollectionState
from typing import Optional, TypedDict, Union

class Highlight(TypedDict):
    spheres: list[tuple[CollectionState, list[Location]]]

# inject this into fulfills_accessibility
if False:
    def fulfills_accessibility(self, state: Optional[CollectionState] = None):
        """Check if accessibility rules are fulfilled with current or supplied state."""
        
        if not state:
            state = CollectionState(self)
        players: Dict[str, Set[int]] = {
            "minimal": set(),
            "items": set(),
            "locations": set()
        }
        for player, access in self.accessibility.items():
            players[access.current_key].add(player)

        beatable_fulfilled = False

        def location_condition(location: Location):
            """Determine if this location has to be accessible, location is already filtered by location_relevant"""
            if location.player in players["minimal"]:
                return False
            return True

        def location_relevant(location: Location):
            """Determine if this location is relevant to sweep."""
            if location.progress_type != LocationProgressType.EXCLUDED \
                and (location.player in players["locations"] or location.event
                     or (location.item and location.item.advancement)):
                return True
            return False

        def all_done() -> bool:
            """Check if all access rules are fulfilled"""
            if not beatable_fulfilled:
                return False
            if any(location_condition(location) for location in locations):
                return False  # still locations required to be collected
            return True

        locations = [location for location in self.get_locations() if location_relevant(location)]
        spheres: list[tuple[CollectionState,list[Location]]] = []
        
        def visualize():
            from Fill import visualize_regions
            visualize_regions(self.get_region("Menu", 1), 'wewlad.puml', state=state, highlights={"spheres":spheres})

        while locations:
            sphere: tuple[CollectionState, list[Location]] = (state.copy(), [])
            for n in range(len(locations) - 1, -1, -1):
                if locations[n].can_reach(sphere[0]):
                    sphere[1].append(locations.pop(n))

            if not sphere[1]:
                # ran out of places and did not finish yet, quit
                logging.warning(f"Could not access required locations for accessibility check."
                                f" Missing: {locations}")
                visualize()
                return False

            for location in sphere[1]:
                if location.item:
                    state.collect(location.item, True, location)

            if self.has_beaten_game(state):
                beatable_fulfilled = True

            spheres.append(sphere)

            if all_done():
                visualize()
                return True
            
        visualize()

        return False

def visualize_regions(root_region: Region, file_name: str, *,
                      show_entrance_names: bool = True, show_locations: bool = True, show_other_regions: bool = True,
                      linetype_ortho: bool = True,
                      state: Optional[CollectionState] = None,
                      highlights: Optional[Highlight] = None) -> None:
    """Visualize the layout of a world as a PlantUML diagram.

    :param root_region: The region from which to start the diagram from. (Usually the "Menu" region of your world.)
    :param file_name: The name of the destination .puml file.
    :param show_entrance_names: (default False) If enabled, the name of the entrance will be shown near each connection.
    :param show_locations: (default True) If enabled, the locations will be listed inside each region.
            Priority locations will be shown in bold.
            Excluded locations will be stricken out.
            Locations without ID will be shown in italics.
            Locked locations will be shown with a padlock icon.
            For filled locations, the item name will be shown after the location name.
            Progression items will be shown in bold.
            Items without ID will be shown in italics.
    :param show_other_regions: (default True) If enabled, regions that can't be reached by traversing exits are shown.
    :param linetype_ortho: (default True) If enabled, orthogonal straight line parts will be used; otherwise polylines.

    Example usage in World code:
    from Utils import visualize_regions
    visualize_regions(self.multiworld.get_region("Menu", self.player), "my_world.puml")

    Example usage in Main code:
    from Utils import visualize_regions
    for player in world.player_ids:
        visualize_regions(world.get_region("Menu", player), f"{world.get_out_file_name_base(player)}.puml")
    """
    assert root_region.multiworld, "The multiworld attribute of root_region has to be filled"
    from collections import deque
    import re

    uml: list[str] = list()
    seen: set[Region] = set()
    accessible_regions: set[Region] = set()
    regions: deque[Region] = deque((root_region,))
    multiworld: MultiWorld = root_region.multiworld
    if state is None:
        state = multiworld.state

    # seen2: set[Region] = set()
    # while regions:
    #     if (current_region := regions.popleft()) not in seen2:
    #         seen2.add(current_region)
    #         for exit in current_region.exits:
    #             if not exit.connected_region: continue
    #             if self.can_reach(exit.name, 'Entrance'):
    #                 accessible_regions.add(exit.connected_region)

    #         regions.extend(exit_.connected_region for exit_ in current_region.exits if exit_.connected_region)

    # regions = deque((root_region,))
    
    regions_by_prime_region: dict[str, list[str]] = {}
    
    # reg = re.compile(r", ([^,]+?)\)$")
    # def parse_region_name(region: Region) -> str:
    #     if region.name == "Menu":
    #         return "Menu"
    #     match = reg.findall(region.name)[0]
    #     return match
    # 
    # def get_prime_region_from_region(region: Region) -> list[str]:
    #     region_name = parse_region_name(region)
    #     return regions_by_prime_region.setdefault(region_name, [])

    def color_from_sphere_index(sphere_ind: int) -> str:
        color = (128+(sphere_ind*40%128), 128+(sphere_ind*70%128), 128+((64+sphere_ind*25)%128))
        return f"#{color[0]:x}{color[1]:x}{color[2]:x}"

    def fmt(obj: Union[Entrance, Item, Location, Region]) -> str:
        name = obj.name
        if isinstance(obj, Item):
            name = multiworld.get_name_string_for_object(obj)
            if obj.advancement:
                name = f"**{name}**"
            if obj.code is None:
                name = f"//{name}//"
        if isinstance(obj, Location):
            if obj.progress_type == LocationProgressType.PRIORITY:
                name = f"**{name}**"
            elif obj.progress_type == LocationProgressType.EXCLUDED:
                name = f"--{name}--"
            if obj.address is None:
                name = f"//{name}//"
        return re.sub("[\".:]", "", name)

    def visualize_exits(region: Region) -> None:
        # prime_region = get_prime_region_from_region(region)

        for exit_ in region.exits:
            if exit_.connected_region:
                exit_sphere = -1
                if highlights:
                    spheres = highlights["spheres"]
                    sphere_ind = next((i for i, (state, _) in enumerate(spheres) if state.can_reach(exit_, "Entrance")), None)
                    if sphere_ind is not None:
                        exit_sphere = sphere_ind
                color = "#ff0000"
                if exit_sphere >= 0:
                    color = color_from_sphere_index(exit_sphere)
                # uml.append(f"\"{fmt(region)}\" -[#{color}]-> \"{fmt(exit_.connected_region)}\" : \"{fmt(exit_)}\"")
                uml.append(f"\"{fmt(region)}\" -[{color},thickness=4]-> \"{fmt(exit_.connected_region)}\"")
            else:
                uml.append(f"circle \"unconnected exit:\\n{fmt(exit_)}\"")
                uml.append(f"\"{fmt(region)}\" --> \"unconnected exit:\\n{fmt(exit_)}\"")

    def visualize_locations(region: Region) -> None:
        # any_lock = any(location.locked for location in region.locations)
        # any_lock = any(location.locked or not self.can_reach_location(location.name) for location in region.locations)
        # prime_region = get_prime_region_from_region(region)

        for location in region.locations:
            location_sphere = -1
            if highlights:
                spheres = highlights["spheres"]
                sphere_ind = next((i for i, (_, sphere) in enumerate(spheres) if location in sphere), None)
                if sphere_ind is not None:
                    location_sphere = sphere_ind
            lock = "<&lock-locked> " if not state.can_reach(location, 'Location') else "<&lock-unlocked,color=transparent> "
            # sphere_text = f" <<Sphere{location_sphere}>>" if location_sphere >= 0 else " <<inaccessible>>"
            # lock = "<&lock-locked> " if location.locked else "<&lock-unlocked,color=transparent> " if any_lock else ""
            if location.item:
                uml.append(f"\"{fmt(region)}\" : {{method}} {lock}{fmt(location)}: {fmt(location.item)}")
            else:
                uml.append(f"\"{fmt(region)}\" : {{field}} {lock}{fmt(location)}")

    def visualize_region(region: Region) -> None:
        location_sphere = -1
        if highlights:
            spheres = highlights["spheres"]
            sphere_ind = next((i for i, (state, _) in enumerate(spheres) if state.can_reach(region, 'Region')), None)
            if sphere_ind is not None:
                location_sphere = sphere_ind

        uml.append(f"class \"{fmt(region)}\"{f' <<Sphere{location_sphere}>>' if location_sphere >= 0 else ' <<inaccessible>>'}")
        if show_locations:
            visualize_locations(region)
        visualize_exits(region)

    def visualize_other_regions() -> None:
        return
        if other_regions := [region for region in multiworld.get_regions(root_region.player) if region not in seen]:
            uml.append("package \"other regions\" <<Cloud>> {")
            for region in other_regions:
                uml.append(f"class \"{fmt(region)}\"")
            uml.append("}")

    uml.append("@startuml")
    uml.append("hide circle")
    uml.append("hide empty members")
    if linetype_ortho:
        uml.append("skinparam linetype ortho")
        
    uml.append("skinparam class {")
    uml.append(f"BackgroundColor<<inaccessible>> #880000")
    for i in range(20):
        color = (128+(i*40%128), 128+(i*70%128), 128+((64+i*25)%128))
        uml.append(f"BackgroundColor<<Sphere{i}>> #{color[0]:x}{color[1]:x}{color[2]:x}")
    uml.append("}")
    while regions:
        if (current_region := regions.popleft()) not in seen:
            seen.add(current_region)
            visualize_region(current_region)
            regions.extend(exit_.connected_region for exit_ in current_region.exits if exit_.connected_region)
    # if show_other_regions:
    #     visualize_other_regions()
    # for region_name, region_uml in regions_by_prime_region.items():
    #     uml.append(f'package "{region_name}" ' "{")
    #     uml.extend(region_uml)
    #     uml.append("}")
    uml.append("class \"Collected\"")
    uml.extend("\"Collected\" : {method} " + f"{name}: {state.count(name, 1)}" for name in sorted(map(lambda x: x[0], state.prog_items)))
    uml.append("@enduml")

    with open(file_name, "wt", encoding="utf-8") as f:
        f.write("\n".join(uml))