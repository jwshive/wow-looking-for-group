# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-14 18:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0005_processedtoons_character_weapon_ilevel'),
    ]

    operations = [
        migrations.AddField(
            model_name='processedtoons',
            name='character_points_spent',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
