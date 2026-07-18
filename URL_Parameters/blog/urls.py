from . import views 
from django.urls import path,re_path

urlpatterns = [
    path("",views.home,name='home'),
    path('post/<int:id>/',views.post_details,name='post_details'),
    path('user/<str:name>/',views.user_profile,name='user_profile'),
    re_path(r'^article/(?P<year>[0-9]{4})/$',views.artivle_by_year,name='artivle_by_year'),
    re_path(r'^gender/(?P<gen>[a-z]{4})/$',views.gender , name='gender'),
    path('article/<int:year>/<int:month>/<int:days>/',views.article,name='h')
]