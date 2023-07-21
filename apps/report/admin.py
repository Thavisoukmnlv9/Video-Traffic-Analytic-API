from django.contrib import admin
from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('color', 'district','image')

    fieldsets = (
        (None, {
            'fields': ('color', 'district','image')
        }),
    )


admin.site.register(Report, ReportAdmin)

