from django.db import models

class StudentData(models.Model):
    URN = models.CharField(max_length=17, primary_key=True)
    First_Name = models.CharField(max_length=45)
    Middle_Name = models.CharField(max_length=45, null=True)
    Last_Name = models.CharField(max_length=45)
    Mother_name = models.CharField(max_length=45, null=True)
    Gender = models.CharField(max_length=45)
    DOB = models.DateField()
    Local_Address = models.CharField(max_length=225)
    Permanent_Address = models.CharField(max_length=225)
    Email = models.CharField(max_length=30)
    Student_Phone_No = models.IntegerField()
    Emergency_Phone = models.IntegerField()
