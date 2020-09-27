from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

account_sid = os.environ.get('twilio_account_sid')
auth_token = os.environ.get('twilio_auth_token')
client = Client(account_sid, auth_token)

def send_sms(text):
    message = client.messages \
                    .create(
                         body=text,
                         from_=os.environ.get('twilio_number'),
                         to=os.environ.get('receiving_number')
                     )

    return message.sid
