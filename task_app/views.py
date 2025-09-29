from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Task

# Create your views here.

def home(request):
    return render(request, 'task_app/home.html')

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'task_app/task_list.html', {'tasks': tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    return render(request, 'task_app/task_detail.html', {'task': task})

def update_task_status(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        new_status = request.POST.get('status')
        if new_status in ['pending', 'in_progress', 'completed']:
            task.status = new_status
            task.save()
            messages.success(request, f'Task status updated to {new_status}!')
        return redirect('task_app:task_detail', task_id=task.id)
    return redirect('task_app:task_list')
