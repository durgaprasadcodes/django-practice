from django.urls import path
from .views import post,create_post

urlpatterns = [
    path("",post,name="post"),
    path("addpost/",create_post,name="create_post")
]