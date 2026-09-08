from django.urls import path
from .views import DashboardView,RegisterRoute,LoginRoute,LogoutView


urlpatterns = [
    path("",DashboardView.as_view(),name="DashboardView"),
    path("register/",RegisterRoute.as_view(),name="RegisterRoute") ,
    path("login/",LoginRoute.as_view(),name="LoginRoute"),
    path("logout/",LogoutView.as_view(),name="LogoutRoute")
]

