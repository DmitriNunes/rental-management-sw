# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm



class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2']
        
        
