# Django Import:
from django.db import models

# Other models Import:
from .credential_model import Credential
from .device_model import Device
from .group_model import Group

# Validators Import:
from ..validators import ColorValueValidator

# Base Model Import:
from main.basemodel import BaseMainModel

# Model code:
class Color(BaseMainModel):
    """ 
        The Color model is working like Tag,
        available to be added to all device,
        group and credential models.
    """

    # Validators:
    color_validator = ColorValueValidator()

    # Main model values:
    hexadecimal = models.CharField(
        unique=True,
        max_length=7,
        validators=[color_validator],
        error_messages={
            'null': 'Colour field is mandatory.',
            'blank': 'Colour field is mandatory.',
            'unique': 'Color with this hexadecimal value already exists.',
            'invalid': 'Enter the correct colour value. It must be a 3/6 hexadecimal number with # character on begining.',
        },
    )

    # Relationships with other models:
    devices = models.ManyToManyField(Device, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    credentials = models.ManyToManyField(Credential, blank=True)