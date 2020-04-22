
from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import path   
from django.conf.urls import url, include
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import TemplateView

from django.urls import path

#registering the app

app_name = 'user'
    
urlpatterns = [
  
    path('admin/', admin.site.urls),
 
]