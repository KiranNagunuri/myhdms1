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
from django.urls import path
from django.views.generic import TemplateView

from HDMS_EMPLOYEE import views

urlpatterns = [
    path('home/',TemplateView.as_view(template_name="hdms_Emphome.html"),name="emp_home"),
    path('view_empprof/',views.View_empProfile.as_view(),name="view_empprof"),
    path('update_empprofile/',views.Update_Empprofile.as_view(),name="update_empprofile"),
    path('saveupdtoneemp/',views.SaveupdtoneEmp.as_view(),name="saveupdtoneemp"),
    path('view_alldevices/',views.View_Alldevices.as_view(),name="viewemp_alldevices"),

]
