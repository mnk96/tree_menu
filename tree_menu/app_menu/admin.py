from django.contrib import admin

from app_menu.models import Menu, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'menu', 'parent')
    list_filter = ('menu',)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('title', 'url')


admin.site.register(Item, ItemAdmin)
admin.site.register(Menu, MenuAdmin)
