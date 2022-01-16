# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.color_serializer import ColorSerializer
from ..serializers.color_serializer import ColorSerializerUpdateCreate

# Models Import:
from ..models.color_model import Color

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


# Color Views:
class ColorView(GenericObjectsView):

    queryset = Color
    serializer_all = ColorSerializer
    serializer_limited = ColorSerializerUpdateCreate


class ColorIdView(GenericObjectView):

    queryset = Color
    serializer_all = ColorSerializer
    serializer_limited = ColorSerializerUpdateCreate
