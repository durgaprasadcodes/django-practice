from django.views.generic import ListView
from django.core.cache import cache
from .models import Users
import time

class UsersRoute(ListView):
    template_name = "user.html"
    context_object_name = "users"

    def get_queryset(self):
        start = time.perf_counter()
        users = cache.get("users")

        if users is None:
            users = list(Users.objects.all())
            cache.set("users", users)
            
        end = time.perf_counter()

        print(f"Total get_queryset time: {end - start:.6f} seconds")
        
        return users
