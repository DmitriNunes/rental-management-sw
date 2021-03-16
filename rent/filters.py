import django_filters
from rent.models import Rentals

class RentalFilter(django_filters.FilterSet):
    class Meta:
        model=Rentals
        fields='__all__'
