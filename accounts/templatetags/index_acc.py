from django import template

register = template.Library()


@register.filter
def index_acc(value, i):
    return value[i]
    