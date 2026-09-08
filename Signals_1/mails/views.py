from django.shortcuts import render
from django.contrib.auth.views import LoginView,LogoutView
from django.views.generic import CreateView,TemplateView,UpdateView
from .forms import RegistrationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import User
from django.urls  import reverse_lazy

def home(request): 
    return render(request,"home.html")

class Dashboard(TemplateView,LoginRequiredMixin):
    template_name = "dashboard.html"

class Registration(CreateView):
    form_class = RegistrationForm
    template_name = "form.html"
    success_url = reverse_lazy("Dashboard")

class Login(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
    

class EditUser(UpdateView):
    model = User
    template_name = "form.html"
    fields = ["name","email"]
    context_object_name = "user"
    success_url =  reverse_lazy("Dashboard")
    
    