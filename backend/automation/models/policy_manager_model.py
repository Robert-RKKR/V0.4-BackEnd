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

    def __init__(self, *args, **kwargs):
        
        # Super on Init method:
        super().__init__(*args, **kwargs)

        # Policy related groups declaration:
        self.all_groups = []
        self._collect_groups()

        # Policy related devices declaration:
        self.all_devices = []
        self._collect_devices()

        # Policy related templates declaration:
        self.all_templates = []
        self._collect_templates()

        # Tasks IDs list declaration:
        tasks_ids = []

        # Perform an action depending on the type of task:
        if self.policy.task == 0:
            pass
        elif self.policy.task == 11:
            for device in self.all_devices:
                tasks_ids.append(str(single_device_check.delay(device.pk)))
                self.tasks_ids = tasks_ids
        elif self.policy.task == 12:
            for device in self.all_devices:
                tasks_ids.append(str(single_device_ssh_collect.delay(device.pk)))
                self.tasks_ids = tasks_ids


    def _collect_groups(self):
        """ Collect all groups that are related with provided policy. """

        # Collect all policy related groups:
        all_groups = self.policy.groups.all()

        # Add all groups to all groups list:
        for group in all_groups:
            self.all_groups.append(group)

    def _collect_devices(self):
        """ Collect all devices that are related with provided policy. """

        # Collect all policy related devices:
        all_devices = self.policy.devices.all()

        # Add all devices to all devices list:
        for device in all_devices:
            self.all_devices.append(device)

        # Collect all devices from all policy related groups:
        for group in self.all_groups:

            # Collect all devices from provided group:
            all_devices = group.devices.all()

            # Add all devices to all devices list:
            for device in all_devices:
                self.all_devices.append(device)
    
    def _collect_templates(self):
        """ Collect all templates that are related with provided policy. """

        # Collect all policy related templates:
        all_templates = self.policy.templates.all()

        # Add all templates to all templates list:
        for template in all_templates:
            self.all_templates.append(template)