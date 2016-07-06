# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20160706_0314'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='post',
            table='posts_post',
        ),
    ]
