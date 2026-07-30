from django.shortcuts import render,redirect
from .models import Contact
from django.http import HttpResponse

def contact_form(request):
    return render(request,'form.html')
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        if name and email:
            Contact.objects.create(name= name,email = email)
            return HttpResponse(f"Thak you, {name} for your work")
        else:
            return HttpResponse("Please Provide Both Name and Email",status = 400)
        
    return redirect('contact_form')