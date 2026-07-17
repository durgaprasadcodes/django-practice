from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This shop Home Page</h1>")

def about(request):
    return HttpResponse("<h1>This shop About Page </h1>")
