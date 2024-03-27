from django.db import models

# Create your models here.
class studentdetail(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    joiningdate=models.CharField(max_length=50,null=True)
    duration=models.CharField(max_length=50)
    rollno=models.IntegerField()

class attendance(models.Model):
    date=models.CharField(max_length=50)
    topic=models.CharField(max_length=50)
    intime=models.CharField(max_length=50)
    outtime=models.CharField(max_length=50)
    feedback=models.CharField(max_length=50) 
    