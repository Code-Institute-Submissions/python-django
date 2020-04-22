from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import auth 
from django.shortcuts import render, redirect
from products.models import Feature, Bug
from django.urls import reverse
from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import redirect
from accounts.forms import  SignUpForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.views import (
    LoginView,
)
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login




#login requirements below
def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect(reverse('publicise_bug.html'))
        
    else:
        messages.error(request, "Unable to log you in at this time!")
        



#log out requirements below
def logout_view(request):
    logout(request)
    return redirect(reverse('index'))
