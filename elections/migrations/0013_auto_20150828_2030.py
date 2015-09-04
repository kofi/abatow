# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0012_auto_20150828_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='middlename',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
