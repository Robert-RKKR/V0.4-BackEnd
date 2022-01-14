# Django Import:
from django.contrib import admin

# Application Import:
from .models import *

# Register Application models in Django Admin:
admin.site.register(Administrator)
admin.site.register(Settings)
