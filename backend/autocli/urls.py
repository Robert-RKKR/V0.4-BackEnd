# Django Import:
from django.contrib import admin
from django.urls import path, include

# Rest Framework Import:
from rest_framework.authtoken import views

urlpatterns = [
    # Admin panel URL:
    path('admin/', admin.site.urls),

    # Token key generator URL:
    path('api-token-auth', views.obtain_auth_token, name='api_key_generator'),

    # Applications URL-s:
    path('api/inventory/', include('inventory.urls')),
    path('api/administration/', include('administration.urls')),
]
