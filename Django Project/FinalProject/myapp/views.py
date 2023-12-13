from django.shortcuts import render,redirect
from .forms import signupForm
from .models import usersignup
from django.contrib.auth import logout

# Create your views here.
def index(request):
    if request.method=='POST': #root
        if request.POST.get('signup')=='signup': #signup
            newuser=signupForm(request.POST)
            if newuser.is_valid():
                newuser.save()
                print("Signup Successfully!")
            else:
                print(newuser.errors)

        elif request.POST.get('login')=='login': #login

            unm=request.POST['username']
            pas=request.POST['password']

            user=usersignup.objects.filter(username=unm,password=pas)
            if user:
                print("Login successfully!")
                request.session['user']=unm
                return redirect('notes')
            else:
                print("Error!Login fail.....Try again")
    return render(request,'index.html')

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    return render(request,'profile.html',{'user':user})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')