from django.shortcuts import render
from django.http import HttpResponse
from todoapp.models import TODOAPP


# Create your views here.
def home(request):
    comp_task=TODOAPP.objects.filter(is_completed=False)
    finish_task=TODOAPP.objects.filter(is_completed=True)
    context={
        'comp_task':comp_task,
        'finish_task':finish_task
        }
    
    return render(request, 'home.html',context)

