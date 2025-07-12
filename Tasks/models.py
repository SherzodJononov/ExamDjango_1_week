from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.CharField()
    phone = models.CharField(max_length=15)
    
class Task(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField()
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)

