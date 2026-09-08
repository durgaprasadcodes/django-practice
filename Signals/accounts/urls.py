from django.urls import path
from .views import Dashboard,UserInfo,Login,LogoutView,Register,EditUserInfo,DeleteUser


urlpatterns = [
    path("",Dashboard.as_view(),name="Dashboard"),
    path("register/",Register.as_view(),name="Register"),
    path("login/",Login.as_view(),name="Login"),
    path("<int:pk>/",UserInfo.as_view(),name="UserInfo"),
    path("edit/<int:pk>/",EditUserInfo.as_view(),name="EditUserInfo"),
    path("delete/<int:pk>/",DeleteUser.as_view(),name="DeleteUser"),
    path("logout/",LogoutView.as_view(),name="Logout")
]