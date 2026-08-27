from django.contrib import admin
from .models import Post


@admin.register(Post)
class Admin(admin.ModelAdmin):
    list_display = ["title", "description"]
    list_filter =  ["title"]