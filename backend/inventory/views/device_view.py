# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.device_serializer import *

# Pagination Import:
from api.pagination import *

# Models Import:
from ..models.device_model import Device

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


class DevicesView(GenericObjectsView):

    queryset = Device
    serializer_all = DeviceSerializerAll


class DeviceView(GenericObjectView):

    queryset = Device
    serializer_all = DeviceSerializerAll
