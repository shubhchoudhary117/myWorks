
from django.db import models

# Create your models here.

class ResultDatabase(models.Model):
    Enrollment=models.CharField(max_length=300)
    RegularPrivate=models.CharField(max_length=500)
    Application=models.BigIntegerField()
    RollNo=models.CharField(max_length=500)
    StudentName=models.CharField(max_length=500)
    FatherName=models.CharField(max_length=500)
    MotherName=models.CharField(max_length=500)
    BirthDate=models.CharField(max_length=300)
    Hindi=models.IntegerField()
    English=models.IntegerField()
    Maths=models.IntegerField()
    Science=models.IntegerField()
    SocialScience=models.IntegerField()
    Sanskrite=models.IntegerField()


    
