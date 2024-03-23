from django.shortcuts import render, redirect
from .models import Tag, Task
from django.http import HttpResponse
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.http import JsonResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import UserSerializer, TaskSerializer, TagSerializer
from django.urls import reverse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required

@login_required
def list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        public = Task.objects.filter(is_public = True)
        private = Task.objects.filter(autor = request.user, is_public = False)

        tag_serializer = TagSerializer(tags, many=True)
        public_serializer = TaskSerializer(public, many=True)
        private_serializer = TaskSerializer(private, many=True)

        context = {
            "public" : public_serializer.data,
            "private" : private_serializer.data,
            "tags" : tag_serializer.data,
        }
        return render(request, "app/index.html", context)

    if request.method == 'POST':
        data = request.POST
        data_ok = {}
        for clave, valor in data.items():
            data_ok[clave] = valor

        #print(data_ok)
        serializer = TaskSerializer(data=data_ok)
        if serializer.is_valid():
            serializer.save(autor = request.user)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"errors": serializer.errors})
        
@login_required        
def select(request, id):
    if request.method == 'GET':
        task = Task.objects.get(id = id)
        if task.estado:
            task.estado = False
        else:
            task.estado = True
        
        task.save()
        serializer = TaskSerializer(task)
        return JsonResponse(serializer.data)

    if request.method == 'DELETE':
        task = Task.objects.get(pk = id)
        task.delete()
        return JsonResponse({"message": "Tarea eliminada"})
    
    if request.method == 'POST':
        data = request.POST
        #print(data)
        data_ok = {}
        for clave, valor in data.items():
            data_ok[clave] = valor
        #print(data_ok)
        task = Task.objects.get(id = id)
        serializer = TaskSerializer(task, data = data_ok)
        if serializer.is_valid():
            serializer.save(autor = request.user)
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"errors": serializer.errors})
        
        
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')  # Reemplaza 'home' con la URL a la que quieres redirigir después del registro
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})

def attach(request, id_task, id_tag):
    task = Task.objects.all(id = id_task)
    tag = Tag.objects.get(id = id_tag)
    tag.tasks.add(task)
    return JsonResponse({"message": "etiqueta agregada a la tarea"})

def detach(request, id_task, id_tag):
    task = Task.objects.all(id = id_task)
    tag = Tag.objects.get(id = id_tag)
    tag.tasks.remove(task)
    return JsonResponse({"message": "etiqueta quitada de la tarea"})
