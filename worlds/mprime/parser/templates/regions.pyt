from BaseClasses import Region
from worlds.AutoWorld import World
from ..locations import MetroidPrimeLocation

def create_regions_and_events(self: World):
    multiworld = self.multiworld
    player = self.player
    def cr(region_name: str):
        return Region(region_name, player, multiworld)
    def cre(region_name: str, event_name: str, skippable: bool = False):
        this_region = cr(region_name)
        this_location = MetroidPrimeLocation(player, region_name, None, this_region)
        this_region.locations.append(this_location)
        event = self.create_event(event_name, skippable)
        this_location.place_locked_item(event)
        return this_region
    def crl(region_name: str):
        this_region = cr(region_name)
        this_location = MetroidPrimeLocation(player, region_name, self.location_name_to_id[region_name], this_region)
        this_region.locations.append(this_location)
        return this_region

    # will be implemented once Randovania does
    # create_items_every_room_region: Callable[[str], Region]
    # if world.items_every_room:
    #     create_items_every_room_region = create_region_with_location
    # else:
    #     create_items_every_room_region = create_region

    menu_region = Region("Menu", player, multiworld)
    multiworld.regions.extend((menu_region,
        {%- for node_from, info in data.node_info.items() -%}
            {%- if info.items_every_room -%}
            {%- elif info.pickup -%}
                crl("{{methods["tuplefmt"](node_from)}}"),
            {%- elif info.event_name is not none -%}
                cre("{{methods["tuplefmt"](node_from)}}","{{info.event_name}}",{{not info.unskippable_event}}),
            {%- else -%}
                cr("{{methods["tuplefmt"](node_from)}}"),
            {%- endif -%}
        {%- endfor -%}))
    menu_region.add_exits({
        "Ship (Landing Site, Tallon Overworld)":
            "Start Game"
    })