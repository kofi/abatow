# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0004_auto_20150827_1831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='country',
            name='nameslug',
            field=models.SlugField(null=True, max_length=64),
        ),
        migrations.AlterField(
            model_name='country',
            name='total_registered',
            field=models.IntegerField(null=True, default=0),
        ),
        migrations.AlterField(
            model_name='election',
            name='electiontype_text',
            field=models.CharField(default='CON', max_length=3, choices=[('NAT', 'National'), ('REG', 'Regional'), ('CON', 'Constituency')]),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='region',
            name='nameslug',
            field=models.SlugField(null=True, max_length=64),
        ),
    ]
