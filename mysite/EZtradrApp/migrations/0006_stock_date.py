# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-30 17:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EZtradrApp', '0005_auto_20170130_0229'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
