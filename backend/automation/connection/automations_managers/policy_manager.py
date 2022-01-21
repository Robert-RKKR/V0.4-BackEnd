# Application Import:
from automation.models.policy_manager_model import PolicyManager as Manager
from automation.models.policy_model import Policy

# Tasks Import:
from automation.tasks.single_device_collect import single_device_ssh_collect
from automation.tasks.single_device_check import single_device_check


class PolicyManager:

    def __init__(self, policy: Policy) -> None:
        """
            The Policy Manager class take policy object to run provided task.

                Class attributes:
                -----------------
                policy: Policy object
                    Provided policy object, to run celery task.
                
                Methods:
                --------
                xxx: (xxx)
                    Description.
        """

        # Policy manager status declaration:
        self.status = None

        # Check if provided policy variable is valid Policy object:
        if isinstance(policy, Policy):
            self.policy = policy
        else:
            self.status = False # Change policy manager status to False.
            raise TypeError('Provided policy is not instance of Policy class')

        # Policy related groups declaration:
        self.all_groups = []
        self._collect_groups()

        # Policy related devices declaration:
        self.all_devices = []
        self._collect_devices()

        # Policy related templates declaration:
        self.all_templates = []
        self._collect_templates()

        # Create new Policy Manager object:
        self.policy_manager_object = Manager(policy=self.policy)
        self.policy_manager_object.save()

        # Tasks IDs list declaration:
        self.tasks_ids = self.policy_manager_object.tasks_ids

    def run_policy(self):
        """ Run policy. """

        # Create new policy manager object:
        self.policy_manager_object = Manager(policy=self.policy)

        # Tasks IDs list local declaration:
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

        # save task id list in manager object:
        self.policy_manager_object.save()

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
