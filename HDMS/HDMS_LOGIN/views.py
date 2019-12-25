from django.shortcuts import render, redirect
from HDMS_LOGIN.models import Login,DocterRegistration
from HDMS_ADMIN.models import Empoyee,FinanceDepartment
from django.views.generic import View, ListView,DeleteView,UpdateView

class LoginChek(View):
    def post(self,request):
        uname=request.POST.get("username")
        password=request.POST.get("password")
        type1=request.POST.get("usertype")
        if type1=="Administrator":
            try:
                Login.objects.get(uname=uname,password=password,type=type1)
            except:
                return render(request,"hdms_login.html",{"data":"inavalid details"})
            else:
                request.session["uname"] = uname
                return render(request,"hdms_adminhome.html")
        if type1=="Doctor":
            try:
                DocterRegistration.objects.get(Login_name=uname,password=password,type=type1)
            except:
                return render(request,"hdms_login.html",{"data":"inavalid details"})
            else:
                request.session["uname"] = uname
                return render(request,"hdms_Doctorhome.html")
        if type1=="Employee":
            try:
                Empoyee.objects.get(Emp_loginname=uname,Emp_password=password,type=type1)
            except :
                return render(request,"hdms_login.html",{"data":"invalid details"})
            else:
                request.session["uname"] = uname
                return render(request,"hdms_Emphome.html")
        if type1=="Finance Department":
            try:
                FinanceDepartment.objects.get(Fd_loginname=uname,Fd_password=password,type=type1)
            except:
                return render(request,"hdms_login.html",{"data":"invalid details"})
            else:
                request.session["uname"] = uname
                return render(request,"hdms_FinDephome.html")

class SaveDocter(View):
    def post(self,request):
        didno=request.POST.get("d_id")
        dname=request.POST.get("d_name")
        dlog=request.POST.get("d_loginname")
        dpass=request.POST.get("d_password")
        ddeg=request.POST.get("d_deg")
        djoin=request.POST.get("d_joindate")
        dcont=request.POST.get("d_contact")
        demail=request.POST.get("d_email")
        type2=request.POST.get("d_type")
        try:
            dr = DocterRegistration.objects.get(Doctor_id=didno)
        except:
            dr = DocterRegistration(Doctor_id=didno, Doctor_name=dname, Designation=ddeg, Login_name=dlog,password=dpass, Date_of_joining=djoin, Contact=dcont, Email=demail, type=type2)
            dr.save()
            return render(request, "hdms_adddoctor.html", {"msg": "Doctor Registration is Success"})
        else:
            return render(request, "hdms_adddoctor.html", {"msg": "Invalid Details"})



class ViewDoctor(ListView):
    model = DocterRegistration
    template_name = 'viewdoctors.html'
    context_object_name = "Doctors"

class DeleteDoctor(DeleteView):
    model = DocterRegistration
    template_name = "deleteDoctor.html"
    success_url = "/HDMS_ADMIN/view_doctor/"


class DeleteCancel(View):
    def get(self,request):
        Doctors=DocterRegistration.objects.all()
        return render(request,"viewdoctors.html",{"Doctors":Doctors})


class GetUpdateDoctor(View):
    def post(self,request):
        idno=request.POST.get("id")
        data=DocterRegistration.objects.filter(Doctor_id=idno)
        return render(request,"Edit_doctor.html",{"d":data})

class ViewDoctorList(ListView):
    model = DocterRegistration
    template_name = 'update_doctor.html'

class SaveupdtDoctor(View):
    def post(self,request):
        didno=request.POST.get("d_id")
        dname=request.POST.get("d_name")
        dlog=request.POST.get("d_loginname")
        dpass=request.POST.get("d_password")
        ddeg=request.POST.get("d_deg")
        djoin=request.POST.get("d_joindate")
        dcont=request.POST.get("d_contact")
        demail=request.POST.get("d_email")
        type2=request.POST.get("d_type")
        try:
            dr=DocterRegistration(Doctor_id=didno,Doctor_name=dname,Designation=ddeg,Login_name=dlog,password=dpass,Date_of_joining=djoin,Contact=dcont,Email=demail,type=type2)
            dr.save()
        except:
            return render(request,"Edit_doctor.html",{"msg":"Details already exist(email/contact/login/password/-any one matched with existing data)"})
        else:

            return render(request, "Edit_doctor.html",{"msg": "Doctor Updating is Success"})


