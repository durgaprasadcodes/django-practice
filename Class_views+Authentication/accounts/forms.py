from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms

User = get_user_model()


class RegistrationForm(UserCreationForm):

    name = forms.CharField(max_length=200,help_text=None)

    email = forms.EmailField(widget=forms.EmailInput,help_text=None)

    password1 = forms.CharField(widget=forms.PasswordInput, help_text=None )

    password2 = forms.CharField(widget=forms.PasswordInput, help_text=None )


    class Meta:
        model = User
        fields = ["name", "email", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email", "").lower()

        if not email:
            raise forms.ValidationError("Email Not Found...")

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists.")

        return email