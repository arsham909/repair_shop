from django import template

register = template.Library()

# it will get the attribute of the form 
@register.filter
def getattribute(obj, attr_name):
    return getattr(obj, attr_name, '')