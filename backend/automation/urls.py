# Django Import:
from django.urls import path

# Application Import:
from .views.test import test

# Views Import:
from .views.policy_view import PolicyView
from .views.policy_view import PolicyIdView

urlpatterns = [
    path('test/<int:pk>', test, name='test'),

    # Policy views:
    path('policy/', PolicyView.as_view(), name='policy'),
    path('policy/<int:pk>', PolicyIdView.as_view(), name='policy_id'),
]