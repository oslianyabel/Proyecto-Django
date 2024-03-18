from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task, Tag

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']

class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    titulo = serializers.CharField(required = True, max_length = 30, allow_blank = False)
    descripcion = serializers.CharField(required=True, allow_blank=True)
    prioridad = serializers.ChoiceField(choices=["alta", "baja", "media"], required=True)
    estado = serializers.BooleanField(required=False, default=False)
    is_public = serializers.BooleanField(required=False, default=False)

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
    nombre = serializers.CharField(max_length = 30, required = True, allow_blank = False)

    class Meta:
        model = Tag
        ordering = ['created']