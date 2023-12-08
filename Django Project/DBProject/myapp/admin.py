from django.contrib import admin
from .models import *


# Register your models here.

class userData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','email','dob']

class signupData(admin.ModelAdmin):
    ordering=['id']
    list_display=['id','firstname','lastname','username','city','mobile']

admin.site.register(userinfo,userData)
admin.site.register(usersignup,signupData)