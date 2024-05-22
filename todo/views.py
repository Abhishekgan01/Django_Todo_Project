from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
from.models import Task

# Create your views here.
def addTask(request):
    task = request.POST['task']
    Task.objects.create(task=task) #first task is task in models that is
    #to store , second task is the task that is get from the box(i.e) in
    #this page - task
    return redirect('home')

def mark_as_done(request,pk):
    task =get_object_or_404(Task,pk=pk)
    task.is_completed =True
    task.save()
    return redirect('home')

def edit_task(request, pk):
    get_task=get_object_or_404(Task,pk=pk)
    if request.method == 'POST':
        new_task=request.POST['task']
        get_task.task=new_task
        get_task.save()
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        return render(request,'edit_task.html',context)
    
def delete_task(request,pk):
    task=get_object_or_404(Task,pk=pk)
    task.delete()
    return redirect('home')