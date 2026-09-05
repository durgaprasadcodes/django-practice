from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

def send_email(request):
    subject = "Welcome to Django Course"
    message = render_to_string("mail.html",{'username':'Rolex','course':'Django Tutorial'})
    email = EmailMessage(
        subject,
        message,
        "durgaprasad04289@gmail.com",
        ["24me1a4289@rcee.ac.in"]
    )
    email.content_subtype = "html"
    email.send()
    return HttpResponse("Email Sended Successfully")