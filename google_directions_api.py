import os
import requests
from pprint import pprint
import json
from dotenv import load_dotenv
from bs4 import BeautifulSoup

load_dotenv()

import twilio_sms

def get_gmap_directions(origin, destination):
    GOOGLE_MAPS_API_URL = 'https://maps.googleapis.com/maps/api/directions/json'

    payload = {
        'origin': origin,
        'destination': destination,
        'key': os.environ.get('google_maps_key')
    }

    req = requests.get(GOOGLE_MAPS_API_URL, params=payload)
    res = req.json()

    return format(res)

def format(response):
    main_dir_dict = response['routes'][0]['legs'][0]
    tot_distance = main_dir_dict['distance']
    tot_duration = main_dir_dict['duration']
    start = main_dir_dict['start_address']
    end = main_dir_dict['end_address']
    
    steps = main_dir_dict['steps']

    all_text_steps = []
    step_number = 0
    for step in steps:
        soup = BeautifulSoup(step['html_instructions'], 'html.parser')
        step_number += 1

        text_instruction = soup.text
        all_text_steps.append(f'{step_number}. {text_instruction}')

    return all_text_steps