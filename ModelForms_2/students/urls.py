from django.urls import path
from .views import home,add_students,edit_students,student_list,delete

urlpatterns = [
    path("",home,name='home'),
    path("add/",add_students,name='add_students'),
    path("edit/<int:id>/",edit_students,name='edit_students'),
    path("edit/",student_list,name='student_list'),
    path("delete/<int:id>/", delete, name='delete')
]