from django.contrib import admin

from .models import Menu


@admin.register(Menu)
class MessageAdmin(admin.ModelAdmin):
    list_display = [
        'pk',
        'item',
        'slug',
    ]
    search_fields = ('item',)
    empty_value_display = '-пусто-'
