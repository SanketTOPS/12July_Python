from django.shortcuts import render,redirect
from .forms import *
from .models import *

# Create your views here.
def index(request):
    if request.method=='POST':
        newstud=studinfoForm(request.POST)
        if newstud.is_valid(): #true
            newstud.save()
            print("Your data has been saved!")
        else:
            print(newstud.errors)
    return render(request,'index.html')


def showdata(request):
    data=studinfo.objects.all()
    return render(request,'showdata.html',{'data':data})

def updatedata(request,id):
    stid=studinfo.objects.get(id=id)
    if request.method=='POST':
        newstud=updateForm(request.POST,instance=stid)
        if newstud.is_valid(): #true
            newstud.save()
            print("Your data has been updated!")
            return redirect('showdata')
        else:
            print(newstud.errors)
    return render(request,'updatedata.html',{'stid':stid})

def deletedata(request,id):
    stid=studinfo.objects.get(id=id)
    studinfo.delete(stid)
    return redirect('showdata')