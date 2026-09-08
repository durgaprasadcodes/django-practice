from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.db.models.signals import post_save
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.signals import user_logged_in

User = get_user_model()

@receiver(post_save,sender=User)
def send_welcome_email(sender,instance,created,**kwargs):
    if created:
        subject = "Welcome To AlgoFlow"
        html_message = render_to_string("registration_mail.html",{"name":instance.name,"welcome_message":"You've officially joined AlgoFlow. Let's build something amazing! 💪"})
        email = EmailMultiAlternatives(
            subject=subject,
            body="Welcome to AlgoFlow!",
            from_email="None",
            to=[instance.email]
            )
        email.attach_alternative(html_message,"text/html")
        email.send()

@receiver(user_logged_in,sender=User)
def login_success(sender,request,user,**kwargs):
    subject = "Login Successful - AlgoFlow"
    html_message = render_to_string("login_mail.html",{"name":user.name,"login_message":"You've successfully logged in to AlgoFlow. Let's build something amazing! 💪","email":user.email})
    email = EmailMultiAlternatives(
        subject=subject,
        body="You have successfully logged in to AlgoFlow.",
        from_email="None",
        to=[user.email]
        )
    email.attach_alternative(html_message,"text/html")
    email.send()