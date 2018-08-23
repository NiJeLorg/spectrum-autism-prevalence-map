# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 03:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autism_prevalence_map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studies',
            name='latitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
        migrations.AddField(
            model_name='studies',
            name='longitude',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]