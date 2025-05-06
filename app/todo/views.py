from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm

def todo_list(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'todo/todo_list.html', {'tasks': tasks, 'form': form})
