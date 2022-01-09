# Django Import:
from django.urls import path

# Application Import:
from .views import LoggersView, LoggerView

urlpatterns = [
    path('log/', LoggersView.as_view(), name='logs'),
    path('log/<int:pk>', LoggerView.as_view(), name='log'),
]