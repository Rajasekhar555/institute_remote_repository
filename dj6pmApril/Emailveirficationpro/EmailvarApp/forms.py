from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import LogData
from .models import Profile
class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    age = forms.IntegerField()

    class Meta:
        model = User
        fields = ('username','name','age','email', )




class LoginDataForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'enter username'
            }
        )
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'place-holder': 'enter password'
            }
        )
    )