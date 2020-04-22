from django.conf.urls import url
from django.contrib import admin
from orders.views import library, order_detail, order_list
from django.urls import path
from . import views
from home import views
from home.views import index

app_name = 'orders'

urlpatterns = [
   
]