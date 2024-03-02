from django.shortcuts import render
from .models import Task
""" from django.http import HttpResponse
from django.template import loader """

# Create your views here.
def index(request):
    """ template = loader.get_template("app/index.html") """
    data = Task.objects.all()
    context = {
        "data" : data
    }
    return render(request, "app/index.html", context)
    """ return HttpResponse(template.render(context, request)) """
