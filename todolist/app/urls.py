from django.urls import path
from . import views

urlpatterns = [
    path("list", views.list, name = "list"),
    path("select/<int:id>", views.select, name = "select"),
    path("login/", views.login, name = "login"),
]