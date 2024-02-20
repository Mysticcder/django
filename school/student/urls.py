from django.urls import path
from . import views

urlpatterns = [
    path('', views.about),
    path('location/', views.location),
    path('fee-structure', views.fee_structure)
]