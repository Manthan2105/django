from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
from phone_field import PhoneField
from django import forms
from django.contrib.auth.models import AbstractUser


# Create your models here.
GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),)
class clientModel(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,default="")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,default="")
    profile_pic=models.ImageField(upload_to="profile_pics",blank=True,default="")
    phone_number=PhoneField(blank=True, help_text='Contact phone number',default="")
    age=models.IntegerField(default=0)
    def __str__(self):
        return self.user.username
