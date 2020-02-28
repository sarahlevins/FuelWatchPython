import django_filters
from django import forms
from .models import FuelStation, FuelPrice

class FuelFilter(django_filters.FilterSet):

    location = django_filters.ModelMultipleChoiceFilter(queryset=FuelStation.objects.all(), widget = forms.CheckboxSelectMultiple) 

    class Meta:
        model = FuelPrice
        fields = ['price', 'fuel_type']