# Django Import:
from django.db import models

# Base model Import:
from main.basemodel import BaseSubModel

# Application Import:
from automation.models.policy_model import Policy

# Tasks Import:
from automation.tasks.single_device_collect import single_device_ssh_collect
from automation.tasks.single_device_check import single_device_check


class PolicyManager(BaseSubModel):
    """ Xxx """

    # Corelation witch policy model:
    policy = models.ForeignKey(Policy, on_delete=models.CASCADE)

    # Policy manager status declaration:
    running = models.BooleanField(default=False)
    status = models.BooleanField(default=False)

    # 
    result = models.JSONField(blank=True, null=True)
    tasks_ids = models.JSONField(blank=True, null=True)
