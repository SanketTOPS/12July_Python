from django.contrib import admin
from django.urls import path,include
from myapp import views

urlpatterns = [
    path('',views.index),
    path('newuser/',views.newuser),
    path('home/',views.home),
    path('otpverify/',views.otpverify,name="otpverify"),
]