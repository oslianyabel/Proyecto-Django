from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("login/", views.login, name = "login"),
    path("insert/", views.insert, name = "insert"),
    path("update/", views.update, name = "update"),
    path("delete/", views.delete, name = "delete"),
    path("complete/", views.complete, name = "complete")
]