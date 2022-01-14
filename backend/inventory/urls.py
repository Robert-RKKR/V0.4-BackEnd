# Django Import:
from django.urls import path

# Devices Import:
from .views.device_view import DeviceView
from .views.device_view import DeviceIdView
from .views.device_view import DeviceDataView
from .views.device_view import DeviceDataIdView
from .views.device_view import DeviceRawDataView
from .views.device_view import DeviceRawDataIdView
from .views.device_view import DeviceInterfaceView
from .views.device_view import DeviceInterfaceIdView

# Colors Import:
from .views.color_view import ColorView
from .views.color_view import ColorIdView
from .views.color_view import ColorDeviceRelationView
from .views.color_view import ColorDeviceRelationIdView
from .views.color_view import ColorGroupRelationView
from .views.color_view import ColorGroupRelationIdView
from .views.color_view import ColorCredentialRelationView
from .views.color_view import ColorCredentialRelationIdView

# Group Import:
from .views.group_view import GroupView
from .views.group_view import GroupIdView
from .views.group_view import GroupDeviceRelationView
from .views.group_view import GroupDeviceRelationIdView

urlpatterns = [
    # Device Views:
    path('device/', DeviceView.as_view(), name='device'),
    path('device/<int:pk>', DeviceIdView.as_view(), name='device_id'),

    # Device Data Views:
    path('device-data/', DeviceDataView.as_view(), name='device_data'),
    path('device-data/<int:pk>', DeviceDataIdView.as_view(), name='device_data_id'),

    # Device RawData View:
    path('device-raw-data/', DeviceRawDataView.as_view(), name='device_raw_data'),
    path('device-raw-data/<int:pk>', DeviceRawDataIdView.as_view(), name='device_raw_data_id'),

    # Device Interface View:
    path('device-interface/', DeviceInterfaceView.as_view(), name='device_interface'),
    path('device-interface/<int:pk>', DeviceInterfaceIdView.as_view(), name='device_interface_id'),

    # Color Views:
    path('color/', ColorView.as_view(), name='color'),
    path('color/<int:pk>', ColorIdView.as_view(), name='color_id'),

    # ColorDeviceRelation Views:
    path('color-device/', ColorDeviceRelationView.as_view(), name='color_device'),
    path('color-device/<int:pk>', ColorDeviceRelationIdView.as_view(), name='color_device_id'),

    # ColorGroupRelation Views:
    path('color-group/', ColorGroupRelationView.as_view(), name='color_group'),
    path('color-group/<int:pk>', ColorGroupRelationIdView.as_view(), name='color_group_id'),

    # ColorCredentialRelation Views:
    path('color-credential/', ColorCredentialRelationView.as_view(), name='color_credential'),
    path('color-credential/<int:pk>', ColorCredentialRelationIdView.as_view(), name='color_credential_id'),

    # Group Views:
    path('group/', GroupView.as_view(), name='group'),
    path('group/<int:pk>', GroupIdView.as_view(), name='group_id'),

    # ColorDeviceRelation Views:
    path('group-device/', GroupDeviceRelationView.as_view(), name='group_device'),
    path('group-device/<int:pk>', GroupDeviceRelationIdView.as_view(), name='group_device_id'),
]