from django.shortcuts import render, redirect
from .models import TODOAPP


# Create your views here.
def make_complete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.is_completed = True
    task.save()
    return redirect('home')


def delete(request, pk):
    task = TODOAPP.objects.get(pk=pk)
    task.delete()
    return redirect('home')


def add_task(request):
    task_name = request.POST['task_name']
    TODOAPP.objects.create(task_name=task_name)
    return redirect('home')
