from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Garden import Garden

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class GardensEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', type=str, help='The username for the owner of the gardens')
        args = parser.parse_args()

        try:
            gardens = json.loads(Garden.objects(username=args['username']).to_json())
        except Exception as e:
            print(e)
            return {}

        return gardens