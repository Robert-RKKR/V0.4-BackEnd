# Django Import:
from django.contrib import admin

# Application Import:
from .models.color import *
from .models.group import *
from .models.credential import *
from .models.device import *

# Register Application models in Django Admin:
admin.site.register(Color)
admin.site.register(ColorDeviceRelation)
admin.site.register(ColorGroupRelation)
admin.site.register(ColorCredentialRelation)
admin.site.register(Credential)
admin.site.register(Group)
admin.site.register(GroupDeviceRelation)
admin.site.register(Device)
