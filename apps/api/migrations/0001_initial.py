# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(null=True, blank=True)),
                ('history', models.TextField(default='', blank=True)),
                ('nfc_id', models.CharField(max_length=255)),
                ('station_id', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['-received'],
            },
        ),
        migrations.CreateModel(
            name='NFCRegister',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('received', models.DateTimeField(auto_now_add=True)),
                ('finished', models.DateTimeField(null=True, blank=True)),
                ('history', models.TextField(default='', blank=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('nfc_id', models.CharField(unique=True, max_length=255)),
                ('backpack_id', models.CharField(unique=True, max_length=6)),
                ('language_id', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
