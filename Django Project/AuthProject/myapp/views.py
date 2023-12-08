from django.shortcuts import render,redirect
from .forms import *
from .models import *
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    if request.method=='POST':
        unm=request.POST['username']
        pas=request.POST['password']

        user=signupdata.objects.filter(username=unm,password=pas)
        if user: #TRUE
            print("Login Successfull!")
            request.session['user']=unm #create a session
            return redirect('home')
        else:
            print("Error! Login Faild....")
    return render(request,'index.html')

def usersignup(request):
    if request.method=='POST':
        newuser=signupForm(request.POST)
        if newuser.is_valid():
            newuser.save()
            print("Signup Successfully!")
            return redirect('/')
        else:
            print(newuser.errors)
    return render(request,'usersignup.html')

#@login_required(login_url='/')
def home(request):
    data=request.session.get('user')
    return render(request,'home.html',{'data':data})

def userlogout(request):
    logout(request)
    return redirect('/')
