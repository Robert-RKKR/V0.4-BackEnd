# Python Import:
import math

# Rest Framework Import:
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


# Pagination's classes:
class TenResultsPagination(PageNumberPagination):
    size = 10
    page_size_query_param = 'page_size'
    max_page_size = size
    page_size = size
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': math.ceil(self.page.paginator.count/self.size),
            'results': data
        })


class HundredResultsPagination(PageNumberPagination):
    size = 100
    page_size_query_param = 'page_size'
    max_page_size = size
    page_size = size
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': math.ceil(self.page.paginator.count/self.size),
            'results': data
        })


class ThousandResultsPagination(PageNumberPagination):
    size = 1000
    page_size_query_param = 'page_size'
    max_page_size = size
    page_size = size
    
    def get_paginated_response(self, data):
        return Response({
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'count': self.page.paginator.count,
            'pages': math.ceil(self.page.paginator.count/self.size),
            'results': data
        })
