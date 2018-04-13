import re
from django import forms
from django.forms import PasswordInput, EmailInput

from django.contrib.auth.models import User
from .email_domain_list import domains


class RegistrationForm(forms.ModelForm):
    password_text = 'Minimum 8 character length. Must contain atleast one capital leter, number and special characters'
    confirm_password = forms.CharField(widget=forms.PasswordInput(), max_length=120)
    password         = forms.CharField(widget=forms.PasswordInput(), max_length=120, help_text=password_text)

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password', 'confirm_password', ]
        widgets = {
            'password': PasswordInput(),
        }
       

    def clean_username(self):
        username = self.cleaned_data.get('username')
        # username check 
        ALPHANUM = re.compile('^[a-zA-Z]+[0-9@#!&_.-]+[0-9@#!&_.-]+$')

        if ALPHANUM.match(username) is None:
            raise forms.ValidationError("Please use valid username. It should start with one letter, number and then special character @#!&_.-")

        if len(username) < 6 or len(username) > 20:
            raise forms.ValidationError("Username length must be between 6 and 20")
        return username

    def clean_confirm_password(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('confirm_password')

        if password1 != password2:
            raise forms.ValidationError("Password Doesn't Match")
        return password2

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("Enter valid email address")
        else:
            name, domain = email.split('@')
            if domain not in domains:
                raise forms.ValidationError("Email address has incorrect domain, please use different email address")
        return email


