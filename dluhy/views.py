# Create your views here.
# -*- coding: UTF-8 -*-
from dluhy.models import Ministr, Rozpocet, Strana

from django.db.models import Sum
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext

def index(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')[:10]
    return render(request, 'index.html', {
        'top': top,
    })

def ministri(request):
    top = Ministr.objects.annotate(bilance = Sum('vlada__rozpocet__bilance')).order_by('bilance')
    return render(request, 'top.html', {
        'top': top,
    })

def info(request):
    return render(request, 'info.html')

def ministr(request, slug):
    ministr = get_object_or_404(Ministr, slug = slug)
    summary = ministr.vlada_set.aggregate(
        bilance = Sum('rozpocet__bilance'),
        vydaje = Sum('rozpocet__vydaje'),
        prijmy = Sum('rozpocet__prijmy'))
    return render(request, 'ministr.html', {
        'ministr': ministr,
        'summary': summary,
    })

def chart(request):
    return render(request, 'chart.js', {
        'rozpocty': Rozpocet.objects.all()
    })
