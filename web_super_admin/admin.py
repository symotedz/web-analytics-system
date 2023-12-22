# admin.py

from django.contrib import admin
from .models import Super_Admin_User, School

@admin.register(Super_Admin_User)
class SuperAdminUserAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'super_admin_user_name')

    def super_admin_user_name(self, obj):
        return obj.user.name if obj.user else ''

    super_admin_user_name.short_description = 'Super Admin User Name'
