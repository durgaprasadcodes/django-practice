from django.urls import path
from .views import Dashboard,Registration,Login,EditUser,LogoutView,home

urlpatterns = [
    path("",home,name="home"),
    path("dashboard/",Dashboard.as_view(),name="Dashboard"),
    path("login/",Login.as_view(),name="Login"),
    path("register/",Registration.as_view(),name="Registration"),
    path("edit/<int:pk>/",EditUser.as_view(),name="EditUser"),
    path("logout/",LogoutView.as_view(),name="LogoutView"),
]