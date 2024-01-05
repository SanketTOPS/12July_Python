from django.shortcuts import render,redirect
from .forms import *
from django.core.mail import send_mail
import random
from OTPVerifyapp import settings



def index(request):
    return render(request,'index.html')

otp=random.randint(1111,9999) #global
def newuser(request):
    if request.method=='POST':
        user=signupForm(request.POST)
        if user.is_valid():
            user.save()
            print("Signup Successfully!")

            #Email Sending OTP
            global otp
            sub="Your One Time Password!"
            msg=f"\nDear User\n\nThank for register with us!\nYour one time password is {otp}.\n\nThanks & Regards!\nTOPS Tech\n+91 9724799469 | www.tops-int.com"
            from_id=settings.EMAIL_HOST_USER
            to_id=[request.POST['username']]

            send_mail(subject=sub,message=msg,from_email=from_id,recipient_list=to_id)
            return redirect('otpverify')
        else:
            print(user.errors)
    return render(request,'newuser.html')

def home(request):
    return render(request,'home.html')

def otpverify(request):
    global otp
    if request.method=='POST':
        if request.POST['otp']==str(otp):
            return redirect('/')
        else:
            print("Error! Invalid OTP")
    return render(request,'otpverify.html')