# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.color_serializer import ColorSerializer
from ..serializers.color_serializer import ColorDeviceRelationSerializer
from ..serializers.color_serializer import ColorGroupRelationSerializer
from ..serializers.color_serializer import ColorCredentialRelationSerializer

# Models Import:
from ..models.color_model import Color
from ..models.color_model import ColorDeviceRelation
from ..models.color_model import ColorGroupRelation
from ..models.color_model import ColorCredentialRelation

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


# Color Views:
class ColorsView(GenericObjectsView):

    queryset = Color
    serializer_all = ColorSerializer


class ColorView(GenericObjectView):

    queryset = Color
    serializer_all = ColorSerializer


# ColorDeviceRelation Views:
class ColorDeviceRelationsView(GenericObjectsView):

    queryset = ColorDeviceRelation
    serializer_all = ColorDeviceRelationSerializer


class ColorDeviceRelationView(GenericObjectView):

    queryset = ColorDeviceRelation
    serializer_all = ColorDeviceRelationSerializer


# ColorGroupRelation Views:
class ColorGroupRelationsView(GenericObjectsView):

    queryset = ColorGroupRelation
    serializer_all = ColorGroupRelationSerializer


class ColorGroupRelationView(GenericObjectView):

    queryset = ColorGroupRelation
    serializer_all = ColorGroupRelationSerializer


# ColorCredentialRelation Views:
class ColorCredentialRelationsView(GenericObjectsView):

    queryset = ColorCredentialRelation
    serializer_all = ColorCredentialRelationSerializer


class ColorCredentialRelationView(GenericObjectView):

    queryset = ColorCredentialRelation
    serializer_all = ColorCredentialRelationSerializer
