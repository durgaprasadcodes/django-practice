from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1> This Is a Blog Home Page </h1>")

def post_details(request,id):
    return HttpResponse(f"<h1>Post id : {id}</h1>")

def user_profile(request,name):
    return HttpResponse(f"<h1>UserName : {name}</h1>")

def artivle_by_year(request,year):
    return HttpResponse(f"<h1>Article from Year {year}</h1>")

def gender(request,gen):
    return HttpResponse(f"<h1>Gender : {gen}</h1>")
def article(request,**kwargs):
    return HttpResponse(f"<h1>Article Time at {kwargs}</h1>")