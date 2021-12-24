# Model Import:
from ...models.device_model import Device


class DataHTTPSCollectionManager:

    def __init__(self, device: Device) -> None:
        """
            Data Collection Manager, take Device class object to collect data from network device.
            Data is collected via HTTPS protocol depending on the operating system
            (Cisco IOS, IOS XE, NX OS or ASA OS) of the network device.

                
        """
        
        # Check if device is instance of Device class:
        if isinstance(device, Device):

            pass

        else: # If device variable is not a instance of Device class, raise type error:

            raise TypeError('Provided device variable is not a instance of Device class.')
