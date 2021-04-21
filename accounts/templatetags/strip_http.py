from django import template

register = template.Library()

@register.filter
def strip_http(value):
    if 'http://' in value:
        return value.replace('http://','')
    if 'https://' in value:
        return value.replace('https://','')