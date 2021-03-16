# -*- coding: utf-8 -*-

from django.urls import path, include
from rent import views
app_name = 'rent'

urlpatterns = [
    path('',views.home, name='home'),
    path('jobs/', views.Job_List.as_view(), name='job_list'),
    path('jobs/<int:pk>/', views.Job_Detail.as_view(), name='job_detail'),
    path('jobs/new/', views.Job_Create.as_view(), name='job_create'),
    path('jobs/<int:pk>/update/', views.Job_Update.as_view(), name='job_update'),
    path('jobs/<int:pk>/delete/', views.Job_Delete.as_view(), name='job_delete'),
    
    path('invoices/',views.Invoice_List.as_view(),name='invoice_list'),
    path('invoices/<int:pk>/', views.Invoice_Detail.as_view(), name='invoice_detail'),
    path('invoices/new/', views.Invoice_Create.as_view(), name='invoice_create'),
    path('invoices/<int:pk>/update/', views.Invoice_Update.as_view(), name='invoice_update'),
    path('invoices/<int:pk>/delete/', views.Invoice_Delete.as_view(), name='invoice_delete'),
    
    path('vendors/',views.Vendor_List.as_view(),name='vendor_list'),
    path('vendors/<int:pk>/', views.Vendor_Detail.as_view(), name='vendor_detail'),
    path('vendors/new/', views.Vendor_Create.as_view(), name='vendor_create'),
    path('vendors/<int:pk>/update/', views.Vendor_Update.as_view(), name='vendor_update'),
    path('vendors/<int:pk>/delete/', views.Vendor_Delete.as_view(), name='vendor_delete'),
    
    path('equipments/',views.Equipment_List.as_view(),name='equipment_list'),
    path('equipments/<int:pk>/', views.Equipment_Detail.as_view(), name='equipment_detail'),
    path('equipments/new/', views.Equipment_Create.as_view(), name='equipment_create'),
    path('equipments/<int:pk>/update/', views.Equipment_Update.as_view(), name='equipment_update'),
    path('equipments/<int:pk>/delete/', views.Equipment_Delete.as_view(), name='equipment_delete'),
    
    path('rentals/',views.Rental_List.as_view(),name='rental_list'),
    path('rentals/<int:pk>/', views.Rental_Detail.as_view(), name='rental_detail'),
    path('rentals/new/', views.Rental_Create.as_view(), name='rental_create'),
    path('rentals/<int:pk>/update/', views.Rental_Update.as_view(), name='rental_update'),
    path('rentals/<int:pk>/delete/', views.Rental_Delete.as_view(), name='rental_delete'),
    
    
   ]

