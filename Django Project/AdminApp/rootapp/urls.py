from django.contrib import admin
from django.urls import path,include
from rootapp import views

urlpatterns = [
   path('',views.home),
]
