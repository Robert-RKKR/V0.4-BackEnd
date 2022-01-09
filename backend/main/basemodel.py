# Django Import:
from django.db import models


class BaseAutoCliModel(models.Model):

    class Meta:
        default_permissions = ['read', 'write']
        permissions = []
        abstract = True
