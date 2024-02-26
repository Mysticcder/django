from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def inner(request):
    return render(request, 'inner-page.html')

def portfolio(request):
    return render(request, 'portfolio-details.html')