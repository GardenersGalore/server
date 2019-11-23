from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Plant import Plant
from fuzzywuzzy import process
from flask import jsonify


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
                    y['description'] = ''
                    plant_list.append(y)

        return jsonify(plant_list)