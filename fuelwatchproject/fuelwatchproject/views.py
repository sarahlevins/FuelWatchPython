from django.http import HttpResponse
from django.shortcuts import render
from fuelwatchproject.fuelwatch import fuelley
from data import data

def index(request):
    return render(request, 'index.html', {
    'fuel': data
})

