import json

from flask_restful import Resource
from flask_restful import reqparse

from models.Garden import Garden
from models.Planting import Planting

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
            gardens = []
            [gardens.append(x["garden_name"]) for x in plant_garden if x["garden_name"] not in gardens]
            for y in gardens:
                j = json.loads(Garden.objects(name=y).to_json())
                if j:
                    gardenPlant.append(j[0])
            gardenPlant = [x for x in gardenPlant if x]

        except Exception as e:
            print(e)
            return {}

        return gardenPlant
