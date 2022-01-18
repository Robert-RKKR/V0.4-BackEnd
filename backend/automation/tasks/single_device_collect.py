# Django import:
from unicodedata import name
from django.shortcuts import get_object_or_404

# Celery Import:
from celery import shared_task
from autocli.celery import app

# Model Import:
from inventory.models.device_model import Device

# Logger import:
from logger.logger import Logger

# Data collection Import:
from automation.connection.collectors.ssh_data_collector import SshDataCollector

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

            # Log starting of device data collection:
            ssh_logger.info(f'Starting of device {device.name} ({device.hostname}), data collection', device, task_id=self.request.id)

            # Collect data from device using Data Collection Manager class:
            data_collection = SshDataCollector(device, self.request.id)
            collect_output = data_collection.collect()

            # Check data collection status:
            if data_collection.status is False:
                ssh_logger.error(f'SSH data collection process failed', device, task_id=self.request.id)

            # Return:
            return collect_output

        else: # If device is not avaliable log error:

            # Log 404 device error:
            ssh_logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', device, task_id=self.request.id)

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
            ssh_logger.error(f'Device with ID {device_pk}, is not avaliable (Error 404).', device, task_id=self.request.id)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device PK variable can only be a intiger.')

    # Return single device collect status:
    return status
