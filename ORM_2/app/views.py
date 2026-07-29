from django.shortcuts import render
from .models import Students

def Users(request):
    Student = Students.objects.all()
    return render(request,'home.html',{'students':Student})