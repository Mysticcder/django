from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='home'),
    path('location/', views.location, name='location'),
    path('fee-structure', views.fee_structure, name='fee-structure')
]