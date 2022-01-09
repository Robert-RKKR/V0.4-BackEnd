# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Pagination Import:
from api.pagination import TenResultsPagination


class GenericObjectsView(APIView, TenResultsPagination):
    """
        Generic Object View, is responsible for API View.
    """

    # Object definition data:
    queryset = None
    # Object serializer data:
    serializer_all = None
    serializer_limited = None
    # Permissions data:
    permission_classes = [permissions.IsAuthenticated]
    # Filters data:
    filter_fields = ('id',)
    # Allowed methods data:
    allowed_methods = ['get', 'post']

    def _filter(self, request):
        """ Filter objects by using request url filtering. """
        # Collect filters data from URL:
        filter_params = self.request.query_params
        
        # Check if collected data exist, if not return all objects:
        if filter_params:
            # Temporary data dictionary:
            filter_dict = {}
            # Collect all object values:
            object_values = self.queryset._meta.get_fields()
            # Check if provided data are validone:
            for key in filter_params:
                for row in object_values:
                    value = row.name
                    if value == key:
                        filter_dict[key] = filter_params[key]
                        break
            # Collect filtered objects from database:
            return self.queryset.objects.filter(**filter_dict)
        else:
            # Collect all objects from database:
            return self.queryset.objects.all()

    # Generic Object GET View:
    def get(self, request, format=None):
        """ Collect all objects from database. Filter options are avaliable. """

        # Check if GET methods is allowed:
        if 'get' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:

                # Filter output objects:
                many_objects = self._filter(request)
                # Pass objects through paginator to receive page breaks:
                paginator = self.paginate_queryset(many_objects, request, view=self)
                # Pass pages through serializer to receive the right view of object data:
                serializer = self.serializer_all(paginator, many=True, context={'request':request})
                # Create response API:
                response = self.get_paginated_response(serializer.data)
                # Return REST API response:
                return response
        
            # Return error message if required data was not provided:
            else:
                if self.queryset is None:
                    raise TypeError('Please provide object data using queryset attributes.')
                elif self.serializer_all is None:
                    raise TypeError('Please provide serializer data using serializer_class attributes.')
        else:
            return Response({'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} objects.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    # Generic Object POST View:
    def post(self, request, format=None):
        """ Create a new object and add them to database. """

        # Check if GET methods is allowed:
        if 'post' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:

                # Use limited serializer if provided or all serializer if limited is not provided:
                if self.serializer_limited:
                    serializer = self.serializer_limited(data=request.data)
                else:
                    serializer = self.serializer_all(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Return error message if required data was not provided:
            else:
                if self.queryset is None:
                    raise TypeError('Please provide object data using queryset attributes.')
                elif self.serializer_all is None:
                    raise TypeError('Please provide serializer data using serializer_class attributes.')
        else:
            return Response({'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} objects.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class GenericObjectView(APIView):
    """
        Generic Object View, is responsible for API View.
    """

    # Object definition data:
    queryset = None
    # Object serializer data:
    serializer_all = None
    serializer_limited = None
    # Permissions data:
    permission_classes = [permissions.IsAuthenticated]
    # Filters data:
    filter_fields = ('id',)
    # Allowed methods data:
    allowed_methods = ['get', 'put', 'delete']

    def _get_object(self, pk):
        return get_object_or_404(self.queryset, pk=pk)

    def get(self, request, pk, format=None):
        """ Create a new object and add them to database. """

        # Check if GET methods is allowed:
        if 'get' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:
                
                one_object = self._get_object(pk)
                serializer = self.serializer_all(one_object)
                return Response(serializer.data, status=status.HTTP_200_OK)
            
            # Return error message if required data was not provided:
            else:
                if self.queryset is None:
                    raise TypeError('Please provide object data using queryset attributes.')
                elif self.serializer_all is None:
                    raise TypeError('Please provide serializer data using serializer_class attributes.')
        else:
            return Response({'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} objects.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, pk, format=None):
        """ Create a new object and add them to database. """

        # Check if GET methods is allowed:
        if 'put' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:
                
                one_object = self._get_object(pk)
                serializer = self.serializer_all(one_object, data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            # Return error message if required data was not provided:
            else:
                if self.queryset is None:
                    raise TypeError('Please provide object data using queryset attributes.')
                elif self.serializer_all is None:
                    raise TypeError('Please provide serializer data using serializer_class attributes.')
        else:
            return Response({'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} objects.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def delete(self, request, pk, format=None):
        """ Create a new object and add them to database. """

        # Check if GET methods is allowed:
        if 'delete' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:
                
                one_object = self._get_object(pk)
                one_object.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            
            # Return error message if required data was not provided:
            else:
                if self.queryset is None:
                    raise TypeError('Please provide object data using queryset attributes.')
                elif self.serializer_all is None:
                    raise TypeError('Please provide serializer data using serializer_class attributes.')
        else:
            return Response({'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} objects.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
