from django import template
from dateutil import parser
from datetime import timedelta
from ..scripts.map import make_map

register = template.Library()

@register.filter(name='toDate')
def toDate(value):
    return parser.parse(value) - timedelta(hours=5)

@register.filter(name='candidateVotePercent')
def candidateVotePercent(value, arg):
    total = 0
    for candidate in arg:
        total += candidate['voteCount']
    
    if total > 0: return value/total
    return 0

def mapVoteCalculator(candidates):
    if len(candidates) > 2:
        return 0
    
    v1 = candidates[0]['voteCount']
    v2 = candidates[1]['voteCount']

    return v1 / (v1 + v2)

@register.filter(name='mapfilter')
def mapFilter(value):
    aggregate = {'name': [], 'votes': []}

    for idx, unit in enumerate(value):
        if not idx == 0:
            print(aggregate['name'])
            aggregate['name'] = aggregate['name'] + [unit['reportingunitName'].upper()]
            aggregate['votes'] = aggregate['votes'] + [mapVoteCalculator(unit['candidates'])]

    return make_map(aggregate)
