from django.urls import path,  include
from . import views, tags_views, login_views

urlpatterns = [
    path("list", views.list, name = "list"),
    path("list/<int:id>", views.filter, name = "filter"),
    path("tags/list", tags_views.list, name = "tags-list"),
    path("tags/<int:id>", views.tags_task, name = "tags_task"),
    path("tags/select/<int:id>", tags_views.select, name = "tags-select"),
    path("tags/select/<int:id_task>/<int:id_tag>", views.attach, name = "attach"),
    path("exit", login_views.exit, name = "exit"),
    path("select/<int:id>", views.select, name = "select"),
]