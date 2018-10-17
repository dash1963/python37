from django import template

register = template.Library()

@register.filter(name='cuts')
def cuts(value, arg):
    """
       This cuts out all values in "arg" from "value"!
    """

    return value.replace(arg,'')

#
# below line commented out to use @ decorator instead
# register.filter('cuts',cuts)
