from django.shortcuts import render
from .forms import regForm
import random
from django.http import HttpResponse
from .models import registration
from django.contrib.auth.models import User
from django.core.mail import EmailMessage

def regView(request):
    form = regForm()
    if request.method == 'POST':
        form = regForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            return render(request,'index.html',{'form':form,'m':'Register Successfully'})

    return render(request,'index.html',{'form':form})

def genOTP(request):
    try:
        name= 'Customer'
        otp = random.randint(100000,999999)
        print(otp)
        subject = 'Account Activation'
        if 'name' in request.GET:
            name = request.GET['name']
        message = 'Dear {} \n {} is your One Time Password for registration \n Thanks for being a part of our organization\n Do not share it with anyone'.format(name,otp)
        receiver = str(request.GET['email'])
        email = EmailMessage(subject,message,to=[receiver,])
        email.send()
        response = ['An OTP Sent to your Email Address @',otp]
        return HttpResponse(response)
    except:
        response = ['OOPs!! Error Occured @',otp]
        return HttpResponse(response)
