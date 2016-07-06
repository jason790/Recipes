# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='search',
            name='term',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='search',
            name='searches',
            field=models.IntegerField(default=1),
        ),
    ]
