from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This is a Home Page</h1>")
def about(reuqest):
    return HttpResponse("<h1>This is a About Page</h1>")