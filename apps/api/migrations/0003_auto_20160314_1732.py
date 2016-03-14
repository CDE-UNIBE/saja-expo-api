# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import api.validators


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_log_history'),
    ]

    operations = [
        migrations.CreateModel(
            name='NFCRegister',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nfc_id', models.CharField(max_length=255)),
                ('backpack_id', models.CharField(max_length=6, unique=True)),
                ('language_id', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='log',
            name='nfc_id',
            field=models.CharField(validators=[api.validators.validate_registered_nfc_id], max_length=255),
        ),
    ]
