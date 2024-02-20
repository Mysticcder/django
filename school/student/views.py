from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request, 'about.html')

def fee_structure(request):
    return render(request, 'fee structure.html')

def location(request):
    return render(request, 'location.html')