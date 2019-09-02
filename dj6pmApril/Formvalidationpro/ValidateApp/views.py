from django.shortcuts import render
from ValidateApp.forms import StudentForm



def student_page(request):
    if request.method=='POST':
        sform=StudentForm(request.POST)
        if sform.is_valid():
            print('Form validation is success and printing information')
            print('Name:',sform.cleaned_data['name'])
            print('Marks:',sform.cleaned_data['marks'])
            sent=True
    sform=StudentForm()
    return render(request,'student_input.html',{'sform':sform})
