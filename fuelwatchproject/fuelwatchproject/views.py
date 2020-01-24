from django.http import HttpResponse
from django.shortcuts import render
from fuelwatchproject.fuelwatch import fuelley

def index(request):
    return render(request, 'index.html', {
    'fuel': fuelley
})