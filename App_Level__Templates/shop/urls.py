from django.urls import path
from . import views

urlpatterns = [
    path("",views.shop,name='shop'),
    path("shopdetails/",views.shop_details,name='shop_details')
]