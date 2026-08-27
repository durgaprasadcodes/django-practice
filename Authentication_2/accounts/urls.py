from django.urls import path
from .views import dashboard,register_form,login_form,log_out

urlpatterns = [
    path("",dashboard,name="dashboard"),
    path("login/",login_form,name="login_form"),
    path("register/",register_form,name="register_form"),
    path("logout/",log_out,name="log_out")
]