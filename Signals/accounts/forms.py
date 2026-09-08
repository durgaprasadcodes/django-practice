from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()

class RegistrationForm(UserCreationForm):
    name = forms.CharField(max_length=200,help_text=None,widget=forms.TextInput(attrs={"placeholder":"Enter your name"}))
    email = forms.EmailField(max_length=200,widget=forms.EmailInput(attrs={"placeholder":"Enter your email"}),help_text=None)
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}),help_text=None)
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"placeholder":"Enter your password"}),help_text=None)
    
    class Meta:
        model = User
        fields = ['name','email','password1','password2']
    
    def clean_email(self):
        email = self.cleaned_data.get('email','').lower()
        if not email:
            raise forms.ValidationError("Email Not Found...")
            
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return email