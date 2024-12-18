from django.db import models

class Course(models.Model):
    SEMESTER_CHOICES = [
        ('F', 'Fall'),
        ('W', 'Winter'),
        ('S', 'Summer'),
    ]

    STATUS_CHOICES = [
        ('A', 'Active'),
        ('I', 'Inactive'),
    ]

    name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=10, unique=True)
    enrollment_capacity = models.PositiveIntegerField()
    semesters_offered = models.CharField(max_length=255, choices=SEMESTER_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=15)
    staff_id = models.CharField(max_length=10, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    courses = models.ManyToManyField(Course, limit_choices_to={'status': 'A'})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    student_id = models.CharField(max_length=10, unique=True, primary_key=True)
    password = models.CharField(max_length=255)
    enrollment_date = models.DateField()
    registered_courses = models.ManyToManyField(Course)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    

