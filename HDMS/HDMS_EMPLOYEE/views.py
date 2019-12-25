from django.shortcuts import render
from django.views.generic import View,ListView

from HDMS_ADMIN.models import Empoyee,Devices

# Create your views here.
class View_empProfile(View):
    def get(self,request):
        ds=request.session["uname"]
        data=Empoyee.objects.get(Emp_loginname=ds)
        return render(request,"view_oneemp.html",{"data":data})

class Update_Empprofile(View):
    def get(self,request):
        ds=request.session["uname"]
        data=Empoyee.objects.filter(Emp_loginname=ds)
        return render(request,"update_oneemp.html",{"data":data})

class SaveupdtoneEmp(View):
        def post(self, request):
            eid = request.POST.get("e_id")
            ename = request.POST.get("e_name")
            e_loginname = request.POST.get("e_loginname")
            e_password = request.POST.get("e_password")
            e_doj = request.POST.get("e_joindate")
            e_contact = request.POST.get("e_contact")
            e_email = request.POST.get("e_email")
            type1 = request.POST.get("e_type")
            try:
                e = Empoyee(Emp_id=eid,Emp_name=ename,Emp_loginname=e_loginname,Emp_password=e_password,Emp_doj=e_doj,Emp_contact=e_contact,Emp_email=e_email,type=type1)
                e.save()
            except:
                return render(request, "update_oneemp.html",
                              {"msg": "Details already exist(email/contact/login/-any one matched with existing data)"})
            else:
                return render(request, "update_oneemp.html", {"msg": "Profile Updating is Success"})


class View_Alldevices(ListView):
    model = Devices
    template_name = "viewemp_alldevices.html"
    context_object_name = "Devices"
