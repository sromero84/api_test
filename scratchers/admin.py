from django.contrib import admin
from scratchers.models import Scratcher, Size
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultAdmin


class UserAdmin(DefaultAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'api_key', 'is_staff')


class ScratcherAdmin(admin.ModelAdmin):
    model = Scratcher
    ordering = ('item_name',)
    list_display = ('item_name', 'item_description', 'size', 'item_cost')


class SizeAdmin(admin.ModelAdmin):
    model = Size
    ordering = ('name',)
    list_display = ('name',)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Scratcher, ScratcherAdmin)
admin.site.register(Size, SizeAdmin)
