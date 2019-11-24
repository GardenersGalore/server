import os

import requests
from flask_restful import Resource
from flask_restful import reqparse


class WeatherEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        # parser.add_argument('longitude', required=True , type=float, help='longitude is a required arguement')
        # parser.add_argument('latitude', required=True , type=float, help='latitude is a required arguement')
        parser.add_argument('city_name', required=True, type=str)
        parser.add_argument('country_name', required=True, type=str)

        args = parser.parse_args()

        params = {
            # "lat" : args['latitude'],
            # "lon" : args['longitude'],
            "city": args['city_name'],
            "country": args['country_name'],
            "key": os.getenv("WEATHER_API_KEY"),
            "days": 5
        }

        url = "https://api.weatherbit.io/v2.0/forecast/daily"

        r = requests.get(url, params=params)

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

        return final
