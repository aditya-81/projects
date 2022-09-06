from datetime import datetime as dt
from data_manager import DataManager
import requests


class FlightData:
    def __init__(self):
        self.now = dt.now()
        self.day = self.now.day
        self.month = int(self.now.month) + 6
        self.year = int(self.now.year)
        self.date_to()
        self.dm = DataManager()
        self.url = "https://tequila-api.kiwi.com/v2/search"
        self.headers = {
            "apikey": "ekqFzpseqBRunPyyTQmyvT2q3dWXKNUF",
        }
        self.data = self.dm.dict()
        self.params = {"fly_from": 'LON', "fly_to": '', "dateFrom": self.form,
                       "dateTo": f"{self.day}/{self.month}/{self.year}","curr": "GBP"}
        self.price = int()

    def get(self):
        for i in self.data.keys():
            self.params.update({"fly_to":i})
            print(self.params)
            try:
                response = requests.get(self.url, params=self.params, headers=self.headers)
                response.raise_for_status()
                print(response.json)
                self.price = response.json()['data'][0]['price']
            except :
                continue
                print()

    def date_to(self):
        self.now = dt.now()
        self.form = self.now.strftime("%d/%m/%Y")
        if int(self.now.month) > 6:
            self.month = (int(self.now.month)+6) % 12
            self.year = int(self.now.year) + 1
            if int(self.now.day) == 31:
                self.day = 30


fd = FlightData()
fd.get()
