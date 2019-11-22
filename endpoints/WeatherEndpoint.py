from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
import requests
import os

class WeatherEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # parser.add_argument('longitude', required=True , type=float, help='longitude is a required arguement')
        # parser.add_argument('latitude', required=True , type=float, help='latitude is a required arguement')
        parser.add_argument('city_name', required=True, type=str )
        parser.add_argument('country_name', required=True, type=str )

        args = parser.parse_args()

        params = {
            # "lat" : args['latitude'],
            # "lon" : args['longitude'],
            "city" : args['city_name'],
            "country" : args['country_name'],
            "key" : os.getenv("WEATHER_API_KEY"),
            "days" : 5
        }

        url = "https://api.weatherbit.io/v2.0/forecast/daily"

        r = requests.get(url,params=params)

        j = r.json()

        final = {}

        final['city_name'] = j['city_name']
        final['lon'] = j['lon']
        final['lat'] = j['lat']
        final['country_code'] = j['country_code']
        res = []

        for day in j["data"]:
            single_res = {}
            single_res["date"] = day["datetime"]
            single_res["rainfall_probability"] = day["pop"]
            single_res["rainfall_amount"] = day["precip"]
            single_res["max_temperature"] = day["max_temp"]
            single_res["min_temperature"] = day["min_temp"]
            single_res["snow"] = day["snow"]
            single_res["weather"] = day["weather"]
            res.append(single_res)

        final['data'] = res
            # "moonrise_ts": 1574354124,
            # "wind_cdir": "ESE",
            # "rh": 83,
            # "pres": 1007.21,
            # "high_temp": 19.2,
            # "sunset_ts": 1574412667,
            # "ozone": 293.662,
            # "moon_phase": 0.152223,
            # "wind_gust_spd": 10.515,
            # "snow_depth": 0,
            # "clouds": 56,
            # "ts": 1574341260,
            # "sunrise_ts": 1574361726,
            # "app_min_temp": 19.2,
            # "wind_spd": 3.5945,
            # "pop": 50,
            # "wind_cdir_full": "east-southeast",
            # "slp": 1013.75,
            # "valid_date": "2019-11-22",
            # "app_max_temp": 22.7,
            # "vis": 20.9725,
            # "dewpt": 17.1,
            # "snow": 0,
            # "uv": 0,
            # "weather": {
            #     "icon": "c03d",
            #     "code": 803,
            #     "description": "Broken clouds"
            # },



        return final