from django import template
from dateutil import parser

register = template.Library()

@register.filter(name='toDate')
def toDate(value):
    return parser.parse(value)