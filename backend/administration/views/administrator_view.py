# Rest Django Import:
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import (
    permissions, status
)

# Application Import:
from ..models.administrator_model import Administrator
from ..models.settings_model import Settings

# Serializers Import:
from ..serializers.administrator_serializer import (
    AdministratorPostSerializer,
    AdministratorSerializer
)

# Pagination's Import:
from api.pagination import TenResultsPagination


class DeviceView(APIView, TenResultsPagination):
    """ Xxx """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        # Collect all objects from database:
        many_objects = Administrator.objects.all()
        # Pass objects through paginator to receive page breaks:
        paginator = self.paginate_queryset(many_objects, request, view=self)
        # Pass pages through serializer to receive the right view of object data:
        serializer = AdministratorSerializer(paginator, many=True, context={'request':request})
        # Create response API:
        response = self.get_paginated_response(serializer.data)
        return response

    def post(self, request, format=None):
        # Create new administrator:
        serializer = AdministratorPostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
