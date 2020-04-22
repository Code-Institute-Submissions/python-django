from django.db import models

from django.urls import path
from django.conf.urls import url
from home.views import index

from django.urls import reverse

from django.shortcuts import redirect
from django.urls import reverse_lazy

app_name = 'home'

urlpatterns = [
    
   path('', index, name='index'),
 
    
]

