# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status

# Serializer Import:
from ..serializers.color_serializer import *

# Models Import:
from ..models.color_model import Color
from ..models.color_model import ColorGroupRelation


class ColorView(APIView):
    """ Xxx """

    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None):
        many_objects = Color.objects.all()
        serializer = ColorSerializer(many_objects, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ColorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ColorIdView(APIView):
    """ Xxx """

    permission_classes = [permissions.AllowAny]

    def get_object(self, pk):
        return get_object_or_404(Color, pk=pk)

    def get(self, request, pk, format=None):
        one_object = self.get_object(pk)
        serializer = ColorSerializer(one_object)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        one_object = self.get_object(pk)
        serializer = ColorSerializer(one_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        one_object = self.get_object(pk)
        one_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
