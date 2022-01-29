# Django Import:
from django.urls import path

# Views Import:
from .views.status import DevicesStatus

urlpatterns = [
    path('status', DevicesStatus.as_view(), name='status'),
]