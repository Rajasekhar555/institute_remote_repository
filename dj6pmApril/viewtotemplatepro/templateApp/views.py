from django.shortcuts import render,redirect
from .forms import LoginForm
from .models import LoginData
from django.http.response import HttpResponse


def dashboard_view(request):
    return render(request,'dashboard.html')


def login_view_page(request):
    if request.method=='POST':
        lform=LoginForm(request.POST)
        if lform.is_valid():
            username=request.POST.get('username','')
            password=request.POST.get('password','')

            if username=="rajasekhar" and password=="plokijuh":
                return redirect(dashboard_view)
            else:
                return HttpResponse('invalid data')

        else:
            lform=LoginForm()
            return render(request,'loginform.html',{'lform':lform})
    else:
        lform=LoginForm()
        return render(request, 'loginform.html', {'lform': lform})

