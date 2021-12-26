# Django Imports:
from django.shortcuts import render

# Application Import:
from ..tasks.single_device_collect import single_device_ssh_collect
from ..tasks.single_device_check import single_device_check
from ..tasks.tasks import test_task1, test_task2
from logger.logger import Logger
from logger.models import LoggerData
from inventory.models.device_model import Device

def test(request, pk):
    data = {
        'output': 'RKKR'
    }

    data['output'] = single_device_ssh_collect(pk)
    # data['output'] = single_device_check.delay(1)
    # data['output'] = single_device_check.delay(1)
    # print(single_device_check.name)

    

    device = Device.objects.get(pk=pk)
    
    # logger = Logger()
    # id_task = data['output']
    # logger.debug(f'New task nr: {id_task}', device)

    log = LoggerData.objects.filter(device=device).order_by('-pk')
    data['log'] = log

    return render(request, 'inventory/test.html', data)


# Test