# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-07-23 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Radios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clave', models.CharField(max_length=6, unique=True)),
                ('PACRadio', models.CharField(max_length=255)),
                ('RadioModel', models.CharField(default=True, max_length=250, null=True)),
                ('VersionFW', models.CharField(default=True, max_length=250, null=True)),
                ('Protocol', models.CharField(default=True, max_length=250, null=True)),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Station', models.CharField(max_length=8, null=True)),
                ('Data', models.CharField(max_length=250, null=True)),
                ('Lat', models.CharField(max_length=50, null=True)),
                ('Lng', models.CharField(max_length=50, null=True)),
                ('Reles', models.CharField(max_length=50, null=True)),
                ('Energia', models.CharField(max_length=50, null=True)),
                ('Blue', models.CharField(max_length=50, null=True)),
                ('Duplicate', models.BooleanField(default=False)),
                ('Snr', models.CharField(max_length=50, null=True)),
                ('AvgSnr', models.CharField(max_length=50, null=True)),
                ('Rssi', models.CharField(max_length=50, null=True)),
                ('SeqNumber', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
