# Django Import:
from django.db import models

# Application Import:
from administrator_model import Administrator

class Settings(models.Model):

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Administrator:
    administrator = models.OneToOneField(Administrator, on_delete=models.CASCADE)

    # Model representation:
    def __str__(self) -> str:
        return f"Settings({self.pk}: {self.administrator})"
