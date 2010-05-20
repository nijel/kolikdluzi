#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import sys
sys.path = ['../'] + sys.path

import urllib
import webbrowser

from django.template.defaultfilters import slugify

from dluhy.models import Vlada, Rozpocet, Ministr, Strana

for m in Ministr.objects.filter(strana = None): #all():
    print m.jmeno
    webbrowser.open(m.wikipedia)
    if m.wikipedia is None:
        u = 'http://cs.wikipedia.org/wiki/%s' % (urllib.quote(m.jmeno.replace(' ', '_').encode('utf-8')))
        webbrowser.open(u)
        s = raw_input('Wikipedia: ')
        if s == '':
            m.wikipedia = u
        elif s != 'x':
            m.wikipedia = s
    if m.url is None:
        s = raw_input('URL: ')
        if s != '':
            m.url = s
    if m.strana is None:
        s = raw_input('Strana (%s): ' % ' '.join(['%d: %s' % (s.id, s.jmeno.encode('utf-8')) for s in Strana.objects.all()]))
        if s != '':
            m.strana = Strana.objects.get(pk = int(s))
    m.save()
