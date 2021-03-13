from django.shortcuts import render, redirect


# Create your views here.
from django.urls import reverse,reverse_lazy
from django.utils import timezone
from django.views import View
from rent.forms import RegisterUser
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from rent.decorators import authenticated_user



def index(request):
    return render(request, 'rent/index.htm')

@login_required(login_url='login')
def home(request):
    return render(request,'rent/home.htm')

@authenticated_user
def register(request):   
    form=RegisterUser(request.POST)
    if request.method=='POST':
        form=RegisterUser(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,"Account succesfully created for  " + user)
            return redirect('login')
                
    context={'form':form}
    return render(request,'rent/register.htm',context)

@authenticated_user    
def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
                
        user=authenticate(request, username=username, password=password)
                
        if user is not None:
            login(request,user)
            return redirect ('home')
        else:
            messages.info(request,"Username or Password is incorrect")
            
            
    context={}
    return render(request,'rent/login.htm',context)    

def logoutUser(request):
    logout(request)
    return redirect ('login')
