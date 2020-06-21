import requests
import feedparser
from pprint import pprint
from datetime import datetime
from bs4 import BeautifulSoup
from .models import FuelPrice, StateRegion, Region, Brand, FuelStation, Product, Suburb


def get_fuel_prices():
    products = (list(Product.objects.values_list('id')))
    for product in products:
        print(product)
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product={product[0]}&Day=tomorrow')
        feed = feedparser.parse(response.content)
        linked_product = Product.objects.get(id=product[0])
        for e in range(len(feed['entries'])):
            entry = feed['entries'][e]
            try:
                linked_fuel_station = FuelStation.objects.get(
                    trading_name=entry.get('trading-name'))
                fuel_price = FuelPrice(
                    price=entry.get('price'),
                    date=entry.get('date'),
                    product=linked_product,
                    fuel_station=linked_fuel_station
                )
            except FuelStation.DoesNotExist:
                print(entry.get('location'))
                linked_brand = Brand.objects.get(name=entry.get('brand'))
                fuel_station = FuelStation(
                    trading_name=entry.get('trading-name'),
                    address=entry.get('address'),
                    phone=entry.get('phone'),
                    latitude=entry.get('latitude'),
                    longitude=entry.get('longitude'),
                    site_features=entry.get('site-features'),
                    brand=linked_brand
                )
                fuel_station.save()
                fuel_price = FuelPrice(
                    price=entry.get('price'),
                    date=entry.get('date'),
                    product=linked_product,
                    fuel_station=fuel_station
                )
            fuel_price.save()


def get_fuel_stations():
    # RECORD FUEL STATIONS BY SUBURB
    suburbs = (list(Suburb.objects.values_list('name')))
    for suburb in suburbs:
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Suburb={suburb[0]}')
        feed = feedparser.parse(response.content)
        for e in range(len(feed['entries'])):
            entry = feed['entries'][e]
            linked_suburb = Suburb.objects.get(name=suburb[0])
            try:
                fuel_station = FuelStation.objects.get(
                    trading_name=entry.get('trading-name'))
                fuel_station.suburb = linked_suburb
                fuel_station.save()
            except FuelStation.DoesNotExist:
                print('fuel station doesnt exist')
                linked_brand = Brand.objects.get(name=entry.get('brand'))
                fuel_station = FuelStation(
                    trading_name=entry.get('trading-name'),
                    address=entry.get('address'),
                    phone=entry.get('phone'),
                    latitude=entry.get('latitude'),
                    longitude=entry.get('longitude'),
                    site_features=entry.get('site-features'),
                    suburb=linked_suburb,
                    brand=linked_brand
                )
                fuel_station.save()
    print('completed suburb loop')

    # RECORD FUEL STATION BY REGION
    regions = (list(Region.objects.values_list('id')))
    for region in regions:
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Region={region[0]}')
        feed = feedparser.parse(response.content)
        linked_region = Region.objects.get(id=region[0])
        for e in range(len(feed['entries'])):
            entry = feed['entries'][e]
            try:
                fuel_station = FuelStation.objects.get(
                    trading_name=entry.get('trading-name'))
                fuel_station.region = linked_region
                fuel_station.save()
            except FuelStation.DoesNotExist:
                linked_brand = Brand.objects.get(name=entry.get('brand'))
                fuel_station = FuelStation(
                    trading_name=entry.get('trading-name'),
                    address=entry.get('address'),
                    phone=entry.get('phone'),
                    latitude=entry.get('latitude'),
                    longitude=entry.get('longitude'),
                    site_features=entry.get('site-features'),
                    region=linked_region,
                    brand=linked_brand
                )
                fuel_station.save()
    print('complete region loop')

    # RECORD FUEL STATION BY STATE REGION
    state_regions = (list(StateRegion.objects.values_list('id')))
    for state_region in state_regions:
        response = requests.get(
            f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?StateRegion={state_region[0]}')
        feed = feedparser.parse(response.content)
        linked_state_region = StateRegion.objects.get(id=state_region[0])
        for e in range(len(feed['entries'])):
            entry = feed['entries'][e]
            try:
                fuel_station = FuelStation.objects.get(
                    trading_name=entry.get('trading-name'))
                fuel_station = FuelStation.objects.get(
                    trading_name=entry.get('trading-name'))
                fuel_station.region = linked_region
                fuel_station.save()
            except FuelStation.DoesNotExist:
                linked_brand = Brand.objects.get(name=entry.get('brand'))
                fuel_station = FuelStation(
                    trading_name=entry.get('trading-name'),
                    address=entry.get('address'),
                    phone=entry.get('phone'),
                    latitude=entry.get('latitude'),
                    longitude=entry.get('longitude'),
                    site_features=entry.get('site-features'),
                    state_region=linked_state_region,
                    brand=linked_brand
                )
                fuel_station.save()
    print('completed state region loop')


def get_filter_types():
    URL = 'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/contentholder.jspx?key=fuelwatchRSS.html'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')

    filter_types_soup = str(soup.find(id='content')).split('===<br/>')[1:]
    filter_types = []
    for filter in enumerate(filter_types_soup):
        if ' codes<br/>' in filter[1]:
            filter_types.append(filter[1][:-11])

    output = {}
    for filter_type in enumerate(filter_types):
        code_soup = str(soup.find(id='content'))[
            :-11].split('===<br/>'+filter_type[1]+' codes<br/>===<br/><br/>')[1].split('br/><br/>===<br/>')[0].split('<br/>')

        codes = {}
        for i in range(len(code_soup)):
            code = code_soup[i].strip('<').split(' - ')
            codes.update({code[0]: code[1]})
        output.update({filter_type[1]: codes})

    # add product type
    output.update({
        'Product':
        {
            '1': 'Unleaded Petrol',
            '2': 'Premium Unleaded',
            '4': 'Diesel',
            '5': 'LPG',
            '6': '98 RON',
            '10': 'E85',
            '11': 'Brand diesel'
        }
    })

    # add suburb
    suburb_soup = BeautifulSoup(requests.get(
        'https://www.fuelwatch.wa.gov.au/fuelwatch/pages/public/quickSearch.jspx').content, 'html.parser').find(id='quickSearch:location_input')
    suburbs = str(suburb_soup).split('"')
    output.update({
        'Suburbs':
        [suburb for suburb in suburbs if suburb.isalpha()][2:]
    })
    return output


def populate_filter_types(filters):
    brand_codes = filters.get('Brand')
    for key, value in brand_codes.items():
        entry = Brand(
            id=key,
            code=key,
            name=value
        )
        entry.save()

    region_codes = filters.get('Region')
    for key, value in region_codes.items():
        entry = Region(
            id=key,
            code=key,
            name=value
        )
        entry.save()

    stateregion_codes = filters.get('StateRegion')
    for key, value in stateregion_codes.items():
        entry = StateRegion(
            id=key,
            code=key,
            name=value
        )
        entry.save()

    product_codes = filters.get('Product')
    for key, value in product_codes.items():
        entry = Product(
            id=key,
            code=key,
            name=value
        )
        entry.save()

    suburbs = filters.get('Suburbs')
    for i in range(len(suburbs)):
        entry = Suburb(
            name=suburbs[i]
        )
        entry.save()
