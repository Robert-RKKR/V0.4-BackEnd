# Model Import:
from ...models.device_model import *

# Constance:
TEMPLATE_PATH = 'inventory/connection/data_collection/ssh_templates/'

# Commands database:
commands_database = {
    'cisco_ios': [
        {
            'command_name': 'ios show version',
            'command_template_name': 'cisco_ios_show_version.textfsm',
            'model': DeviceData,
        },
        {
            'command_name': 'show interfaces status',
            'command_template_name': 'cisco_ios_show_interfaces_status.textfsm',
            'model': DeviceInterface,
        },
    ],
    'cisco_nxos': [
        None,
    ],
    'cisco_asa': [
        None,
    ]
}


class DataSSHCollectionManager:

    def __init__(self, device: Device) -> None:
        """
            Data Collection Manager, take Device class object to collect data from network device.
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

            # Che
            self._manage_system_version()

        else: # If device variable is not a instance of Device class, raise type error:
            raise TypeError('Provided device variable is not a instance of Device class.')

    def _manage_system_version(self):

        pass

    def _manage_data_collection(self):

        pass

    def _collect_data(self):

        pass

    def _save_raw_data(self):

        pass

    def _parse_data(self):

        pass
