from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        dob=request.POST['dob']
        mob=request.POST['mobile']
        add=request.POST['address']
        userinfo.objects.create(firstname=fnm,lastname=lnm,email=email,dob=dob,mobile=mob,address=add)
        print("Your data has been inserted!")
    else:
        print("Error!Something went wrong...")
    return render(request,'index.html')


def showdata(request):
    data=userinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=userinfo.objects.get(id=id)
    if request.method=='POST':
        fnm=request.POST['firstname']
        lnm=request.POST['lastname']
        email=request.POST['email']
        dob=request.POST['dob']
        mob=request.POST['mobile']
        add=request.POST['address']
        userinfo.objects.filter(id=id).update(firstname=fnm,lastname=lnm,email=email,dob=dob,mobile=mob)
        return redirect('showdata')
    else:
        print("Error!Something went wrong...Try again!")
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=userinfo.objects.get(id=id)
    userinfo.delete(stid)
    return redirect('showdata')
    


