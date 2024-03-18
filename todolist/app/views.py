from django.shortcuts import render, redirect
from .models import Task
from django.http import HttpResponse
from django.utils.dateformat import DateFormat
from datetime import datetime
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, TaskSerializer, TagSerializer

# Create your views here.
def index(request):
    data = Task.objects.all()
    context = {
        "data" : data
    }
    return render(request, "app/index.html", context)

def insert(request):
    """ titulo = request.POST["titulo"]
    descripcion = request.POST["descripcion"]
    vence = request.POST["vence"]
    prioridad = request.POST["prioridad"]
    print("titulo:", titulo, "descripcion:", descripcion, "vence", vence, "prioridad:",prioridad)
    autor = User.objects.all()
    task = Task(titulo=titulo, descripcion=descripcion, vence=vence, estado=False, prioridad=prioridad, autor=request.user, is_public=False)
    task.save()
    return redirect("index") """
    serializer = TaskSerializer(data = request.data)
    serializer.save()
    return serializer

def login(request):
    context = {}
    return render(request, "app/login.html", context)


def update(request):
    return HttpResponse("Update")

def delete(request):
    return HttpResponse("Delete")

def complete(request):
    return HttpResponse("Complete")

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer