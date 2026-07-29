from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ('name','age','email')
    search_fields = ('name','email')
    list_filter = ['age','email']