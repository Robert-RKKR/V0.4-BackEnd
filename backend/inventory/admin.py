# Django Import:
from django.contrib import admin

# Application Import:
from .models.color_model import *
from .models.group_model import *
from .models.credential_model import *
from .models.device_model import *

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(Credential)
admin.site.register(Group)
admin.site.register(DeviceType)
admin.site.register(DeviceData)
admin.site.register(DeviceRawData)
admin.site.register(DeviceInterface)

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    empty_value_display = '-None-'
    list_display = (
        'name', 'hostname', 'ssh_status',
        'https_status',
    )
    list_filter = (
        'active', 'device_type', 'credential',
    )
    search_fields = (
        'name', 'hostname',
    )
    ordering = (
        'name', 'hostname',
    )
    fields = (
        'active',
        ('name', 'hostname'),
        ('device_type', 'ico'),
        ('ssh_port', 'https_port'),
        ('credential', 'secret', 'token'),
        'certificate',
        'description',
    )
