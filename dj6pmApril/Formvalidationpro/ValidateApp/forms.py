from django import forms
from django.core import validators


class StudentForm(forms.Form):

    name=forms.CharField()
    marks=forms.IntegerField()

    def clean_name(self):
        inputname=self.cleaned_data['name']
        if len(inputname)<4:
            raise forms.ValidationError('The number of characters should be more than 4 ')
        return inputname
    def clean_marks(self):
        inputmarks=self.cleaned_data['marks']
        if inputmarks < 35:
            raise forms.ValidationError('you are failed')
        return inputmarks

