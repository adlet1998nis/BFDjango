from django.shortcuts import render
from datetime import datetime, timedelta
from main.models import Owner, Task
# Create your views here.

def toDoReturn(request):
    tasks = Task.objects.order_by('-name')
    context = {
        'list': tasks
    }
    return render(request, 'todo_list.html', context)

def toCompleteReturn(request, number):
    tasks = Task.objects.filter(name = 'Task {}'.format(number))
    context = {
        'list': tasks
    }
    return render(request, 'completed_todo_list.html', context)

