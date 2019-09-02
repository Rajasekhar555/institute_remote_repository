from django import forms

class ImageForm(forms.Form):
    name=forms.CharField(
        label="Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Name'
            }
        )
    )
    age=forms.IntegerField(
        label="Enter your Age",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Age'
            }
        )
    )
    location=forms.CharField(
        label="enter your location",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Location'
            }

        )
    )
    photo=forms.ImageField(
        label="Select image",
        widget=forms.FileInput(
            attrs={
                'class':'form-control',
                'placeholder':'Photo'
            }
        )

    )

















