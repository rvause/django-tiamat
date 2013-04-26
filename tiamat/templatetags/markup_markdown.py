import markdown as md

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter
@stringfilter
def markdown(string):
    return mark_safe(md.markdown(string))
