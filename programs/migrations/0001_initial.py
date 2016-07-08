# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('slug', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('starting_at', models.DateTimeField(verbose_name='date starting at', default=datetime.datetime.now, blank=True)),
                ('created_at', models.DateTimeField(verbose_name='date created', auto_now_add=True)),
                ('updated_at', models.DateTimeField(verbose_name='date updated', auto_now_add=True)),
            ],
        ),
    ]
