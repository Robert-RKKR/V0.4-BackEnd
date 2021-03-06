# Python Import:
from django.shortcuts import get_object_or_404

# Rest Framework Import:
from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

# Pagination Import:
from api.pagination import HundredResultsPagination


class GenericResponse(APIView):
    """
        Generic response, used to return python dictionary
    """

    pass


class GenericObjectsView(APIView, HundredResultsPagination):
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
    # All orders:
    orders = None


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
                if self.serializer_limited:
                     serializer = self.serializer_limited(data=request.data)
                else:
                    serializer = self.serializer_all(data=request.data)
                
                # Use serializer to create a new object, based on provided JSON data:
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

    def _key_check(self, key):
        """
            Check if provided key is valid and sub parameter of provided key is allowed.
                - Return an error list if one of the above statements is not satisfied.
                - Return True value if all of above statements are satisfied.
        """

        # Collect all object values:
        object_values = self.queryset._meta.get_fields()
        # Collect errors if they occur:
        key_errors = []
        # List of valid sub parameters:
        key_paramaters = [
            ('contains', 'all'),
            ('icontains', 'all'),
            ('has_key', ['JSONField']),
            # 'contained_by' # Only for Django 4.0 and higher.
        ]
        # List of excluded keys:
        excluded_keys = ['page', 'order']
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
                is_valid = False
                for value in key_paramaters:
                    # Collect main values:
                    key_parameter_name = value[0]
                    key_parameter_allowed = value[1]
                    # Check if sub parameter is in key parameter list:
                    if key_parameter == key_parameter_name:
                        # Check if sub parameter is always allowed:
                        if key_parameter_allowed == 'all':
                            is_valid = True
                        else: # Check if sub parameter is valid for used key object type:
                            for row in object_values:
                                value = row.name
                                if key_name == value:
                                    class_name = row.__class__.__name__
                                    if class_name in key_parameter_allowed:
                                        is_valid = True
                                    else:
                                        key_errors.append({key_name: f"Parameter '{key_parameter}' is not allowed with key {key_name}, because class attributes is {class_name} type."})
                                        is_valid = None
                # If provided sub parameter is not valid, add error to queen:
                if is_valid is False:
                    key_errors.append({key_name: f"Key {key_name} possesses invalid sub parameter '{key_parameter}'."})
            elif len(key_pieces) == 1:
                pass 
            else: # Add error to error list:
                parameters = [parameter for parameter in key_pieces if parameter != key_name]
                key_errors.append({key_name: f'Key {key_name} contains to meany arguments {parameters}.'})

            # Check if the specified key is a valid object attribute:
            valid_object = False
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

    def _order_check(self, parameter, key):
        """ Check if order value is valid. """

        # Collect all object values:
        object_values = self.queryset._meta.get_fields()

        # Check if order value is valid:
        for row in object_values:
            value = row.name
            if parameter[0] == '-':
                if parameter[1:] == value:
                    return parameter
            else:
                if parameter == value:
                    return parameter

        # Return error if provided order value is not valid:
        return [{key: f"Provided order value '{parameter}' is not valid."}]

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
        # Create order list:
        self.orders = []
        # Check if provided parameters are valid:
        for key in filter_params:

            # Collect kay parameter:
            parameter = filter_params[key]

            # Separate the key containing the order parameter, from other keys:
            if key == 'order':
                # Add order parameter to order list if valid:
                check_order_response = self._order_check(parameter, key)
                if isinstance(check_order_response, list):
                    filter_errors.append(check_order_response)
                else:
                    self.orders.append(check_order_response)
                
            else:
                # Check if provided key is valid:
                key_check_response = self._key_check(key)
                # Check if response is valid:
                if key_check_response is True:
                    # If provided key is valid, add key and value into dictionary: 
                    filter_parameters[key] = parameter
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
        # Filter data:
        filter_data = None

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
            else: # Return the filtered objects to filter data:
                filter_data = filter_response
        
        # Check if filters are provided, if no return all objects:
        try:
            if filter_data is None:
                if isinstance(self.orders, list):
                    return self.queryset.objects.all().order_by(*self.orders)
                else:
                    return self.queryset.objects.all()
            else:
                if isinstance(self.orders, list):
                    return self.queryset.objects.filter(**filter_data).order_by(*self.orders)
                else:
                    return self.queryset.objects.filter(**filter_data)
        except:
            return {'detail': {'error': 'Unknown error 5674.'}}


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
                
                # Provide one object from database:
                one_object = self._get_object(pk)
                # Use serializer:
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
                
                # Provide one object from database:
                one_object = self._get_object(pk)
                # Use limited serializer if provided or all serializer if limited is not provided:
                if self.serializer_limited:
                     serializer = self.serializer_limited(one_object, data=request.data)
                else:
                    serializer = self.serializer_all(one_object, data=request.data)
                
                # Use serializer to update object, based on provided JSON data:
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
                
                # Provide one object from database:
                one_object = self._get_object(pk)
                # Delete object from database:
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
