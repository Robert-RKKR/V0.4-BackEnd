# Django Import:
from django.urls import path

# Application Import:
from .views.administrator_view import DeviceView, Test

urlpatterns = [
    path('test', Test.as_view(), name='test'),
    path('administrator', DeviceView.as_view(), name='administrator'),
]