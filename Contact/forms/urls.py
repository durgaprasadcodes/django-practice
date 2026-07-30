from django.urls import path
from .views import contact_form,submit_contact
urlpatterns = [
    path('',contact_form,name='contact_form'),
    path('submit/',submit_contact,name='submit_contact')
]