# Django Import:
from django.urls import path

# Application Import:
from .views.test import test

# Views Import:
from .views.policy_view import PolicyView
from .views.policy_view import PolicyIdView
from .views.policy_manager_view import PolicyManagerView
from .views.policy_manager_view import PolicyManagerIdView

urlpatterns = [
    path('test/<int:pk>', test, name='test'),

    # Policy views:
    path('policy/', PolicyView.as_view(), name='policy'),
    path('policy/<int:pk>', PolicyIdView.as_view(), name='policy_id'),

    # Policy manager views:
    path('policy-manager/', PolicyManagerView.as_view(), name='policy_manager'),
    path('policy-manager/<int:pk>', PolicyManagerIdView.as_view(), name='policy_manager_id'),
]