from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .models import Tag, Task
from .serializers import TaskSerializer, TagSerializer
from django.contrib.auth import logout

def custom_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            #print(user)
            if user is not None:
                login(request, user)
                return redirect("list")
            else:
                tags = Tag.objects.all()
                public = Task.objects.filter(is_public = True)
                private = Task.objects.filter(autor = request.user, is_public = False)

                tag_serializer = TagSerializer(tags, many=True)
                public_serializer = TaskSerializer(public, many=True)
                private_serializer = TaskSerializer(private, many=True)

                context = {
                    "public" : public_serializer.data,
                    "private" : private_serializer.data,
                    "tags" : tag_serializer.data,
                    "errors" : "El usuario o la contraseña han sido incorrectos",
                }
                return render(request, "app/index.html", context)
    else:
        return redirect('custom_login')
    
def exit(request):
    logout(request)
    return redirect("login")
