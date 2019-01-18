from django import template

register = template.Library()


@register.filter('field_or_na')
def field_or_na(field_value):
    """
        Many of the mineral fields are optional, if a field is not provided,
        "N/A" will be printed in the HTML to denote a missing field
    """
    if not field_value:
        return 'N/A'

    return field_value
