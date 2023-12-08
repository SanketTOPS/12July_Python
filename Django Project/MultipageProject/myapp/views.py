from django.shortcuts import render
import random

# Create your views here.

def index(request):
    name='Hitesh' #static
    #num=random.randint(1111,9999)
    return render(request,'index.html',{'nm':name,'num':random.randint(1111,9999)})

n=1
def about(request):
    global n
    n+=1
    return render(request,'about.html',{'n':n})

def contact(request):
    return render(request,'contact.html')