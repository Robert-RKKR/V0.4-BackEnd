# Django Import:
from django.urls import path

# Application Import:
from .views.test import test

urlpatterns = [
    path('test/<int:pk>', test, name='test')
]