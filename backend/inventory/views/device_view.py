# Python Import:
from django.shortcuts import get_object_or_404

# Pagination Import:
from api.pagination import *

# Models Import:
from ..models.device_model import Device

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView

# Serializer Import:
from ..serializers.device_serializer import DeviceDataSerializerUpdateCreate
from ..serializers.device_serializer import DeviceSerializerUpdateCreate
from ..serializers.device_serializer import DeviceDataSerializer
from ..serializers.device_serializer import DeviceSerializer


class DevicesView(GenericObjectsView):

    queryset = Device
    serializer_all = DeviceSerializer
    serializer_limited = DeviceSerializerUpdateCreate


class DeviceView(GenericObjectView):

    queryset = Device
    serializer_all = DeviceSerializer
    serializer_limited = DeviceSerializerUpdateCreate


class DevicesDataView(GenericObjectsView):

    queryset = Device
    serializer_all = DeviceDataSerializer
    serializer_limited = DeviceDataSerializerUpdateCreate


class DeviceDataView(GenericObjectView):

    queryset = Device
    serializer_all = DeviceDataSerializer
    serializer_limited = DeviceDataSerializerUpdateCreate
