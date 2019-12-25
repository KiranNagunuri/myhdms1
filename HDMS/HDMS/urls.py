"""HDMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,include
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',TemplateView.as_view(template_name="hdms_home.html")),
    path('login/',TemplateView.as_view(template_name="hdms_login.html"),name="login"),
    path('home/', TemplateView.as_view(template_name="hdms_home.html"), name="home"),
    path('about_us/',TemplateView.as_view(template_name="hdms_about.html"),name="about_us"),
    path('contact/',TemplateView.as_view(template_name="hdms_contact.html"),name="contact"),


    path('HDMS_LOGIN/',include('HDMS_LOGIN.urls')),
    path('HDMS_ADMIN/',include('HDMS_ADMIN.urls')),
    path('HDMS_DOCTOR/',include('HDMS_DOCTOR.urls')),
    path('HDMS_EMPLOYEE/',include('HDMS_EMPLOYEE.urls')),
    path('HDMS_FINANCE/',include('HDMS_FINANCE.urls')),

]
