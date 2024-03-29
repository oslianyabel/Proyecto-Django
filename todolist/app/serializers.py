from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Tag

OPCIONES = [
    ("baja", "Baja"),
    ("media", "Media"),
    ("alta", "Alta"),
]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(max_length = 20, allow_blank = False)
    descripcion = serializers.CharField(allow_blank=True)
    prioridad = serializers.ChoiceField(choices=OPCIONES, required=True)
    estado = serializers.BooleanField(default=False)
    vence = serializers.CharField(default=None)
    is_public = serializers.BooleanField(default=False)

    class Meta:
        model = Task
        ordering = ['created']

    def create(self, validated_data):
        return Task.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.titulo = validated_data["titulo"]
        instance.descripcion = validated_data["descripcion"]
        instance.prioridad = validated_data["prioridad"]
        instance.estado = validated_data["estado"]
        instance.is_public = validated_data["is_public"]
        instance.save()
        return instance

class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nombre = serializers.CharField(max_length = 30, required = True, allow_blank = False)

    class Meta:
        model = Tag
        ordering = ['created']

    def create(self, validated_data):
        return Tag.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.nombre = validated_data["nombre"]
        instance.save()
        return instance