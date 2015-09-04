# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0005_auto_20150827_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='regiontype_text',
            field=models.CharField(max_length=3, default='CON', choices=[('REG', 'Regional'), ('CON', 'Constituency')]),
        ),
    ]
