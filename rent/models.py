from django.db import models
from django.utils import timezone
from datetime import date
# Create your models here.


class Job(models.Model):
    Job_no=models.CharField(max_length=10,null=False,blank=False,unique=True)
    PO_no=models.IntegerField(null=False,blank=False)
    Job_name=models.CharField(max_length=20,null=False, blank=False)
    Phase=models.CharField(max_length=20,null=False, blank=False)
    Job_status=models.BooleanField(default=False)
    
    def __str__(self):
        return '%s %s' %(self.Job_no,self.Job_name)
    
class Invoice(models.Model):
    Invoice_Date=models.DateField(default=timezone.now)
    Invoice_no=models.CharField(max_length=10,null=False,blank=False,unique=True)
    Rental_Period=models.IntegerField(null=False,blank=False)
    Invoice_Amount=models.DecimalField(null=True, max_digits=10,decimal_places=2)
    job=models.ForeignKey(Job, to_field='Job_no', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.Invoice_no
    
    
class Vendor(models.Model):
    Vendor_no=models.CharField(max_length=10,null=False,blank=False,unique=True)
    Vendor_name=models.CharField(max_length=20, null=False, blank=False)
    Salesman=models.CharField(max_length=20,null=False, blank=False)
    Phone=models.IntegerField(null=False,blank=False)
    
    def __str__(self):
        return '%s %s' %(self.Vendor_no,self.Vendor_name)
    

class Equipment(models.Model):
    Equipment_name=models.CharField(max_length=20,null=False,blank=False)
    Equipment_ID=models.CharField(max_length=10,null=False,blank=False,unique=True)
    Serial_no=models.IntegerField(null=False,blank=False)
    Category=models.CharField(max_length=20, null=False,blank=False)
    Model=models.CharField(max_length=20, null=False,blank=False)
    Make=models.CharField(max_length=20, null=False,blank=False)
    Buy_price=models.DecimalField(null=True, max_digits=10,decimal_places=2)
    Rent_price=models.DecimalField(null=True, max_digits=10,decimal_places=2)
    vendor=models.ForeignKey(Vendor, to_field='Vendor_no', on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.Equipment_ID
        

class Rentals(models.Model):
    Rental_ID=models.CharField(max_length=10,blank=False, null=False)
    Buy_or_Rent=models.CharField(max_length=10,blank=False,null=False)
    Date_Received=models.DateField(default=timezone.now)
    Return_Status=models.BooleanField(default=False)
    Date_Returned=models.DateField(blank=True, null= True)
    Expected_Duration=models.IntegerField(blank=False, null=False)
    job=models.ForeignKey(Job, to_field='Job_no', on_delete=models.SET_NULL, null=True)
    vendor=models.ForeignKey(Vendor, to_field='Vendor_no', on_delete=models.SET_NULL, null=True)
    equipment_ID=models.ForeignKey(Equipment, to_field='Equipment_ID',on_delete=models.SET_NULL,null=True)
    Invoice_number=models.ForeignKey(Invoice,to_field='Invoice_no', on_delete=models.SET_NULL, null=True)
    
    class Meta:
        verbose_name='Rentals'
        verbose_name_plural='Rentals'
    
    def __str__(self):
        return self.Rental_ID
    
    
    
    

    
    
    
    
    