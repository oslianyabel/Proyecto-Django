from django.shortcuts import render, redirect
from .models import Tag, Task
from django.http import HttpResponse
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, TagForm

@login_required
def list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        public = Task.objects.filter(is_public = True)
        private = Task.objects.filter(autor = request.user, is_public = False)
        form = TaskForm()

        context = {
            "public" : public,
            "private" : private,
            "tags" : tags,
            "form": form,
        }
        return render(request, "app/index.html", context)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.autor = request.user
            instance.save()
            return JsonResponse({"message": "Tarea Guardada"})
        else:
            return JsonResponse({"errors": form.errors})
        
@login_required        
def select(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id = id)
        if task.estado:
            task.estado = False
        else:
            task.estado = True
        
        task.save()
        return JsonResponse({"message": "Estado cambiado"})

    if request.method == 'DELETE':
        task = Task.objects.get(pk = id)
        task.delete()
        return JsonResponse({"message": "Tarea eliminada"})
    
    if request.method == 'POST':
        task = Task.objects.get(id = id)
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.autor = request.user
            instance.save()
            return JsonResponse({"message": "Tarea Actualizada"})
        else:
            return JsonResponse({"errors": form.errors})
        
        
def tags_task(request, id):
    task = Task.objects.get(id = id)
    tags = Tag.objects.exclude(tasks=task)
    tags_task = task.tag_set.all()
    
    context = {
        "task": task,
        "tags": tags,
        "tags_task": tags_task,
    }
    return render(request, "app/tags_task.html", context)


def attach(request, id_task, id_tag):
    task = Task.objects.get(id = id_task)
    tag = Tag.objects.get(id = id_tag)
    if request.method == 'GET':
        tag.tasks.add(task)
        return JsonResponse({"message": "etiqueta agregada a la tarea"})
    if request.method == 'DELETE':
        tag.tasks.remove(task)
        return JsonResponse({"message": "etiqueta quitada de la tarea"})
    else:
        return JsonResponse()
    
def filter(request, id):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id = id)
    public = Task.objects.filter(is_public = True, tag = tag)
    private = Task.objects.filter(autor = request.user, is_public = False, tag = tag)

    context = {
        "public" : public,
        "private" : private,
        "tags" : tags,
    }
    return render(request, "app/index.html", context)
    
