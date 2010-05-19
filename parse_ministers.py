#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import sys
sys.path = ['../'] + sys.path

import re

DATEMATCHER = re.compile('\((\d+)\. *(\d+)\. *(\d+) - (\d+)\. *(\d+)\. *(\d+)\).*')

from django.template.defaultfilters import slugify

from dluhy.models import Vlada, Rozpocet, Ministr

f = file('ministri.txt', 'r')

for line in f.read().split('\n\n'):
    parts = line.split('\n')
    name = parts[0].split(' - ')[0].replace('Mgr. ', '').replace('Ing. ', '').replace('RNDr. ', '').replace('MUDr. ', '').replace('MVDr. ', '').replace('PhDr. ', '').replace('JUDr. ', '').replace('Doc. ', '').replace(', D.E.A.', '').replace(', Ph.D.', '').replace(', CSc.', '').replace('arch. ', '').replace('Ing ', '').replace(', PhD', '')
    slug = slugify(name)

    ministr, created = Ministr.objects.get_or_create(jmeno = name, slug = slug)

    vlada = parts[1]
    m = DATEMATCHER.match(vlada)
    start = int(m.groups(1)[2]) + 1
    end = int(m.groups(1)[5])

    for rok in xrange(start, end + 1, 1):
        vlada, created = Vlada.objects.get_or_create(ministr = ministr, rozpocet = Rozpocet.objects.get(pk = rok))
        print vlada.__unicode__()
