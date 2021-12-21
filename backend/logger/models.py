# Django Import:
from django.db import connection, models

# Application Import:
from inventory.models import *

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
    severity = models.IntegerField(choices=SEVERITY)
    message = models.CharField(max_length=1024)
    connection = models.BooleanField(default=False)

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
