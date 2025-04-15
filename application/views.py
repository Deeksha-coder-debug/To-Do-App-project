from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import Task
# Create your views here.

def index(request):
    # tasks = Task.objects.all()  # Fetch all tasks from the database
    # return render(request, 'application/index.html', {'tasks': tasks})
    pending_tasks = Task.objects.filter(complete=False).order_by('due_date')
    completed_tasks = Task.objects.filter(complete=True).order_by('-due_date')

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm()

    return render(request, 'application/index.html', {
        'form': form,
        'pending_tasks': pending_tasks,
        'completed_tasks': completed_tasks,
    })

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by its ID
    task.delete()  # Delete the task from the database
    return redirect('index')  # Redirect to the task list page

def complete_task(request, task_id):
    task = Task.objects.get(id=task_id)  # Get the task by its ID
    task.complete = True  # Mark the task as complete
    task.save()  # Save the task with the updated status
    return redirect('index')  # Redirect to the task list page

# Add task using TaskForm
def add_task(request):
    if request.method == 'POST':  # If the form is submitted via POST
        form = TaskForm(request.POST)  # Create a form instance with the POST data
        if form.is_valid():  # Check if the form is valid
            form.save()  # Save the new task to the database
            return redirect('index')  # Redirect to the task list page after saving the task
    else:
        form = TaskForm()  # Create an empty form instance if it's a GET request

    return render(request, 'application/add_task.html', {'form': form})  # Render the form

def edit_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TaskForm(instance=task)
    return render(request, 'application/edit_task.html', {'form': form, 'task': task})
