# Django Imports:
from django.shortcuts import render

# Application Import:
from logger.models import LoggerData
from inventory.models.device_model import Device
from automation.tasks.single_device_check import single_device_check
from automation.tasks.new_task import new_task
from automation.models.policy_model import Policy
from automation.automations_managers.policy_manager import PolicyManager

            




def test(request, pk):
    data = {
        'output': 'RKKR'
    }
    device = Device.objects.get(pk=pk)
    # data['output'] = single_device_check.delay(device.pk)
    # data['output'] = new_task.delay(device.pk)
    logs = LoggerData.objects.filter(device=device).order_by('-pk')
    data['log'] = logs

    policy = Policy.objects.get(pk=pk)
    policy_manager = PolicyManager(policy)

    data['policy'] = policy_manager.all_templates


    return render(request, 'inventory/test.html', data)


# Test