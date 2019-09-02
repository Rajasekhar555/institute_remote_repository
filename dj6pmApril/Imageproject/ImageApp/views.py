from django.shortcuts import render

from .models import Iamge
from .forms import ImageForm


def image_view(request):
    if request.method=='POST':
        iform=ImageForm(request.POST)
        if iform.is_valid():
            name=request.POST.get('name','')
            location=request.POST.get('location','')
            photo=request.POST.get('photo','')
            age=request.POST.get('age','')

            data=Iamge(
                name=name,
                location=location,
                age=age,
                photo=photo
            )
            data.save()
            iform=ImageForm()
            return render(request,'Image_form.html',{'iform':iform})


    else:
        iform=ImageForm()
        return render(request,'Image_form.html',{'iform':iform})


def images(request):
    imgs=Iamge.objects.all()
    return render(request,'images_display.html',{'imgs':imgs})






















