# Django Imports:
from django.shortcuts import render

# Application Import:
from automation.connection.automations_managers.policy_manager import PolicyManager
from logger.models import LoggerData
from inventory.models.device_model import Device
from automation.tasks.single_device_check import single_device_check
from automation.tasks.new_task import new_task
from automation.models.policy_model import Policy

            




def test(request, pk):
    data = {
        'output': 'RKKR'
    }
    device = Device.objects.get(pk=pk)
    # data['output'] = single_device_check.delay(device.pk)
    # data['output'] = new_task.delay(device.pk)
    # logs = LoggerData.objects.filter(device=device).order_by('-pk')
    # data['logs'] = logs

    policy = Policy.objects.get(pk=6)
    policy_manager = PolicyManager(policy)
    policy_manager.run_policy()

    return render(request, 'test.html', data)


# Test