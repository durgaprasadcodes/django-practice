from django.shortcuts import render,redirect,get_object_or_404
from .models import Task
from .forms import TaskForm

def tasks(request):
    tasks  = Task.objects.all().order_by("-created")
    return render(request,'tasks.html',{'tasks':tasks})

def success(request):
    return render(request,'success.html')

def taskForm(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = TaskForm()
    return render(request, 'form.html', {"form": form})

def editTask(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("success")
    else:
        form = TaskForm(instance=task)
    return render(request, "form.html", {"form": form})

def delete(request,id):
    task = get_object_or_404(Task,id=id)
    task.delete()
    return redirect("tasks")