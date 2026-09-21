from django.urls import path
from .views import UsersRoute

urlpatterns = [
    path("",UsersRoute.as_view(),name="UserRoute")
]