from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

import google_directions_api
import json

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome():
    return "WELCOME TO SMS NAVIGATE ME"

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():
    body = request.values.get('Body', None)

    addresses = body.split(";")
    origin = str(addresses[0])
    destination = str(addresses[1])

    directions = google_directions_api.get_gmap_directions(origin, destination)

    intro = '\U0001F441\U0001F444\U0001F441 There are the directions you were looking for: \n\n'
    outro =  '\n\nGOOD LUCK \U0001F31F'
    replyText = intro + '\n\n'.join(directions) + outro

    resp = MessagingResponse()
    resp.message(replyText)

    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)