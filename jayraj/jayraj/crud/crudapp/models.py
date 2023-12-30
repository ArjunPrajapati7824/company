from django.db import models


# Create your models here.

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.IntegerField()
    salary = models.DecimalField(max_digits=10, decimal_places=2)
