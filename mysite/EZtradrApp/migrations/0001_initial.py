# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-06 21:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('assetId', models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('assetName', models.CharField(max_length=50)),
                ('open', models.CharField(max_length=50)),
                ('close', models.CharField(max_length=50)),
                ('volume', models.IntegerField(default=0.0)),
                ('high', models.CharField(max_length=50)),
                ('low', models.CharField(max_length=50)),
                ('adjClose', models.CharField(max_length=50)),
                ('date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userId', models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Watch',
            fields=[
                ('watchId', models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('watchName', models.CharField(max_length=50)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EZtradrApp.User')),
            ],
        ),
        migrations.CreateModel(
            name='WatchAsset',
            fields=[
                ('watchAssetId', models.AutoField(auto_created=True, max_length=20, primary_key=True, serialize=False)),
                ('assetId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EZtradrApp.Asset')),
                ('watchId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EZtradrApp.Watch')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='watchasset',
            unique_together=set([('watchId', 'assetId')]),
        ),
    ]
