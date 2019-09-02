from django.shortcuts import render
from formvalidateApp.forms import FeedbackForm,SignupForm




def feedback_view(request):
    if request.method=='POST':
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            print('validation is completed')
            print('Name:',fform.cleaned_data['name'])
            print('Rollno:',fform.cleaned_data['rollno'])
            print('Email:',fform.cleaned_data['email'])
            print('Feedback:',fform.cleaned_data['Feedback'])
        return render(request,'formvalidateApp/feedback.html',{'fform':fform})
    else:
        fform=FeedbackForm()
        return render(request,'formvalidateApp/feedback.html',{'fform':fform})




def signup_view(request):
    if request.method=='POST':
        sform=SignupForm(request.POST)
        if sform.is_valid():
            print('validation is compleated..')
            print('Name:',sform.cleaned_data['name'])
            print('Password:',sform.cleaned_data['password'])
            print('Email',sform.cleaned_data['email'])
        return render(request,'formvalidateApp/signup.html',{'sform':sform})
    else:
        sform=SignupForm()
        return render(request,'formvalidateApp/signup.html',{'sform':sform})
