from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .forms import *


class RegistrationView(CreateView):
    form_class =  RegistrationForm
    template_name = 'registration.html'
    model = User
    success_url = reverse_lazy('account:login')

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'login.html'

def logout_page(request):
    logout(request)
    return redirect('main:home')