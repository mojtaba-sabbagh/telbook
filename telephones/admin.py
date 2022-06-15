from django.contrib import admin

# Register your models here.
from .models import Profile, Department, Telephone, PositionType, Position, Assign

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }

@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }

@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
