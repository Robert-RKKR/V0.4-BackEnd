# Application Import:
from .models import LoggerData

# Serializes Import:
from .serializers import LoggerDataSerializer
from .serializers import LoggerDataSerializerUpdateCreate

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


class LoggerView(GenericObjectsView):

    from rest_framework import permissions
    permission_classes = [permissions.AllowAny]
    queryset = LoggerData
    serializer_all = LoggerDataSerializer
    serializer_limited = LoggerDataSerializerUpdateCreate


class LoggerIdView(GenericObjectView):

    queryset = LoggerData
    serializer_all = LoggerDataSerializer
    serializer_limited = LoggerDataSerializerUpdateCreate