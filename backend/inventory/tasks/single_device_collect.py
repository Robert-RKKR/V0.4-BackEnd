# Django import:
from unicodedata import name
from django.shortcuts import get_object_or_404

# Celery Import:
from celery import shared_task
from autocli.celery import app

# Model Import:
from ..models.device_model import Device

# Logger import:
from logger.logger import Logger

# Data collection Import:
from ..connection.data_collection.data_ssh_collection import DataSSHCollectionManager

# Logger class initiation:
ssh_logger = Logger('Single device SSH collect')
https_logger = Logger('Single device HTTPS collect')

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

            ######### TEST LOG
            ssh_logger.info(f'--------------------------------------------------------------------------', device)

            # Log starting of device data collection:
            ssh_logger.info(f'Starting of device {device.name} ({device.hostname}), data collection', device)

            # Collect data from device using Data Collection Manager class:
            data_collection = DataSSHCollectionManager(device)
            return data_collection.collect()

        else: # If device is not avaliable log error:

            # Log 404 device error:
            ssh_logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', device)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device PK variable can only be a intiger.')

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
        raise TypeError('Device PK variable can only be a intiger.')

    # Return single device collect status:
    return status
