from django.shortcuts import render
from .forms import SignUpForm
from django.http.response import HttpResponse
from .models import User


def signup_view(request):
    form =SignUpForm()
    if request.method=='POST':
        user=form.save()
        user.set_password(user.password)
        user.save()
        return HttpResponseRedirect('/accounts/login')
