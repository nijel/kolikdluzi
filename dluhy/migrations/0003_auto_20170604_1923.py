# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-04 19:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dluhy', '0002_auto_20170604_1856'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ministr',
            options={'ordering': ('jmeno',)},
        ),
        migrations.AlterModelOptions(
            name='rozpocet',
            options={'ordering': ('rok',)},
        ),
        migrations.AlterModelOptions(
            name='strana',
            options={'ordering': ('jmeno',)},
        ),
    ]