from django.shortcuts import render
from .forms import signupForm
from .models import usersignup

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
            else:
                print("Error!Login fail.....Try again")
    return render(request,'index.html')

def notes(request):
    return render(request,'notes.html')

def profile(request):
    return render(request,'profile.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')