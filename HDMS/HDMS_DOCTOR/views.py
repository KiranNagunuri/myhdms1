from django.shortcuts import render

# Create your views here.
from django.views.generic import View,ListView,DetailView

from HDMS_ADMIN.models import Devices,DeviceRequest,Status,DoctorDevices
from HDMS_LOGIN.models import DocterRegistration

class View_Docprofile(View):
    def get(self,request):
        ds=request.session["uname"]
        data=DocterRegistration.objects.get(Login_name=ds)
        return render(request,"view_onedoc.html",{"data":data})

class Update_Docprofile(View):
    def get(self,request):
        ds=request.session["uname"]
        data=DocterRegistration.objects.filter(Login_name=ds)
        return render(request,"update_onedoc.html",{"data":data})

class SaveupdtoneDoc(View):
        def post(self, request):
            did = request.POST.get("d_id")
            dname = request.POST.get("d_name")
            ddeg = request.POST.get("d_deg")
            d_loginname = request.POST.get("d_loginname")
            d_password = request.POST.get("d_password")
            d_doj = request.POST.get("d_joindate")
            d_contact = request.POST.get("d_contact")
            d_email = request.POST.get("d_email")
            type1 = request.POST.get("d_type")
            try:
                dr = DocterRegistration(Doctor_id=did,Doctor_name=dname,Designation=ddeg,Date_of_joining=d_doj,Contact=d_contact,Login_name=d_loginname,password=d_password,Email=d_email,type=type1)
                dr.save()
            except:
                return render(request, "update_onedoc.html",{"msg": "Details already exist(email/contact/login/-any one matched with existing data)"})
            else:
                return render(request, "update_onedoc.html", {"msg": "Profile Updating is Success"})


class View_Alldevices(ListView):
    model = Devices
    template_name = "viewdoc_alldevices.html"
    context_object_name = "Devices"


class Req_Device(View):
    def get(self,request,id):
        did=Devices.objects.get(Device_id=id)
        return render(request,"docreq_issues.html",{"did":did})

class SaveReq(View):
    def post(self,request):
        DR_ID=request.POST.get("drid")
        DEV_ID=request.POST.get("device_id")
        DEV_NAME=request.POST.get("device_name")
        status = request.POST.get("status")
        di = request.session["uname"]
        d = DocterRegistration.objects.get(Login_name=di)
        Doct_name=d.Doctor_name
        DOCT_ID = d.Doctor_id
        try:
            dr = DeviceRequest(DR_ID=DR_ID,DOCTOR_ID=DOCT_ID,DOCTOR_NAME=Doct_name,DEVICE_ID=DEV_ID,DEVICE_NAME=DEV_NAME, STATUS_ID=status)
        except:
            return render(request, "hdms_Doctorhome.html", {"msg": "INVALID DATA"})
        else:
            dr.save()
            return render(request, "hdms_Doctorhome.html", {"msg": "REQUEST SEND TO ADMIN"})


class Allocate_Dev(View):
    def get(self,request):
        ses=request.session["uname"]
        try:
            dr1=DocterRegistration.objects.get(Login_name=ses)
            dr2=dr1.Doctor_id
            dr= DoctorDevices.objects.get(DOCTOR_ID=dr2)

        except:
            return render(request, "docallocated_dev.html", {"mg": "No device is Allocate"})
        else:
            return render(request, "docallocated_dev.html",{"dd":dr})


class Showdev(DetailView):
    def post(self,request):
        id=request.POST.get("doc_id")
        try:
            d=DoctorDevices.objects.filter(DOCTOR_ID=id)

        except:
            return render(request, "docallocated_dev.html", {"msg": "No device is Allocate"})
        else:
            return render(request,"docallocated_dev.html",{"d":d})