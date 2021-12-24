# Model Import:
from ...models.device_model import *

# Logger import:
from logger.logger import Logger

# Application Import:
from ...connection.netcon import NetCon

# Logger class initiation:
logger = Logger('Data SSH Collector')

# Constance:
TEMPLATE_PATH = 'inventory/connection/data_collection/ssh_templates/'

# Commands database:
commands_database = {
    'cisco_ios': [
        {
            'command_name': 'show version',
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

        else: # If device variable is not a instance of Device class, raise type error:
            raise TypeError('Provided device variable is not a instance of Device class.')

    def collect(self) -> bool:
        """ Xxx """
        # Check device type supported status if yes collect data:
        device_type = self._system_version_check()
        if device_type == 'unsupported':
            logger.error('This device type is currently not supported.')
            self.status = False
            return False
        else:
            output = self._manage_data_collection(device_type)
            return output

    def _system_version_check(self):
        """ Check if device type is supported """
        # Check device type supported status function:
        def check(device_type):
            for commands_device_type in commands_database:
                if commands_device_type == device_type:
                    if commands_database[commands_device_type] is None:
                        return 'unsupported'
                    else:
                        return device_type
                else:
                    return 'unsupported'

        # Device type value:
        device_type = None

        # Change device ID type to device type name:
        if self.device.device_type == 1:
            # Check if device is supported:
            device_type = check('cisco_ios')
        elif self.device.device_type == 2:
            # Check if device is supported:
            device_type = check('cisco_xr')
        elif self.device.device_type == 3:
            # Check if device is supported:
            device_type = check('cisco_xe')
        elif self.device.device_type == 4:
            # Check if device is supported:
            device_type = check('cisco_nxos')
        else:
            device_type = 'unsupported'

        # Run data collection manager:
        return device_type

    def _manage_data_collection(self, device_type):
        """ Xxx """
        # Collect commands list related to current device type:
        for commands_device_type in commands_database:
            if commands_device_type == device_type:
                commands_list = commands_database[commands_device_type]

                # Clear current Device Raw Data:
                try:
                    DeviceRawData.objects.filter(device=self.device).delete()
                except:
                    pass

                # Iterate thru command list:
                for command_data in commands_list:

                    # Collect data based in provided command:
                    collected_data = self._collect_data(command_data)
                    
                    # Save raw data to database:
                    self._save_raw_data(collected_data, command_data)

                    # Parse collected data using collected data and template:
                    self._parse_data(collected_data)

    def _collect_data(self, command_data):
        """ Xxx """
        ssh_connection = NetCon(self.device)
        output = ssh_connection.send_command(command_data['command_name'])
        return output

    def _save_raw_data(self, collected_data, command_data):
        """ Xxx """
        new_raw_data = DeviceRawData(
            device=self.device,
            command_name=command_data['command_name'],
            command_data=collected_data,
        )
        new_raw_data.save()
        return new_raw_data

    def _parse_data(self, collected_data):
        """ Xxx """
        pass
