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

# Create your views here.
def list(request):
    if request.method == 'GET':
        public = Task.objects.filter(is_public = True)
        private = Task.objects.filter(autor = request.user)

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

        serializer = TaskSerializer(data=data_ok)
        if serializer.is_valid():
            serializer.save(autor = request.user)
            return redirect("list")
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
    if request.method == 'DELETE':
        print("entró!")
        task = Task.objects.get(pk = id)
        task.delete()
        print("tarea borrada")
        return HttpResponseRedirect("/tasks/list")

def delete(request, id):#GET
    Task.objects.get(id = id).delete()
    return HttpResponseRedirect(reverse("list"))

def update(request):#POST
    task = Task.objects.get(pk = request.POST["id"])
    data = request.POST
    data_ok = {}
    for clave, valor in data.items():
        data_ok[clave] = valor

    serializer = TaskSerializer(task, data = data_ok)

    if serializer.is_valid():
        serializer.save(autor = request.user)
        return redirect("list")
    else:
        public = Task.objects.filter(is_public = True)
        private = Task.objects.filter(autor = request.user)

        public_serializer = TaskSerializer(public, many=True)
        private_serializer = TaskSerializer(private, many=True)
            
        context = {
            "public" : public_serializer.data,
            "private" : private_serializer.data,
            "update" : {},
            "errors" : serializer.errors,
        }
        return render(request, "app/index.html", context)
        
def update_form(request, id):#GET
    task = Task.objects.get(id = id)
    public = Task.objects.filter(is_public = True)
    private = Task.objects.filter(autor = request.user)

    public_serializer = TaskSerializer(public, many=True)
    private_serializer = TaskSerializer(private, many=True)
    serializer = TaskSerializer(task)

    context = {
        "public" : public_serializer.data,
        "private" : private_serializer.data,
        "update" : serializer.data,
    }
    return render(request, "app/index.html", context)


def login(request):
    context = {}
    return render(request, "app/login.html", context)

def complete(request, id):
    print("fdsfds")
    task = Task.objects.get(id = id)
    if task.estado:
        task.estado = False
    else:
        task.estado = True
    task.save()
    return redirect("list")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer