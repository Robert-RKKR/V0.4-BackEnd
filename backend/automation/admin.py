# Django Import:
from django.contrib import admin

# Models Import:
from .models.device_type_template_model import DeviceTypeTemplate
from .models.fsm_template_model import FsmTemplate


# Register your models here.
admin.site.register(FsmTemplate)
admin.site.register(DeviceTypeTemplate)