# Python Import:
import textfsm
import json

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
            Data Collection Manager, takes a Device class object to retrieve data from a network device.
            Data are collected via SSH protocol. Depending on the operating system
            (Cisco IOS, IOS XE, NX OS, or ASA OS), the data collection process may be different.
            Information about the support of different network systems are retrieved from JSON files.

                Class attributes:
                -----------------
                device: Device object
                    Device from which data will be collected.
                
                Methods:
                --------
                collect_data:
        """
        # Check if collected device variable is instance of Device class:
        if isinstance(device, Device):

            self.device = device
            self.status = None
            self.saved = False
            self.collected_data = {}
            self.processed_data = {}

        else: # If device variable is not a instance of Device class, raise type error:
            raise TypeError('Provided device variable is not a instance of Device class.')

    def collect(self) -> bool:
        """
            Collect data from a network device using the SSH protocol.
            Process collected data using TextFSM templates.
            Save processed data to objects that would be linked to the main Device class.
        """

        pass

    def collect_data(self) -> bool:
        """
            Collect data from a network device using the SSH protocol.
        """

        # Collect collector template:
        collector_template = self._collect_template(self.device.get_device_type_display)

        # Check if collected data are valid:
        if collector_template is not False:
            # Check collector template is ready to use:
            if collector_template.get('status', False) is True:
                pass
            else:
                logger.error('This device type is currently not supported.')
        else:
            logger.error('This device type is currently not supported.')

    def process_data(self) -> bool:
        """ Process collected data using TextFSM templates. """

        pass

    def save_data(self) -> bool:
        """ Save processed data to objects that would be linked to the main Device class. """

        pass

    def _collect_template(self, device_type_name):
        """ Collect collector template. """

        # Create collector template path:
        path_to_template = COLLRECTOR_TEMPLATE_PATH + device_type_name + '.json'
        
        # Try to collect data:
        try:
            # Collect collector template from JSON file:
            template_text = open(path_to_template).read()
            # Return python dictionary based on collected JSON data:
            return json.loads(template_text)
        except:
            # Return False if error occurs during data collection process:
            return False