from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> This Is a Home Page </h1>")