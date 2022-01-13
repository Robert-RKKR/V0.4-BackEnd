# Python Import:
from django.shortcuts import get_object_or_404

# Pagination Import:
from api.pagination import *

# Models Import:
from ..models.device_model import Device
from ..models.device_model import DeviceData
from ..models.device_model import DeviceRawData
from ..models.device_model import DeviceInterface

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView

# Serializer Import:
from ..serializers.device_serializer import DeviceDataSerializerUpdateCreate
from ..serializers.device_serializer import DeviceDataSerializer
from ..serializers.device_serializer import DeviceSerializerUpdateCreate
from ..serializers.device_serializer import DeviceSerializer
from ..serializers.device_serializer import DeviceRawDataSerializerUpdateCreate
from ..serializers.device_serializer import DeviceRawDataSerializer
from ..serializers.device_serializer import DeviceInterfaceSerializerUpdateCreate
from ..serializers.device_serializer import DeviceInterfaceSerializer


# Device View:
class DeviceView(GenericObjectsView):

    queryset = Device
    serializer_all = DeviceSerializer
    serializer_limited = DeviceSerializerUpdateCreate


class DeviceIdView(GenericObjectView):

    queryset = Device
    serializer_all = DeviceSerializer
    serializer_limited = DeviceSerializerUpdateCreate


# Device Data View:
class DeviceDataView(GenericObjectsView):

    queryset = DeviceData
    serializer_all = DeviceDataSerializer
    serializer_limited = DeviceDataSerializerUpdateCreate


class DeviceDataIdView(GenericObjectView):

    queryset = DeviceData
    serializer_all = DeviceDataSerializer
    serializer_limited = DeviceDataSerializerUpdateCreate



# Device RawData View:
class DeviceRawDataView(GenericObjectsView):

    queryset = DeviceRawData
    serializer_all = DeviceRawDataSerializer
    serializer_limited = DeviceRawDataSerializerUpdateCreate


class DeviceRawDataIdView(GenericObjectView):

    queryset = DeviceRawData
    serializer_all = DeviceRawDataSerializer
    serializer_limited = DeviceRawDataSerializerUpdateCreate



# Device Data View:
class DeviceInterfaceView(GenericObjectsView):

    queryset = DeviceInterface
    serializer_all = DeviceInterfaceSerializer
    serializer_limited = DeviceInterfaceSerializerUpdateCreate


class DeviceInterfaceIdView(GenericObjectView):

    queryset = DeviceInterface
    serializer_all = DeviceInterfaceSerializer
    serializer_limited = DeviceInterfaceSerializerUpdateCreate
