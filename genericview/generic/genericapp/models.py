from django.db import models

# Create your models here.
from django.db import models

class Employee(models.Model):
    name=models.CharField(max_length=10)
    address=models.TextField()
    number=models.IntegerField()
    salary=models.DecimalField(max_digits=10,decimal_places=2)



