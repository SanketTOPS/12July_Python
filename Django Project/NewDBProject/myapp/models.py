from django.db import models

# Create your models here.

class studinfo(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    city=models.CharField(max_length=20)
    dob=models.DateField()