from django.contrib import admin
from .models import RequestedParses, SiteSettings, ProcessedToons

# Register your models here.
class RequestedParsesAdmin(admin.ModelAdmin):
    list_display = ('requesting_member', 'requesting_member_realm', 'created_at')

admin.site.register(RequestedParses, RequestedParsesAdmin)
admin.site.register(SiteSettings)
admin.site.register(ProcessedToons)
