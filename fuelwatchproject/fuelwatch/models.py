from django.db import models
import uuid


class Suburb (models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class StateRegion (models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Region (models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class Brand (models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    name = models.CharField(max_length=100)
    code = models.IntegerField(blank=True)

    def __str__(self):
        return self.name


class FuelStation(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    trading_name = models.CharField(
        max_length=100, unique=True)
    address = models.CharField(max_length=500)
    suburb = models.ForeignKey(Suburb, on_delete=models.CASCADE, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, null=True)
    phone = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    site_features = models.CharField(max_length=500)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, null=True)
    state_region = models.ForeignKey(
        StateRegion, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.trading_name


class FuelPrice(models.Model):
    id = models.CharField(primary_key=True, unique=True,
                          max_length=100, default=uuid.uuid4)
    price = models.FloatField()
    date = models.DateField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    fuel_station = models.ForeignKey(FuelStation, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.price) + ' - ' + str(self.fuel_station)
