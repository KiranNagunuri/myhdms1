from django.shortcuts import render,redirect
from django.views.generic import View,ListView,DeleteView,DetailView
from HDMS_LOGIN.models import DocterRegistration
from HDMS_ADMIN.models import Empoyee,FinanceDepartment,Devices,DeviceRequest,Status

class SaveEmp(View):
    def post(self,request):
        eid=request.POST.get("e_id")
        ename=request.POST.get("e_name")
        e_loginname=request.POST.get("e_loginname")
        e_password=request.POST.get("e_password")
        e_doj=request.POST.get("e_joindate")
        e_contact=request.POST.get("e_contact")
        e_email=request.POST.get("e_email")
        type1=request.POST.get("e_type")
        try:
            emp = Empoyee.objects.get(Emp_id=eid)
        except:
            emp=Empoyee(Emp_id=eid,Emp_name=ename,Emp_loginname=e_loginname,Emp_password=e_password,Emp_doj=e_doj,Emp_contact=e_contact,Emp_email=e_email,type=type1)
            emp.save()
            return render(request, "addemp.html", {"msg": "Employee Registration is Success"})
        else:
            return render(request, "addemp.html", {"msg": "Invalid Details"})

class DeleteEmp(DeleteView):
    model = Empoyee
    template_name = "delete_emp.html"
    success_url = "/HDMS_ADMIN/view_emp/"


class DeleteCancelEmp(View):
    def get(self,request):
        emp=Empoyee.objects.all()
        return render(request,"view_emp.html",{"Employee":emp})


class GetUpdateEmp(View):
    def post(self,request):
        idno=request.POST.get("id")
        data=Empoyee.objects.filter(Emp_id=idno)
        return render(request,"Edit_emp.html",{"d":data})

class ViewEmpList(ListView):
    model = Empoyee
    template_name = 'update_emp.html'

class SaveupdtEmp(View):
    def post(self,request):
        eid = request.POST.get("e_id")
        ename = request.POST.get("e_name")
        e_loginname = request.POST.get("e_loginname")
        e_password = request.POST.get("e_password")
        e_doj = request.POST.get("e_joindate")
        e_contact = request.POST.get("e_contact")
        e_email = request.POST.get("e_email")
        type1 = request.POST.get("e_type")
        try:
            emp = Empoyee(Emp_id=eid,Emp_name=ename,Emp_loginname=e_loginname, Emp_password=e_password, Emp_doj=e_doj,Emp_contact=e_contact, Emp_email=e_email, type=type1)
            emp.save()
        except:
            return render(request,"Edit_emp.html",{"msg":"Details already exist(email/contact/login/-any one matched with existing data)"})
        else:
            return render(request, "Edit_emp.html",{"msg": "Employee Updating is Success"})

class ViewEmp(ListView):
    model = Empoyee
    template_name = 'view_emp.html'
    context_object_name = "Employee"


class SaveFd(View):
    def post(self,request):
        fdid=request.POST.get("fd_id")
        fdname=request.POST.get("fd_name")
        fd_loginname=request.POST.get("fd_loginname")
        fd_password=request.POST.get("fd_password")
        fd_doj=request.POST.get("fd_joindate")
        fd_contact=request.POST.get("fd_contact")
        fd_email=request.POST.get("fd_email")
        type1=request.POST.get("fd_type")
        try:
            fd = FinanceDepartment.objects.get(Fd_id=fdid)
        except:
            fd = FinanceDepartment(Fd_id=fdid, Fd_name=fdname, Fd_loginname=fd_loginname, Fd_password=fd_password,Fd_doj=fd_doj, Fd_contact=fd_contact, Fd_email=fd_email, type=type1)
            fd.save()
            return render(request,"addfd.html",{"msg":"Finanace Manager Registration is Success"})
        else:
            return render(request, "addfd.html",{"msg": "invalid details"})


class ViewFd(ListView):
    model = FinanceDepartment
    template_name = 'view_fd.html'
    context_object_name = "Finance"

class DeleteFd(DeleteView):
    model = FinanceDepartment
    template_name = "delete_fd.html"
    success_url = "/HDMS_ADMIN/view_fd/"


