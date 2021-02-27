from django.shortcuts import render


# Create your views here.

def index(request):
    task1 = {
        'name': 'Task 1',
        'created': '10/09/2018',
        'dueon': '12/09/2018',
        'owner': 'admin',
    }
    task2 = {
        'name': 'Task 2',
        'created': '10/09/2018',
        'dueon': '12/09/2018',
        'owner': 'admin',
    }
    task3 = {
        'name': 'Task 3',
        'created': '10/09/2018',
        'dueon': '12/09/2018',
        'owner': 'admin',
    }
    context = {
        'task1': task1,
        'task2': task2,
        'task3': task3,

    }
    return render(request, 'todo_list.html', context=context)


def completed(request):
    comp1 = {
        'name': 'Task 1',
        'created': '10/09/2018',
        'dueon': '12/09/2018',
        'owner': 'admin',
    }

    context = {
        'comp1': comp1,

    }
    return render(request, 'completed_todo_list.html', context=context)
