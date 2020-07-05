from django.http import HttpResponse
from django.views.generic.detail import DetailView
from django.shortcuts import render
from .models import FuelPrice, FuelStation, Suburb
from .filters import FuelFilter


def index(request):
    fuel_list = FuelPrice.objects.all()
    fuel_filter = FuelFilter(request.GET, queryset=fuel_list)
    return render(request, 'index.html', {'fuel': fuel_list, 'fuel_filter': fuel_filter})


# def getfuelprices(request):
#     get_fuel_prices()
#     return HttpResponse(200)


# def getfuel(request):
#     populate_filter_types(get_filter_types())
#     get_fuel_stations()
#     return HttpResponse(200)


class FuelStationDetail(DetailView):
    model = FuelStation
    context_object_name = 'fuel_station'
    template_name = 'fuel_station_detail.html'
