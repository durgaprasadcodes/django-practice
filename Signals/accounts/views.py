from django.shortcuts import render
from .models import User
from django.contrib.auth.views import LogoutView,LoginView
from django.views.generic import CreateView,UpdateView,ListView,DeleteView,DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .forms import RegistrationForm

class Dashboard(ListView,LoginRequiredMixin):
    model = User
    template_name = 'dashboard.html'
    context_object_name = 'users'

class UserInfo(DetailView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'
    
class Login(LoginView):
    template_name = 'login.html'
    redirect_authenticated_user = True

class Register(CreateView):
    form_class = RegistrationForm
    template_name = 'form.html'
    success_url = reverse_lazy("Dashboard")

class EditUserInfo(UpdateView):
    model = User
    fields = ["name","email"]
    context_object_name = "user"
    template_name = 'form.html'
    success_url = reverse_lazy("Dashboard")

class DeleteUser(DeleteView):
    model = User
    success_url = reverse_lazy("Dashboard")

