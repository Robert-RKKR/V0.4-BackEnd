# Django Import:
from django.urls import path

# Application Import:
from .views.test import test
from .views.device_view import *

urlpatterns = [
    path('device', DeviceView.as_view(), name='device'),
    path('device/<int:pk>/', DeviceIdView.as_view(), name='device_id'),
]