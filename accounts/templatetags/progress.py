from django import template

register = template.Library()

@register.filter
def progress(value):
    progress = value/14*100
    progress = round(progress, 2)
    return progress
    