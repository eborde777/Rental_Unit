from django import forms
from .models import Contact
from rental_unit.email_domain_list import domains

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if "@" not in email:
            raise forms.ValidationError("Enter valid email address")
        else:
            name, domain = email.split('@')
            if domain not in domains:
                raise forms.ValidationError("Email address has incorrect domain, please use different email address")
        return email