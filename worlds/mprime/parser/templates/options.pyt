{% for trick_name, trick_data in items %}
class {{trick_name}}(Range):
    """{{trick_data["description"]}}"""
    display_name = {{trick_data["long_name"]}}
    range_start = 0
    range_end = 5
    default = 0
{%- endfor %}

options = {
{% for trick_name, trick_data in items %}
{{get_underscored(f"metroid_prime_{trick_name}")}}: {{trick_name}}
{%- endfor %}
}