from django import template
from django.core.paginator import EmptyPage

register = template.Library()

@register.filter(name='message_bootstrapize')
def addclass(value):
    if value == "info":
      return "info"
    elif value == "warning":
      return "warning"
    elif value == "success":
      return "success"
    elif value == "error":
      return "danger"