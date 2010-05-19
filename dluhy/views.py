# Create your views here.
# -*- coding: UTF-8 -*-
from models import Ministr, Rozpocet, Vlada

from django.db.models import Sum, Count, Max, Avg, Min
from django.shortcuts import render_to_response, get_object_or_404
from django.core.cache import cache
from django.template import RequestContext

def index(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')[:10]
    return render_to_response('index.html', RequestContext(request, {
        'top': top,
    }))

def top(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')
    return render_to_response('top.html', RequestContext(request, {
        'top': top,
    }))

def info(request):
    return render_to_response('info.html', RequestContext(request, {
    }))

def chart(request):
    return render_to_response('chart.js', RequestContext(request, {
        'rozpocty': Rozpocet.objects.all()
    }))
