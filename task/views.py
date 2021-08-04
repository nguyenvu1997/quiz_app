from django.shortcuts import render
from django.views.generic import ListView , CreateView, DetailView, DeleteView, UpdateView
from django.urls import reverse_lazy

from .models import Task
from task import models

# Create your views here.

class TaskList(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = 'tasks'

class TaskCreate(CreateView):
    model = Task
    fields = '__all__'
    template_name = 'task/task_create.html'
    success_url = reverse_lazy('tasks')

class TaskDetail(DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = 'task'

class TaskDelete(DeleteView):
    model = Task
    template_name = 'task/task_confirm_delete.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')

class TaskUpdate(UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    template_name = 'task/task_edit.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')