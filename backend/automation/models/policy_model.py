# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel
from main.basemodel import BaseSubModel

# Models Import:
from automation.models.fsm_template_model import FsmTemplate
from django_celery_beat.models import IntervalSchedule
from inventory.models.device_model import Device
from inventory.models.group_model import Group


TASKS = (
    (0, ('Devices configuration')),
    (1, ('Single device check')),
    (2, ('Single device collect')),
)


class Policy(BaseMainModel):
    """ Xxx """

    # Corelation witch scheduler model:
    scheduler = models.ForeignKey(IntervalSchedule, on_delete=models.CASCADE, null=True, blank=True)

    # Relationships with other models:
    devices = models.ManyToManyField(Device, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    templates = models.ManyToManyField(FsmTemplate, blank=True)

    # Main model values:
    task = models.IntegerField(choices=TASKS, default=0)
