from . import MetroidPrimeTestBase
# from pyvis.network import Network
import typing
from typing import Union, cast
from BaseClasses import Region
from test.TestBase import TestBase

class TestItemAccess(MetroidPrimeTestBase):

    def visualize_regions(self,
                          root_region: Region, file_name: str, *,
                          show_entrance_names: bool = False, show_locations: bool = True, show_other_regions: bool = True,
                          linetype_ortho: bool = True) -> None:
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
        from BaseClasses import Entrance, Item, Location, LocationProgressType, MultiWorld, Region
        from collections import deque
        import re

        uml: typing.List[str] = list()
        seen: typing.Set[Region] = set()
        accessible_regions: set[Region] = set()
        regions: typing.Deque[Region] = deque((root_region,))
        multiworld: MultiWorld = root_region.multiworld

        seen2: set[Region] = set()
        while regions:
            if (current_region := regions.popleft()) not in seen2:
                seen2.add(current_region)
                for exit in current_region.exits:
                    if not exit.connected_region: continue
                    if self.can_reach_entrance(exit.name):
                        accessible_regions.add(exit.connected_region)

                regions.extend(exit_.connected_region for exit_ in current_region.exits if exit_.connected_region)

        regions = deque((root_region,))

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
            for exit_ in region.exits:
                if exit_.connected_region:
                    if show_entrance_names:
                        color = "green" if self.can_reach_entrance(exit_.name) else "red"
                        # uml.append(f"\"{fmt(region)}\" -[#{color}]-> \"{fmt(exit_.connected_region)}\" : \"{fmt(exit_)}\"")
                        uml.append(f"\"{fmt(region)}\" -[#{color}]-> \"{fmt(exit_.connected_region)}\"")
                    else:
                        try:
                            uml.remove(f"\"{fmt(exit_.connected_region)}\" --> \"{fmt(region)}\"")
                            uml.append(f"\"{fmt(exit_.connected_region)}\" <--> \"{fmt(region)}\"")
                        except ValueError:
                            uml.append(f"\"{fmt(region)}\" --> \"{fmt(exit_.connected_region)}\"")
                else:
                    uml.append(f"circle \"unconnected exit:\\n{fmt(exit_)}\"")
                    uml.append(f"\"{fmt(region)}\" --> \"unconnected exit:\\n{fmt(exit_)}\"")

        def visualize_locations(region: Region) -> None:
            any_lock = any(location.locked for location in region.locations)
            # any_lock = any(location.locked or not self.can_reach_location(location.name) for location in region.locations)
            for location in region.locations:
                lock = "<&lock-locked> " if not self.can_reach_location(location.name) else "<&lock-unlocked,color=transparent> "
                # lock = "<&lock-locked> " if location.locked else "<&lock-unlocked,color=transparent> " if any_lock else ""
                if location.item:
                    uml.append(f"\"{fmt(region)}\" : {{method}} {lock}{fmt(location)}: {fmt(location.item)}")
                else:
                    uml.append(f"\"{fmt(region)}\" : {{field}} {lock}{fmt(location)}")

        def visualize_region(region: Region) -> None:
            uml.append(f"class \"{fmt(region)}\"{' <<accessible>>' if region in accessible_regions else ''}")
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
        uml.append("BackgroundColor<<accessible>> PaleGreen")
        uml.append("}")
        while regions:
            if (current_region := regions.popleft()) not in seen:
                seen.add(current_region)
                visualize_region(current_region)
                regions.extend(exit_.connected_region for exit_ in current_region.exits if exit_.connected_region)
        if show_other_regions:
            visualize_other_regions()
        uml.append("@enduml")

        with open(file_name, "wt", encoding="utf-8") as f:
            f.write("\n".join(uml))
    def test_morph_ball(self):
        """Test locations that require Morph Ball"""
        reachable_locs = [
            "Pickup (Missile Expansion) (Landing Site, Tallon Overworld)",
            "Pickup (Missile Expansion) (Training Chamber Access, Chozo Ruins)"
        ]
        unreachable_locs = [
            "Pickup (Energy Tank) (Training Chamber, Chozo Ruins)",
            "Pickup (Missile Expansion) (Frigate Crash Site, Tallon Overworld)",
            "Pickup (Missile Expansion) (Gathering Hall, Chozo Ruins)"
        ]

        # starting_items = ["Power Suit", "Power Beam", "Combat Visor", "Scan Visor"]
        # self.collect_by_name(starting_items)
        self.multiworld.worlds[1].create_items()

        possible_items = [["Morph Ball", "Space Jump Boots", "Missile Launcher"]]

        print(self.multiworld.state.prog_items, self.multiworld.state.events)
        # all_items = [item_name for item_names in possible_items for item_name in item_names]

        # self.collect_all_but(all_items)

        reach_color = "#00ff00"
        cant_reach_color = "#ff0000"
        region_color = "#aaaaaa"

        for item_names in possible_items:
            items = self.collect_by_name(item_names)
            for location in reachable_locs:
                can_reach = self.can_reach_location(location)
                if not can_reach:
                    self.visualize_regions(self.multiworld.get_region("Menu", 1), "test.puml")
                    # net = Network()
                    # for region in self.multiworld.regions:
                    #     net.add_node(region.name, None, "dot" if len(region.locations) == 0 else "star", region_color)
                    #     # net.add_node(region.name, None, "dot", reach_color if region.can_reach(self) else cant_reach_color)
                    #     for entrance in region.entrances:
                    #         net.add_node(entrance.name, None, "square", reach_color if self.can_reach_entrance(entrance.name) else cant_reach_color)
                    #         net.add_edge(entrance.name, entrance.connected_region.name)
                    #         net.add_edge(region.name, entrance.name)
                    # net.save_graph('wew.html')
                self.assertTrue(can_reach,
                                f"{location} not reachable with {item_names} but should be")
            for location in unreachable_locs:
                can_reach = self.can_reach_location(location)
                if can_reach:
                    self.visualize_regions(self.multiworld.get_region("Menu", 1), "test.puml")
                self.assertFalse(can_reach,
                                 f"{location} reachable with {item_names} but shouldn't be")
            self.remove(items)