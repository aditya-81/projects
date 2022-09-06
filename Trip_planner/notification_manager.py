from twilio.rest import Client

TWILIO_SID = "ACb284ed1ed3d96f59efe909cd4b88bfae"
TWILIO_AUTH_TOKEN = "6c432d17f53dca57252f5ad0b46d915f"
TWILIO_VIRTUAL_NUMBER = "+19785791161"
TWILIO_VERIFIED_NUMBER = '+918825057720'


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            # from_=TWILIO_VIRTUAL_NUMBER,
            messaging_service_sid="MG03fd27013b0c77a21aa0f7b35fcc59f2",
            to=TWILIO_VERIFIED_NUMBER
        )
        # Prints if successfully sent.
        print(message.sid)
