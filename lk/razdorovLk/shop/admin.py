from django.contrib import admin
from .models import ShopItem


class ShoptAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', ]


admin.site.register(ShopItem)

