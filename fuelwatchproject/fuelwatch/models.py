from django.db import models

class FuelStation(models.Model):
    trading_name = models.CharField(max_length=200, primary_key=True)
    brand = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__ (self):
        return self.trading_name

class FuelPrice(models.Model):
    title = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    date = models.DateTimeField()
    fuel_type = models.IntegerField()
    fuel_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)    
    
    def __str__ (self):
        return self.title