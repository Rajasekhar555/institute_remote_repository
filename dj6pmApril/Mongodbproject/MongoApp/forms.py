from django import forms
from .models import APPoliceInfo,TSpoliceInfo

class APPoliceInfoForm(forms.Form):
    name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )
    age = forms.IntegerField(
        label='Enter your age',
        widget=forms.TextInput (
            attrs={
                'class': 'form-control',
                'placeholder': 'Your name'
            }
        )
    )name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )name=forms.CharField(
        label='Enter your name',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Your name'
            }
        )
    )