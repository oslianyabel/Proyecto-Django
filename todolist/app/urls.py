from django.urls import path,  include
from . import views, tags_views, login_views

urlpatterns = [
    path("list", views.list, name = "list"),
    path("login", login_views.custom_login, name = "custom_login"),
    path("exit", login_views.exit, name = "exit"),
    path("select/<int:id>", views.select, name = "select"),
    path("tags/list", tags_views.list, name = "tags-list"),
    path("tags/select/<int:id>", tags_views.select, name = "tags-select"),
]