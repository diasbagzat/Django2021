from rest_framework.views import APIView
from django.shortcuts import render
from rest_framework.response import Response
from todo.serializers import TaskSerializer
from todo.models import TodoList
from django.views.generic import TemplateView


# Create your views here.



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


class ListView(APIView):
    template_name = 'todo_list.html'

    def get(self, request):
        tasks = TodoList.objects.all()
        args = {'tasks': tasks}
        serializer = TaskSerializer(tasks, many=True)
        return render(request, self.template_name, args)


def TaskView(request, task_id):
    task = TodoList.objects.get(id=task_id)
    arg = {'task' : task}
    return render(request, 'completed_todo_list.html', arg)
