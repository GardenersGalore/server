from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Plant import Plant


"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class PlantEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Common Name of the plant you want to search')
        args = parser.parse_args()

        try:
            plant = json.loads(Plant.objects.get(name=args['name']).to_json())
        except Exception as e:
            print(e)
            return {}

        return plant