from django import template

register = template.Library()


@register.filter
def strengths_list(strength_str, separator):
    strength = strength_str.split(separator)
    return strength



@register.filter
def hint_delimiter(notes, i):
    strength = notes.split('#')
    try:
        item = strength[i]
    except:
        item = None
    return item
