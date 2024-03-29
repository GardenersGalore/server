import json

from flask import jsonify
from flask_restful import Resource
from flask_restful import reqparse
from fuzzywuzzy import process

from models.Plant import Plant

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class PlantSearchEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Common Name of the plant you want to search')
        args = parser.parse_args()

        try:
            plant = json.loads(Plant.objects().to_json())

        except Exception as e:
            print(e)
            return {}

        plant_names = [x['name'] for x in plant]
        plant_choices = process.extract(args['name'], plant_names)
        plant_choices = [x for x in plant_choices if x[1] > 80]
        plant_list = []

        for x in plant_choices:
            for y in plant:
                if y['name'] == x[0]:
                    plant_list.append(y)

        return jsonify(plant_list)
