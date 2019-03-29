from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import LoginForm, RegistrationForm

# Create your views here.

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('userapp:userpage'))
        else:
            return render(request, 'authapp/login.html', {'login_form': form})
    else:
        form = LoginForm()
        return render(request, 'authapp/login.html', {'login_form': form})

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('auth:authlogin'))

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('auth:authlogin'))

    else:
        form = RegistrationForm()

    return render(request, 'authapp/registration.html', {'registration_form': form})

