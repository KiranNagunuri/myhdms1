from django.db import models

class Login(models.Model):
    uname=models.CharField(max_length=30,primary_key=True)
    password=models.CharField(max_length=30)
    type=models.CharField(max_length=30)
class DocterRegistration(models.Model):
    Doctor_id=models.IntegerField(primary_key=True)
    Doctor_name=models.CharField(max_length=30)
    Login_name=models.CharField(max_length=30,unique=True)
    password=models.CharField(max_length=30,unique=True)
    Designation=models.CharField(max_length=30)
    Date_of_joining=models.DateField()
    Contact=models.IntegerField(unique=True)
    Email=models.EmailField(unique=True)
    type=models.CharField(max_length=30,default=False)