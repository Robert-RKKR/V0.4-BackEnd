# Django Imports:
from django.shortcuts import render

# Application Import:
from ..tasks import *

def test(request):
    data = {
        'output': 'RKKR'
    }

    data['output'] = test_task2.delay(56)
    print(test_task2.name)

    from logger.logger import Logger
    from inventory.models.device_model import Device

    device = Device.objects.get(pk=3)
    
    logger = Logger()
    id_task = data['output']
    logger.debug(f'New task nr: {id_task}', device)

    return render(request, 'inventory/test.html', data)
