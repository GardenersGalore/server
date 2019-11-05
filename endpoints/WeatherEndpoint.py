from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
import requests
import os

class WeatherEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('longitude', required=True , type=float, help='longitude is a required arguement')
        parser.add_argument('latitude', required=True , type=float, help='latitude is a required arguement')
        args = parser.parse_args()

        params = {
            "lat" : args['latitude'],
            "lon" : args['longitude'],
            "key" : os.getenv("WEATHER_API_KEY"),
            "hours" : 48
        }

        url = "https://api.weatherbit.io/v2.0/forecast/hourly"

        r = requests.get(url,params=params)

        return r.json()