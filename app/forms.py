from django import forms
from .models import Task, Tag

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["titulo", "descripcion", "prioridad", "vence", "is_public"]
        
class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["nombre"]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control w-25', 'id': 'nombreEtiqueta', 'placeholder': 'Nombre de la etiqueta'}),
        }