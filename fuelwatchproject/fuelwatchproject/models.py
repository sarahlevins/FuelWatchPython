from django.db import models

class FuelPrice(models.Model):
    price = models.DecimalField(max_digits=8, decimal_places=2)
    fuel_type = models.IntegerField()
    address = models.CharField(max_length=100)