from django import template
import calendar

register = template.Library()


@register.filter
def month_name(month_number):
    month_number = int(month_number)
    return calendar.month_name[month_number]