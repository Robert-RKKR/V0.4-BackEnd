# Rest Django Import:
from rest_framework import generics
from rest_framework import permissions

# Application Import:
from .models import LoggerData

# Serializes Import:
from .serializers import LoggerDataSerializer

# Pagination Import:
from api.pagination import HundredResultsPagination

# Create your views here.
class LoggerDataAllAPI(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = LoggerData.objects.all().order_by('-pk')
    serializer_class = LoggerDataSerializer
    pagination_class = HundredResultsPagination
