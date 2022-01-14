# Python Import:
import time

# Netmiko Import:
from paramiko import ssh_exception
from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_exception import  AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

# Model Import:
from inventory.models.device_model import DeviceType
from inventory.models.device_model import Device

# Logger import:
from logger.logger import Logger


class NetCon:

    # Logger class initiation:
    logger = Logger('SSH connection')

    def __init__(self, device: Device) -> None:
        """
            The NetCon class uses netmiko library, to establish a SSH connection with networks device.

                Class attributes:
                -----------------
                device: Device object
                    Description
                
                Methods:
                --------
                send_command: (command)
                    Description
                config_commands: (response)
                    Description
        """
        # Device declaration:
        self.device = device

        # Connection status:
        self.status = None

        # Execution timer:
        self.execution_time = None

        # Check if device is Device object:
        if isinstance(device, Device):
            self.device_type = self.device.device_type
            # Collect device type name if device type is not none:
            if self.device_type is None:
                self.device_type = 'autodetect'
            else: # If device type is not none, collect device type name:
                self.device_type = self.device.device_type.value
        else:
            self.status = False # Change connection status to False.
            raise TypeError('Provided device is not instance of Device class')

        # Collect user information:
        try:
            self.username = self.device.credential.username
            self.password = self.device.credential.password
        except AttributeError as error:
            # Use default user data from settings:
            self.username = 'admin'
            self.password = 'password'

        # The purpose of the repeat loop is to repeat the call if the previous call failed:
        for _ in range(1):
            
            # Try connect to device:
            try:
                # Log start of SSH connection:
                NetCon.logger.debug('SSH connection has been started.', self.device, True)

                # Check if device type is not a autodetect type:
                if self.device_type != 'autodetect':
                    # Connect to device:
                    self.__ssh_connect()
                else:
                    # Connect to device to check device type:
                    check_device_type = SSHDetect(**{
                        'device_type': 'autodetect',
                        'host': device.hostname,
                        'username': self.username,
                        'password': self.password,
                        'port': device.ssh_port,
                    })
                    device_type = check_device_type.autodetect()
                    
                    # Change current device type:
                    try:
                        device_type_object = DeviceType.objects.get(value=device_type)
                        self.device.device_type = device_type_object
                    except:
                        NetCon.logger.info(f'Device {self.device.name} currently possess an unsupported system {device_type}.', self.device, True)
                    
                    # Update device object:
                    self.device.save()

                    # Connect to device:
                    self.__ssh_connect()

                # Log end of SSH connection
                NetCon.logger.info('SSH connection has been established.', self.device, True)
                self.status = True # Change connection status to True:

                # Break connection loop in success:
                break

            # Handel exceptions:
            except AuthenticationException as error:
                NetCon.logger.error(error, self.device, True)
                # Change connection status to False:
                self.status = False
                # Break connection loop in case of authentication error: 
                break
            except NetMikoTimeoutException as error:
                NetCon.logger.error(error, self.device, True)
                # Change connection status to False:
                self.status = False
                # # Break connection loop in case of timeout error: 
                # break
            except ssh_exception.SSHException as error:
                NetCon.logger.error(error, self.device, True)
                # Change connection status to False:
                self.status = False
            except SSHException as error:
                NetCon.logger.error(error, self.device, True)
                # Change connection status to False:
                self.status = False

        # Wait 1 second i case of connection failure, and reppeat them:
        time.sleep(1)

    def __ssh_connect(self):
        # Connect to device:
        self.connection = ConnectHandler(**{
            'device_type': self.device_type,
            'host': self.device.hostname,
            'username': self.username,
            'password': self.password,
            'port': self.device.ssh_port,
            'secret': self.password,
        })  

    def __del__(self):
        """ End of SSH connection """
        NetCon.logger.info('SSH session ended.', self.device, True)

    def __repr__(self) -> str:
        """ Connection class representation is IP address and port number of Https server. """
        return self.device.hostname

    def send_command(self, command) -> str:
        """ 
            Takes list of strings or string (Networks commands), and send to network device using SSH protocol.
            Usable only with enable levels commends.
        """

        # Check connection status:
        if self.status is False:
            # NetCon.logger.error('No connection available.', self.device, True)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                # Collect data from device:
                NetCon.logger.debug(f'Sending of a new CLI command has been started. Command: {command}', self.device, True)
                if isinstance(command, list):
                    for one_command in command:
                        return_data = self.connection.send_command(one_command)
                else:
                    return_data = self.connection.send_command(command)
                NetCon.logger.debug('The CLI command has been sent. Command: {command}', self.device, True)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device, True)
                return error

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)
            
            # Return data:
            return return_data

    def config_commands(self, command) -> str:
        """ 
            Takes list of strings or string (Networks commands), and send to network device using SSH protocol.
            Usable only with configuration terminal levels commends.
        """

        # Check connection status:
        if self.status is False:
            # NetCon.logger.error('No connection available.', self.device, True)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                NetCon.logger.debug('Sending of a new CLI command has started. Command: {command}', self.device, True)
                return_data = self.connection.send_config_set(command)
                NetCon.logger.debug('The CLI command has been sent. Command: {command}', self.device, True)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device)
                return error
            except:
                NetCon.logger.error('CLI command error.', self.device, True)

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Return data:
            return return_data
