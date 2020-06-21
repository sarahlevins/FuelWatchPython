import requests
import feedparser
from pprint import pprint
from datetime import datetime
from .models import FuelPrice, FuelStation, Suburb

get_fuel_stations():
    suburbs = Suburbs.objects.all()
    for suburb in suburbs:
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb={suburb}')
        feed = feedparser.parse(response.content)
    # loop through suburbs to create stations
        # test if station exists by trading name
        # set and save station details
    # loop through regions to add region info
    # loop through state regions to add state region info
    # loop through brand to add brand info


def get_fuel():
    regions = [26]
    fuel_type = 1
    output = {}
    # loop through regions
    for r in range(len(regions)):
        info = []
        # get fuel data from fuelwatch and parse it
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={fuel_type}&Region={regions[r]}&Day=today')
        feed = feedparser.parse(response.content)
        # loop through data and create fuel pump data
        for i in range(len(feed['entries'])):
            pump = feed['entries'][i]
            # create suburb
            suburb = Suburb(
                suburb_name=pump.get('location'),
                region=regions[r]
            )
            suburb.save()
            # create fuelstation
            fuel_station = FuelStation(
                trading_name=pump.get('trading-name'),
                brand=pump.get('brand'),
                suburb=suburb,
                address=pump.get('address'),
            )
            fuel_station.save()
            # save fuelprice
            fuel_price = FuelPrice(
                title=pump.get('title'),
                fuel_type=fuel_type,
                date=datetime.strptime(pump.get('date'), '%Y-%m-%d').date(),
                price=pump.get('price'),
                fuel_station=fuel_station,
            )
            fuel_price.save()
            print('saved price: ' + fuel_price.title)

# {'title': '149.9: Caltex The Foodary Yangebup',
# 'title_detail': {
#     'type': 'text/plain',
#     'language': None,
#     'base': '',
#     'value': '149.9: Caltex The Foodary Yangebup'
#     },
# 'summary': 'Address: 289 Beeliar Dr, YANGEBUP, Phone: 0467 778 235',
# 'summary_detail': {
#      'type': 'text/html',
#      'language': None,
#      'base': '',
#      'value': 'Address: 289 Beeliar Dr, YANGEBUP, Phone: 0467 778 235'
#      },
# 'brand': 'Caltex',
# 'updated': '2020-02-27',
# 'price': '149.9',
# 'trading-name': 'Caltex The Foodary Yangebup',
# 'location': 'YANGEBUP',
# 'address': '289 Beeliar Dr',
# 'phone': '0467 778 235',
# 'latitude': '-32.127568',
# 'longitude': '115.799158',
# 'site-features': ','}
