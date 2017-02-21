#!/usr/bin/python
# -*- coding: UTF-8 -*-
# vim: expandtab sw=4 ts=4 sts=4:

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import sys
sys.path = ['../'] + sys.path

import urllib
import webbrowser

from dluhy.models import Ministr, Strana

for m in Ministr.objects.filter(wikipedia = ''): #all():
    print m.jmeno
    webbrowser.open(m.wikipedia)
    if m.wikipedia is None or m.wikipedia == '':
        u = 'http://cs.wikipedia.org/wiki/{0!s}'.format((urllib.quote(m.jmeno.replace(' ', '_').encode('utf-8'))))
        webbrowser.open(u)
        s = raw_input('Wikipedia: ')
        if s == '':
            m.wikipedia = u
        elif s != 'x':
            m.wikipedia = s
    if m.url is None or m.url == '':
        s = raw_input('URL: ')
        if s != '':
            m.url = s
    if m.strana is None:
        s = raw_input('Strana ({0!s}): '.format(' '.join(['{0:d}: {1!s}'.format(strana.id, strana.jmeno.encode('utf-8')) for strana in Strana.objects.all()])))
        if s != '':
            m.strana = Strana.objects.get(pk = int(s))
    m.save()
