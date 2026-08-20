from django.urls import path
from .views import tasks,taskForm,success,editTask,delete
urlpatterns = [
    path("",tasks,name="tasks"),
    path("add/",taskForm,name="addTask"),
    path("success/",success,name='success'),
    path("edit/<int:id>/",editTask,name="editTask"),
    path("delete/<int:id>/", delete, name="delete"),
]