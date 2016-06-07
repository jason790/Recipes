# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('slug', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('post_status', models.CharField(max_length=12)),
                ('post_type', models.CharField(max_length=255)),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('excerpt', models.CharField(max_length=255)),
                ('picture', models.CharField(max_length=255)),
                ('body', tinymce.models.HTMLField()),
                ('views', models.IntegerField(default=0)),
                ('shares', models.IntegerField(default=0)),
                ('likes', models.IntegerField(default=0)),
                ('comments', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(verbose_name='date published')),
                ('updated_at', models.DateTimeField(verbose_name='date updated')),
            ],
        ),
    ]
