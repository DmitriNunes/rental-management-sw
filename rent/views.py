from django.shortcuts import render, redirect


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
from django.contrib.auth.mixins import PermissionRequiredMixin

########################### Login/Logout + Authentication ##############################
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
            user=form.save()
            username=form.cleaned_data.get('username')
            group=Group.objects.get(name='Viewer')
            user.groups.add(group)
            messages.success(request,"Account succesfully created for  " + username)
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
            return redirect ('rent:home')
        else:
            messages.info(request,"Username or Password is incorrect")
            
            
    context={}
    return render(request,'rent/login.htm',context)    

def logoutUser(request):
    logout(request)
    return redirect ('login')
#####################################################################################
    

######################## Forms for Job ########################################## 

class Job_List(ListView):
    model = Job
    form_class=JobForm
    template_name = 'rent/job_list.htm'
    context_object_name = 'job'

class Job_Detail(DetailView):
    model = Job
    form_class=JobForm
    template_name = 'rent/job_detail.htm'
    context_object_name = 'job'

class Job_Create(PermissionRequiredMixin, CreateView):
    permission_required='job.add_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_create.htm'
    success_url = reverse_lazy('rent:job_list')

class Job_Update(PermissionRequiredMixin, UpdateView):
    permission_required='job.change_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_update.htm'
    success_url = reverse_lazy('rent:job_list')

class Job_Delete(PermissionRequiredMixin,DeleteView):
    permission_required='job.delete_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_delete.htm'
    success_url = reverse_lazy('rent:job_list')    
###################################################################################
    
######################### Forms for Invoice #######################################
    
class Invoice_List(ListView):
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_list.htm'
    context_object_name = 'invoice'

class Invoice_Detail(DetailView):
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_detail.htm'
    context_object_name = 'invoice'

class Invoice_Create(CreateView):
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_create.htm'
    success_url = reverse_lazy('rent:invoice_list')

class Invoice_Update(UpdateView):
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_update.htm'
    success_url = reverse_lazy('rent:invoice_list')

class Invoice_Delete(DeleteView):
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_delete.htm'
    success_url = reverse_lazy('rent:invoice_list')    
#####################################################################################
    
#########################Forms for Vendor ###########################################

class Vendor_List(ListView):
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_list.htm'
    context_object_name = 'vendor'

class Vendor_Detail(DetailView):
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_detail.htm'
    context_object_name = 'vendor'

class Vendor_Create(CreateView):
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_create.htm'
    success_url = reverse_lazy('rent:vendor_list')

class Vendor_Update(UpdateView):
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_update.htm'
    success_url = reverse_lazy('rent:vendor_list')

class Vendor_Delete(DeleteView):
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_delete.htm'
    success_url = reverse_lazy('rent:vendor_list')    
#####################################################################################

#############################Forms for Equipment#####################################
    
class Equipment_List(ListView):
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_list.htm'
    context_object_name = 'equipment'

class Equipment_Detail(DetailView):
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_detail.htm'
    context_object_name = 'equipment'

class Equipment_Create(CreateView):
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_create.htm'
    success_url = reverse_lazy('rent:equipment_list')

class Equipment_Update(UpdateView):
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_update.htm'
    success_url = reverse_lazy('rent:equipment_list')

class Equipment_Delete(DeleteView):
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_delete.htm'
    success_url = reverse_lazy('rent:equipment_list')        
    
#######################################################################################
    
############################## Forms for Rentals ######################################

class Rental_List(ListView):
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_list.htm'
    context_object_name = 'rental'

class Rental_Detail(DetailView):
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_detail.htm'
    context_object_name = 'rental'

class Rental_Create(CreateView):
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_create.htm'
    success_url = reverse_lazy('rent:rental_list')

class Rental_Update(UpdateView):
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_update.htm'
    success_url = reverse_lazy('rent:rental_list')

class Rental_Delete(DeleteView):
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_delete.htm'
    success_url = reverse_lazy('rent:rental_list')       
###################################################################################    

    