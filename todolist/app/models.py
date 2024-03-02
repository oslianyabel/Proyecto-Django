from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30)

    def __str__(self):
        return self.username

class Task(models.Model):
    titulo = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100)
    prioridad = models.CharField(max_length = 10)
    vence = models.DateField()
    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
    
class TaskPublic(models.Model):
    titulo = models.CharField(max_length = 30)
    descripcion = models.CharField(max_length = 100)
    prioridad = models.CharField(max_length = 10)
    vence = models.DateField()
    ultimo_uso = models.CharField(max_length = 30)

    def __str__(self):
        return self.titulo