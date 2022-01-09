# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.color_serializer import ColorSerializer

# Models Import:
from ..models.color_model import Color
from ..models.color_model import ColorGroupRelation

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


class ColorsView(GenericObjectsView):

    queryset = Color
    serializer_all = ColorSerializer


class ColorView(GenericObjectView):

    queryset = Color
    serializer_all = ColorSerializer
