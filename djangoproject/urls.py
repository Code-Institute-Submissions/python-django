"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path
from home.views import index
from products.views import bugs, features, user_history
from orders.urls import library, order_detail, order_list
from django.views.generic import TemplateView
from products.views import  bug_comment, feature_comment, publicise_bug, view_bugs, view_features, skills, planning, mobile, it_solutions, publicise_features, pricing, datascience
from django.urls import path 
from django.views.generic.base import TemplateView 
from user.views import SignUpView 
from django.contrib.auth import views as auth_views






# This url pattern below is acting like a quater back control the the url, to what goes where and where everthing is routed. If a url is not below here, then the program will not recognize or run it.
urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('products/', include('products.urls')),
    path('', index, name='index'),
    path('account/', include('accounts.urls')),
    #path('admin/', admin.site.urls),
    path('users/', include('user.urls')),
    path('users/', include('django.contrib.auth.urls')),
    path('signup/', SignUpView.as_view(), name='signup'), 
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/login/',auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('bugs/',bugs, name='bugs'),
    path('features/',features, name='features'),
    path('pricing/',pricing, name='pricing'),
    path('list/',list, name='list'),
    path('profile/',TemplateView.as_view(template_name="profile.html"), name='profile'),
    path('mission/',TemplateView.as_view(template_name="mission.html"), name='mission'),
    path('aboutus/',TemplateView.as_view(template_name="aboutus.html"), name='aboutus'),
    path('team/',TemplateView.as_view(template_name="team.html"), name='team'),
    path('library/', library, name='library'),
    path('order_detail/', order_detail, name='order_detail'),
    path('order_list/',order_list, name='order_list'),
    path('user_history/',user_history, name='user_history'),
    path('submit_bug_comment/',bug_comment, name='bug_comment'),
    path('submit_feature_comment/',feature_comment, name='feature_comment'),
    path('publicise_bug/', publicise_bug, name='publicise_bug'),
    path('view_bug/',view_bugs, name='view_bugs'),
    path('view_feature/',view_features, name='view_features'), 
    path('skills/',skills, name='skills'),
    path('planning/',planning, name='planning'),
    path('datascience/',datascience, name='datascience'),
    path('mobile/',mobile, name='mobile'),
    path('it_solutions/',it_solutions, name='it_solutions'),
    path('publicise_feature/',publicise_features, name='publicise_features')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
