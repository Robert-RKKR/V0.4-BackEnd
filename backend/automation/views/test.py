# Django Imports:
from django.shortcuts import render

# Application Import:
from logger.logger import Logger
from logger.models import LoggerData
from inventory.models.device_model import Device
from inventory.models.device_model import DeviceType
from automation.tasks.single_device_check import single_device_check
from automation.tasks.new_task import new_task


def test(request, pk):
    data = {
        'output': 'RKKR'
    }

    ### data['output'] = single_device_ssh_collect(pk)

    # test_object_values = Device._meta.get_fields()
    
    # for row in test_object_values:
    #     print(row.name)
    
    # data['output'] = single_device_check.delay(1)
    # print(single_device_check.name)


    device = Device.objects.get(pk=pk)

    # from ..tasks.task_test import test
    # data['output'] = test.delay(device.pk)
    # data['output'] = single_device_check.delay(device.pk)

    data['output'] = new_task.delay(device.pk)
    

    # logger = Logger()
    # id_task = data['output']
    # logger.debug(f'New task nr: {id_task}', device)

    logs = LoggerData.objects.filter(device=device).order_by('-pk')
    data['log'] = logs

    return render(request, 'inventory/test.html', data)


# Test