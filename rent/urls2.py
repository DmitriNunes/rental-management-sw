from django.urls import path, include
from rent import views
app_name = 'rent'

urlpatterns = [
    
    path('',views.Invoice_List.as_view(),name='invoice_list'),
    path('<int:pk>/', views.Invoice_Detail.as_view(), name='invoice_detail'),
    path('new/', views.Invoice_Create.as_view(), name='invoice_create'),
    
   ]# -*- coding: utf-8 -*-

