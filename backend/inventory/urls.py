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

# Group Import:
from .views.group_view import GroupView
from .views.group_view import GroupIdView

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

    # Group Views:
    path('group/', GroupView.as_view(), name='group'),
    path('group/<int:pk>', GroupIdView.as_view(), name='group_id'),
]