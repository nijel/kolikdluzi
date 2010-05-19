# Create your views here.
# -*- coding: UTF-8 -*-
from models import Ministr, Rozpocet, Vlada

from django.shortcuts import render_to_response, get_object_or_404
from django.core.cache import cache
from django.template import RequestContext

def index(request):
    return render_to_response('index.html', RequestContext(request, {
    }))

def chart(request):
    return render_to_response('chart.js', RequestContext(request, {
        'rozpocty': Rozpocet.objects.all()
    }))
