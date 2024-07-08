from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegistrationForm


def login_view(request):
    page_name = 'login'
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # No backend authenticated the credentials (user does not exist)
            pass   
    elif request.user.is_authenticated:
        return redirect('home')

    context = {'page_name': page_name}
    return render(request, 'account/login_register.html', context)

def logout_view(request):
    logout(request)
    return redirect('home')

def register_view(request):
    page_name = 'register'
    form = RegistrationForm(request.POST or None, request.FILES or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()

            login(request, user)
            return redirect('home')
        else:
            # An error occured during registration
            pass
    elif request.user.is_authenticated:
        return redirect('home')
        
    context = {'form': form,
               'page_name': page_name
               }
    print(request.POST)
    print(request.FILES)
    return render(request, 'account/login_register.html', context)