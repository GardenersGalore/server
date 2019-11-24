import json

from flask import request
from flask_restful import Resource, abort, reqparse

from models.Garden import Garden

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class GardenEndpoint(Resource):
    def post(self):
        j = request.get_json()

        # need to ensure the required fields are in the json

        if "name" not in j:
            abort(422, message="name is not in json body")
        else:
            name = j["name"]

        if "username" not in j:
            abort(422, message="username not in json body")
        else:
            username = j["username"]

        garden_obj = Garden(
            name=name,
            username=username,
        )

        if "country_name" in j:
            garden_obj.country_name = j["country_name"]

        if "city_name" in j:
            garden_obj.city_name = j["city_name"]

        if "description" in j:
            garden_obj.description = j["description"]

        if "garden_width" in j:
            garden_obj.garden_width = j["garden_width"]

        if "garden_height" in j:
            garden_obj.garden_height = j["garden_height"]

        if "pictureURL" in j:
            garden_obj.pictureURL = j["pictureURL"]

        d = garden_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str, help='The name of the garden')

        args = parser.parse_args()

        try:
            garden = Garden.objects.get(name=args['name'])
            r = garden.delete()
        except Exception as e:
            print(e)
            abort(404, message="Planting in garden: {} doesn't exist".format(args['garden_name']))

        return r

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True, type=str, help='The name of the garden')

        args = parser.parse_args()

        try:
            garden = json.loads(Garden.objects.get(name=args['name']).to_json())
        except Exception as e:
            print(e)
            return {}

        return garden
