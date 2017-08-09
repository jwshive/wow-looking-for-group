from django.db import models
from django.contrib.postgres.fields import JSONField

# Create your models here.
class SiteSettings(models.Model):
    client_id = models.CharField(max_length=50)
    client_secret = models.CharField(max_length=50)
    blizzard_api_url_base = models.CharField(max_length=100)
    blizzard_api_image_url_base = models.CharField(max_length=100)
    blizzard_armory_base_link = models.CharField(max_length=100)

    def __str__(self):
        return self.client_id

    class Meta:
        managed = True
        db_table = 'site_settings'
        verbose_name_plural = 'Website Settings'


class RequestedParses(models.Model):
    requesting_member = models.CharField(max_length=12)
    requesting_member_realm = models.CharField(max_length=50)
    group_string = models.TextField()
    json_string = JSONField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return ("[%s] %s - %s" % (self.pk, self.requesting_member, self.requesting_member_realm))


    class Meta:
       managed = True
       db_table = 'group_lookup_requests'
       verbose_name_plural = 'Group Lookups'


class ProcessedToons(models.Model):
    character_name = models.CharField(max_length=12)
    character_race = models.CharField(max_length=15)
    character_faction = models.CharField(max_length=15)
    character_server = models.CharField(max_length=20)
    character_class = models.CharField(max_length=20)
    character_spec = models.CharField(max_length=20)
    character_level = models.IntegerField()
    character_thumbnail = models.CharField(max_length=100)
    character_equipped_ilevel = models.IntegerField()
    character_legendaries = models.CharField(max_length=100)
    character_progression = models.TextField()
    group_lookup_trackback = models.ForeignKey(RequestedParses)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ("%s => %s => %s => %s => %s => %s" % (self.character_name, self.character_race, self.character_faction, self.character_server, self.character_class, self.character_spec))

    class Meta:
        managed = True
        db_table = 'processed_toons'
        verbose_name_plural = 'Processed Characters'


class Classes(models.Model):
    class_id = models.IntegerField(primary_key=True)
    class_name = models.CharField(max_length=20)

    def __str__(self):
        return self.class_name

    class Meta:
        managed = True
        db_table = 'wow_classes'
        verbose_name_plural = 'WoW Classes'


class Races(models.Model):
    race_id = models.IntegerField(primary_key=True)
    race_name = models.CharField(max_length=20)

    def __str__(self):
        return "[%s] %s" % (self.race_id, self.race_name)

    class Meta:
        managed = True
        db_table = 'wow_races'
        verbose_name_plural = 'WoW Races'


class Faction(models.Model):
    faction_id = models.IntegerField(primary_key=True)
    faction_name = models.CharField(max_length=20)

    def __str__(self):
        return self.faction_name

    class Meta:
        managed = True
        db_table = 'wow_factions'
        verbose_name_plural = 'WoW Factions'


class ItemsOfValue(models.Model):
    item_name = models.CharField(max_length=20)

    def __str__(self):
        return self.item_name

    class Meta:
        managed = True
        db_table = 'wow_items_of_value'
        verbose_name_plural = 'WoW Items Of Value'


class RaidIDs(models.Model):
    raid_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return str(self.raid_id)

    class Meta:
        managed = True
        db_table = 'wow_raid_ids'
        verbose_name_plural = 'WoW Watched Raid IDs'


class RaidLevels(models.Model):
    raid_level = models.CharField(max_length=20)

    def __str__(self):
        return self.raid_level

    class Meta:
        managed = True
        db_table = 'wow_raid_levels'
        verbose_name_plural = 'WoW Raid Difficulties'


    
