from django.shortcuts import render,redirect
from .forms import signupForm
from .models import usersignup
from django.contrib.auth import logout

# Create your views here.
def index(request):
    user=request.session.get('user')
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
            fnm=usersignup.objects.get(username=unm)
            uid=usersignup.objects.get(username=unm)
            print("Firstname:",fnm.firstname)
            print("Current UID:",uid.id)
            if user:
                print("Login successfully!")
                #request.session['user']=unm
                request.session['user']=fnm.firstname
                request.session['uid']=uid.id
                return redirect('notes')
            else:
                print("Error!Login fail.....Try again")
    return render(request,'index.html',{'user':user})

def notes(request):
    user=request.session.get('user')
    return render(request,'notes.html',{'user':user})

def profile(request):
    user=request.session.get('user')
    uid=request.session.get('uid')
    cuser=usersignup.objects.get(id=uid)
    if request.method=='POST':
        updateuser=signupForm(request.POST,instance=cuser)
        if updateuser.is_valid():
            #updateuser=signupForm(request.POST,instance=cuser)
            updateuser.save()
            return redirect('notes')
            print("Profile updated!")
        else:
            print(updateuser.errors)
    return render(request,'profile.html',{'user':user,'cuser':cuser})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def userlogout(request):
    logout(request)
    return redirect('/')