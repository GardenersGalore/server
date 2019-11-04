from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Planting import Planting


"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class PlantingsEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('garden_name', type=str, help='Garden Name')
        args = parser.parse_args()

        try:
            plantings = json.loads(Planting.objects(garden_name=args['garden_name']).to_json())
        except Exception as e:
            print(e)
            return {}

        return plantings