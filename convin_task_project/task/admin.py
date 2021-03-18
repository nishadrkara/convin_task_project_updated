from django.contrib import admin
from task.models import Task,TaskTracker


# Register your models here.

admin.site.register(Task)
admin.site.register(TaskTracker)
