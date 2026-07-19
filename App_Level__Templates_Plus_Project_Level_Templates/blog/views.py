from django.shortcuts import render

def blog(request):
    return render(request,'blog.html')
def blogdetails(request):
    return render(request,'blogdetails.html')