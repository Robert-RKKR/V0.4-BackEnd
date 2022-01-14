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

    def debug(self, message: str, model: object = None, system_message: bool = False, task_id: str = None) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                model: string
                    Module or function name.
                system_message: boolean
                    True if related witch system message log.
        """
        return self.__log(DEBUG, message, model, system_message, task_id)

    def info(self, message: str, model: object = None, system_message: bool = False, task_id: str = None) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                system_message: boolean
                    True if related witch system message log.
        """
        return self.__log(INFO, message, model, system_message, task_id)


    def warning(self, message: str, model: object = None, system_message: bool = False, task_id: str = None) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                system_message: boolean
                    True if related witch system message log.
        """
        return self.__log(WARNING, message, model, system_message, task_id)


    def error(self, message: str, model: object = None, system_message: bool = False, task_id: str = None) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                system_message: boolean
                    True if related witch system message log.
        """
        return self.__log(ERROR, message, model, system_message, task_id)

    def critical(self, message: str, model: object = None, system_message: bool = False, task_id: str = None) -> Tuple:
        """
            Create a new log based on the following data:

                Method attributes:
                -----------------
                message: string
                    Logging message string value. 
                module: string
                    Module or function name.
                system_message: boolean
                    True if related witch system message log.
        """
        return self.__log(CRITICAL, message, model, system_message, task_id)

    def __log(self, severity, message: str, model: object, system_message: bool, task_id: str) -> Tuple:
        """ Create new log in Database """

        # Collect log data:
        log_data = {
            'application': self.application,
            'severity': severity,
            'message': str(message),
            'system_message': system_message,
            'task_id': task_id,
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
                raise TypeError('Provided model is not supported by log')
            
            # Define log:
            new_log = None

            # Tyr to create a new log:
            try:
                # Create nwe log:
                new_log = LoggerData.objects.create(**log_data)
            except:
                return False

            # Return created log object:
            return (new_log)

        else:
            raise TypeError('Provided model is not object type')
