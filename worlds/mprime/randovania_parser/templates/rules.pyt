from BaseClasses import CollectionState
from worlds.AutoWorld import World
from typing import Callable, Optional, cast

ConnectionRule = Callable[[CollectionState], bool]
ConnectionNameTuple = tuple[str, Optional[ConnectionRule]]
NodeRules = tuple[str, tuple[ConnectionNameTuple, ...]]

def set_rules(self: World):
 from ..options import MetroidPrimeOptions
 {{logic_imports}}
 p=self.player
 o=cast(MetroidPrimeOptions, self.options)
 t: dict[str, ConnectionRule] = {
  {%- for template_name, requirements in templates %}
  "{{template_name}}": {{requirements}},
  {%- endfor %}
 }
 entrance_rules:tuple[NodeRules,...]=(
  {%- for node_from, nodes in rules %}
("{{node_from}}",(
   {%- for node_to, rule in nodes.items() %}
 ("{{node_to}}",{{rule}}),
   {%- endfor -%}
)),
  {%- endfor -%}
 )
 get_region = self.multiworld.get_region
 for region_name, exits in entrance_rules:
  connect_to = get_region(region_name,p).connect
  for connecting_region_name, rule in exits:
   connect_to(get_region(connecting_region_name, p), None, rule)