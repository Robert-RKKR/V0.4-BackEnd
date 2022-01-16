# Django Import:
from django.contrib import admin

# Models Import:
from .models.fsm_template_model import FsmTemplate
from .models.policy_manager_model import PolicyManager
from .models.policy_model import Policy
from .models.task_manager_model import TaskManager


# Register your models here.
admin.site.register(FsmTemplate)
admin.site.register(PolicyManager)
admin.site.register(Policy)
admin.site.register(TaskManager)