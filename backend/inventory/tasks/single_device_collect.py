# Django import:
from unicodedata import name
from django.shortcuts import get_object_or_404

# Celery Import:
from celery import shared_task
from autocli.celery import app

# Application Import:
from ..connection.netcon import NetCon
from ..connection.restcon import RestCon

# Model Import:
from ..models.device_model import Device

# Logger import:
from logger.logger import Logger

# Logger class initiation:
ssh_logger = Logger('single_device_ssh_collect')
https_logger = Logger('single_device_https_collect')

@shared_task(bind=True, track_started=True, name='Collect device data (SSH)')
def single_device_ssh_collect(self, device_pk: int) -> bool:
    """
        Collect data from device, using SSH protocol.
    """
    # Single device collect status:
    status = None

    # Check if device_pk variable is intiger:
    if isinstance(device_pk, int):

        # Find Device object by ID:
        device = get_object_or_404(Device, pk=device_pk)

        # Check if device is instance of Device class:
        if isinstance(device, Device):

            # Log starting of device data collection:
            ssh_logger.error(f'Starting of device {device.hostname}, data collection', device)

            # Collect data from device:
            ssh_connection = NetCon(device)
            ssh_connection.send_command('show interfaces')

        else: # If device is not avaliable log error:

            # Log 404 device error:
            ssh_logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', device)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('device variable can only be a intiger.')

    # Return single device collect status:
    return status

@shared_task(bind=True, track_started=True, name='Collect device data (HTTPS)')
def single_device_https_collect(self, device_pk: int) -> bool:
    """
        Collect data from device, using HTTPS protocol.
    """
    # Single device collect status:
    status = None

    # Check if device_pk variable is intiger:
    if isinstance(device_pk, int):

        # Find Device object by ID:
        device = get_object_or_404(Device, pk=device_pk)

        # Check if device is instance of Device class:
        if isinstance(device, Device):

            pass

        else: # If device is not avaliable log error:

            # Log 404 device error:
            ssh_logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', device)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('device variable can only be a intiger.')

    # Return single device collect status:
    return status
