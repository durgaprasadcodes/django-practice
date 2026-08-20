from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskManager(admin.ModelAdmin):
    list_display = ["task_name", "task", "created", "updated", "is_complete"]
    list_filter = ["is_complete", "created", "updated"]