import json

from flask import jsonify
from flask_restful import Resource
from flask_restful import reqparse
from fuzzywuzzy import process

from models.Garden import Garden
from models.Planting import Planting

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class PlantGardenSearchEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='The plant present in every garden')
        args = parser.parse_args()

        try:
            planting = json.loads(Planting.objects().to_json())

        except Exception as e:
            print(e)
            return {}

        plant_names = []
        for x in planting:
            if x['plant_name'] not in plant_names:
                plant_names.append(x['plant_name'])

        plant_choices = process.extract(args['name'], plant_names)
        garden_list = []

        for x in plant_choices:
            for y in planting:
                if y['plant_name'] == x[0]:
                    if y['garden_name'] not in garden_list:
                        garden_list.append(y['garden_name'])

        garden_complete = []
        for x in garden_list:
            gardens = json.loads(Garden.objects(name=x).to_json())
            if len(gardens) != 0:
                garden_complete.append(gardens[0])

        return jsonify(garden_complete)
