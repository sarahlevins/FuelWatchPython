from django.contrib import admin
from .models import FuelPrice, StateRegion, Region, Brand, Product, Suburb, FuelStation

admin.site.register(FuelPrice)
admin.site.register(StateRegion)
admin.site.register(Region)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Suburb)
admin.site.register(FuelStation)
