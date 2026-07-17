from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This Blog Home Page</h1>")

def about(request):
    return HttpResponse("<h1>This Blog About Page </h1>")
