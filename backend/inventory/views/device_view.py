# Python Import:
from django.shortcuts import get_object_or_404

# Serializer Import:
from ..serializers.device_serializer import *

# Pagination Import:
from api.pagination import *

# Models Import:
from ..models.device_model import Device

# Generic objects Import:
from api.generic_objects import GenericObjectsView
from api.generic_objects import GenericObjectView


class DevicesView(GenericObjectsView):

    queryset = Device
    serializer_all = DeviceSerializerAll
    serializer_limited = DeviceSerializerLimited


class DeviceView(GenericObjectView):

    queryset = Device
    serializer_all = DeviceSerializerAll


# class DeviceView(APIView, TenResultsPagination):
#     """ Xxx """

#     permission_classes = [permissions.AllowAny]
#     filter_fields = ('name', 'hostname')
#     # permission_classes = [permissions.IsAuthenticated]

#     def get(self, request, format=None):
#         # Filter output objects:
#         filter_params = self.request.query_params
#         if filter_params:
#             filter_dict = {}
#             for key in filter_params:
#                 filter_dict[key] = filter_params[key]
#             print(filter_dict)
#             # Collect filtered objects from database:
#             many_objects = Device.objects.filter(**filter_dict)
#         else:
#             # Collect all objects from database:
#             many_objects = Device.objects.all()
#         # Pass objects through paginator to receive page breaks:
#         paginator = self.paginate_queryset(many_objects, request, view=self)
#         # Pass pages through serializer to receive the right view of object data:
#         serializer = DeviceSerializer(paginator, many=True, context={'request':request})
#         # Create response API:
#         response = self.get_paginated_response(serializer.data)
#         # Return REST API response:
#         return response

#     def post(self, request, format=None):
#         serializer = DeviceSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class DeviceIdView(APIView):
#     """ Xxx """

#     permission_classes = [permissions.IsAuthenticated]

#     def get_object(self, pk):
#         return get_object_or_404(Device, pk=pk)

#     def get(self, request, pk, format=None):
#         one_object = self.get_object(pk)
#         serializer = DeviceSerializerAll(one_object)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     def put(self, request, pk, format=None):
#         one_object = self.get_object(pk)
#         serializer = DeviceSerializerAll(one_object, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         one_object = self.get_object(pk)
#         one_object.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class DeviceView(generics.ListCreateAPIView):

#     permission_classes = [permissions.AllowAny]
#     serializer_class = DeviceSerializer
#     queryset = Device.objects.all()
#     filter_fields = ('name', 'hostname')


# class DeviceView(GenericAPIView, ListModelMixin, CreateModelMixin):

#     permission_classes = [permissions.AllowAny]
#     filter_fields = ('name', 'hostname')
#     search_fields = ('name', 'hostname')
#     serializer_class = DeviceSerializer
#     queryset = Device.objects.all()

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         self.serializer_class = DeviceDataSerializer
#         return self.create(request, *args, **kwargs)
