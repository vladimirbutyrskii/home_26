from django import template
from django.conf import settings
register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"

# from django import template
# from django.conf import settings
#
# register = template.Library()
#
#
# @register.filter
# def media_filter(value):
#     if value:
#         return f'{settings.MEDIA_URL}{value}'
#     return ''
