import json

from flask_restful import Resource
from flask_restful import reqparse

from models.Blog import Blog
from models.Garden import Garden
from models.Plant import Plant
from models.Planting import Planting
from models.User import User

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class UserAllEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, type=str, help='The username of the User')

        args = parser.parse_args()

        try:
            seen_plants = dict()
            favourite_plant_count = dict()
            user = json.loads(User.objects.get(username=args['username']).to_json())
            gardens = json.loads(Garden.objects(username=args['username']).to_json())
            for garden in gardens:
                plantings = json.loads(Planting.objects(garden_name=garden['name']).to_json())

                for planting in plantings:
                    if planting['plant_name'] in seen_plants:
                        planting['plant'] = seen_plants[planting['plant_name']]
                        favourite_plant_count[planting['plant_name']] += 1
                    else:
                        plant = json.loads(Plant.objects.get(name=planting['plant_name']).to_json())
                        planting['plant'] = plant
                        seen_plants[planting['plant_name']] = plant
                        favourite_plant_count[planting['plant_name']] = 1
                garden['plantings'] = plantings

            favourite_plants = []
            for key, value in favourite_plant_count.items():
                favourite_plants.append({"plant": seen_plants[key], "count": value})

            blogs = json.loads(Blog.objects(username=args['username']).to_json())

            user['favourite_plants'] = favourite_plants
            user['blogs'] = blogs
            user['gardens'] = gardens

        except Exception as e:
            print(e)
            return {}

        return user
