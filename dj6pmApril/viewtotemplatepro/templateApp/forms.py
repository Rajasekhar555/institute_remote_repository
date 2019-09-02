from django import forms
from .models import LoginData

class LoginForm(forms.Form):
    username=forms.CharField(
        label="enter user name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'username'
            }
        )
    )
    password = forms.CharField(
        label="enter password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'password'
            }
        )
    )