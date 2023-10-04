from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import StudentData
from .serializers import StudentDataSerializer

@csrf_exempt
def get_all_students(request):
    if request.method == 'GET':
        students = StudentData.objects.all()
        students_serializer = StudentDataSerializer(students, many = True)
        return JsonResponse(students_serializer.data, safe=False)
    
@csrf_exempt
def student_detail(request, pk):
    """
    Retrieve, update or delete a student.
    """
    try:
        student = StudentData.objects.get(pk=pk)
    except StudentData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = StudentDataSerializer(student)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = StudentDataSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        student.delete()
        return HttpResponse(status=204)
    
@csrf_exempt

def create_student(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        student = StudentData()
        serializer = StudentDataSerializer(student, data=data)
        if serializer.is_valid():
            serializer.save()
            return HttpResponse(status=200)