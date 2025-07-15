from django.db import models
from datetime import datetime
# Create your models here.

class Student(models.Model):
    fullname = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    email = models.CharField(max_length=50)
    image = models.ImageField(upload_to=True)
    created_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.fullname    

class IdCard(models.Model):
    student = models.OneToOneField('Tasks.Student',on_delete=models.CASCADE)
    name_of_card = models.CharField(default='null')
    number_of_card = models.CharField(max_length=20)
    

class Task(models.Model):
    student = models.ForeignKey('Tasks.Student',on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

class Course(models.Model):
    student = models.ManyToManyField('Tasks.Student')
    course_name = models.CharField(max_length=100,null=True)
    courser_price = models.IntegerField(default=1000)
    registration_date = models.DateTimeField(default=datetime.now())
    created_at = models.DateTimeField(auto_now=True)


