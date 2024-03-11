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
    estado = models.BooleanField(default = False)
    is_public = models.BooleanField(default = False)
    vence = models.CharField(max_length = 30)
    autor = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.titulo
    
class Tag(models.Model):
    nombre = models.CharField(max_length = 30)

    def __str__(self):
        return self.nombre

class Tag_Task(models.Model):
    tag_id = models.ForeignKey(Tag, on_delete=models.CASCADE)
    task_id = models.ForeignKey(Task, on_delete = models.CASCADE)