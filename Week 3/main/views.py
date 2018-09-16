from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def toDoReturn(request):
    tasks = [{
        'name': 'Task {}'.format(i),
        'created': datetime.today().strftime("%d/%m/%y"),
        'due_to': (datetime.today() + timedelta(days=2)).strftime("%d/%m/%y"),
        'owner': 'admin',
        'mark': True
        }
        for i in range(1, 5)
    ]
    context = {
        'list': tasks
    }
    return render(request, 'todo_list.html', context)

def toCompleteReturn(request, number):
    tasks = [{
        'name': 'Task {}'.format(number),
        'created': datetime.today().strftime("%d/%m/%y"),
        'due_to': (datetime.today() + timedelta(days=2)).strftime("%d/%m/%y"),
        'owner': 'admin',
        'mark': True
        }
    ]
    context = {
        'list': tasks
    }
    return render(request, 'completed_todo_list.html', context)

