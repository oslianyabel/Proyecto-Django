from django.shortcuts import render
from .models import Tag
from django.http import JsonResponse
from .forms import TagForm

def list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        form = TagForm()
        context = {
            "etiquetas": tags,
            "form": form,
        }
        return render(request, "app/tags.html", context)
    
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Etiqueta creada"})
        else:
            return JsonResponse({"errors": form.errors})
        
def select(request, id):
    if request.method == 'DELETE':
        tag = Tag.objects.get(id = id)
        tag.delete()
        return JsonResponse({"message": "Etiqueta eliminada"})
    
    if request.method == 'POST':
        tag = Tag.objects.get(id = id)
        form = TagForm(request.POST, instance=tag)
        if form.is_valid():
            form.save()
            return JsonResponse({"message": "Etiqueta actualizada"})
        else:
            return JsonResponse({"errors": form.errors})