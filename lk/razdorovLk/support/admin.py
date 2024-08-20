from django.contrib import admin
from .models import Support


class SupportAdmin(admin.ModelAdmin):
    list_display = ["topic", "completed"]
    list_filter = ["completed", "topic"]



admin.site.register(Support, SupportAdmin)
