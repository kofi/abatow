# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0011_auto_20150828_1747'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='ispublished',
            new_name='is_published',
        ),
    ]
