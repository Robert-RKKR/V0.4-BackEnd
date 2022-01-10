# Application Import:
from .models import LoggerData

# Serializes Import:
from .serializers import LoggerDataSerializer

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


class LoggersView(GenericObjectsView):

    from rest_framework import permissions
    permission_classes = [permissions.AllowAny]
    queryset = LoggerData
    serializer_all = LoggerDataSerializer
    allowed_methods = ['get']


class LoggerView(GenericObjectView):

    queryset = LoggerData
    serializer_all = LoggerDataSerializer