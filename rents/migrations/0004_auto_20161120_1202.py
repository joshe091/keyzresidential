# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 17:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20161119_1947'),
        ('rents', '0003_auto_20161119_1949'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rent',
            name='place',
        ),
        migrations.AddField(
            model_name='contract',
            name='place',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='places.Place'),
            preserve_default=False,
        ),
    ]
