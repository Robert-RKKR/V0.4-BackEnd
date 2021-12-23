# Django Import:
from django.urls import path

# Application Import:
from .views import LoggerDataAllAPI

urlpatterns = [
    path('log', LoggerDataAllAPI.as_view(), name='log'),
]