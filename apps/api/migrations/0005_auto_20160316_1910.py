# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20160316_1900'),
    ]

    operations = [
        migrations.AddField(
            model_name='nfcregister',
            name='finished',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='nfcregister',
            name='history',
            field=models.TextField(default='', blank=True),
        ),
        migrations.AddField(
            model_name='nfcregister',
            name='received',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 16, 18, 10, 6, 365327, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
    ]
