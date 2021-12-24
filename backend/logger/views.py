# Rest Django Import:
from rest_framework import generics

# Application Import:
from .models import LoggerData

# Serializes Import:
from .serializers import LoggerDataSerializer

# Pagination Import:
from api.pagination import HundredResultsPagination

# Create your views here.
class LoggerDataAllAPI(generics.ListAPIView):
    queryset = LoggerData.objects.all().order_by('-pk')
    serializer_class = LoggerDataSerializer
    pagination_class = HundredResultsPagination
