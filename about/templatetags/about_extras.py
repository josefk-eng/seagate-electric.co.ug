from django import template

register = template.Library()


@register.filter
def strengths_list(strength_str, separator):
    strength = strength_str.split(separator)
    return strength
