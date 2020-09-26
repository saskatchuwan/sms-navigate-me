from twilio.rest import Client
import os

account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token
client = Client(account_sid, auth_token)

def send_sms(text):
    message = client.messages \
                    .create(
                         body=text,
                         from_=config.twilio_number,
                         to=config.recieving_number
                     )

    return message.sid
