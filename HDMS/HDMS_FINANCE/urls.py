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

from HDMS_FINANCE import views

urlpatterns = [
    path('home/',TemplateView.as_view(template_name="hdms_FinDephome.html"),name="finance_home"),
    path('view_fd_profile/',views.ViewProfile.as_view(),name="view_fd_profile"),
    path('update_fd_profile/',views.UpdateProfile.as_view(),name="update_fd_profile"),
    path('saveupdtonefd/',views.SaveProfile.as_view(),name="saveupdtonefd"),
    path('adddevice/',views.AddDevice.as_view(),name="adddevice"),
    path('savedevice/',views.SaveDevice.as_view(),name="savedevice"),
    path('viewdevice/',views.ViewDevice.as_view(),name='viewdevice'),
    path('del_device/<int:pk>',views.DeleteDevice.as_view(),name="del_device"),
    path('delcancel_device/',views.DelCancel_Device.as_view(),name="delcancel_device"),
    path('update_device/',TemplateView.as_view(template_name="update_device.html"),name="update_device"),
    path('getupdate_device/',views.Getupdate_Device.as_view(),name="getupdate_device"),
    path('saveupdtdevice/',views.SaveupdtDevice.as_view(),name="saveupdtdevice"),
    path('view_devicelist/',views.View_DeviceList.as_view(),name="view_devicelist"),
    path('finance_req/',views.Finance_req.as_view(),name="finance_req"),
    path('allowcate<int:id>/',views.DeviceAllowcate.as_view(),name="allowcate"),
    path('save_allocate_device/', views.Save_Allocate.as_view(), name="save_allocate_device"),


]
