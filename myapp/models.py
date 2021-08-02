from django.db import models

# Create your models here.
class voters(models.Model):
    name=models.CharField(max_length=50)
    gender=models.CharField(max_length=50,default="no")
    age=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    status=models.CharField(max_length=50,default="no")