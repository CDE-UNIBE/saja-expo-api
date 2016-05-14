# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_delete_nfcregister'),
    ]

    operations = [
        migrations.RenameField(
            model_name='log',
            old_name='nfc_id',
            new_name='backpack_url',
        ),
    ]
