from django.db import models


class Task(models.Model):
    task_name = models.CharField(max_length=150)
    task = models.TextField(default="You Forgot to Add Task")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_complete = models.BooleanField(default=False)