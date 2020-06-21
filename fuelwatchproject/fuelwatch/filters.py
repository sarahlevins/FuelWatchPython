import django_filters
from django import forms
from .models import FuelStation, FuelPrice, Suburb


class FuelFilter(django_filters.FilterSet):

    suburbs = Suburb.objects.all()

    fuel_station__suburb = django_filters.ModelMultipleChoiceFilter(
        queryset=suburbs, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = FuelPrice
        fields = ['price', 'fuel_station__suburb']


# forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )
