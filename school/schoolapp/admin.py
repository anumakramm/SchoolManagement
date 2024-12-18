from django.contrib import admin
from django.db import models
from .models import Course, Teacher, Student

admin.site.register(Course) 
admin.site.register(Teacher) 
admin.site.register(Student)