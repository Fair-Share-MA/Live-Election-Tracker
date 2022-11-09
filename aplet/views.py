from django.shortcuts import render
from .scripts.api import get_races
from requests_cache import CachedSession

session = CachedSession(expire_after=30)

def home(request):
    sel = request.GET.get('idx', 1)

    return render(request, 'aplet/home.html', {
        'races': get_races(session),
        'sel': sel
    })