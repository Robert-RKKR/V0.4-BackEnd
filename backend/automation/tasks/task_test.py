# Celery Import:
from autocli.celery import app
from celery import shared_task
from inventory.models.device_model import Device
from automation.connection.netcon import NetCon

@shared_task(bind=True, track_started=True, name='test-task-name')
def test_task2(self, number):
    print(self)
    return 'RKKR', str(number), self.request.id, self.request.args, self.request.retries, self.request.parent_id

@shared_task(bind=True, track_started=True, name='test')
def test(self, pk):
    device = Device.objects.get(pk=pk)

    connection = NetCon(device)
    output = connection.send_command('show version')
    
    return output
