from django.contrib import admin
from . models import Student
from . models import Teacher
from . models import School

# Register your models here.

admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(School)
