from django import forms
from django.core import validators

class FeedbackForm(forms.Form):
    name=forms.CharField()
    rollno=forms.IntegerField()
    email=forms.EmailField()
    Feedback=forms.CharField(widget=forms.Textarea)


    def clean(self):
        total_cleaned_data=super().clean()
        inputname=total_cleaned_data['name']
        if len(inputname) < 4:
            raise forms.ValidationError('the name should be more than 4 characters..')
        inputrollno=total_cleaned_data['rollno']
        if inputrollno < 0:
            raise forms.ValidationError('number should be greater than 0')
class SignupForm(forms.Form):
    name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput)
    rpassword=forms.CharField(label='Reenter password',widget=forms.PasswordInput)
    email=forms.EmailField()

    def clean(self):
        total_cleaned_data=super().clean()
        pwd=total_cleaned_data['password']
        rpwd=total_cleaned_data['rpassword']

        if pwd!=rpwd:
            raise forms.ValidationError('both passwords must be same..')
