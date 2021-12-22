# Django Import:
from django.db import models

# Validators Import:
from ..validators import (
    NameValueValidator,
    DescriptionValueValidator
)

# Other models Import:
from .device_model import Device


# Model code:
class Group(models.Model):
    """ Groups allow you to group network devices. """

    # Validators:
    name_validator = NameValueValidator()
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
            'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.',
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
    devices = models.ManyToManyField(Device, through='GroupDeviceRelation')

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"

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
class GroupDeviceRelation(models.Model):

    # Creation values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)

    # Relations values:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"GroupDeviceRelation({self.device}/{self.group})"

    # Override default Delete method:
    def delete(self, *args, **kwargs):
        """
            Override the default Delete method to see if the device was created by the Root user,
            if true don't change anything.
        """
        # Check if root value is True:
        if self.root == True:
            # Inform the user that the object cannot be deleted because is a root object:
            assert self.pk is not None, (
                f"{self._meta.object_name} object can't be deleted because its a root object.")
        else:
            super().delete(*args, **kwargs)

    class Meta:
        unique_together = [['device', 'group']]