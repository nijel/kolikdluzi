# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ministr',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jmeno', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('wikipedia', models.URLField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Rozpocet',
            fields=[
                ('rok', models.IntegerField(serialize=False, primary_key=True, db_index=True)),
                ('prijmy', models.IntegerField()),
                ('vydaje', models.IntegerField()),
                ('bilance', models.IntegerField(blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Strana',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('jmeno', models.CharField(max_length=100)),
                ('slug', models.SlugField(unique=True)),
                ('wikipedia', models.URLField(null=True, blank=True)),
                ('url', models.URLField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vlada',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ministr', models.ForeignKey(to='dluhy.Ministr')),
                ('rozpocet', models.ForeignKey(to='dluhy.Rozpocet')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='vlada',
            unique_together=set([('ministr', 'rozpocet')]),
        ),
        migrations.AddField(
            model_name='ministr',
            name='strana',
            field=models.ForeignKey(blank=True, to='dluhy.Strana', null=True),
            preserve_default=True,
        ),
    ]
