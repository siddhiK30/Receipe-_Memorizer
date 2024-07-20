from django.db import models

# Create your models here.
class Student(models.Model):
    name= models.CharField(max_length=100)
    age=models.IntegerField()


class product(models.Model):
    price=models.IntegerField()

class vegie(models.Model):
    name=models.ImageField()
