# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20160316_1910'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='log',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='log',
            name='perma_id',
        ),
        migrations.AddField(
            model_name='log',
            name='station_id',
            field=models.CharField(max_length=20, default=''),
            preserve_default=False,
        ),
    ]
