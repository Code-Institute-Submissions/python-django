from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from user.models import User, MyModel
from user.forms import CustomUserCreationForm


#Routing, where you are directing the urls and how they are requesting by my code
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'





def login_view(request):
     return render(request, 'login.html')

    