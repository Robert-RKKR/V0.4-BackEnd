# Django Imports:
from django.shortcuts import render

# Application Import:
from logger.models import LoggerData
from inventory.models.device_model import Device
from automation.tasks.single_device_check import single_device_check
from automation.tasks.new_task import new_task
from automation.models.policy_model import Policy

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

        # Policy related groups declaration:
        self.all_groups = []

        # Policy related devices declaration:
        self.all_devices = []

        # Policy related templates declaration:
        self.all_templates = []
        
        # Check if provided policy variable is valid Policy object:
        if isinstance(policy, Policy):
            self.policy = policy
        else:
            self.status = False # Change policy manager status to False.
            raise TypeError('Provided policy is not instance of Policy class')

        def _collect_groups(self):
            """ Collect all groups that are related with provided policy. """


            




def test(request, pk):
    data = {
        'output': 'RKKR'
    }
    device = Device.objects.get(pk=pk)
    # data['output'] = single_device_check.delay(device.pk)
    # data['output'] = new_task.delay(device.pk)
    logs = LoggerData.objects.filter(device=device).order_by('-pk')
    data['log'] = logs

    policy = Policy.objects.get(pk=1)
    

    data['policy'] = policy



    return render(request, 'inventory/test.html', data)


# Test