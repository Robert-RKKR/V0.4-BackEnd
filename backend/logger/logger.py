# Python Imports:
from typing import Tuple

# Application Imports:
from .models import LoggerData
from inventory.models import *

# Severity constants declaration:
FULLDEBUG = 0
DEBUG = 1
INFO = 2
WARNING = 3
ERROR = 4
CRITICAL = 5


class Logger():

    def __init__(self, application: str = 'NoName') -> None:
        self.application = application

    def debug(self, message: str, model: object = None, connection: bool = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                model: string
                    Module or function name.
                connection: boolean
                    True if related witch connection log.
        """
        return self.__log(DEBUG, message, model, connection)

    def info(self, message: str, model: object = None, connection: bool = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                connection: boolean
                    True if related witch connection log.
        """
        return self.__log(INFO, message, model, connection)


    def warning(self, message: str, model: object = None, connection: bool = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                connection: boolean
                    True if related witch connection log.
        """
        return self.__log(WARNING, message, model, connection)


    def error(self, message: str, model: object = None, connection: bool = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                connection: boolean
                    True if related witch connection log.
        """
        return self.__log(ERROR, message, model, connection)

    def critical(self, message: str, model: object = None, connection: bool = False) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                connection: boolean
                    True if related witch connection log.
        """
        return self.__log(CRITICAL, message, model, connection)

    def __log(self, severity, message: str, model: object, connection: bool) -> Tuple:
        """ Create new log in Database """

        # Define Model name:
        model_name = None

        # Collect log data:
        log_data = {
            'severity': severity,
            'message': str(message),
            'connection': connection,
        }

        # Check if Model is object:
        if isinstance(model, object):

            # Check model type:
            if model is None:
                pass
            elif isinstance(model, Device):
                log_data['device'] = model
            elif isinstance(model, Color):
                log_data['color'] = model
            elif isinstance(model, Credential):
                log_data['credential'] = model
            elif isinstance(model, Group):
                log_data['group'] = model
            else:
                raise 'Provided model is not supported by log'
            
            # Define log:
            new_log = None

            # Create nwe log:
            new_log = LoggerData.objects.create(**log_data)

            return (new_log)

        else:
            raise 'Provided model is not object type'
