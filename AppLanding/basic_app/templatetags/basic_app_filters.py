from django import template

register = template.Library()

@register.filter(name='times')
def times(number):
    number=int(number/2)
    return range(number)
