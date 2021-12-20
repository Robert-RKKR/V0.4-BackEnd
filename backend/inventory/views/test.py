# Django Imports:
from django.shortcuts import render

# Application Import:
from ..tasks import *

def test(request):
    data = {
        'output': 'RKKR'
    }

    #data['output'] = test_task(56)
    #data['output'] = test_task1.delay(56)
    data['output'] = test_task2.delay(56)
    print(test_task2.name)

    return render(request, 'inventory/test.html', data)
