# Django Import:
from django.db import models

# Validators Import:
from ..validators import (
    NameValueValidator,
    DescriptionValueValidator
)

# Applications Import:
from ..managers import ActiveManager


# Model code:
class Credential(models.Model):
    """ 
        The Credential specifies the login information (Login, password)
        needed in the login process when connecting to network devices.
    """

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
        verbose_name='Credential name',
        max_length=16,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'invalid': 'Enter the correct name value. It must contain 8 to 16 digits, letters and special characters -, _ or spaces.',
        },
    )
    username = models.CharField(
        verbose_name='User login',
        max_length=64, blank=False
    )
    password = models.CharField(
        verbose_name='User password',
        max_length=64, null=True, blank=True,
    )
    description = models.CharField(
        verbose_name='Credentials description',
        max_length=256, default='Credentials description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 16 digits, letters and special characters -, _, . or spaces.',
        },
    )

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

    # Meta sub class:
    class Meta:
        app_label = 'inventory'
        verbose_name = 'Credential'
        verbose_name_plural = 'Credentials'