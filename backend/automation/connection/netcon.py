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

    def __init__(self, device: Device, task_id: str = None, repeat: int = 1) -> None:
        """
            The NetCon class uses netmiko library, to establish a SSH connection with networks device.

                Class attributes:
                -----------------
                device: Device object
                    Provided device object, to establish a SSH connection.
                task_id: String
                    Specifies the Celery task ID value, that will be added to logs messages.
                repeat: Intiger
                    Specifies how many times the SSH connection will be retried.
                
                Methods:
                --------
                send_command: (command)
                    Executes commands that do not require privileged mode.
                config_commands: (command)
                    Executes commands that require privileged mode.
        """
        # Device declaration:
        self.device = device

        # Connection status declaration:
        self.status = None

        # Execution timer declaration:
        self.execution_time = None

        # Celery task ID declaration:
        self.task_id = task_id

        # Device unsupported declaration:
        self.unsupported = None

        # Check if provided device variable is Device object:
        if isinstance(device, Device):
            # Collect information about device type:
            self.device_type = self.device.device_type
            # Specify the device type name:
            if self.device_type is None:
                # If device type is not provided, treat device as autodetect:
                self.device_type = 'autodetect'
            else: # If device type is provided, collect device type name:
                self.device_type = self.device.device_type.value
        else:
            self.status = False # Change connection status to False.
            raise TypeError('Provided device is not instance of Device class')

        # Collect user information:
        if self.device.credential is None:
            # Use default user data:
            self.username = 'admin'
            self.password = 'password'
        else: # Collect username and password from credential Model:
            self.username = self.device.credential.username
            self.password = self.device.credential.password

        # Performs the specified number of SSH connection attempts to the specified device.
        # Until the connection is established.
        for _ in range(repeat):

            # Check if device type is supported:
            if self.unsupported is not True:

                # Log start of SSH connection:
                NetCon.logger.debug('SSH connection has been started.', self.device, True, self.task_id)

                # Depending on the type of network device, connect to the device using SSH protocol.
                # Or specify the type of device first (If device type is autodetect).

                # If the device type is autodetect, connect to the device to determine its type:
                if self.device_type == 'autodetect':

                    # Connect to device to check device type, using SSH protocol:
                    device_type = self._ssh_connect(True)
                    
                    # Change current device type:
                    try: # Try to collect device type object that match current device type:
                        device_type_object = DeviceType.objects.get(value=device_type)
                        self.device.device_type = device_type_object
                        
                        # Update device object:
                        self.device.save()

                        # Connect to device, using SSH protocol:
                        self._ssh_connect()

                        # Log end of SSH connection
                        NetCon.logger.info('SSH connection has been established.', self.device, True, self.task_id)
                        self.status = True # Change connection status to True.

                        # Break connection loop in success:
                        break
                    
                    except: # If there is not device that match any device type objects, that device is not supported:
                        NetCon.logger.info(f'Device {self.device.name} currently possess an unsupported system {device_type}.', self.device, True, self.task_id)
                        self.unsupported = True
                        self.status = False
                    
                else:
                    # Connect to device, using SSH protocol:
                    self._ssh_connect()

                    # Log end of SSH connection
                    NetCon.logger.info('SSH connection has been established.', self.device, True, self.task_id)
                    self.status = True # Change connection status to True.

                    # Break connection loop in success:
                    break

            # Wait 1 second i case of connection failure, and reppeat them:
            time.sleep(1)

    def _ssh_connect(self, autoconnect: bool = False):
        """ Connect to device using SSH protocol. """
        
        try: # Try connect to device, using SSH protocol:
        
            if autoconnect is False:

                # Connect to device, using SSH protocol:
                self.connection = ConnectHandler(**{
                    'device_type': self.device_type,
                    'host': self.device.hostname,
                    'username': self.username,
                    'password': self.password,
                    'port': self.device.ssh_port,
                    'secret': self.password,
                })
            
            # If the device type is autodetect, connect to the device to determine its type:
            else:

                # Connect to device to check device type, using SSH protocol:
                check_device_type = SSHDetect(**{
                    'device_type': 'autodetect',
                    'host': self.device.hostname,
                    'username': self.username,
                    'password': self.password,
                    'port': self.device.ssh_port,
                })
                # Collect information about device type:
                return check_device_type.autodetect()

        # Handel exceptions:
        except AuthenticationException as error:
            NetCon.logger.error(error, self.device, True)
            # Change connection status to False:
            self.status = False
        except NetMikoTimeoutException as error:
            NetCon.logger.error(error, self.device, True)
            # Change connection status to False:
            self.status = False
        except ssh_exception.SSHException as error:
            NetCon.logger.error(error, self.device, True)
            # Change connection status to False:
            self.status = False
        except SSHException as error:
            NetCon.logger.error(error, self.device, True)
            # Change connection status to False:
            self.status = False  

    def __del__(self):
        """ End of SSH connection """
        NetCon.logger.info('SSH session ended.', self.device, True, self.task_id)

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
            return False
        else:
            # Clear clock count time:
            self.execution_time = 0.00

            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                # Collect data from device:
                NetCon.logger.debug(f'Sending of a new CLI command "{command}" has been started.', self.device, True, self.task_id)
                return_data = self.connection.send_command(command)
                NetCon.logger.info(f'The CLI command "{command}" has been sent.', self.device, True, self.task_id)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device, True)
                return error

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Log time of command execution:
            if self.execution_time > 2:
                NetCon.logger.debug(f'Execution of "{command}" command taken {self.execution_time} seconds.', self.device, True, self.task_id)
            else:
                NetCon.logger.debug(f'Execution of "{command}" command taken {self.execution_time} second.', self.device, True, self.task_id)
            
            # Return data:
            return return_data

    def config_commands(self, command) -> str:
        """ 
            Takes list of strings or string (Networks commands), and send to network device using SSH protocol.
            Usable only with configuration terminal levels commends.
        """

        # Check connection status:
        if self.status is False:
            return False
        else:
            # Clear clock count time:
            self.execution_time = 0.00

            # Start clock count:
            start_time = time.perf_counter()

            # Collect data from device:
            return_data = None

            # Try to sent command into network device:
            try:
                NetCon.logger.debug(f'Sending of a new CLI command "{command}" has started.', self.device, True, self.task_id)
                return_data = self.connection.send_config_set(command)
                NetCon.logger.info(f'The CLI command "{command}" has been sent.', self.device, True, self.task_id)
            except UnboundLocalError as error:
                NetCon.logger.error(error, self.device)
                return error

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Log time of command execution:
            if self.execution_time > 2:
                NetCon.logger.debug(f'Execution of "{command}" command taken {self.execution_time} seconds.', self.device, True, self.task_id)
            else:
                NetCon.logger.debug(f'Execution of "{command}" command taken {self.execution_time} second.', self.device, True, self.task_id)

            # Return data:
            return return_data
