# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Serializer Import:
from ..serializers.device_serializer import *

# Models Import:
from ..models.device_model import Device


class DeviceView(APIView):
    """ Xxx """

    def get(self, request, format=None):
        devices = Device.objects.all()
        serializer = DeviceGetSerializer(devices, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DeviceModifySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceIdView(APIView):
    """ Xxx """

    def get_object(self, pk):
        return get_object_or_404(Device, pk=pk)

    def get(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceGetSerializer(device)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        device = self.get_object(pk)
        serializer = DeviceModifySerializer(device, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        device = self.get_object(pk)
        device.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
