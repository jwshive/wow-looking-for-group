# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-09 16:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontdoor', '0003_banhammer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.IntegerField(primary_key=True, serialize=False)),
                ('class_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'WoW Classes',
                'managed': True,
                'db_table': 'wow_classes',
            },
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('faction_id', models.IntegerField(primary_key=True, serialize=False)),
                ('faction_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'WoW Factions',
                'managed': True,
                'db_table': 'wow_factions',
            },
        ),
        migrations.CreateModel(
            name='ItemsOfValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'WoW Items Of Value',
                'managed': True,
                'db_table': 'wow_items_of_value',
            },
        ),
        migrations.CreateModel(
            name='Races',
            fields=[
                ('race_id', models.IntegerField(primary_key=True, serialize=False)),
                ('race_name', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'WoW Races',
                'managed': True,
                'db_table': 'wow_races',
            },
        ),
        migrations.CreateModel(
            name='RaidIDs',
            fields=[
                ('raid_id', models.IntegerField(primary_key=True, serialize=False)),
            ],
            options={
                'verbose_name_plural': 'WoW Watched Raid IDs',
                'managed': True,
                'db_table': 'wow_raid_ids',
            },
        ),
        migrations.CreateModel(
            name='RaidLevels',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raid_level', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'WoW Raid Difficulties',
                'managed': True,
                'db_table': 'wow_raid_levels',
            },
        ),
        migrations.RemoveField(
            model_name='banhammer',
            name='character_name',
        ),
        migrations.DeleteModel(
            name='BanHammer',
        ),
    ]
