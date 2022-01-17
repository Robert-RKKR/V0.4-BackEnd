# Django Import:
from django.contrib import admin

# Models Import:
from .models.fsm_template_model import FsmTemplate
from .models.policy_model import Policy


# Register your models here.
admin.site.register(FsmTemplate)
admin.site.register(Policy)