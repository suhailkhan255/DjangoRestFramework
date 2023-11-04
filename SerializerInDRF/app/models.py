from django.db import models

# Create your models here.



class Student(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField()
    city = models.CharField(max_length=20)

class Employee(models.Model):
    name = models.CharField(max_length=20)
    empId = models.IntegerField()
    city = models.CharField(max_length=20)

class Car(models.Model):
    modelNumber = models.CharField(max_length=20)
    brand = models.CharField(max_length=20)
    prize =models.IntegerField(max_length=20)