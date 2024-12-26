from django import template
from flowers.models import Type

register = template.Library()

@register.inclusion_tag('flowers/types_list.html')
def show_types():
    types = Type.objects.all()
    return {'types': types}
