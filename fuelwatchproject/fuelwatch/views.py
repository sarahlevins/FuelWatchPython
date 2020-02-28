from django.http import HttpResponse
from django.shortcuts import render
from fuelwatch.get_fuel import get_fuel
from .models import FuelPrice, FuelStation
from .filters import FuelFilter
from data import data

def index(request):
    fuel_list = FuelPrice.objects.order_by('price')
    fuel_filter = FuelFilter(request.GET, queryset=fuel_list)
    return render(request, 'index.html', {'fuel': fuel_list, 'filter': fuel_filter})