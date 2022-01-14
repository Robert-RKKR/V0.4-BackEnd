# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel

# Models Import:
from inventory.models.device_model import DeviceType


class DeviceTypeTemplate(BaseMainModel):
    """ Xxx """

    # Corelation witch device type model:
    device_type = models.OneToOneField(DeviceType, on_delete=models.PROTECT)
