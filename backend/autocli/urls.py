# Django Import:
from django.contrib import admin
from django.urls import path, include

# Rest Framework Import:
from rest_framework.authtoken import views
from rest_framework import permissions

# Drf yasg Import:
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="AutoCli API",
      default_version='v0.1',
      description="Auto Cli API view.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="robert.kucharski.rkkr@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Swagger API view:
    # path('^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    # Admin panel URL:
    path('admin/', admin.site.urls),

    # Token key generator URL:
    path('api-token-auth', views.obtain_auth_token, name='api_key_generator'),

    # Applications URL-s:
    path('api/inventory/', include('inventory.urls')),
    path('api/administration/', include('administration.urls')),
]
