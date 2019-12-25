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

from HDMS_LOGIN import views
from HDMS_ADMIN import views as v

urlpatterns = [
    path('home/',TemplateView.as_view(template_name="hdms_adminhome.html"),name="Adminhome"),
    path('adddoctor/',TemplateView.as_view(template_name='hdms_adddoctor.html'),name='adddoctor'),
    path('savedoctor/',views.SaveDocter.as_view(),name="savedoctor"),
    path('view_doctor/',views.ViewDoctor.as_view(),name="view_doctor"),
    path('del_doctor/<int:pk>',views.DeleteDoctor.as_view(),name="del_doctor"),
    path('delcancel/',views.DeleteCancel.as_view(),name="delcancel"),
    path('update_doctor/',TemplateView.as_view(template_name="update_doctor.html"),name="update_doctor"),
    path('getupdatedoctor/',views.GetUpdateDoctor.as_view(),name="getupdatedoctor"),
    path('view_doctorlist/',views.ViewDoctorList.as_view(),name="view_doctorlist"),
    path('saveupdtdoctor/',views.SaveupdtDoctor.as_view(),name="saveupdtdoctor"),

    path('addemp/',TemplateView.as_view(template_name="addemp.html"),name="addemp"),
    path('save_emp/',v.SaveEmp.as_view(),name="save_emp"),
    path('view_emp/',v.ViewEmp.as_view(),name="view_emp"),
    path('del_emp/<int:pk>',v.DeleteEmp.as_view(),name="del_emp"),
    path('delcancel_emp/',v.DeleteCancelEmp.as_view(),name="delcancel_emp"),
    path('update_emp/',TemplateView.as_view(template_name="update_emp.html"),name="update_emp"),
    path('getupdate_emp/',v.GetUpdateEmp.as_view(),name="getupdate_emp"),
    path('view_emplist/',v.ViewEmpList.as_view(),name="view_emplist"),
    path('saveupdtemp/',v.SaveupdtEmp.as_view(),name="saveupdtemp"),

    path('addfd/', TemplateView.as_view(template_name="addfd.html"), name="addfd"),
    path('save_fd/', v.SaveFd.as_view(), name="save_fd"),
    path('view_fd/', v.ViewFd.as_view(), name="view_fd"),
    path('del_fd/<int:pk>', v.DeleteFd.as_view(), name="del_fd"),
    path('delcancel_fd/', v.DeleteCancelFd.as_view(), name="delcancel_fd"),
    path('update_fd/', TemplateView.as_view(template_name="update_fd.html"), name="update_fd"),
    path('getupdate_fd/', v.GetUpdateFd.as_view(), name="getupdate_fd"),
    path('view_fdlist/', v.ViewFdList.as_view(), name="view_fdlist"),
    path('saveupdtfd/', v.SaveupdtFd.as_view(), name="saveupdtfd"),

    path('admin_logout/',TemplateView.as_view(template_name="hdms_login.html"),name="admin_logout"),
    path('doctor_logout/',TemplateView.as_view(template_name='hdms_login.html'),name="doctor_logout"),
    path('finance_logout/', TemplateView.as_view(template_name='hdms_login.html'), name="finance_logout"),
    path('emp_logout/', TemplateView.as_view(template_name='hdms_login.html'), name="Emp_logout"),

    path('device_info/',v.Device_Info.as_view(),name="device_info"),
    path('req_issue/',v.Req_Issue.as_view(),name="req_issue"),
    path('forward<int:id>/',v.Forward.as_view(),name="forward"),
    path('sendforward_data/',v.Sendforward_Data.as_view(),name="sendforward_data"),
    path('reject<int:id>/', v.Reject.as_view(), name="reject"),
    path('sendreject_data/', v.Sendreject_Data.as_view(), name="sendreject_data"),


]
