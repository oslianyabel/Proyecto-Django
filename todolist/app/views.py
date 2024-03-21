from django.shortcuts import render, redirect
from .models import Task
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

# Create your views here.
def list(request):
    if request.method == 'GET':
        public = Task.objects.filter(is_public = True)
        private = Task.objects.filter(autor = request.user, is_public = False)

        public_serializer = TaskSerializer(public, many=True)
        private_serializer = TaskSerializer(private, many=True)

        context = {
            "public" : public_serializer.data,
            "private" : private_serializer.data,
            "update" : {},
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
            public = Task.objects.filter(is_public = True)
            private = Task.objects.filter(autor = request.user)

            public_serializer = TaskSerializer(public, many=True)
            private_serializer = TaskSerializer(private, many=True)
            
            context = {
                "public" : public_serializer.data,
                "private" : private_serializer.data,
                "update" : {},
                "errors" : serializer.errors
            }
            return render(request, "app/index.html", context)
        
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
        print(data)
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

def login(request):
    context = {}
    return render(request, "app/login.html", context)

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
