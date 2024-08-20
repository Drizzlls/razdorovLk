from django.contrib import admin
from .models import Employees, Affairs, StageAffairs

class StageAffairsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Employees)
admin.site.register(Affairs)
admin.site.register(StageAffairs, StageAffairsAdmin)
