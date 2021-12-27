# Python Import:
import textfsm

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
            'command_name': 'show interfaces description',
            'command_template_name': 'cisco_ios/cisco_ios_show_interfaces_description.textfsm',
            'model': DeviceInterface,
        },
        # {
        #     'command_name': 'show interfaces status',
        #     'command_template_name': 'cisco_ios/cisco_ios_show_interfaces_status.textfsm',
        #     'model': DeviceInterface,
        # },
        # {
        #     'command_name': 'show interfaces switchport',
        #     'command_template_name': 'cisco_ios/cisco_ios_show_interfaces_switchport.textfsm',
        #     'model': DeviceInterface,
        # },
        {
            'command_name': 'show interfaces',
            'command_template_name': 'cisco_ios/cisco_ios_show_interfaces.textfsm',
            'model': DeviceInterface,
        },
        # {
        #     'command_name': 'show vrf',
        #     'command_template_name': 'cisco_ios/xxxx.textfsm',
        #     'model': DeviceData,
        # },
        # {
        #     'command_name': 'show vrf interface',
        #     'command_template_name': 'cisco_ios/xxxx.textfsm',
        #     'model': DeviceData,
        # },
        # {
        #     'command_name': 'show cdp neighbors detail',
        #     'command_template_name': 'cisco_ios/xxxx.textfsm',
        #     'model': DeviceData,
        # },
        # {
        #     'command_name': 'show running-config',
        #     'command_template_name': 'cisco_ios/xxxx.textfsm',
        #     'model': DeviceData,
        # },
        # {
        #     'command_name': 'show ip dhcp pool',
        #     'command_template_name': 'cisco_ios/xxxx.textfsm',
        #     'model': DeviceData,
        # },
        {
            'command_name': 'show version',
            'command_template_name': 'cisco_ios/cisco_ios_show_version.textfsm',
            'model': DeviceData,
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
        if self.device.device_type == 0:
            # Check device type, by connecting to them:
            NetCon(self.device)
 
        if self.device.device_type == 1:
            device_type = check('cisco_ios')
        elif self.device.device_type == 2:
            device_type = check('cisco_xr')
        elif self.device.device_type == 3:
            device_type = check('cisco_ios')
        elif self.device.device_type == 4:
            device_type = check('cisco_nxos')
        else:
            device_type = 'unsupported'

        # Run data collection manager:
        return device_type

    def _manage_data_collection(self, device_type):
        """ Manage the data collection process. """
        # Collect commands list related to current device type:
        for commands_device_type in commands_database:
            if commands_device_type == device_type:
                commands_list = commands_database[commands_device_type]

                # Connect to device using SSH protocol:
                ssh_connection = NetCon(self.device)

                # Iterate thru command list:
                for command_data in commands_list:

                    # Collect data based in provided command:
                    collected_data = self._collect_data(command_data, ssh_connection)
                    
                    # Save raw data to database:
                    self._save_raw_data(collected_data, command_data)

                    # Parse collected data using collected data and template:
                    self._parse_data(collected_data, command_data)

    def _collect_data(self, command_data, ssh_connection):
        """ Collect data from device using information taken from command_list. """
        output = ssh_connection.send_command(command_data['command_name'])
        return output

    def _save_raw_data(self, collected_data, command_data):
        """ Edit existing raw data or create new one. """

        # Try to update Raw Data object if exist or create if not exist yet:
        try:
            raw_data_object = DeviceRawData.objects.get(device=self.device, command_name=command_data['command_name'])
            raw_data_object.command_data = collected_data
            raw_data_object.save()
        except:
            raw_data_object = DeviceRawData(
                device=self.device,
                command_name=command_data['command_name'],
                command_data=collected_data,
            )
            raw_data_object.save()          

        # Return raw data object:
        return raw_data_object

    def _parse_data(self, collected_data, command_data):
        """ Xxx """

        # TextFSM result list, that contains one or many dicts:
        fsm_result = []

        # Try to parse collected data into Text FSM result:
        try:
            # Pars collected data:
            with open(TEMPLATE_PATH + command_data['command_template_name']) as template:
                fsm = textfsm.TextFSM(template)
                result = fsm.ParseText(collected_data)

            # Create one or many dict from Text FSM result:
            for value in result:
                fsm_result.append(dict(zip(fsm.header, value)))
        except:
            pass

        # Update object if exist or create newone:
        object_values = command_data['model'].__dict__.keys()
        object_values_string = command_data['model'].__doc__
        # Check if Test FSM outputs contains one or many dicts inside:
        if len(fsm_result) <= 1:

            # Try to collect object if exist:
            try:
                object_data = command_data['model'].objects.get(device=self.device)
            except:
                object_data = command_data['model'](device=self.device)
                object_data.save()

            # Iterate thru object values list to update data based on Text FSM single dict output:
            for value in object_values:
                if value in object_values_string:
                    fsm_value = fsm_result[0].get(value.upper(), None)
                    if fsm_value is not None:
                        print('---------->', fsm_result[0].get(value.upper(), None))
                        print('---------->', value.upper())
                        object_data.__dict__[value] = fsm_value

            # Save object:
            object_data.save()

        else:

            pass   
        