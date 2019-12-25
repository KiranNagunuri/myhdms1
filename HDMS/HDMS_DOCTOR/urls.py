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

from HDMS_DOCTOR import views

urlpatterns = [
    path('home/',TemplateView.as_view(template_name="hdms_Doctorhome.html"),name="d_home"),
    path('view_docprofile/',views.View_Docprofile.as_view(),name="view_docprofile"),
    path('update_docprofile/',views.Update_Docprofile.as_view(),name="update_docprofile"),
    path('saveupdtonedoc/',views.SaveupdtoneDoc.as_view(),name="saveupdtonedoc"),
    path('view_alldevices/',views.View_Alldevices.as_view(),name="view_alldevices"),

    path('req_device<int:id>/',views.Req_Device.as_view(),name='req_device'),
    path('savereq/',views.SaveReq.as_view(),name="savereq"),
    path('req_cancel/',TemplateView.as_view(template_name="hdms_Doctorhome.html"),name="req_cancel"),
    path('allocate_dev/',views.Allocate_Dev.as_view(),name="allocate_dev"),
    path('showdev/',views.Showdev.as_view(),name="showdev")


]

