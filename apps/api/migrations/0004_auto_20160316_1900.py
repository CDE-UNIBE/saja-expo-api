# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20160314_1732'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='tag_id',
            new_name='perma_id',
        ),
        migrations.AddField(
            model_name='log',
            name='content_type',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nfcregister',
            name='nfc_id',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
