import requests
import feedparser
from pprint import pprint

response = requests.get('https://www.fuelwatch.wa.gov.au/fuelwatch/fuelWatchRSS')

feed = feedparser.parse(response.content)
pprint(feed, indent=4)