from django.shortcuts import render
from django.views.generic import View,ListView,DeleteView
from  HDMS_ADMIN.models import FinanceDepartment,Devices,DeviceRequest,Status,DoctorDevices
from HDMS_LOGIN.models import DocterRegistration
# Create your views here.
class ViewProfile(View):
    def get(self,request):
        un=request.session["uname"]
        result=FinanceDepartment.objects.get(Fd_loginname=un)
        return render(request,"view_onefd.html",{"data":result})

class UpdateProfile(View):
    def get(self,request):
        un=request.session["uname"]
        result = FinanceDepartment.objects.filter(Fd_loginname=un)
        return render(request, "update_onefd.html", {"data": result})

class SaveProfile(View):
    def post(self,request):
        fdid = request.POST.get("fd_id")
        fdname = request.POST.get("fd_name")
        fd_loginname = request.POST.get("fd_loginname")
        fd_password = request.POST.get("fd_password")
        fd_doj = request.POST.get("fd_joindate")
        fd_contact = request.POST.get("fd_contact")
        fd_email = request.POST.get("fd_email")
        type1=request.POST.get("fd_type")
        try:
            fd = FinanceDepartment(Fd_id=fdid, Fd_name=fdname, Fd_loginname=fd_loginname, Fd_password=fd_password,Fd_doj=fd_doj, Fd_contact=fd_contact, Fd_email=fd_email,type=type1)
            fd.save()
        except:
            return render(request, "update_onefd.html",{"msg": "Details already exist(email/contact/login/-any one matched with existing data)"})
        else:
            return render(request, "update_onefd.html", {"msg": "Profile Updating is Success"})

class AddDevice(View):
    def get(self,request):
        return render(request,"add_device.html")

class SaveDevice(View):
    def post(self,request):
        device_id = request.POST.get("device_id")
        device_name = request.POST.get("device_name")
        date_of_purchase = request.POST.get("device_dop")
        cost_of_device = request.POST.get("device_cost")
        total_devices = request.POST.get("devices_total")
        try:
            ad=Devices(Device_id=device_id,Device_name=device_name,Date_Of_Purchase=date_of_purchase,Cost_Of_Devices=cost_of_device,Total_Devices=total_devices)
            ad.save()
        except:
            return render(request,"add_device.html",{"msg":"Device id alredy exit"})
        else:
            return render(request,"add_device.html",{"msg":"Device is succesfully added"})


class ViewDevice(ListView):
    model = Devices
    template_name = "view_devices.html"
    context_object_name = "Devices"


class DeleteDevice(DeleteView):
        model = Devices
        template_name = "delete_device.html"
        success_url = "/HDMS_FINANCE/viewdevice/"

class DelCancel_Device(View):
    def get(self,request):
        all_d=Devices.objects.all()
        return render(request,"view_devices.html",{"Devices":all_d})

class Getupdate_Device(View):
    def post(self,request):
        idno=request.POST.get("id")
        data=Devices.objects.filter(Device_id=idno)
        return render(request,"Edit_device.html",{"d":data})

class SaveupdtDevice(View):
    def post(self, request):
        deviceid = request.POST.get("device_id")
        devicename = request.POST.get("device_name")
        device_dop = request.POST.get("date_of_purchase")
        devicecost = request.POST.get("device_cost")
        totaldevices = request.POST.get("total_devices")

        try:
            d = Devices(Device_id=deviceid,Device_name=devicename,Date_Of_Purchase=device_dop,Cost_Of_Devices=devicecost,Total_Devices=totaldevices)
            d.save()
        except:
            return render(request, "Edit_device.html",{"msg": "invalid data"})
        else:
            return render(request, "Edit_device.html",{"msg": "Device Updating is Success"})


class View_DeviceList(ListView):
    model = Devices
    template_name = 'update_device.html'

class Finance_req(View):
    def get(self,request):
        try:

            d=DeviceRequest.objects.all()
        except:
            return render(request,"finance_reqissue.html",{"msg": "NO REQUEST IS AVAILABLE"})
        else:
            return render(request, "finance_reqissue.html",{"ddr":d})


class DeviceAllowcate(View):
    def get(self,request,id):
        allocate=DeviceRequest.objects.get(DR_ID=id)
        return render(request,"device_allocate.html",{"allocate":allocate})


class Save_Allocate(View):
    def post(self,request):
        DD_ID=request.POST.get("allocate_id")
        DOCT_ID=request.POST.get("doc_id")
        DOCT_NAME = request.POST.get("doc_name")
        DEVICE_ID=request.POST.get("dev_id")
        DEVICE_NAME = request.POST.get("dev_name")
        STATUS_IDNO=request.POST.get("status_id")
        print(STATUS_IDNO)
        try:
            d=DoctorDevices(DOCTOR_ID=DOCT_ID,DEVICE_ID=DEVICE_ID,DD_ID=DD_ID,DOCTOR_NAME=DOCT_NAME,DEVICE_NAME=DEVICE_NAME)
            d.save()
            td = Devices.objects.all()
            if td:
                for x in td:
                    total=int(x.Total_Devices)
                count2=total-1
                c=Devices.objects.get(Device_id=DEVICE_ID)
                if count2>=0:
                    c.Total_Devices=count2
                    c.save()
                dd = DeviceRequest.objects.get(DR_ID=DD_ID)
                dd.STATUS_ID = STATUS_IDNO
                dd.save()

        except:
            return render(request,"finance_reqissue.html",{"msg":"invalid data"})
        else:

            return render(request,"finance_reqissue.html",{"msg":"Device Allocated succesfully"})