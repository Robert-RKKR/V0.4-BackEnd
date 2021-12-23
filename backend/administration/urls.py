# Django Import:
from django.urls import path

# Application Import:
from .views.administrator_view import DeviceView

urlpatterns = [
    path('administrator', DeviceView.as_view(), name='administrator'),
]