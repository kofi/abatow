# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('elections', '0008_election_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidate',
            name='middle_initial',
        ),
        migrations.AddField(
            model_name='candidate',
            name='middlename',
            field=models.CharField(null=True, blank=True, max_length=1),
        ),
    ]
