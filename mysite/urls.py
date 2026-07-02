"""
URL configuration for mysite2026 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import render
from . import views

import socket

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('8.8.8.8', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

def info(request):
    ip = request.META.get('REMOTE_ADDR')
    if ip in ('127.0.0.1', '::1'):
        ip = get_local_ip()
    res_text = f"<h1>Your IP Address is: {ip}</h1><br>"
    for k, v in request.headers.items():
        res_text += f"<p>{k} : {v}</p>"
    return HttpResponse(res_text)

def home(request):
    ip = request.META.get('REMOTE_ADDR')
    if ip in ('127.0.0.1', '::1'):
        ip = get_local_ip()
    return render(request, 'home.html', {'ip': ip})

urlpatterns = [
    path('', home),
    path('info/', info),
    path('admin/', admin.site.urls),
    # Previous task endpoints
    path('info', info),
    path('hello', views.hello_view, name='hello'),
    path('quiz/', include('mysite.vc.urls')),
]
