# Python Import:
import textfsm
import json
import io

# Model Import:
from ...models import *

# Logger import:
from logger.logger import Logger

# Application Import:
from ..netcon import NetCon

# Models Import:
from automation.models.fsm_template_model import FsmTemplate
from inventory.models.device_model import DeviceRawData
from inventory.models.device_model import DeviceInterface
from inventory.models.device_model import DeviceData
from inventory.models.device_model import Device

# Logger class initiation:
logger = Logger('SSH data Collector')

# Constance:
SSH_TEMPLATE_PATH = 'inventory/connection/data_collection/ssh_templates/'
COLLRECTOR_TEMPLATE_PATH = 'inventory/connection/data_collection/collector_templates/'

class SshDataCollector:

    def __init__(self, device: Device, task_id: str = None) -> None:
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

        # Task ID declaration:
        self.task_id = task_id

        # Device type declaration:
        self.device_type = self.device.device_type

        # Templates list declaration:
        self.templates = self._collect_template()

    def collect(self) -> bool:
        """
            Collect data from a network device using the SSH protocol.
            Process collected data using TextFSM templates.
            Save processed data to objects that would be linked to the main Device class.
        """

        # Collect data from device based on SFM templates:
        collected_data = self._collect_data()

        # Save collected data in Raw Data objects:
        self._save_raw_data(collected_data)

        # Process collected data:
        process_data = self._process_data(collected_data)
        
        # Save proceeded data into proper database model:
        self._save_data(process_data)

    def _collect_data(self) -> dict:
        """
            Collect data from a network device using the SSH protocol.
        """

        # Connect to device using SSH protocol:
        ssh_connection = NetCon(self.device, self.task_id)

        # Prepare dictionary of collected data to return:
        return_data = {}

        # Collect data and add them to return dictionary:
        for template in self.templates:
            output = ssh_connection.send_command(template.command)
            return_data[template] = output

        # Return all collected data:
        return return_data

    def _save_raw_data(self, collected_data) -> None:
        """ Save rav data to Raw Data objects. """

        # Iterate thru all collected data, to add them into new Raw Data objects:
        for data in collected_data:
            try:
                # Check if Raw Data object exist:
                raw_data_object = DeviceRawData.objects.get(device=self.device, command_name=data.command)
                # Update data in Raw Data object:
                raw_data_object.command_data = collected_data[data]
                # Save existing Raw Data object:
                raw_data_object.save()
            except:
                # Create new Raw Data object:
                new_raw_data_object = DeviceRawData(device=self.device, command_name=data.command, command_data=collected_data[data])
                # Save new Raw Data object:
                new_raw_data_object.save()

    def _process_data(self, collected_data) -> None:
        """ Process collected data using TextFSM templates. """

        # Prepare dictionary of process data:
        return_data = {}

        # Iterate thru all collected data, to proccess them using TextFSM:
        for data in collected_data:
            
            # Collect FSM Template:
            template = data.sfm_expression
            template_as_file = io.StringIO(template)
            # FSM result list:
            fsm_result = []
            # Try to parse collected data from Text FSM:
            try:
                fsm = textfsm.TextFSM(template_as_file)
                result = fsm.ParseText(collected_data[data])
                # Create one or many dict from Text FSM result:
                for value in result:
                    fsm_result.append(dict(zip(fsm.header, value)))
            except:
                pass
            # Add FSM result into dictionary of process data:
            return_data[data] = fsm_result

        # Return all process data:
        return return_data

    def _save_data(self, process_data) -> dict:
        """ Save processed data to objects that would be linked to the main Device class. """

        # Chose Device sub model that will be fill with data collected from provided template:
        for data in process_data:
            if data.device_data is True:

                # Collect Device Data Values:
                object_values = DeviceData._meta.get_fields()

                try: # Add data to existing object, or create newone:
                    device_data_object = DeviceData.objects.get(device=self.device)
                except:
                    device_data_object = DeviceData(device=self.device)
                    device_data_object.save()

                # Iterate thru object values list to update data based on Text FSM single dict output:
                for row in object_values:
                    value = row.name
                    fsm_value = process_data[data][0].get(value.upper(), None)
                    if fsm_value is not None:
                        device_data_object.__dict__[value] = fsm_value

                # Save object changes:
                device_data_object.save()

            elif data.device_interface is True:

                # Collect Device Data Values:
                object_values = DeviceInterface._meta.get_fields()

                for data_row in process_data[data]:

                    try: # Add data to existing object, or create newone:
                        device_interface_object = DeviceInterface.objects.get(device=self.device, port=data_row.get('PORT', None))
                    except:
                        device_interface_object = DeviceInterface(device=self.device, port=data_row.get('PORT', None))
                        device_interface_object.save()

                    # Iterate thru object values list to update data based on Text FSM single dict output:
                    for row in object_values:
                        value = row.name
                        fsm_value = data_row.get(value.upper(), None)
                        if fsm_value is not None:
                            device_interface_object.__dict__[value] = fsm_value

                    # Save object changes:
                    device_interface_object.save()

            else: # If any model was chousen, log error:
                logger.error(f'Policy {data.name} is not connected to any of Device Models.', self.device, task_id=self.request.id)

    def _collect_template(self):
        """
            Collect collector template.

            Return: Dictionary
                {
                    <FsmTemplate: Class>: [List of one or many dictionary's],
                    ...
                }
        """

        # Collect all templates related to provided device type:
        templates = FsmTemplate.objects.filter(device_type=self.device_type)

        # Prepare list of templates to return:
        return_data = []

        # Add templates to return list:
        for template in templates:
            # Add only devices templates to return list:
            if template.device_template is True:
                return_data.append(template)
        
        # Return all collected templates:
        return return_data
