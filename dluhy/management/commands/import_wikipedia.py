# -*- coding: UTF-8 -*-
from __future__ import unicode_literals

import hashlib
import os

from django.core.management.base import BaseCommand

from mwclient import Site
import mwparserfromhell


ROWS = ('', '2', '3', '4', '5', '6', '7', '8', '9')


class Command(BaseCommand):
    help = 'stahne informace o vladach z Wikipedie'

    def handle(self, *args, **options):
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
                else:
                    raise Exception('Unknown name: {0}'.format(name))

                party = template.get('strana' + row).value.strip()
                if 'nestr' in party:
                    party = 'Nestraník'
                else:
                    party = party.split(']')[0].strip(']').strip('[').split('|')[-1]
