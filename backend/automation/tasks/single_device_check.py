# Django import:
from django.shortcuts import get_object_or_404

# Celery Import:
from celery import shared_task
from autocli.celery import app

# Application Import:
from ..connection.netcon import NetCon
from ..connection.restcon import RestCon

# Model Import:
from inventory.models.device_model import Device

# Logger import:
from logger.logger import Logger

# Logger class initiation:
logger = Logger('Single device check')

@shared_task(bind=True, track_started=True, name='Check device status')
def single_device_check(self, device_pk: int) -> bool:
    """
        Check if device is available by using HTTPS request at the beginning,
        and an SSH connection if the HTTPS request fails.
    """
    # Single device check task status:
    status = None

    # Check if device_pk variable is intiger:
    if isinstance(device_pk, int):
        
        # Find Device object by ID:
        device = get_object_or_404(Device, pk=device_pk)

        # Check if device is instance of Device class:
        if isinstance(device, Device):
            
            # Connect to device using HTTPS request:
            https_connection = RestCon(device, self.request.id)
            https_connection.get('restconf')

            # Check HTTPS request output and change device status:
            if https_connection.status is True:
                # Log about HTTPS connection status:
                logger.debug(f'HTTPS testing connection to device {device.hostname}, was success.', device, task_id=self.request.id)

                # Update information about device status and task status:
                device.https_status = True
                device.ssh_status = True
                status = True
                device.save()
            else:
                # Connect to device using SSH connection:
                ssh_connection = NetCon(device, self.request.id)
            
                # Check SSH request output and change device status:
                if ssh_connection.status is True:
                    # Log about HTTPS and SSH connection status:
                    logger.debug(f'HTTPS testing connection to device {device.hostname}, failed.', device, device, task_id=self.request.id)
                    logger.debug(f'SSH testing connection to device {device.hostname}, was success.', device, device, task_id=self.request.id)

                    # Update information about device status and task status:
                    device.https_status = False
                    device.ssh_status = True
                    status = True
                    device.save()
                else:
                    # Log about HTTPS and SSH connection status:
                    logger.debug(f'HTTPS and SSH testing connection to device {device.hostname}, failed.', device, device, task_id=self.request.id)

                    # Update information about device status and task status:
                    device.https_status = False
                    device.ssh_status = False
                    status = False
                    device.save()

        else:  # If device is not avaliable log error:

            # Log 404 device error:
            logger.debug(f'Device with ID {device_pk}, is not avaliable (Error 404).', device, device, task_id=self.request.id)

    else: # If device variable is not a intiger, raise type error:
        raise TypeError('Device PK variable can only be a intiger.')

    # Return single device check status:
    return status
