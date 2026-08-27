from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .form import RegistrationForm

User = get_user_model()

@login_required(login_url="login_form")
def dashboard(request):
    return render(request,'dashboard.html')


def register_form(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            messages.success(request,'Registration Successfull')
            return redirect('dashboard')
        else:
            messages.error(request,'Registration Failed')
    else:
        form = RegistrationForm()
    return render(request,'register.html',{'forms':form})
    
def login_form(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, email=email, password=password)
        if user :
            login(request,user)
            messages.success(request,'Login Successfull')
            return redirect('dashboard')
        else:
            messages.error(request,'Login Failed')
    return render(request,'login.html')
def log_out(request):
    logout(request)
    return redirect("login_form")