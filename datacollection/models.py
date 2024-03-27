from django.db import models

# Create your models here.
class studentdetail(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    joiningdate=models.DateField()
    duration=models.CharField(max_length=50)
    rollno=models.IntegerField()

class attendance(models.Model):
    date=models.DateField()
    topic=models.CharField(max_length=50)
    intime=models.TimeField()
    outtime=models.TimeField()
    feedback=models.CharField(max_length=50) 
    