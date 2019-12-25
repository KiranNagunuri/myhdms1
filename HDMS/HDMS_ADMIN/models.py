from django.db import models

class Empoyee(models.Model):
    Emp_id=models.IntegerField(primary_key=True)
    Emp_name=models.CharField(max_length=30)
    Emp_loginname=models.CharField(max_length=30,unique=True)
    Emp_password=models.CharField(max_length=30)
    Emp_doj=models.DateField()
    Emp_contact=models.IntegerField(unique=True,default=True)
    Emp_email=models.EmailField(unique=True)
    type=models.CharField(max_length=30)

class FinanceDepartment(models.Model):
    Fd_id = models.IntegerField(primary_key=True)
    Fd_name = models.CharField(max_length=30)
    Fd_loginname = models.CharField(max_length=30, unique=True)
    Fd_password = models.CharField(max_length=30)
    Fd_doj = models.DateField()
    Fd_contact = models.IntegerField(unique=True,)
    Fd_email = models.EmailField(unique=True)
    type = models.CharField(max_length=30)

class Devices(models.Model):
    Device_id=models.IntegerField(primary_key=True)
    Device_name=models.CharField(max_length=30)
    Date_Of_Purchase=models.DateField()
    Cost_Of_Devices=models.FloatField()
    Total_Devices=models.IntegerField()

class DeviceRequest(models.Model):
    DR_ID=models.IntegerField(primary_key=True)
    DEVICE_ID=models.IntegerField()
    DEVICE_NAME=models.CharField(max_length=20,default=False)
    DOCTOR_ID=models.IntegerField()
    DOCTOR_NAME=models.CharField(max_length=20,default=False)
    STATUS_ID=models.IntegerField()

class DoctorDevices(models.Model):
    DD_ID=models.IntegerField(primary_key=True)
    DEVICE_ID=models.IntegerField()
    DEVICE_NAME=models.CharField(max_length=25,default=False)
    DOCTOR_ID=models.IntegerField()
    DOCTOR_NAME = models.CharField(max_length=30,default=False)

class Status(models.Model):
    STATUS_ID=models.IntegerField(primary_key=True)
    STATUS=models.CharField(max_length=30)

