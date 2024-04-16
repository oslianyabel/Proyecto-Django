from django.shortcuts import render, redirect
from .models import Tag, Task
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .forms import TaskForm, TagForm
from rest_framework.response import Response
from .serializers import TaskSerializer, TagSerializer
from rest_framework.decorators import api_view
from rest_framework.views import APIView

class list(APIView):
    def get(self, request):
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
    
    def post(self, request):
        form = TaskForm(request.POST)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.autor = request.user
            instance.save()
            return JsonResponse({"message": "Tarea Guardada"})
        else:
            return JsonResponse({"errors": form.errors})

#@login_required 
class select(APIView):
    def get(self, request, id):
        task = Task.objects.get(id = id)
        if task.estado:
            task.estado = False
        else:
            task.estado = True
        
        task.save()
        return JsonResponse({"message": "Estado cambiado"})
    
    def delete(self, request, id):
        task = Task.objects.get(id = id)
        task.delete()
        return JsonResponse({"message": "Tarea eliminada"})
    
    def post(self, request, id):
        task = Task.objects.get(id = id)
        form = TaskForm(request.POST, instance = task)
        if form.is_valid():
            instance = form.save(commit = False)
            instance.autor = request.user
            instance.save()
            return JsonResponse({"message": "Tarea Actualizada"})
        else:
            return JsonResponse({"errors": form.errors})
        
class tags_task(APIView):
    def get(self, request, id):
        task = Task.objects.get(id = id)
        tags = Tag.objects.exclude(tasks=task)
        tags_task = task.tag_set.all()
        
        context = {
            "task": task,
            "tags": tags,
            "tags_task": tags_task,
        }
        
        return render(request, "app/tags_task.html", context)
    
class attach(APIView):
    def get(self, request, id_task, id_tag):
        task = Task.objects.get(id = id_task)
        tag = Tag.objects.get(id = id_tag)
        tag.tasks.add(task)
        return JsonResponse({"message": "etiqueta agregada a la tarea"})
        
    def delete(self, request, id_task, id_tag):
        task = Task.objects.get(id = id_task)
        tag = Tag.objects.get(id = id_tag)
        tag.tasks.remove(task)
        return JsonResponse({"message": "etiqueta quitada de la tarea"})
    
class filter(APIView):
    def get(self, request, id):
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