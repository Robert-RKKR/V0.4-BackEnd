# Python Import:
import time

# Netmiko Import:
from paramiko import ssh_exception
from netmiko import ConnectHandler
from netmiko.ssh_autodetect import SSHDetect
from netmiko.ssh_exception import  AuthenticationException
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException

# Application Import:
from logger.logger import Logger
from inventory.models import Device


class NetCon:

    # Logger class initiation:
    logger = Logger('NetCon')

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
            # Change device type name to netmiko name:
            if self.device.device_type == 0:
                self.device_type = 'autodetect'
            elif self.device.device_type == 1:
                self.device_type = 'cisco_ios'
            elif self.device.device_type == 2:
                self.device_type = 'cisco_xr'
            elif self.device.device_type == 3:
                self.device_type = 'cisco_xe'
            elif self.device.device_type == 4:
                self.device_type = 'cisco_nxos'
        else:
            self.status = False # Change connection status to False.
            raise TypeError('Provided device is not instance of Device class')

        # Collect user information:
        try:
            self.username = self.device.credential.username
            self.password = self.device.credential.password
        except AttributeError as error:
            # Use default user data from settings:
            # Add settings.
            self.username = 'admin'
            self.password = 'admin'

        # Try connect to device:
        try:
            # Log start of SSH connection:
            NetCon.logger.debug('SSH connection has been started.', self.device)

            # Check if device type is not a autodetect type:
            if self.device.device_type != 0:
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
                
                # Change device type name to intiger:
                if device_type == 'cisco_ios':
                    self.device.device_type = 1
                elif device_type == 'cisco_xr':
                    self.device.device_type = 2
                elif device_type == 'cisco_xe':
                    self.device.device_type = 3
                elif device_type == 'cisco_nxos':
                    self.device.device_type = 4
                else:
                    self.device.device_type = 0
                
                # Update device object:
                self.device.save()

                # Connect to device:
                self.__ssh_connect()

            NetCon.logger.info('SSH connection has been established.', self.device)
            self.status = True # Change connection status to True:

        # Handel exceptions:
        except AuthenticationException as error:
            NetCon.logger.error(error, self.device)
            self.status = False # Change connection status to False.
        except NetMikoTimeoutException as error:
            NetCon.logger.error(error, self.device)
            self.status = False # Change connection status to False.
        except ssh_exception.SSHException as error:
            NetCon.logger.error(error, self.device)
            self.status = False # Change connection status to False.
        except SSHException as error:
            NetCon.logger.error(error, self.device)
            self.status = False # Change connection status to False.

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
        NetCon.logger.info('SSH session ended.', self.device)

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
            NetCon.logger.error('No connection available.', self.device)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                # Collect data from device:
                NetCon.logger.debug('The sending of a new CLI command has been started.\nCommand: {command}', self.device)
                if isinstance(command, list):
                    for one_command in command:
                        return_data = self.connection.send_command(one_command)
                else:
                    return_data = self.connection.send_command(command)
                NetCon.logger.debug('The CLI command has been sent.', self.device)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device)
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
            NetCon.logger.error('No connection available.', self.device)
            return None

        else:
            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                NetCon.logger.debug('The sending of a new CLI command has started.\nCommand: {command}', self.device)
                return_data = self.connection.send_config_set(command)
                NetCon.logger.debug('The CLI command has been sent.', self.device)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device)
                return error
            except:
                NetCon.logger.error('CLI command error.', self.device)

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Return data:
            return return_data