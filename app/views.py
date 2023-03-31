from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from threading import Thread



# Create your views here.

def index(request):
    return render(request, 'public_page/index.html')

@login_required
def dash(request):
    if request.method == 'POST':
        form = ConsultationForm()
    else:
        form = ConsultationForm()
    return render(request, 'dash_page/dash.html', {'form':form})

def signup(request):
    if request.method == 'POST':
        form = AllUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            name = form.cleaned_data.get('name')
            return redirect('dash')
        else:
            return render(request, 'public_page/signup.html')
    else:
        form = AllUserCreationForm()
    return render(request, 'public_page/signup.html', {'form': form})

def loginn(request):
    message=''
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                message = messages.success(request, 'Vous êtes connecté.')
                return redirect('dash')
            else:
                message = messages.error(request, 'Identifiants invalides.')
    return render(
        request, 'public_page/login.html', context={'form': form, 'message': message})

def logoutt(request):
    logout(request)
    return redirect('home')
