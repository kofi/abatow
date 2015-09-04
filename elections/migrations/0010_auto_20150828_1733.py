# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0009_auto_20150828_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='total_registered',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='region',
            name='total_registered',
            field=models.BigIntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='result',
            name='votes',
            field=models.BigIntegerField(default=0),
        ),
    ]
