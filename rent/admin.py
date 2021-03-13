from django.contrib import admin
from rent.models import Job,Invoice,Vendor,Equipment,Rentals
# Register your models here.
admin.site.register(Job)
admin.site.register(Invoice)
admin.site.register(Vendor)
admin.site.register(Equipment)
admin.site.register(Rentals)