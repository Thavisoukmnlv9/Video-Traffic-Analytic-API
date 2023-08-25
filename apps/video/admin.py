from django.contrib import admin
from .models import Video

class VideoAdmin(admin.ModelAdmin):
    list_display = ('location_name', 'video',)
    
    fieldsets = (
        (None, {
            'fields': ('location_name', 'video',)
        }),
    )

admin.site.register(Video, VideoAdmin)
