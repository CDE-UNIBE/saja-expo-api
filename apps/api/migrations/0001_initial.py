# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import api.validators


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(blank=True, null=True)),
                ('history', models.TextField(blank=True, default='')),
                ('backpack_url', models.CharField(max_length=255, validators=[api.validators.is_url])),
                ('station_id', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ['-received'],
            },
        ),
    ]
