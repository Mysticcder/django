from django.shortcuts import render
from django.http import HttpResponse
from . models import Student
from . models import Teacher
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')

def student(request):
    student = Student.objects.all()
    return render(request, 'students.html', {"student": student})

def teacher(request):
    teacher = Teacher.objects.all()
    return render(request, 'teachers.html', {"teacher": teacher})