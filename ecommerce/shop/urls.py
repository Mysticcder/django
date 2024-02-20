from django.urls import path
from . import views

urlpatterns = [

    path('', views.home),
    path('about/', views.about),
    path('location/', views.location),
    path('shop/', views.shop)


]