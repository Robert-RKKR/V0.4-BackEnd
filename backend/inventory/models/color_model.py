# Django Import:
from django.db import models

# Other models Import:
from .credential_model import Credential
from .device_model import Device
from .group_model import Group

# Validators Import:
from ..validators import (
    NameValueValidator,
    DescriptionValueValidator,
    ColorValueValidator
)

# Applications Import:
from ..managers import NotDeleted

# Model code:
class Color(models.Model):
    """ 
        The Color model is working like Tag,
        available to be added to all device,
        group and credential models.
    """

    # Validators:
    name_validator = NameValueValidator()
    color_validator = ColorValueValidator()
    description_validator = DescriptionValueValidator()

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    # Main model values:
    name = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'invalid': 'Enter the correct name value. It must contain 8 to 32 digits, letters and special characters -, _ or spaces.',
        },
    )
    hexadecimal = models.CharField(
        unique=True,
        max_length=7,
        validators=[color_validator],
        error_messages={
            'null': 'Colour field is mandatory.',
            'blank': 'Colour field is mandatory.',
            'invalid': 'Enter the correct colour value. It must be a 3/6 hexadecimal number with # character on begining.',
        },
    )
    description = models.CharField(
        max_length=256, default='Credentials description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Relationships with other models:
    devices = models.ManyToManyField(Device, through='ColorDeviceRelation', blank=True)
    groups = models.ManyToManyField(Group, through='ColorGroupRelation', blank=True)
    credentials = models.ManyToManyField(Credential, through='ColorCredentialRelation', blank=True)

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"

    # Object managers:
    objects = NotDeleted()

    # Override default Delete method:
    def delete(self):
        """
            Override the default Delete method to see if the device was created by the Root user,
            if true don't change anything, otherwise change deleted value to true.
        """
        # Check if root value is True:
        if self.root == True:
            # Inform the user that the object cannot be deleted because is a root object:
            assert self.pk is not None, (
                f"{self._meta.object_name} object can't be deleted because its a root object.")
        else:
            # Change deleted value to True, to inform that object is deleted:
            self.deleted = True


# Relations models:
class ColorDeviceRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"ColorDeviceRelation({self.device}/{self.color})"

    class Meta:
        unique_together = [['device', 'color']]


class ColorGroupRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)

    # Relations values:
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"ColorGroupRelation({self.group}/{self.color})"

    class Meta:
        unique_together = [['group', 'color']]


class ColorCredentialRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)

    # Relations values:
    credential = models.ForeignKey(Credential, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"ColorCredentialRelation({self.credential}/{self.color})"

    class Meta:
        unique_together = [['credential', 'color']]
