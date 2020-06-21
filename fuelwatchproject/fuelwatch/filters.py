import django_filters
from django import forms
from .models import FuelStation, FuelPrice


# class FuelFilter(django_filters.FilterSet):

#     SUBURB_CHOICES = Suburb.objects.all()

#     print(type(SUBURB_CHOICES))

#     fuel_station__suburb = django_filters.ModelMultipleChoiceFilter(
#         queryset=SUBURB_CHOICES, widget=forms.CheckboxSelectMultiple)

#     class Meta:
#         model = FuelPrice
#         fields = ['price', 'fuel_station__suburb']


# forms.MultipleChoiceField(
#         required=False,
#         widget=forms.CheckboxSelectMultiple,
#         choices=FAVORITE_COLORS_CHOICES,
#     )
