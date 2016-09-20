# Create your views here.
# -*- coding: UTF-8 -*-
from models import Ministr, Rozpocet, Vlada, Strana

from django.db.models import Sum, Count, Max, Avg, Min
from django.shortcuts import render_to_response, get_object_or_404
from django.core.cache import cache
from django.template import RequestContext

def index(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')[:10]
    return render_to_response('index.html', RequestContext(request, {
        'top': top,
    }))

def ministri(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')
    return render_to_response('top.html', RequestContext(request, {
        'top': top,
    }))

def info(request):
    return render_to_response('info.html', RequestContext(request, {
    }))

def strana(request, slug):
    strana = get_object_or_404(Strana, slug = slug)
    return render_to_response('strana.html', RequestContext(request, {
        'strana': strana,
    }))

def ministr(request, slug):
    ministr = get_object_or_404(Ministr, slug = slug)
    summary = ministr.vlada_set.aggregate(
        bilance = Sum('rozpocet__bilance'),
        vydaje = Sum('rozpocet__vydaje'),
        prijmy = Sum('rozpocet__prijmy'))
    return render_to_response('ministr.html', RequestContext(request, {
        'ministr': ministr,
        'summary': summary,
    }))

def chart(request):
    return render_to_response('chart.js', RequestContext(request, {
        'rozpocty': Rozpocet.objects.all()
    }))
