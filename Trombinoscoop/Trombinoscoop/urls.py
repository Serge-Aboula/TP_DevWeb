"""
URL configuration for Trombinoscoop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path

from Trombinoscoop.views import welcome, login, register, add_friend, show_profile

urlpatterns = [
    path('admin/', admin.site.urls),
    path('welcome/', welcome),    
    path('', welcome), # au lieu de login   
    path('login/', login),    
    path('register/', register),    
    path('addFriend/', add_friend),    
    path('showProfile/', show_profile),    
]
