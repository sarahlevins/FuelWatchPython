import requests
import feedparser
from pprint import pprint

def fuelley(): 
    day = ['today', 'tomorrow']
    regions = [25, 26]
    output={}
    # loop through days
    for d in range(len(day)):
        # loop through regions
        for r in range(len(regions)):
            info = {}
            # get fuel data from fuelwatch and parse it
            response = requests.get(f'https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS?Product=1&Region={regions[r]}&Day={day[d]}')
            feed = feedparser.parse(response.content)
            # loop through data and create fuel pump data
            for i in range(len(feed['entries'])):
                pump = feed['entries'][i]
                info.update({
                    pump['trading-name'] : 
                        {'price': pump['price'], 
                        'location': pump['location'], 
                        'address': pump['address'], 
                        }
                })
        output.update({day[d]: info})
    print(output)
    return output
