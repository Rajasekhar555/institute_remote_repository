from django.shortcuts import render
from django.http.response import HttpResponse
from Appsession.forms import LoginForm
import datetime

def index(request):
    request.session.set_test_cookie()
    return HttpResponse("<h1>Index page</h1>")
def check_view(request):
    if request.session.test_cookie_worked():
        print('cookies are working properly')
        request.session.test_cookie_worked()
        return HttpResponse('<h1>checking page</h1>')

def count_view(request):
    if 'count' in request.COOKIES:
        newcount=int(request.COOKIES['count'])+1
    else:
        newcount=1
    response=render(request,'Appsession/count.html',{'count':newcount})
    response.set_cookie('count',newcount)
    return response
def home_view(request):
    form=LoginForm()
    return render(request,'Appsession/home.html',{'form':form})

def date_time_view(request):
    name=request.GET['name']
    response=render(request,'Appsession/datetime.html',{'name':name})
    response.set_cookie('name',name)
    return response
def result_view(request):
    name=request.COOKIES['name']
    date_time=datetime.datetime.now()
    my_dict={'name':name,'date':date_time}
    return render(request,'Appsession/result.html',my_dict)
















