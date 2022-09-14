from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_data import UserData
from cost_estimator import EstimatedCost

user = UserData()
user.input()

data_manager = DataManager(user)
data_manager.add_user_Data()

sheet_data = data_manager.get_destination_data()

flight_search = FlightSearch()
notification_manager = NotificationManager(user)

ORIGIN_CITY_IATA = "DEL"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:

        if flight.price < destination["lowestPrice"]:
            # # cost = EstimatedCost(flight.destination_city)
            # Get
            # hotels as low
            # " \
            #                   f" as {cost.cost()} / per
            # night!! Book
            # tickets
            # now!!✈️
            # "
            message = f"Low price alert! Only Rs.{flight.price} to fly from" \
                      f" {flight.origin_city}-{flight.origin_airport} to✈️ {flight.destination_city}-" \
                      f"{flight.destination_airport}, from {flight.out_date} to {flight.return_date}."
            notification_manager.send_sms(
                message=message
            )
            notification_manager.send_mail(message)
    except:
        pass

