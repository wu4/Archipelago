from dataclasses import dataclass
from Options import Range

{% for trick_name, trick_data in data.header["resource_database"]["tricks"].items() -%}
{{trick_name}}=type("{{trick_name}}",(Range,),{"__doc__":"""{{methods["parse_trick_desc"](trick_data['description'])}}""","display_name":"{{trick_data['long_name']}}","range_start":0,"range_end":5,"default":0})
{% endfor -%}

@dataclass
class GeneratedOptions:
{%- for trick_name, trick_data in data.header["resource_database"]["tricks"].items() %}
    {{methods["trick_name_gen"](trick_data["long_name"])}}:{{trick_name}}
{%- endfor -%}