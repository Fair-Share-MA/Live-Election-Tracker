from django import template
from dateutil import parser

register = template.Library()

@register.filter(name='toDate')
def toDate(value):
    return parser.parse(value)

@register.filter(name='candidateVotePercent')
def candidateVotePercent(value, arg):
    total = 0
    for candidate in arg:
        total += candidate['voteCount']
    
    if total > 0: return value/total
    return 0