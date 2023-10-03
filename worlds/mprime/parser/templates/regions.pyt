from BaseClasses import MultiWorld, Region
from worlds.AutoWorld import World
from .Locations import MetroidPrimeLocation
from .Utils import region_format
from typing import Callable

locations = (
    {%- for node_from, node_rules in rules %}
        {%- if node_rules.has_location in ['pickup', 'pickup_every_room'] %}
            "{{node_from}}",
        {%- endif %}
    {%- endfor %}
)

items_every_room_locations = (
    {%- for node_from, node_rules in rules %}
        {%- if node_rules.has_location in ['pickup_every_room'] %}
            "{{node_from}}",
        {%- endif %}
    {%- endfor %}
)

def create_regions(world: World, multiworld: MultiWorld, player: int):
    def create_region(region_name: str):
        return Region(region_name, player, multiworld)
    def create_region_with_event(region_name: str, event_name: str, skippable: bool = False):
        this_region = create_region(region_name)
        this_location = MetroidPrimeLocation(player, region_name, None, this_region)
        this_region.locations.append(this_location)
        event = world.create_event(event_name, skippable)
        this_location.place_locked_item(event)
        return this_region
    def create_region_with_location(region_name: str):
        this_region = create_region(region_name)
        this_location = MetroidPrimeLocation(player, region_name, world.location_name_to_id[region_name], this_region)
        this_region.locations.append(this_location)
        return this_region

    # will be implemented once Randovania does
    # create_items_every_room_region: Callable[[str], Region]
    # if world.items_every_room:
    #     create_items_every_room_region = create_region_with_location
    # else:
    #     create_items_every_room_region = create_region

    menu_region = Region("Menu", player, multiworld)
    multiworld.regions.extend((
        menu_region,
        {%- for node_from, node_rules in rules %}
            {%- if node_rules.has_location == "pickup" %}
                create_region_with_location("{{node_from}}"),
            {%- elif node_rules.has_location == "event" %}
                create_region_with_event("{{node_from}}", "{{node_rules.event_name}}", {{node_rules.event_skippable}}),
            {%- elif node_rules.has_location == "items_every_room" %}
                # create_items_every_room_region("{{node_from}}"),
            {%- else %}
                create_region("{{node_from}}"),
            {%- endif %}
        {%- endfor %}
    ))
    menu_region.add_exits({
        region_format("Ship", "Landing Site", "Tallon Overworld"):
        # region_format("Ship Save", "Exterior Docking Hangar", "Frigate Orpheon"):
            "Start Game"
    })
