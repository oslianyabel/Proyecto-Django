from django.shortcuts import render
from .models import Tag
from .serializers import TagSerializer
from django.http import JsonResponse

def list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serializer = TagSerializer(tags, many=True)
        context = {
            "etiquetas": serializer.data,
        }
        return render(request, "app/tags.html", context)
    
    if request.method == 'POST':
        data = request.POST
        data_ok = {}
        for clave, valor in data.items():
            data_ok[clave] = valor

        serializer = TagSerializer(data = data_ok)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"errors": serializer.errors})
        
def select(request, id):
    if request.method == 'DELETE':
        tag = Tag.objects.get(id = id)
        tag.delete()
        return JsonResponse({"message": "Etiqueta eliminada con exito"})
    
    if request.method == 'POST':
        tag = Tag.objects.get(id = id)
        data = request.POST
        data_ok = {}
        for clave, valor in data.items():
            data_ok[clave] = valor

        serializer = TagSerializer(tag, data = data_ok)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        else:
            return JsonResponse({"errors": serializer.errors})