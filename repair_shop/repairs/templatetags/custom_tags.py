from django import template

register = template.Library()

@register.filter
def getattribute(obj, attr_name):
    
    
    return getattr(obj, attr_name, '')