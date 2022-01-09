# Django Import:
from django.urls import path

# Application Import:
from .views.test import test
from .views.device_view import *
from .views.color_view import *

urlpatterns = [
    path('test/<int:pk>', test, name='test'),

    path('device/', DevicesView.as_view(), name='device'),
    path('device/<int:pk>', DeviceView.as_view(), name='device_id'),

    # Color Views:
    path('color/', ColorsView.as_view(), name='color'),
    path('color/<int:pk>', ColorView.as_view(), name='color_id'),

    # ColorDeviceRelation Views:
    path('color-device/', ColorDeviceRelationsView.as_view(), name='color-device'),
    path('color-device/<int:pk>', ColorDeviceRelationView.as_view(), name='color-device_id'),

    # ColorGroupRelation Views:
    path('color-group/', ColorGroupRelationsView.as_view(), name='color-group'),
    path('color-group/<int:pk>', ColorGroupRelationView.as_view(), name='color-group_id'),

    # ColorCredentialRelation Views:
    path('color-credential/', ColorCredentialRelationsView.as_view(), name='color-credential'),
    path('color-credential/<int:pk>', ColorCredentialRelationView.as_view(), name='color-credential_id'),
]