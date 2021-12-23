# Django Import:
from django.db import models


class Settings(models.Model):

    # Creation data values:
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    # Status values:
    root = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)

    # Administrator:
    administrator = models.OneToOneField(
        'Administrator',
        on_delete=models.CASCADE,
    )

    # User application settings:
    default_connection_username = models.CharField(
        max_length=64,
        default='admin',
    )
    default_connection_password = models.CharField(
        max_length=64,
        default='password',
    )

    # Model representation:
    def __str__(self) -> str:
        return f"Settings({self.pk}: {self.administrator})"
