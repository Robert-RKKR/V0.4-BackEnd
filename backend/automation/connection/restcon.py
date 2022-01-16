# Python Import:
import requests
import xmltodict
import json
import time

# Model Import:
from inventory.models.device_model import Device

# Logger import:
from logger.logger import Logger


class RestCon:
    
    # Logger class initiation:
    logger = Logger('RestCon')

    def __init__(self, device: Device, task_id: str = None) -> None:
        """
            The RestCon class uses requests library, to connect with device using HTTPS protocol.

                Class attributes:
                -----------------
                device: Device object
                    Provided device object, to establish a HTTPS connection.
                task_id: String
                    Specifies the Celery task ID value, that will be added to logs messages.

                Methods:
                --------
                get, post, put, delete.
        """
        # Device declaration:
        self.device = device

        # Celery task ID declaration:
        self.task_id = task_id

        # Connection status declaration:
        self.status = None
        self.xml_status = None
        self.json_status = None

        # Execution timer declaration:
        self.execution_time = None

        # Check if device is Device object:
        if isinstance(device, Device):
            pass
        else:
            self.status = False # Change connection status to False.
            raise ConnectionError

    def __repr__(self):
        """ Connection class representation is IP address and port number of Https server. """
        return self.device.hostname

    def get(self, url, payload: str = None, headers: dict = None) -> requests:
        """
            Send HTTPS GET request, using HTTPS protocol.

            Parameters:
            -----------
            url: string
                URL string used to construct HTTPS request.
            payload: string
                Additional data used to construct HTTPS request.
            headers: dict
                Additional header information.
            
            return:
            -------
            jsonResponse: dict
                Return date collected from HTTPS server.
        """

        return self._connection(url, payload, headers)

    def _connection(self, url, payload, headers):
        """ Connect to server using HTTPS protocol. """

        # Create URL Address from tamplate:
        request_url = f'''https://{self.device.hostname}:{self.device.https_port}/{url}'''

        # Cisco default headers:
        if headers is None:
            headers = {
                'Accept': 'application/yang-data+json',
                'Content-Type': 'application/yang-data+json',
            }

            # Add token to header if provided:
            if self.device.token is not None:
                headers['x-token'] = self.device.token

        # Try to connect with device:
        try:
            # Log starting of a new connection to https server:
            RestCon.logger.info('Starting a new Https connection.', self.device, True, self.task_id)

            # Start clock count:
            start_time = time.perf_counter()

            # Collect user information:
            if self.device.credential is None:
                # Use default user data:
                username = 'admin'
                password = 'password'
            else: # Collect username and password from credential Model:
                username = self.device.credential.username
                password = self.device.credential.password

            # Connect to https server with password and username or by token:
            if self.device.token is None:
                response = requests.get(
                    request_url,
                    headers=headers,
                    auth=(username, password),
                    data=payload,
                    verify=self.device.certificate,
                )
            else:
                response = requests.get(
                    request_url,
                    headers=headers,
                    data=payload,
                    verify=self.device.certificate,
                )

            # Log when https connection was established:
            RestCon.logger.debug('Https connection was established.', self.device, True, self.task_id)

            # Finish clock count & method execution time:
            finish_time = time.perf_counter()
            self.execution_time = round(finish_time - start_time, 5)

            # Log time of command execution:
            if self.execution_time > 2:
                RestCon.logger.debug(f'HTTPS connection taken {self.execution_time} seconds.', self.device, True, self.task_id)
            else:
                RestCon.logger.debug(f'HTTPS connection taken {self.execution_time} second.', self.device, True, self.task_id)
            
            # Convert HTTPS response:
            return self._check_response(response)

        except requests.exceptions.SSLError as error:
            RestCon.logger.error(error, self.device, True, self.task_id)
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.Timeout as error:
            RestCon.logger.error(error, self.device, True, self.task_id) 
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.InvalidURL as error:
            RestCon.logger.error(error, self.device, True, self.task_id)        
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.ConnectionError as error:
            RestCon.logger.error(error, self.device, True, self.task_id)        
            # Change connection status to False:
            self.status = False
            return self.status

    def _check_response(self, response):
        """ Check type of HTTPS request response. """

        # Try to convert JSON response to python dictionary:
        try:
            convertResponse = json.loads(response.text)
            self.json_status = True
        except:
            # Log when python dictionary convert process fail:
            RestCon.logger.warning('Python JSON -> dictionary convert process fail.', self.device, True, self.task_id)
            convertResponse = False
            self.json_status = False

            # Try to convert XML response to python dictionary if JSON fails:
            try:
                convertResponse = xmltodict.parse(response.text)
                self.xml_status = True
            except:
                # Log when python dictionary convert process fail:
                RestCon.logger.warning('Python XML -> dictionary convert process fail.', self.device, True, self.task_id)
                convertResponse = False
                self.xml_status = False

        # Check response status:
        if response.status_code < 200: # All respons from 0 to 199.
            RestCon.logger.warning(f'Connection to {self.device.hostname}, was a informational HTTPS request.\nHttps response returned {response.status_code} code.', self.device, True, self.task_id)
            # Change connection status to True:
            self.status = True

        elif response.status_code < 300: # All respons from 200 to 299.
            RestCon.logger.debug(f'Connection to {self.device.hostname}, was a success HTTPS request.\nHttps response returned {response.status_code} code.', self.device, True, self.task_id)
            # Change connection status to True:
            self.status = True

        elif response.status_code < 400: # All respons from 300 to 399.
            RestCon.logger.warning(f'Connection to {self.device.hostname}, returned redirection HTTPS error.\nHttps response returned {response.status_code} code.', self.device, True, self.task_id)
            # Change connection status to False:
            self.status = False

        elif response.status_code < 500: # All respons from 400 to 499.
            RestCon.logger.error(f'Connection to {self.device.hostname}, returned client HTTPS error.\nHttps response returned {response.status_code} code.', self.device, True, self.task_id)
            # Change connection status to False:
            self.status = False

        elif response.status_code < 600: # All respons from 500 to 599.
            RestCon.logger.error(f'Connection to {self.device.hostname}, returned server HTTPS error.\nHttps response returned {response.status_code} code.', self.device, True, self.task_id)
            # Change connection status to False:
            self.status = False
        
        # Return Https response in Json format:
        return convertResponse
