from celery import shared_task
from inventory.models.device_model import Device
from automation.connection.netcon import NetCon

@shared_task(bind=True, track_started=True, name='New task')
def new_task(self, pk):
    device = Device.objects.get(pk=pk)

    connection = NetCon(device)
    output = connection.send_command('show version')
    
    return output