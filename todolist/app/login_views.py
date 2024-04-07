from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Tag, Task
from django.contrib.auth.forms import UserCreationForm

def exit(request):
    logout(request)
    return redirect("login")

def registro(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'app/register.html', {'form': form})