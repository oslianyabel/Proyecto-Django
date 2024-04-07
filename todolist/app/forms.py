from django import forms
from .models import Task, Tag

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)

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