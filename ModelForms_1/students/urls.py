from django.urls import path
from .views import create_student,student_list,student_details,edit_student,delete_student

urlpatterns = [
    path('',student_list,name='student_list'),
    path("addstudent/",create_student,name='create_student'),
    path("studentdetails/<int:id>",student_details,name='student_details'),
    path('edit/<int:id>',edit_student,name='edit_student'),
    path('delete/<int:id>',delete_student,name='delete_student')
]