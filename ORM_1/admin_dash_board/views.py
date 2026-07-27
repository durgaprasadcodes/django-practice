from django.shortcuts import render
from .models import User

def dashboard(request):
    users = User.objects.all()
    return render(request,'dash.html',{'users':users})
