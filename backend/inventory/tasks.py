# Celery Import:
from autocli.celery import app
from celery import shared_task

@app.task
def test_task1(number):
    return 'RKKR' + str(number)

@shared_task(bind=True, track_started=True)
def test_task2(self, number):
    return 'RKKR' + str(number)