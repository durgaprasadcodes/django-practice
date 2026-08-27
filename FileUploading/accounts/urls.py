from django.urls import path
from .views import upload,profile

urlpatterns = [
    path("upload/",upload,name="upload"),
    path("profile/",profile,name="profile")
]