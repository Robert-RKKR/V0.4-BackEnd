# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseMainModel

# Models Import:
from .device_type_template_model import DeviceTypeTemplate

class FsmTemplate(BaseMainModel):
    """ Xxx """

    # Corelation witch device type template:
    device_type = models.ForeignKey(DeviceTypeTemplate, on_delete=models.PROTECT)

    # Main model values:
    command = models.CharField(max_length=128)
    sfm_expression = models.TextField()

    # Connections with other device models:
    device_data = models.BooleanField(default=False)
    device_interface = models.BooleanField(default=False)
