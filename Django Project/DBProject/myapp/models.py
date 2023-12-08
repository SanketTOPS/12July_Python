from django.db import models

# Create your models here.

class userinfo(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    email=models.EmailField()
    mobile=models.BigIntegerField()
    dob=models.DateField()
    address=models.TextField()

class usersignup(models.Model):
    created=models.DateTimeField(auto_now_add=True)
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    username=models.EmailField()
    password=models.CharField(max_length=12)
    city=models.CharField(max_length=30)
    mobile=models.BigIntegerField()
   


 