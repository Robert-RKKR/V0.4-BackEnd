# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel
from main.basemodel import BaseSubModel

# Models Import:
from inventory.models.device_model import DeviceType
from inventory.models.group_model import Group
from inventory.models.device_model import Device 


class Policy(BaseMainModel):
    """ Xxx """

    # Corelation witch device type model:
    device_type = models.OneToOneField(DeviceType, on_delete=models.PROTECT)

    # Main model values:


# Relations models:
class PolicyDeviceRelation(BaseSubModel):

    # Relations values:
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['policy', 'device']]

# Relations models:
class PolicyGroupRelation(BaseSubModel):

    # Relations values:
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['policy', 'group']]
