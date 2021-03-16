# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from rent.models import Job, Invoice, Equipment, Vendor, Rentals



class RegisterUser(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','email','password1','password2','groups']
#
# class EnterGroup(forms.ModelForm):
#     class Meta:
#     model=Group 
#     fields=['group_name']       
        
class JobForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        
class EquipmentForm(forms.ModelForm):
    class Meta:
        model=Equipment
        fields='__all__'
    
class VendorForm(forms.ModelForm):
    class Meta:
        model=Vendor
        fields='__all__'
        
class InvoiceForm(forms.ModelForm):
    class Meta:
        model=Invoice
        fields='__all__'
        
class RentalsForm(forms.ModelForm):
    class Meta:
        model=Rentals
        fields='__all__'