from django import forms
from django.contrib.auth.models import User
from basic_app.models import UserProfileInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
        }
    ))
    confirm_password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
    }
    ))
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
             'placeholder':'Enter your username'
        }
    ))
    email=forms.EmailField(widget=forms.TextInput(
        attrs={
             'class':'form-control',
             'placeholder':'Enter your email adress'
        }
    ))



    class Meta():
        model = User
        fields = ('username','email','password')

class UserProfileInfoForm(forms.ModelForm):
    contact_number=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
             'placeholder':'01XXXXXXXXX'
        }
    ))
    class Meta():
        model=UserProfileInfo
        fields=('contact_number',)
