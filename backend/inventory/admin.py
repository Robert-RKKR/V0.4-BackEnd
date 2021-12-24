# Django Import:
from django.contrib import admin

# Application Import:
from .models.color_model import *
from .models.group_model import *
from .models.credential_model import *
from .models.device_model import *

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(ColorDeviceRelation)
admin.site.register(ColorGroupRelation)
admin.site.register(ColorCredentialRelation)
admin.site.register(Credential)
admin.site.register(Group)
admin.site.register(GroupDeviceRelation)
admin.site.register(Device)
admin.site.register(DeviceData)
admin.site.register(DeviceRawData)
admin.site.register(DeviceInterface)
