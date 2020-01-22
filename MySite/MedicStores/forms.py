from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from MedicStores.models import clientModel


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','first_name','last_name','email','password','is_staff')
        widgets = {'is_staff': forms.HiddenInput()}
class UserInfoForm(forms.ModelForm):
    class Meta():
        model=clientModel
        fields=('gender','profile_pic','phone_number','age')
