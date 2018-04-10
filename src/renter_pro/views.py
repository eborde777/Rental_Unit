from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def home_page(request):
    return render(request, 'home_page.html', {})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home_page')

        else:
            messages.error(request, 'Invalid Username or Password')

    return render(request, 'login_page.html', {})

def logout_view(request):
    logout(request)
    return redirect('login_page')

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            user = authenticate(request, username = username, password = password1)
            login(request, user)
            return redirect('home_page')

    else:
        form = RegistrationForm()
    return render(request, 'register_page.html', {'form': form})

def about_view(request):
    return render(request, 'about_page.html', {})

def contact_view(request):
    return render(request, 'contact_page.html', {})