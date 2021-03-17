from django.shortcuts import render, redirect
from rent.filters import RentalFilter

# Create your views here.
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.views import View
from rent.forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rent.decorators import authenticated_user,allowed_users
from rent.forms import JobForm,EquipmentForm,VendorForm,InvoiceForm,RentalsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rent.models import Job, Invoice, Equipment, Vendor, Rentals
from django.contrib.auth.models import Group
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin


def AllRentals(request):
    
    

