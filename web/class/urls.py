from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('inner/', views.inner),
    path('portfolio/', views.portfolio),
    path('student/', views.student),
    path('teacher/', views.teacher)

]