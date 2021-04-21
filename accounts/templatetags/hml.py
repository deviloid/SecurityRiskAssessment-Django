from django import template

register = template.Library()

@register.filter
def hml(value):
    if value >= 90:
        return "High"
    if value < 90 and value >= 50:
        return "Medium"
    else:
        return "Low"
    