# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0010_auto_20150828_1733'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='date_published',
            field=models.DateTimeField(blank=True, editable=False, null=True),
        ),
        migrations.AddField(
            model_name='result',
            name='ispublished',
            field=models.BooleanField(default=False),
        ),
    ]
