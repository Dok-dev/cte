from django.contrib import admin

# Register your models here.

from .models import (
    Project,
    PrivateCloudPassport,
    S3Passport,
    MinimalYaml,
    ProjectDocuments,
    Manufacturer,
    Equipment,
    Server,
    Switch,
    Storage
)

# Настройка администраторских классов

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class PrivateCloudPassportAdmin(admin.ModelAdmin):
    list_display = ('project',)
    search_fields = ('project__name',)

class S3PassportAdmin(admin.ModelAdmin):
    list_display = ('project',)
    search_fields = ('project__name',)

class MinimalYamlAdmin(admin.ModelAdmin):
    list_display = ('project',)
    search_fields = ('project__name',)

class ProjectDocumentAdmin(admin.ModelAdmin):
    list_display = ('project', 'name')
    search_fields = ('project__name', 'name')

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('manufacturer', 'type', 'model', 'project')
    list_filter = ('type', 'manufacturer')
    search_fields = ('manufacturer__name', 'model', 'project__name')

class ServerAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'cpu', 'ram', 'storage_capacity', 'operating_system')
    search_fields = ('equipment__model', 'cpu', 'ram')

class SwitchAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'port_count', 'throughput', 'layer')
    search_fields = ('equipment__model', 'port_count', 'throughput')

class StorageAdmin(admin.ModelAdmin):
    list_display = ('equipment', 'capacity', 'type', 'raid_support')
    search_fields = ('equipment__model', 'capacity', 'type')

# Регистрация моделей и администраторских классов

admin.site.register(Project, ProjectAdmin)
admin.site.register(PrivateCloudPassport, PrivateCloudPassportAdmin)
admin.site.register(S3Passport, S3PassportAdmin)
admin.site.register(MinimalYaml, MinimalYamlAdmin)
admin.site.register(ProjectDocuments, ProjectDocumentAdmin)
admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Server, ServerAdmin)
admin.site.register(Switch, SwitchAdmin)
admin.site.register(Storage, StorageAdmin)
