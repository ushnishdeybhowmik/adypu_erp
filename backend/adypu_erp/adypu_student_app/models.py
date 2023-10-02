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
        ("ACTIVE", "ACTIVE"),
        ("INACTIVE", "INACTIVE")
    ]
    
    EDUCATION_LOAN_CHOICES = [
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
    Physical_Handicap = models.CharField(choices=PHYSICAL_HANDICAP_CHOICES, max_length=1)
    Category = models.CharField(choices=CATEGORY_CHOICES, max_length=3)
    Blood_Group = models.CharField(choices=BLOOD_GROUP_CHOICES, max_length=3)
    Religion = models.CharField(choices=RELIGION_CHOICES, max_length=2, null=True)
    Nationality = models.CharField(max_length=45)
    State_And_City = models.CharField(max_length=45)
    Student_Status = models.CharField(choices=STUDENT_STATUS_CHOICES, max_length=8)
    Academic_Year = models.IntegerField()
    Program = models.CharField(max_length=45)
    Course = models.CharField(max_length=45)
    Semester = models.IntegerField()
    Father_Occupation = models.CharField(max_length=45)
    Father_Phone_No = models.IntegerField()
    Father_Email_ID = models.CharField(max_length=225)
    Mother_Phone_No = models.IntegerField(null=True)
    Family_Income = models.IntegerField()
    Education_Loan_Availed = models.CharField(choices=EDUCATION_LOAN_CHOICES, max_length=1)
    Photo = models.ImageField()
    
    def __str__(self):
        return self.URN
