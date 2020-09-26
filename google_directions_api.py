import os
import requests
from pprint import pprint
import json
import config

def get_gmap_directions(origin, destination):
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json'

    payload = {
        'origin': origin,
        'destination': destination,
        'key': config.google_maps_key
    }

    req = requests.get(GOOGLE_MAPS_API_URL, params=payload)
    res = req.json()
    print(res)

    return format(res)

def format(response):
    #Use beautiful soup here?
    main_dir_dict = response['routes'][0]['legs'][0]
    tot_distance = main_dir_dict['distance']    #{'text': '4.2 mi', 'value': 6765}
    tot_duration = main_dir_dict['duration']    #{'text': '15 mins', 'value': 906}
    start = main_dir_dict['start_address']      #str
    end = main_dir_dict['end_address']          #str
    
    steps = main_dir_dict['steps']              #list/array

    all_text_steps = []
    for step in steps:
        all_text_steps.append(step['html_instructions'])

    return all_text_steps

# if __name__ == '__main__':
#     origin = os.environ.get('origin', '825 Battery St, San Francisco, CA')
#     destination = os.environ.get('destination', '389 Valencia St, San Francisco, CA 94103')

#     x = get_gmap_directions(origin, destination)

#     twilio_sms.send_sms(x)

#     pprint(x)
