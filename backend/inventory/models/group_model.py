# Django Import:
from django.db import models

# Other models Import:
from .device_model import Device

# Base Model Import:
from main.basemodel import BaseMainModel
from main.basemodel import BaseSubModel


# Model code:
class Group(BaseMainModel):
    """ Groups allow you to group network devices. """

    # Relationships with other models:
    devices = models.ManyToManyField(Device, through='GroupDeviceRelation')


# Relations models:
class GroupDeviceRelation(BaseSubModel):

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['device', 'group']]