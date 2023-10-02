from django.db import models

class StudentData(models.Model):
    
    PHYSICAL_HANDICAP_CHOICES = [
        ("Y", "YES"),
        ("N", "NO")
    ]
    
    CATEGORY_CHOICES = [
        ("GEN", "GENERAL"),
        ("OBC", "OBC"),
        ("SC", "SC"),
        ("ST", "ST"),
        ("EWS", "EWS")
    ]
    
    BLOOD_GROUP_CHOICES = [
        ("O+", "O POSITIVE"),
        ("O-", "O NEGATIVE"),
        ("A+", "A POSITIVE"),
        ("A-", "A NEGATIVE"),
        ("B+", "B POSITIVE"),
        ("B-", "B NEGATIVE"),
        ("AB+", "AB POSITIVE"),
        ("AB-", "AB NEGATIVE"),
        ("BOM", "BOMBAY")
    ]
    
    RELIGION_CHOICES = [
        ("HI", "HINDU"),
        ("MU", "MUSLIM"),
        ("CH", "CHRISTIAN"),
        ("SI", "SIKH"),
        ("PA", "PARSI"),
        ("JE", "JEWISH"),
        ("BU", "BUDDHIST"),
        ("TA", "TAOIST"),
        ("OT", "OTHER")
    ]
    
    STUDENT_STATUS_CHOICES = [
        ("Y", "ACTIVE"),
        ("N", "INACTIVE")
    ]
    
    EDUATION_LOAN_CHOICES = [
        ("Y", "YES"),
        ("N", "NO")
    ]
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
    Aadhar_Card_No = models.IntegerField()
    Physical_Handicap = models.e