class DeleteCancelFd(View):
    def get(self,request):
        fd=FinanceDepartment.objects.all()
        return render(request,"view_fd.html",{"Finance":fd})


class GetUpdateFd(View):
    def post(self,request):
        idno=request.POST.get("id")
        data=FinanceDepartment.objects.filter(Fd_id=idno)
        return render(request,"Edit_fd.html",{"d":data})


class ViewFdList(ListView):
    model = FinanceDepartment
    template_name = 'update_fd.html'


class SaveupdtFd(View):
    def post(self,request):
        fdid = request.POST.get("fd_id")
        fdname = request.POST.get("fd_name")
        fd_loginname = request.POST.get("fd_loginname")
        fd_password = request.POST.get("fd_password")
        fd_doj = request.POST.get("fd_joindate")
        fd_contact = request.POST.get("fd_contact")
        fd_email = request.POST.get("fd_email")
        type1 = request.POST.get("fd_type")
        try:
            fd = FinanceDepartment(Fd_id=fdid,Fd_name=fdname,Fd_loginname=fd_loginname,Fd_password=fd_password,Fd_doj=fd_doj,Fd_contact=fd_contact,Fd_email=fd_email, type=type1)
            fd.save()
        except:
            return render(request,"Edit_fd.html",{"msg":"Details already exist(email/contact/login/-any one matched with existing data)"})
        else:
            return render(request, "Edit_fd.html",{"msg": "Finance_dept Updating is Success"})

class Device_Info(ListView):
    model = Devices
    template_name = "Device_info.html"
    context_object_name = "Devices"

class Req_Issue(View):
    def get(self,request):
        try:
            dr=DeviceRequest.objects.all()
            ds=Devices.objects.all()
        except:
            return render(request,"req_issue.html",{"msg":"NO REQUEST IS AVAILABLE"})
        else:
            return render(request,"req_issue.html",{"dr":dr,"msg":"NO REQUEST IS AVAILABLE"})
class Forward(View):
    def get(self,request,id):
        forward=DeviceRequest.objects.get(DR_ID=id)
        return render(request,"forward_req.html",{"forward":forward})

class Sendforward_Data(View):
    def post(self,request):
        DR_ID=request.POST.get("docreq_id")
        DOCT_ID=request.POST.get("doc_id")
        DOCT_NAME = request.POST.get("doc_name")
        DEVICE_ID=request.POST.get("dev_id")
        DEVICE_NAME = request.POST.get("dev_name")
        STATUS_ID=request.POST.get("status_id")
        try:
            df=DeviceRequest.objects.get(DR_ID=DR_ID,DOCTOR_ID=DOCT_ID,DOCTOR_NAME=DOCT_NAME,DEVICE_ID=DEVICE_ID,DEVICE_NAME=DEVICE_NAME)
        except:
            return render(request,"forward_req.html",{"msg":"invalid data"})
        else:
            df.STATUS_ID=STATUS_ID
            df.save()
            return render(request,"req_issue.html",{"msg":"Request forwarded to Finance department succesfully"})


class Reject(View):
    def get(self,request,id):
        reject=DeviceRequest.objects.get(DR_ID=id)
        return render(request,"reject_req.html",{"reject":reject})


class Sendreject_Data(View):
    def post(self,request):
        DR_ID=request.POST.get("docreq_id")
        DOCT_ID=request.POST.get("doc_id")
        DOCT_NAME = request.POST.get("doc_name")
        DEVICE_ID=request.POST.get("dev_id")
        DEVICE_NAME = request.POST.get("dev_name")
        STATUS_ID=request.POST.get("status_id")
        try:
            df=DeviceRequest.objects.get(DR_ID=DR_ID,DOCTOR_ID=DOCT_ID,DOCTOR_NAME=DOCT_NAME,DEVICE_ID=DEVICE_ID,DEVICE_NAME=DEVICE_NAME)
            df.STATUS_ID=STATUS_ID

        except:
            return render(request,"reject_req.html",{"msg":"invalid data"})
        else:
            df.save()
            return render(request,"reject_req.html",{"msg":"Request forwarded to Finance department succesfully"})
