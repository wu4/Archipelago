from Options import Range
{% for trick_name, trick_data in tricks %}
class {{trick_name}}(Range):
    """{{parse_trick_desc(trick_data["description"])}}"""
    display_name = "{{trick_data["long_name"]}}"
    range_start = 0
    range_end = 5
    default = 0
{%- endfor %}

generated_options = {
{% for trick_name, trick_data in tricks %}
    "{{trick_name_gen(trick_data["long_name"])}}": {{trick_name}},
{%- endfor %}
}