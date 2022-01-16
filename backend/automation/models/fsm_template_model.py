# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel

# Models Import:
from inventory.models.device_model import DeviceType


class FsmTemplate(BaseMainModel):
    """ Xxx """

    # Corelation witch device type template:
    device_type = models.ForeignKey(DeviceType, on_delete=models.PROTECT, null=True, blank=True)

    # Main model values:
    device_template = models.BooleanField(default=False)
    command = models.CharField(max_length=128, null=True, blank=True)
    sfm_expression = models.TextField()

    # Connections with other device models:
    device_data = models.BooleanField(default=False)
    device_interface = models.BooleanField(default=False)
