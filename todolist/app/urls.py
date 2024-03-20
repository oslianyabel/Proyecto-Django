from django.urls import path
from . import views

urlpatterns = [
    path("list", views.list, name = "list"),
    path("<int:id>", views.select, name = "select"),
    path("update", views.update, name = "update"),
    path("update-form/<int:id>", views.update_form, name = "update-form"),
    path("delete/<int:id>", views.delete, name = "delete"),
    path("login/", views.login, name = "login"),
    path("complete/<int:id>", views.complete, name = "complete")
]