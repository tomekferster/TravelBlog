from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # No backend authenticated the credentials (user does not exist)
            pass   
    context = {}
    return render(request, 'account/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    if request.method == 'POST':
        print(request.POST)
    else:
        form = UserCreationForm()
    context = {}
    print(request.POST)
    return render(request, 'account/login_register.html', context)