from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from menu.models import MenuItem


@admin.register(MenuItem)
class MenuItemMPTTModelAdmin(MPTTModelAdmin):
    mptt_level_indent = 20
    list_display = [
        'name',
        'slag',
    ]
    search_fields = ['name']
    list_filter = ['parent']
