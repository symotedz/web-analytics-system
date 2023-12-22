# admin.py

from django.contrib import admin
from .models import Super_Admin_User, School

@admin.register(Super_Admin_User)
class SuperAdminUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'Registration_date', 'status', 'country', 'contact', 'email', 'end_date')

    def end_date(self, obj):
        return obj.End_Date if obj.End_Date else ''
    
    end_date.short_description = 'End Date'

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('name', 'super_admin_user_name', 'Registration_date', 'status', 'country', 'County', 'location', 'contact', 'email', 'end_date')

    def super_admin_user_name(self, obj):
        return obj.user.name if obj.user else ''

    super_admin_user_name.short_description = 'Super Admin User Name'

    def end_date(self, obj):
        return obj.End_Date if obj.End_Date else ''
    
    end_date.short_description = 'End Date'
