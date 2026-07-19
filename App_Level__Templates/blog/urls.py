from django.urls import path
from . import views
urlpatterns = [
    path("",views.blog,name='blog_html'),
    path("blogdetails/",views.blog_details,name='blog_details')
]