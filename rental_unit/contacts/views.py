from django.shortcuts import render
from .forms import ContactForm
from .models import Contact

# Create your views here.

def contact_view(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        form.save()

    return render(request, "contact_page.html", {'form':form})
    
