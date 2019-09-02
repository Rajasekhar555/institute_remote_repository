from django import forms
from django.contrib.auth.models import User
from .models import registration

class regForm(forms.ModelForm):
    confirm_password = forms.CharField(widget= forms.PasswordInput())
    enter_OTP = forms.IntegerField()
    class Meta:
        model = User
        fields = ('first_name','last_name','username','email','password')
        widgets = {
        'password':forms.PasswordInput(attrs={'type':'password'})
        }