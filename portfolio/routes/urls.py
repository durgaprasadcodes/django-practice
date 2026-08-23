from django.urls import path
# pyrefly: ignore [missing-import]
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("skills/", views.skills, name="skills"),
    path("contact/",views.contact,name='contact'),
    path("footer/", views.footer, name="footer")
]