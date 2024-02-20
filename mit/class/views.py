from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to my home page")

def about(request):
    return HttpResponse("This is all about me")

def contact(request):
    return HttpResponse("Drop a line @...,,,")

def email(request):
    return HttpResponse("info@gmail.com")
