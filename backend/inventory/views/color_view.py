# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework import generics

# Serializer Import:
from ..serializers.color_serializer import *

# Models Import:
from ..models.color_model import Color


class ColorView(generics.ListCreateAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer


class ColorIdView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorGetSerializer
