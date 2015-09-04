# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0002_remove_result_country'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='congress',
            options={'verbose_name_plural': 'congress'},
        ),
    ]
