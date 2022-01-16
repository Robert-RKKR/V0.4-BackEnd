# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel
from main.basemodel import BaseSubModel

# Models Import:
from inventory.models.device_model import DeviceType
from inventory.models.group_model import Group
from inventory.models.device_model import Device
from django_celery_beat.models import IntervalSchedule

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
    devices = models.ManyToManyField(Device)
    groups = models.ManyToManyField(Group)

    # Main model values:
    task = models.IntegerField(choices=TASKS, default=0)
