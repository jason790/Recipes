# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20160607_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='WPPost',
            fields=[
                ('id', models.BigIntegerField(serialize=False, db_column='ID', primary_key=True)),
                ('title', models.TextField(db_column='post_title')),
                ('link', models.CharField(db_column='guid', max_length=255)),
                ('slug', models.CharField(db_column='post_name', max_length=200)),
                ('description', models.TextField(db_column='post_excerpt')),
                ('body', models.TextField(db_column='post_content')),
                ('post_author', models.BigIntegerField()),
                ('post_date', models.DateTimeField()),
                ('post_date_gmt', models.DateTimeField()),
                ('post_status', models.CharField(max_length=20)),
                ('comment_status', models.CharField(max_length=20)),
                ('ping_status', models.CharField(max_length=20)),
                ('post_password', models.CharField(max_length=20)),
                ('to_ping', models.TextField()),
                ('pinged', models.TextField()),
                ('post_modified', models.DateTimeField()),
                ('post_modified_gmt', models.DateTimeField()),
                ('post_content_filtered', models.TextField()),
                ('post_parent', models.BigIntegerField()),
                ('menu_order', models.IntegerField()),
                ('post_type', models.CharField(max_length=20)),
                ('post_mime_type', models.CharField(max_length=100)),
                ('comment_count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_posts',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WpPostmeta',
            fields=[
                ('id', models.BigIntegerField(serialize=False, db_column='meta_id', primary_key=True)),
                ('meta_key', models.CharField(db_column='meta_key', max_length=255)),
                ('meta_value', models.TextField(db_column='meta_value')),
            ],
            options={
                'db_table': 'wp_postmeta',
                'managed': False,
                'ordering': ['-pk'],
            },
        ),
        migrations.CreateModel(
            name='WpTermRelationships',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('object_id', models.BigIntegerField()),
                ('term_taxonomy_id', models.BigIntegerField()),
                ('term_order', models.IntegerField()),
            ],
            options={
                'db_table': 'wp_term_relationships',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WpTerms',
            fields=[
                ('term_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200)),
                ('term_group', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_terms',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='WpTermTaxonomy',
            fields=[
                ('term_taxonomy_id', models.BigIntegerField(serialize=False, primary_key=True)),
                ('term_id', models.BigIntegerField()),
                ('taxonomy', models.CharField(max_length=32)),
                ('description', models.TextField()),
                ('parent', models.BigIntegerField()),
                ('count', models.BigIntegerField()),
            ],
            options={
                'db_table': 'wp_term_taxonomy',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'managed': False},
        ),
    ]
