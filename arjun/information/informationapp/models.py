from django.db import models


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=10)
    age = models.IntegerField()
    address = models.TextField()
    designation = models.CharField(max_length=10)
    salary = models.DecimalField(decimal_places=2, max_digits=10)

