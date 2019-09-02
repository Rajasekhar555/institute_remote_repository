
from signuploginApp.forms import SignUpDataForm,LoginDataForm
from .models import SignUpData
from django.http.response import HttpResponse
from django.shortcuts import render, redirect

def sign_page(request):
    if request.method=='POST':
        sform=SignUpDataForm(request.POST)
        if sform.is_valid():
            name=request.POST.get('name','')
            age=request.POST.get('age','')
            email_id=request.POST.get('email_id','')
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            data=SignUpData(
                name=name,
                age=age,
                email_id=email_id,
                username=username,
                password=password
            )
            data.save()
            lform=LoginDataForm()
            return render(request,'login_form.html',{'lform':lform})
        else:
            return HttpResponse("Plz all fields are required...")
    else:
        sform=SignUpDataForm()
        return render(request,'sign_form.html',{'sform':sform})


def login_page(request):
    if request.method=='POST':
        lform=LoginDataForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            uname=SignUpData.objects.filter(username=username)
            pwd=SignUpData.objects.filter(password=password)

            if uname and pwd:
                return redirect(dashboard_view)
            else:
                return HttpResponse('wrong username and password...')
        else:
            return HttpResponse('invalid data')

    else:
        lform=LoginDataForm()
        return render(request,'login_form.html',{'lform':lform})


def dashboard_view(request):
    ddata=SignUpData.objects.all()


    return render(request,'dashboard.html',{'ddata':ddata})

