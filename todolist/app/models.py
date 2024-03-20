from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Task(models.Model):
    titulo = models.CharField(max_length = 30)
    descripcion = models.TextField()
    prioridad = models.CharField(max_length = 10)
    estado = models.BooleanField(default = False)
    is_public = models.BooleanField(default = False)
    vence = models.DateTimeField(null = True)
    created = models.DateTimeField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Tag(models.Model):
    nombre = models.CharField(max_length = 30)
    tasks = models.ManyToManyField(Task)

    def __str__(self):
        return self.nombre