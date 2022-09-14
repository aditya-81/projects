import requests
from user_data import UserData
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/a8282b732d4a0d57d0f1c0015545594b/copyOfFlightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/a8282b732d4a0d57d0f1c0015545594b/copyOfFlightDeals/users"


class DataManager:

    def __init__(self,user):
        self.userdata = user
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def add_user_Data(self):
        json = {"user":
                    {"firstName":self.userdata.first_name,
                     "lastName":self.userdata.last_name,
                     "email":self.userdata.email,
                     }

                }
        response = requests.post(url = SHEETY_USERS_ENDPOINT,json = json)
        print(response.json())