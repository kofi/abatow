# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import uuid
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('middle_initial', models.CharField(blank=True, max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('nameslug', models.SlugField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Congress',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('year', models.DateField(default=datetime.datetime.today)),
                ('election_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('nameslug', models.SlugField(max_length=64)),
                ('total_registered', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('electiontype_text', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('congress', models.ForeignKey(to='elections.Congress')),
            ],
        ),
        migrations.CreateModel(
            name='Party',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('nameslug', models.SlugField(max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='elections.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, serialize=False)),
                ('name', models.CharField(blank=True, max_length=250)),
                ('nameslug', models.SlugField(max_length=64)),
                ('total_registered', models.IntegerField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('country', models.ForeignKey(to='elections.Country')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('votes', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('candidate', models.ForeignKey(to='elections.Candidate')),
                ('country', models.ForeignKey(to='elections.Country')),
                ('election', models.ForeignKey(to='elections.Election')),
            ],
        ),
        migrations.AddField(
            model_name='election',
            name='region',
            field=models.ForeignKey(to='elections.Region'),
        ),
        migrations.AddField(
            model_name='congress',
            name='country',
            field=models.ForeignKey(to='elections.Country'),
        ),
        migrations.AddField(
            model_name='candidate',
            name='party',
            field=models.ForeignKey(to='elections.Party'),
        ),
    ]
