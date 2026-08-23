from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

from .form import RegistrationForm

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request,user)
            messages.success(request,'Registration Successfull')
            return redirect('dashboard')
        else:
            messages.error(request,'Registration Failed')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'forms':form})

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username=username,password=password)
        if user :
            auth_login(request,user)
            messages.success(request,'Login Successfull')
            return redirect('dashboard')
        else:
            messages.error(request,'Login Failed')
    return render(request,'login.html')

def logout(request):
    auth_logout(request)
    messages.success(request,'Logged Out')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request,'dashboard.html')