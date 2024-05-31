from django.urls import path
from . import tags_views, login_views, views_class

urlpatterns = [
    path("list", views_class.list.as_view(), name = "list"),
    path("list/<int:id>", views_class.filter.as_view(), name = "filter"),
    path("tags/list", tags_views.list, name = "tags-list"),
    path("tags/<int:id>", views_class.tags_task.as_view(), name = "tags_task"),
    path("tags/select/<int:id>", tags_views.select, name = "tags-select"),
    path("tags/select/<int:id_task>/<int:id_tag>", views_class.attach.as_view(), name = "attach"),
    path("exit", login_views.exit, name = "exit"),
    path("select/<int:id>", views_class.select.as_view(), name = "select"),
]