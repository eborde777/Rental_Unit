from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
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
    form = RegistrationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        password = form.cleaned_data['password']
        instance.set_password(password)
        instance.save()
        return redirect('login_page')

    return render(request, 'register_page.html', {'form': form})

def about_view(request):
    return render(request, 'about_page.html', {})
