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

    def _key_check(self, key):
        """
            Check if provided key is valid and sub parameter of provided key is allowed.
                - Return an error list if one of the above statements is not satisfied.
                - Return True value if all of above statements are satisfied.
        """

        # Collect errors if they occur:
        key_errors = []
        # List of valid sub parameters:
        key_paramaters = ['contains']
        # List of excluded keys:
        excluded_keys = ['page']
        # Split key into pieces:
        key_pieces = key.split('__')
        key_name = key_pieces[0]

        # Check if sub parameter is excluded:
        if key_name not in excluded_keys:
            # Check that the key contains the correct sub parameter.
            # And there is only one sub parameter:
            if len(key_pieces) == 2:
                key_parameter = key_pieces[1]
                # Check if provided sub parameter is valid:
                if key_parameter not in key_paramaters:
                    key_errors.append({key_name: f"Key {key_name} possesses invalid sub parameter '{key_parameter}'."})
            elif len(key_pieces) == 1:
                pass 
            else: # Add error to error list:
                parameters = [parameter for parameter in key_pieces if parameter != key_name]
                key_errors.append({key_name: f'Key {key_name} contains to meany arguments {parameters}.'})

            # Collect all object values:
            object_values = self.queryset._meta.get_fields()
            valid_object = False
            # Check if the specified key is a valid object attribute:
            for row in object_values:
                value = row.name
                if key_name == value:
                    valid_object = True
            # If key is not valid add error to list of errors:
            if valid_object is False:
                key_errors.append({key_name: f"Value '{key_name}' is not valid key for {self.queryset._meta.object_name} object."})

            # Check for any errors occur, if not return filter dictionary:
            if len(key_errors) > 0:
                return key_errors
            else:
                return True

        # Return false if key is excluded:
        else:
            return False

    def _filter(self, filter_params):
        """
            Filter objects by using request url filtering.
                - Return list of errors, if provided request URL is invalid.
                - Return a dictionary containing the filter parameters.
        """

        # Collect filter parameters:
        filter_parameters = {}
        # Collect errors if they occur:
        filter_errors = []
        # Check if provided parameters are valid:
        for key in filter_params:
            key_check_response = self._key_check(key)
            # Check if response is valid:
            if key_check_response is True:
                # If provided key is valid, add key and value into dictionary: 
                filter_parameters[key] = filter_params[key]
            elif key_check_response is False:
                # Pass if key is excluded:
                pass
            else: # If provided key is not valid, add error to error list:
                filter_errors.append(key_check_response)

        # Check for any errors occur, if not return filter dictionary:
        if len(filter_errors) > 0:
            return filter_errors
        else: # Return filter dictionary:
            return filter_parameters
    
    def _collect_objects(self, request):
        """
            Collect all object based on request URL address.
                - Return dictionary contains error, if provided request URL is invalid.
                - Return object/s if provided request URL is valid.
        """

        # Collect filters data from URL:
        filter_params = self.request.query_params

        # Check if provided URL address contains additional parameters:
        if filter_params:
            # Run filter process:
            filter_response = self._filter(filter_params)
            # If filter method returned error list, return error dictionary:
            if isinstance(filter_response, list):
                # Create response dictionary:
                response_errors = {'detail': {}}
                # Fill response dictionary:
                for error_group in filter_response:
                    # Add error to response dictionary:
                    error_list = []
                    for one_error in error_group:
                        for key_name in one_error:
                            error_list.append(one_error[key_name])
                        response_errors['detail'][f'Error with key {key_name}'] = error_list
                # Return error dictionary:
                return response_errors
            else: # Return the filtered objects: 
                return self.queryset.objects.filter(**filter_response)
        # Return all object if additional parameters are not provided:
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

                # Collect object or error/s if the specified request URL is invalid:
                collect_object_response = self._collect_objects(request)
                # If the collect method returns an error dictionary, return the error page:
                if isinstance(collect_object_response, dict):
                    return Response(
                        collect_object_response,
                        status=status.HTTP_405_METHOD_NOT_ALLOWED)
                # Collect objects if provided by collect method:
                else:
                    many_objects = collect_object_response
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
            return Response(
                {'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} object.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

    # Generic Object POST View:
    def post(self, request, format=None):
        """ Create a new object and add them to database. """

        # Check if GET methods is allowed:
        if 'post' in self.allowed_methods:
            # Check if required data are provided:
            if self.queryset and self.serializer_all:

                # Use limited serializer if provided or all serializer if limited is not provided:
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
            return Response(
                {'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} object.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )


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
            return Response(
                {'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} object.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

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
            return Response(
                {'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} object.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )

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
            return Response(
                {'detail': f'Method {self.request.method} is not allowed on {self.queryset._meta.object_name} object.'},
                status=status.HTTP_405_METHOD_NOT_ALLOWED
            )
