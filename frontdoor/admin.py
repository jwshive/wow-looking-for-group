from django.contrib import admin
from .models import RequestedParses, SiteSettings, ProcessedToons, BanHammer

# Register your models here.
class RequestedParsesAdmin(admin.ModelAdmin):
    list_display = ('requesting_member', 'requesting_member_realm', 'created_at')

class ProcessedToonsAdmin(admin.ModelAdmin):
    list_display = ('character_name', 'character_race', 'character_faction', 'character_server', 'character_class', 'character_spec', 'character_level', 'character_equipped_ilevel')


admin.site.register(RequestedParses, RequestedParsesAdmin)
admin.site.register(SiteSettings)
admin.site.register(ProcessedToons, ProcessedToonsAdmin)
admin.site.register(BanHammer)
