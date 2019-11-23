from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Garden import Garden
from fuzzywuzzy import process
from flask import jsonify



"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class GardenSearchEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='The name of the gardens')
        args = parser.parse_args()

        try:
            gardens = json.loads(Garden.objects().to_json())
        except Exception as e:
            print(e)
            return {}

        garden_name = [x['name'] for x in gardens]
        garden_choices = process.extract(args['name'], garden_name)
        garden_choices = [x for x in garden_choices if x[1] > 80]

        garden_list = []

        for x in garden_choices:
            for y in gardens:
                if y['name'] == x[0]:
                    garden_list.append(y)

        return jsonify(garden_list)