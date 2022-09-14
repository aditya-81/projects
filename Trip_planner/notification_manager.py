from twilio.rest import Client
import smtplib

TWILIO_SID = "ACb284ed1ed3d96f59efe909cd4b88bfae"
TWILIO_AUTH_TOKEN = "58f7be39b346f7e07c47c5b239413c6a"
TWILIO_VIRTUAL_NUMBER = "+15735704313"
TWILIO_VERIFIED_NUMBER = '+918825057720'




class NotificationManager:

    def __init__(self,user):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
        self.user = user

        self.email = "bhatadityatest@yahoo.com"
        self.password = "icgxjojzmqcgxanr"
    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            # messaging_service_sid="MG03fd27013b0c77a21aa0f7b35fcc59f2",
            to=TWILIO_VERIFIED_NUMBER
        )
        # Prints if successfully sent.

    def send_mail(self,msg):
        stp = smtplib.SMTP("smtp.mail.yahoo.com", port=587)
        stp.starttls()
        stp.login(user=self.email, password=self.password)
        stp.sendmail(self.email, self.user.email, msg)
