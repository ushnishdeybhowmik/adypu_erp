from rest_framework import serializers
from .models import StudentData


class StudentDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentData
        fields = ['URN', 'First_Name', 'Middle_Name', 'Last_Name', 'Mother_name', 'Gender',
                  'DOB', 'Local_Address', 'Permanent_Address', 'Email', 'Student_Phone_No', 'Emergency_Phone',
                  'Aadhar_Card_No', 'Physical_Handicap', 'Category', 'Blood_Group', 'Religion', 'Nationality', 'State_And_City',
                  'Student_Status', 'Academic Year', 'Program', 'Course']