from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>This Is Big Home Page </h1>")