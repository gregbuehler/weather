import os
import requests
from opencage.geocoder import OpenCageGeocode


def get_location(query):
    try:
        key = os.environ.get('OPENCAGE_KEY')
        geocoder = OpenCageGeocode(key)
        results = geocoder.geocode(query)
    except Exception as ex:
        raise ex

    return results[0]


def get_weather(lat, lng):
    key = os.environ.get('DARKSKY_KEY')
    url = f"https://api.darksky.net/forecast/{key}/{lat},{lng}"

    try:
        r = requests.get(url)
        if r.status_code != 200:
            raise Exception('Weather provider error')

        weather = r.json()
    except Exception as ex:
        raise ex

    return weather


def lookup(query):
    try:
        location = get_location(query)
        lat = location['geometry']['lat']
        lng = location['geometry']['lng']

        weather = get_weather(lat, lng)

        return location, weather
    except Exception as ex:
        raise ex
