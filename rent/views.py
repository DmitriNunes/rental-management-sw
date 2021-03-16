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
from rent.decorators import authenticated_user #allowed_users
from rent.forms import JobForm,EquipmentForm,VendorForm,InvoiceForm,RentalsForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rent.models import Job, Invoice, Equipment, Vendor, Rentals
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.auth.mixins import PermissionRequiredMixin,LoginRequiredMixin

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
            usergroup=form.cleaned_data.get('groups')
            user.groups.add(usergroup[0])
            user.save()
            # if usergroup == Group.objects.get(name='Administrator'):
            #     user.groups.add(usergroup)
            #     user.save()
            # else:
            #     usergroup=Group.objects.get(name='Viewer')
            #     user.groups.add(usergroup)
            #     user.save()
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

class Job_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_list.htm'
    context_object_name = 'job'


class Job_Detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_detail.htm'
    context_object_name = 'job'

class Job_Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.add_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_create.htm'
    success_url = reverse_lazy('rent:job_list')

class Job_Update(LoginRequiredMixin,PermissionRequiredMixin, UpdateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.change_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_update.htm'
    success_url = reverse_lazy('rent:job_list')

class Job_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.delete_job'
    model = Job
    form_class=JobForm
    template_name = 'rent/job_delete.htm'
    success_url = reverse_lazy('rent:job_list')    
###################################################################################
    
######################### Forms for Invoice #######################################
   
class Invoice_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_invoice'
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_list.htm'
    context_object_name = 'invoice'

class Invoice_Detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_invoice'
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_detail.htm'
    context_object_name = 'invoice'

class Invoice_Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.add_invoice'
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_create.htm'
    success_url = reverse_lazy('rent:invoice_list')

class Invoice_Update(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.change_invoice'
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_update.htm'
    success_url = reverse_lazy('rent:invoice_list')

class Invoice_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.delete_invoice'
    model = Invoice
    form_class=InvoiceForm
    template_name = 'rent/invoice_delete.htm'
    success_url = reverse_lazy('rent:invoice_list')    
#####################################################################################
    
#########################Forms for Vendor ###########################################

class Vendor_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_vendor'
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_list.htm'
    context_object_name = 'vendor'

class Vendor_Detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_vendor'
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_detail.htm'
    context_object_name = 'vendor'

class Vendor_Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.add_vendor'
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_create.htm'
    success_url = reverse_lazy('rent:vendor_list')

class Vendor_Update(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.change_vendor'
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_update.htm'
    success_url = reverse_lazy('rent:vendor_list')

class Vendor_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.delete_vendor'
    model = Vendor
    form_class=VendorForm
    template_name = 'rent/vendor_delete.htm'
    success_url = reverse_lazy('rent:vendor_list')    
#####################################################################################

#############################Forms for Equipment#####################################
    
class Equipment_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_equipment'
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_list.htm'
    context_object_name = 'equipment'

class Equipment_Detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_equipment'
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_detail.htm'
    context_object_name = 'equipment'

class Equipment_Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.add_equipment'
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_create.htm'
    success_url = reverse_lazy('rent:equipment_list')

class Equipment_Update(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.change_equipment'
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_update.htm'
    success_url = reverse_lazy('rent:equipment_list')

class Equipment_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.delete_equipment'
    model = Equipment
    form_class=EquipmentForm
    template_name = 'rent/equipment_delete.htm'
    success_url = reverse_lazy('rent:equipment_list')        
    
#######################################################################################
    
############################## Forms for Rentals ######################################

class Rental_List(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_rentals'
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_list.htm'
    context_object_name = 'rental'

##################### filter ##########################    
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['filter']=RentalFilter(self.request.GET,queryset=self.get_queryset())
        return context
#########################################################    



class Rental_Detail(LoginRequiredMixin,PermissionRequiredMixin,DetailView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.view_rentals'
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_detail.htm'
    context_object_name = 'rental'

class Rental_Create(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.add_rentals'
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_create.htm'
    success_url = reverse_lazy('rent:rental_list')

class Rental_Update(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.change_rentals'
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_update.htm'
    success_url = reverse_lazy('rent:rental_list')

class Rental_Delete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    login_url='login'
    redirect_field_name='redirect_to'
    permission_required='rent.delete_rentals'
    model = Rentals
    form_class=RentalsForm
    template_name = 'rent/rental_delete.htm'
    success_url = reverse_lazy('rent:rental_list')       
###################################################################################
    

    