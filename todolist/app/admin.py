from django.contrib import admin
from .models import Task, User, Tag, Tag_Task

# Register your models here.
admin.site.register(Task)
admin.site.register(User)
admin.site.register(Tag)
admin.site.register(Tag_Task)