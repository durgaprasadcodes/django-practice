from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class RegistrationForm(UserCreationForm):
    
    name = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'placeholder':'Enter Your Name'}),help_text=None)
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={'placeholder':'Enter Your Email'}),help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Your Password'}),help_text=None)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Rewrite The Password '}),help_text=None)
    
    class Meta:
        model = User
        fields = ["name","email","password1","password2"]
    
    def clean_email(self):
        email = self.cleaned_data.get('email','').lower()

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email Already Existed")
        return email
    