import requests
from flight_search import FlightSearch
import requests

from flight_search import FlightSearch


class DataManager:
    def __init__(self):
        self.data = {}
        self.fs = FlightSearch()
        self.get()

    def get(self):
        response = requests.get("https://api.sheety.co/a8282b732d4a0d57d0f1c0015545594b/copyOfFlightDeals/prices")
        d = response.json()
        for i in range(len(d['prices'])):
            if d['prices'][i]['iataCode'] != '':
                pass
            else:
                params = {
                    'price': {
                        'city': d['prices'][i]['city'],
                        'iataCode': self.fs.get_code(d['prices'][i]['city']),
                        'lowestPrice': d['prices'][i]['lowestPrice']
                    }}
                response = requests.put(
                    f"https://api.sheety.co/a8282b732d4a0d57d0f1c0015545594b/copyOfFlightDeals/prices/{i + 2}",
                    json=params)
            self.data.update({d['prices'][i]['iataCode']: d['prices'][i]['lowestPrice']}
            )

    def dict(self):
        return self.data

