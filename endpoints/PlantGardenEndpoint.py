from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Planting import Planting
from models.Garden import Garden


"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class PlantGardenEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('plant', type=str, help='The plant present in every garden')
        args = parser.parse_args()

        try:
            plant_garden = json.loads(Planting.objects(plant_name=args['plant']).to_json())
            gardenPlant = []
            for x in plant_garden:
                j = json.loads(Garden.objects(name=x['garden_name']).to_json())
                gardenPlant.append(j)
                gardenPlant = [x for x in gardenPlant if x]
                gardenPlant = sum(gardenPlant, [])
        except Exception as e:
            print(e)
            return {}

        return gardenPlant