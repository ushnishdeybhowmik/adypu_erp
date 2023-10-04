from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.get_all_students),
    path('students/<slug:pk>/', views.student_detail),
    path('students/add/', views.create_student),
]