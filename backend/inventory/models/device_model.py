# Django Import:
from unicodedata import name
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

# Base Model Import:
from main.basemodel import BaseAutoCliModel


# Model code:
class Device(BaseAutoCliModel, models.Model):
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
        max_length=32,
        blank=False,
        unique=True,
        validators=[name_validator],
        error_messages={
            'null': 'Name field is mandatory.',
            'blank': 'Name field is mandatory.',
            'unique': 'Device with this name already exists.',
            'invalid': 'Enter the correct name value. It must contain 4 to 32 digits, letters and special characters -, _ or spaces.',
        },
    )
    hostname = models.CharField(
        max_length=32,
        blank=False,
        unique=True,
        validators=[hostname_validator],
        error_messages={
            'null': 'IP / DNS name field is mandatory.',
            'blank': 'IP / DNS name field is mandatory.',
            'unique': 'Device with this hostname already exists.',
            'invalid': 'Enter a valid IP address or DNS resolvable hostname. It must contain 4 to 32 digits, letters and special characters -, _, . or spaces.',
        },
    )
    device_type = models.IntegerField(choices=DEVICE_TYPE, default=0)
    ico = models.IntegerField(choices=ICONS, default=0)
    ssh_port = models.IntegerField(default=22)
    https_port = models.IntegerField(default=443)
    description = models.CharField(
        max_length=256, default='Device description.',
        validators=[description_validator],
        error_messages={
            'invalid': 'Enter the correct description value. It must contain 8 to 256 digits, letters and special characters -, _, . or spaces.',
        },
    )

    # Security and credentials:
    credential = models.ForeignKey(Credential, on_delete=models.PROTECT, null=True, blank=True)
    secret = models.CharField(max_length=64, null=True, blank=True)
    token = models.CharField(max_length=128, null=True, blank=True)
    certificate = models.BooleanField(default=False)

    # Object managers:
    objects = NotDeleted()

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
            self.save()


class DeviceData(BaseAutoCliModel, models.Model):

    # Corelation witch device model:
    device = models.OneToOneField(Device, on_delete=models.CASCADE)

    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

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

    # Model representation:
    def __str__(self) -> str:
        return f"DeviceData({self.pk}: device({self.device}))"


class DeviceInterface(BaseAutoCliModel, models.Model):

    # Corelation witch device model and unique:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    port = models.CharField(max_length=64, blank=True, null=True)

    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # # Show interfaces status output:
    # name = models.CharField(max_length=64, blank=True, null=True)
    # status = models.CharField(max_length=64, blank=True, null=True)
    # vlan = models.CharField(max_length=64, blank=True, null=True)
    # type = models.CharField(max_length=64, blank=True, null=True)

    # Show interfaces output:
    link_status = models.CharField(max_length=64, blank=True, null=True)
    protocol_status = models.CharField(max_length=64, blank=True, null=True)
    hardware_type = models.CharField(max_length=64, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    bia = models.CharField(max_length=64, blank=True, null=True)
    description = models.CharField(max_length=64, blank=True, null=True)
    ip_address = models.CharField(max_length=64, blank=True, null=True)
    mtu = models.CharField(max_length=64, blank=True, null=True)
    duplex = models.CharField(max_length=64, blank=True, null=True)
    speed = models.CharField(max_length=64, blank=True, null=True)
    media_type = models.CharField(max_length=64, blank=True, null=True)
    bandwidth = models.CharField(max_length=64, blank=True, null=True)
    delay = models.CharField(max_length=64, blank=True, null=True)
    encapsulation = models.CharField(max_length=64, blank=True, null=True)
    last_input = models.CharField(max_length=64, blank=True, null=True)
    last_output = models.CharField(max_length=64, blank=True, null=True)
    last_output_hang = models.CharField(max_length=64, blank=True, null=True)
    queue_strategy = models.CharField(max_length=64, blank=True, null=True)
    input_rate = models.CharField(max_length=64, blank=True, null=True)
    output_rate = models.CharField(max_length=64, blank=True, null=True)
    input_packets = models.CharField(max_length=64, blank=True, null=True)
    output_packets = models.CharField(max_length=64, blank=True, null=True)
    input_errors = models.CharField(max_length=64, blank=True, null=True)
    crc = models.CharField(max_length=64, blank=True, null=True)
    abort = models.CharField(max_length=64, blank=True, null=True)
    output_errors = models.CharField(max_length=64, blank=True, null=True)


    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk}: {self.port}: device({self.device})"

    class Meta:
        unique_together = [['device', 'port']]


class DeviceRawData(BaseAutoCliModel, models.Model):

    # Corelation witch device model:
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    # Creation data:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Command raw data:
    command_name = models.CharField(max_length=64)
    command_data = models.TextField(null=True, blank=True)

    # Model representation:
    def __str__(self) -> str:
        return f"DeviceRawData({self.pk}: device({self.device}), '{self.command_name}')"

    class Meta:
        unique_together = [['device', 'command_name']]

