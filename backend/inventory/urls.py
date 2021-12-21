# Django Import:
from django.urls import path

# Application Import:
from .views.test import test
from .views.device_view import *
from .views.color_view import *

urlpatterns = [
    path('test', test, name='test'),

    path('device', DeviceView.as_view(), name='device'),
    path('device/<int:pk>', DeviceIdView.as_view(), name='device_id'),

    path('color', ColorView.as_view(), name='color'),
    path('color/<int:pk>', ColorIdView.as_view(), name='color_id'),
]