# Django Import:
from django.db import models

# Base Model Import:
from main.basemodel import BaseMainModel


class Settings(BaseMainModel):

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
