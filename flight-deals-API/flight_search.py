import requests
class FlightSearch:
    def __init__(self):
        self.url = "https://tequila-api.kiwi.com/locations/query"
        self.headers = {
            "apikey":"ekqFzpseqBRunPyyTQmyvT2q3dWXKNUF",
        }
        self.params = {}

        
    def get_code(self,city):
        self.params = {"term": city}
        response = requests.get(self.url,params=self.params,headers=self.headers)
        return response.json()['locations'][0]['code']


