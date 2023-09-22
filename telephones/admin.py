from django.contrib import admin

# Register your models here.
from .models import Profile, Department, Telephone, PositionType, Position, Assign

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    search_fields = ['last_name', 'first_name']

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    search_fields = ['dep_name']

@admin.register(Telephone)
class TelephoneAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    search_fields = ['extension']

@admin.register(PositionType)
class PositionTypeAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    search_fields = ['title']

@admin.register(Position)
class PositionAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    list_filter = ('dep',)
    search_fields = ['dep__dep_name', 'owner__last_name', 'owner__first_name']

@admin.register(Assign)
class AssignAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    css = {
             'all': ('templates/css/admin-extra.css ',)
        }
    search_fields = ['tel__extension', 'position__owner__last_name', 'position__dep__dep_name', 'position__owner__first_name']
