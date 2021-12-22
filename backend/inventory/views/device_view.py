# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    permissions, status
)

# Serializer Import:
from ..serializers.device_serializer import *

# Pagination Import:
from api.pagination import *

# Models Import:
from ..models.device_model import Device

class DeviceView(APIView, TenResultsPagination):
    """ Xxx """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Collect all objects from database:
        many_objects = Device.objects.all()
        # Pass objects through paginator to receive page breaks:
        paginator = self.paginate_queryset(many_objects, request, view=self)
        # Pass pages through serializer to receive the right view of object data:
        serializer = DeviceSerializer(paginator, many=True, context={'request':request})
        # Create response API:
        response = self.get_paginated_response(serializer.data)
        return response

    def post(self, request, format=None):
        serializer = DeviceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceIdView(APIView):
    """ Xxx """

    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Device, pk=pk)

    def get(self, request, pk, format=None):
        one_object = self.get_object(pk)
        serializer = DeviceSerializer(one_object)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        one_object = self.get_object(pk)
        serializer = DeviceSerializer(one_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        one_object = self.get_object(pk)
        one_object.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
