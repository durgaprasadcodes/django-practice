
from .forms import RegistrationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,TemplateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin


class DashboardView(LoginRequiredMixin,TemplateView):
    template_name = "dashboard.html"

class RegisterRoute(CreateView):
    form_class = RegistrationForm
    template_name = "register.html"
    success_url = reverse_lazy("login")

class LoginRoute(LoginView):
    template_name = "login.html"
    redirect_authenticated_user = True
