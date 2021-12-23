# Django Imports:
from django.shortcuts import render

# Application Import:
from ..tasks.single_device_check import single_device_check
from ..tasks.tasks import test_task1, test_task2


def test(request):
    data = {
        'output': 'RKKR'
    }

    data['output'] = single_device_check.delay(1)
    # data['output'] = single_device_check.delay(1)
    # print(single_device_check.name)

    from logger.logger import Logger
    from inventory.models.device_model import Device

    device = Device.objects.get(pk=1)
    
    logger = Logger()
    id_task = data['output']
    logger.debug(f'New task nr: {id_task}', device)

    return render(request, 'inventory/test.html', data)
