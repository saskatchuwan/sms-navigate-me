# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

import google_directions_api
import json

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def incoming_sms():

    # Get the message the user sent our Twilio number
    #ideally, it would be one string: "origin_address;destination address"
    body = request.values.get('Body', None)

    #get arguments for get_gmap_directions method
    addresses_arr = body.split(";")
    origin = str(addresses_arr[0])
    destination = str(addresses_arr[1])

    # origin = ''
    # destination = ''

    # #get google directions json output
    directions = google_directions_api.get_gmap_directions(origin, destination)

    # Start our TwiML response
    resp = MessagingResponse()

    #respond
    resp.message(str(directions))

    return str(resp)

if __name__ == "__main__":
    #app.run(debug=True) #run development server in debug mode
    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)