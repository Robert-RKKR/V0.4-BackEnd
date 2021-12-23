# Celery Import:
from autocli.celery import app
from celery import shared_task

@app.task
def test_task1(number):
    return 'RKKR' + str(number)

@shared_task(bind=True, track_started=True, name='test-task-name')
def test_task2(self, number):
    print(self)
    return 'RKKR', str(number), self.request.id, self.request.args, self.request.retries, self.request.parent_id
