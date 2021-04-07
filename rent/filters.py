import django_filters
from rent.models import Rentals

class RentalFilter(django_filters.FilterSet):
    class Meta:
        model=Rentals
        fields='__all__'

class WeeklyFilter(django_filters.FilterSet):
    Date_Received = django_filters.DateRangeFilter()
   #Date_Received = django_filters.DateFromToRangeFilter()
    class Meta:
        model=Rentals
        fields=['Date_Received']
        
# class FlexibleFilter(django_filters.FilterSet):
#     Date_Received = django_filters.DateFromToRangeFilter()
#     class Meta:
#         model=Rentals
#         fields=['Date_Received']
    