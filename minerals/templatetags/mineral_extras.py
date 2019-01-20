from random import randint

from django import template
from ..models import Mineral

register = template.Library()


@register.simple_tag
def random_mineral_id():
    """
    Returns a random ID of a mineral in the database. TO be used in a link that
    appears in the bottom of the templates.
    :return: Random ID of a mineral
    """
    minerals = Mineral.objects.all()
    random_num = randint(0, len(minerals) - 1)
    mineral = minerals[random_num]
    return mineral.id


@register.filter('field_or_na')
def field_or_na(field_value):
    """
        Many of the mineral fields are optional, if a field is not provided,
        "N/A" will be printed in the HTML to denote a missing field
    """
    if not field_value:
        return 'N/A'

    return field_value
