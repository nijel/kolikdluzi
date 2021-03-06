# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import datetime
import hashlib
import os

try:
    from urllib import quote
except ImportError:
    from urllib.parse import quote

from django.core.management.base import BaseCommand
from django.utils.http import urlencode
from django.utils.text import slugify

from mwclient import Site
import mwparserfromhell

from dluhy.models import Ministr, Strana, Vlada, Rozpocet


ROWS = ('', '2', '3', '4', '5', '6', '7', '8', '9')


def wikilink(name):
    return 'https://cs.wikipedia.org/wiki/' + quote(name.replace(' ', '_').encode('utf-8'))


def parsedate(value):
    parts = value.strip().split('}')[0].strip('{').split('|')
    if parts[0] == 'úřadující':
        return datetime.date.today()
    elif parts[0] == 'dts':
        date = [int(x) for x in parts[1:]]
        return datetime.date(date[2], date[1], date[0])
    raise ValueError('Invalid date: {0}'.format(value))


class Command(BaseCommand):
    help = 'stahne informace o vladach z Wikipedie'

    def handle(self, *args, **options):
        letos = datetime.date.today().year
        site = Site('cs.wikipedia.org')

        page = site.pages['Seznam_ministrů_České_republiky']
        wikicode = mwparserfromhell.parse(page.text())
        for template in wikicode.filter_templates(matches='Seznam politiků'):
            for row in ROWS:
                if not template.has('jméno' + row):
                    break
                name = template.get('jméno' + row).value.strip()
                if name.startswith('{{sortname|'):
                    parts = name.split('}')[0].strip('}').strip('{').split('|')
                    if len(parts) == 4:
                        first, last, wiki = parts[1:]
                    else:
                        first, last = parts[1:]
                        wiki = '{0} {1}'.format(first, last)
                    jmeno = '{0} {1}'.format(first, last)
                    wiki = wikilink(wiki)
                else:
                    raise Exception('Unknown name: {0}'.format(name))

                party = template.get('strana' + row).value.strip()
                if 'nestr' in party or party == '–':
                    party = 'Nestraník'
                    wikiparty = None
                else:
                    parts = party.split(']')[0].strip(']').strip('[').split('|')
                    if len(parts) == 1:
                        party = wikiparty = parts[0]
                    else:
                        wikiparty, party = parts
                    wikiparty = wikilink(wikiparty)

                strana, created = Strana.objects.get_or_create(
                    jmeno=party,
                    defaults={
                        'slug': slugify(party),
                        'wikipedia': wikiparty,
                    }
                )
                if created:
                    self.stdout.write('Vytvorena strana {0}'.format(strana))
                else:
                    if strana.wikipedia != wikiparty:
                        self.stderr.write('Ruzne wiki pro {0}: {1}, {2}'.format(strana, strana.wikipedia, wikiparty))
                        strana.wikipedia = wikiparty
                        strana.save()

                start = parsedate(template.get('datum-od' + row).value)
                end = parsedate(template.get('datum-do' + row).value)

                if start.year >= letos:
                    continue

                ministr, created = Ministr.objects.get_or_create(
                    jmeno=jmeno,
                    defaults={
                        'slug': slugify(jmeno),
                        'wikipedia': wiki,
                        'strana': strana,
                    }
                )

                if created:
                    self.stdout.write('Vytvoren ministr {0}'.format(ministr))
                else:
                    if strana != ministr.strana:
                        self.stderr.write('Ruzna strana pro {0}: {1}, {2}'.format(ministr, ministr.strana, strana))
                        ministr.strana = strana
                        ministr.save()
                    if wiki != ministr.wikipedia:
                        self.stderr.write('Ruzne wiki pro {0}: {1}, {2}'.format(ministr, ministr.wikipedia, wiki))
                        ministr.wikipedia = wiki
                        ministr.save()

                for rok in range(start.year, end.year + 1):
                    if rok < 2013 or rok >= letos:
                        continue
                    rozpocet, created = Rozpocet.objects.get_or_create(
                        rok=rok,
                        defaults={'prijmy': 0, 'vydaje': 0}
                    )
                    if created:
                        self.stdout.write('Vytvoren rozpocet {0}'.format(rozpocet))
                    vlada, created = Vlada.objects.get_or_create(
                        rozpocet=rozpocet, ministr=ministr
                    )
                    if created:
                        self.stdout.write('Vytvoreno vladnuti {0}'.format(vlada))
