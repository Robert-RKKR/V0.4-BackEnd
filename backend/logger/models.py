# Django Import:
from django.db import models

# Application Import:
from inventory.models import Credential
from inventory.models import Device
from inventory.models import Color
from inventory.models import Group

# Base Model Import:
from main.basemodel import BaseMainModel
from main.basemodel import BaseSubModel

# Loggers models:
class LoggerData(models.Model):
    SEVERITY = (
        (1, 'DEBUG'),
        (2, 'INFO'),
        (3, 'WARNING'),
        (4, 'ERROR'),
        (5, 'CRITICAL'),
    )

    # Timestamp:
    timestamp = models.DateTimeField(auto_now_add=True)

    # Data:
    application = models.CharField(max_length=128)
    severity = models.IntegerField(choices=SEVERITY)
    message = models.CharField(max_length=1024)
    task_id = models.CharField(max_length=128, null=True)
    system_message = models.BooleanField(default=False)

    # Models:
    device = models.ForeignKey(
        Device, on_delete=models.CASCADE,
        null=True, blank=True
    )
    color = models.ForeignKey(
        Color, on_delete=models.CASCADE,
        null=True, blank=True
    )
    credential = models.ForeignKey(
        Credential, on_delete=models.CASCADE,
        null=True, blank=True
    )
    group = models.ForeignKey(
        Group, on_delete=models.CASCADE,
        null=True, blank=True
    )

    # Model representation:
    def __str__(self) -> str:
        return f"{self.pk} - {self.severity} - {self.application} - {self.message}"
