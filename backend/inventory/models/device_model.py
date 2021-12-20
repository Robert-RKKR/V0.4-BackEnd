# Django Import:
from django.db import models

# Validators Import:
from ..validators import (
    HostnameValueValidator,
    NameValueValidator,
    DescriptionValueValidator
)

# Applications Import:
from ..managers import NotDeleted, ActiveManager
from .icons import ICONS

# Other models Import:
from .credential_model import Credential


# Model code:
class Device(models.Model):
    """ 
        Devices is the main component of the AutoCli application,
        it contains basic network Information about devices that
        are not collected directly from the devices themselves.
    """

    # Validators:
    hostname_validator = HostnameValueValidator()
    name_validator = NameValueValidator()
    description_validator = DescriptionValueValidator()

    # Static values:
    DEVICE_TYPE = (
        (0, 'Autodetect'),
        (1, 'Cisco IOS'),
        (2, 'Cisco XR'),
        (3, 'Cisco XE'),
        (4, 'Cisco NXOS'),
        (6, 'Cisco ASA'),
    )

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    # Device status:
    ssh_status = models.BooleanField(default=False)
    https_status = models.BooleanField(default=False)

    # Main model values:
    name = models.CharField(
        verbose_name='Device name',
        max_length=32,
        blank=False,
        unique=True,
        validators=[hostname_validator],
        error_messages={
            'null': 'Hostname field is mandatory.',
            'blank': 'Hostname field is mandatory.',
            'invalid': 'Enter the correct name value. It must contain 8 to 16 digits, letters and special characters -, _ or spaces.',
        },
    )
    hostname = models.CharField(
        verbose_name='IP / DNS name',
        max_length=32,
        blank=False,
        unique=True,
        validators=[hostname_validator],
        error_messages={
            'null': 'IP / DNS name field is mandatory.',
            'blank': 'IP / DNS name field is mandatory.',
            'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.',
        },
    )
    device_type = models.IntegerField(
        verbose_name='Device type',
        choices=DEVICE_TYPE,
        default=0
    )
    ico = models.IntegerField(
        verbose_name='Device graphic',
        choices=ICONS,
        default=0
    )
    ssh_port = models.IntegerField(
        verbose_name='SSH port',
        default=22
    )
    https_port = models.IntegerField(
        verbose_name='HTTPS port',
        default=443
    )
    description = models.CharField(
        verbose_name='Device description',
        max_length=256, default='Device description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 16 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Security and credentials:
    credential = models.ForeignKey(
        Credential, on_delete=models.PROTECT, null=True, blank=True
    )
    secret = models.CharField(
        verbose_name='Cisco secret password',
        max_length=64, null=True, blank=True
    )
    token = models.CharField(
        verbose_name='Device token',
        max_length=128, null=True, blank=True
    )
    certificate = models.BooleanField(
        verbose_name='Device certificate check',
        default=False
    )

    # Object managers:
    objects = NotDeleted()
    active = ActiveManager()

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.name}"

    # Override default Delete method:
    # def delete(self):
    #     """
    #         Override the default Delete method to see if the device was created by the Root user,
    #         if true don't change anything, otherwise change deleted value to true.
    #     """
    #     # Check if root value is True:
    #     if self.root == True:
    #         # Inform the user that the object cannot be deleted because is a root object:
    #         assert self.pk is not None, (
    #             f"{self._meta.object_name} object can't be deleted because its a root object.")
    #     else:
    #         # Change deleted value to True, to inform that object is deleted:
    #         self.deleted = True


    # Meta sub class:
    class Meta:
        app_label = 'inventory'
        verbose_name = 'Device'
        verbose_name_plural = 'Devices'


class DeviceData(models.Model):

    # Corelation witch device model:
    device = models.ForeignKey(Device, on_delete=models.CASCADE, null=False, blank=False)

    # Creation data:
    created = models.DateTimeField(auto_now_add=True)

    # Show version output:
    version = models.CharField(max_length=64, blank=True, null=True)
    hostname = models.CharField(max_length=64, blank=True, null=True)
    uptime = models.CharField(max_length=64, blank=True, null=True)
    reload_reason = models.CharField(max_length=64, blank=True, null=True)
    running_image = models.CharField(max_length=64, blank=True, null=True)
    config_register = models.CharField(max_length=64, blank=True, null=True)
    hardware_list = models.JSONField(blank=True, null=True)
    serial_list = models.JSONField(blank=True, null=True)
    mac_list = models.JSONField(blank=True, null=True)
