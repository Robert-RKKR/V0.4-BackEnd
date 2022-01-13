# Python Import:
import textfsm

# Model Import:
from ...models.device_model import *

# Logger import:
from logger.logger import Logger

# Application Import:
from ...connection.netcon import NetCon

# Logger class initiation:
logger = Logger('SSH data Collector')

# Constance:
SSH_TEMPLATE_PATH = 'inventory/connection/data_collection/ssh_templates/'
COLLRECTOR_TEMPLATE_PATH = 'inventory/connection/data_collection/collector_templates/'

class SshDataCollector:

    def __init__(self, device: Device) -> None:
        """
            Data Collection manager, take Device class object to collect data from network device.
            Data is collected via SSH protocol depending on the operating system
            (Cisco IOS, IOS XE, NX OS or ASA OS) of the network device.

                Class attributes:
                -----------------
                device: Device object
                    Device from which data will be collected.
                
                Methods:
                --------
                
        """
        # Check if device is instance of Device class:
        if isinstance(device, Device):

            self.device = device
            self.status = None

        else: # If device variable is not a instance of Device class, raise type error:
            raise TypeError('Provided device variable is not a instance of Device class.')