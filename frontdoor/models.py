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
        return ("%s - %s" % (self.requesting_member, self.requesting_member_realm))


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
    created_at = models.DateTimeField(auto_now_add=True)

    #def __str__(self):
    #    return ("%s => %s => %s => %s => %s => %s" % (character_name, character_race, character_faction, character_server, character_class, character_spec))

    class Meta:
        managed = True
        db_table = 'processed_toons'
        verbose_name_plural = 'Processed Characters'
