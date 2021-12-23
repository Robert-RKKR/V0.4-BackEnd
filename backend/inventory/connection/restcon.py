# Python Import:
import requests
import xmltodict
import json

# Model Import:
from ..models.device_model import Device

# Logger import:
from logger.logger import Logger


class RestCon:
    
    # Logger class initiation:
    logger = Logger('RestCon')

    def __init__(self, device: Device) -> None:
        """
            The RestCon class uses requests library, to connect with Https server for API connections.

            Class attributes:
                -----------------
                device: Device object
                    Description

            Methods:
            --------
            connect: (url, connectionType='GET', payload=None)
                Description
        """
        # Device declaration:
        self.device = device

        # Connection status:
        self.status = None
        self.xml_status = None
        self.json_status = None

        # Execution timer:
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

    def get(self, url, payload: str = None, header: dict = None) -> requests:
        """
            Send HTTPS GET request.

            Parameters:
            -----------
            url: string
                URL string used to construct HTTPS request.
            payload: string
                Additional data used to construct HTTPS request.
            header: dict
                Additional header information.
            return:
            -------
            jsonResponse: dict
                Return date collected from HTTPS server.
        """

        # Create URL Address from tamplate:
        request_url = f'''https://{self.device.hostname}:{self.device.https_port}/{url}'''

        # Cisco default headers:
        if header is None:
            header = {
                'Accept': 'application/yang-data+json',
                'Content-Type': 'application/yang-data+json',
            }

        # Try to connect with device:
        try:
            # Log starting of a new connection to https server:
            RestCon.logger.info('Starting a new Https connection.', self.device, True)

            # Collect user information:
            try:
                username = self.device.credential.username
                password = self.device.credential.password
            except AttributeError as error:
                # Use default user data from settings:
                # Add settings.
                username = 'admin'
                password = 'admin'

            # Connect to https server with password and username or by token:
            if self.device.token is not None:
                response = requests.get(
                    request_url,
                    headers=header,
                    data=payload,
                    verify=self.device.certificate,
                )
            else: # Token inside header:
                response = requests.get(
                    request_url,
                    headers=header,
                    auth=(username, password),
                    data=payload,
                    verify=self.device.certificate,
                )

            # Log when https connection was established:
            RestCon.logger.debug('Https connection was established.', self.device, True)
            
            # Convert HTTPS response:
            return self.__connect(response)

        except requests.exceptions.SSLError as error:
            RestCon.logger.error(error, self.device, True)
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.Timeout as error:
            RestCon.logger.error(error, self.device, True) 
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.InvalidURL as error:
            RestCon.logger.error(error, self.device, True)        
            # Change connection status to False:
            self.status = False
            return self.status

        except requests.exceptions.ConnectionError as error:
            RestCon.logger.error(error, self.device, True)        
            # Change connection status to False:
            self.status = False
            return self.status

    def __connect(self, response):
        """
            Convert HTTPS response to ridable data.

            Parameters:
            -----------
            response: 
                Description
        """
        convertResponse = None
            
        # Try to convert JSON response to python dictionary:
        try:
            convertResponse = json.loads(response.text)
            self.json_status = True
        except:
            # Log when python dictionary convert process fail:
            RestCon.logger.warning('Python JSON -> dictionary convert process fail.', self.device, True)
            convertResponse = False
            self.json_status = False

            # Try to convert XML response to python dictionary if JSON fails:
            try:
                convertResponse = xmltodict.parse(response.text)
                self.xml_status = True
            except:
                # Log when python dictionary convert process fail:
                RestCon.logger.warning('Python XML -> dictionary convert process fail.', self.device, True)
                convertResponse = False
                self.xml_status = False

        # Check response status:
        if response.status_code < 200: # All respons from 0 to 199.
            RestCon.logger.warning(f'Connection to {self.device.hostname}, was a informational HTTPS request.', self.device, True)
            # Change connection status to True:
            self.status = True

        elif response.status_code < 300: # All respons from 200 to 299.
            RestCon.logger.info(f'Connection to {self.device.hostname}, was a success HTTPS request.', self.device, True)
            # Change connection status to True:
            self.status = True

        elif response.status_code < 400: # All respons from 300 to 399.
            RestCon.logger.warning(f'Connection to {self.device.hostname}, returned redirection HTTPS error.', self.device, True)
            # Change connection status to False:
            self.status = False

        elif response.status_code < 500: # All respons from 400 to 499.
            RestCon.logger.error(f'Connection to {self.device.hostname}, returned client HTTPS error.', self.device, True)
            # Change connection status to False:
            self.status = False

        elif response.status_code < 600: # All respons from 500 to 599.
            RestCon.logger.error(f'Connection to {self.device.hostname}, returned server HTTPS error.', self.device, True)
            # Change connection status to False:
            self.status = False

        # Log https response type:
        RestCon.logger.debug(f'Https response returned {response.status_code} code.', self.device, True)
        
        # Return Https response in Json format:
        return convertResponse