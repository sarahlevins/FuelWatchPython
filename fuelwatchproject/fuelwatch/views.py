from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render
from fuelwatch.get_fuel import populate_filter_types, get_filter_types, get_fuel_stations, get_fuel_prices
from .models import FuelPrice, FuelStation, Suburb
# from .filters import FuelFilter
from data import data


def index(request):
    fuel_list = FuelPrice.objects.order_by('price')
    # fuel_filter = FuelFilter(request.GET, queryset=fuel_list)
    return render(request, 'index.html', {'fuel': fuel_list})


def getfuelprices(request):
    get_fuel_prices()
    return HttpResponse(200)


def getfuel(request):
    populate_filter_types(get_filter_types())
    get_fuel_stations()
    return HttpResponse(200)

# class FuelStationDetail(DetailView):
#     model = FuelStation
#     context_object_name = 'fuel_station'
#     template_name = 'fuel_station_detail.html'
