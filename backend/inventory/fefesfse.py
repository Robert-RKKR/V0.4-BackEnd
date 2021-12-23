# Django import:
from asgiref.sync import async_to_sync
from django.shortcuts import get_object_or_404

# Channels import:
from channels.layers import get_channel_layer

# Celery Import:
from celery import shared_task

# Application Import:
from .connection.netcon import NetCon
from .connection.restcon import RestCon
from .models.device import *

# Channels variable:
channel_layer = get_channel_layer()

@shared_task(bind=True, track_started=True)
def single_device_collect(self, device_pk: int) -> bool:
    """
        Collect data from device.
    """
    # Active devices check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_pk, int):

        # Find Device object by ID:
        device = get_object_or_404(Device, pk=device_pk)

        # Raport start of task:
        self.update_state(state=f'Collecting data about device: {device.hostname}.')

        # Collect data from device:
        ssh_connection = NetCon(self.device)
        ssh_connection.send_command('show interfaces')

        # Raport end of task:
        self.update_state(state=f'Data fom device {device.hostname} was collected.')

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('device variable can only be a intiger.')

    async_to_sync(channel_layer.group_send)('collect', {'type': 'send_collect', 'text': 'The task was completed'})


@shared_task(bind=True, track_started=True)
def single_device_check(self, device_pk: int) -> bool:
    """
        Check if device is available by using HTTPS request at the beginning,
        and an SSH connection if the HTTPS request fails.
    """
    # Single device check status:
    status = None

    # Check if device_id variable is intiger:
    if isinstance(device_pk, int):
        
        # Find Device object by ID:
        device = get_object_or_404(Device, pk=device_pk)
            
        # Connect to device using HTTPS request:
        https_connection = RestCon(device)
        https_connection.get('restconf')

        # Check HTTPS request output and change device status:
        if https_connection.status is True:
            device.https_status = True
            device.ssh_status = True
            status = True
            device.save()
        else:
            # Connect to device using SSH connection:
            ssh_connection = NetCon(device)
        
            # Check SSH request output and change device status:
            if ssh_connection.status is True:
                device.https_status = False
                device.ssh_status = True
                status = True
                device.save()
            else:
                device.https_status = False
                device.ssh_status = False
                status = False
                device.save()

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device variable can only be a intiger.')

    # Return single device check status:
    return status

@shared_task(bind=True, track_started=True)
def active_devices_check(self) -> bool:
    """
        Check all active devices if the are available by using HTTPS request at the beginning,
        and an SSH connection if the HTTPS request fails.
    """
    # Active devices check status:
    status = None
        
    # Collect all active devices:
    devices = Device.active.all()

    # Iterate thru all active devices:
    for device in devices:
            
        # Check device status:
        single_device_check.delay(device.pk)

    # Return active devices check status:
    return status
