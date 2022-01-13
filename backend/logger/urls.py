# Django Import:
from django.urls import path

# Application Import:
from .views import LoggerIdView
from .views import LoggerView

urlpatterns = [
    path('log/', LoggerView.as_view(), name='logs'),
    path('log/<int:pk>', LoggerIdView.as_view(), name='log'),
]