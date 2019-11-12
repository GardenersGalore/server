from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DoesNotExist
from flask_restful import Resource, abort, reqparse
import json
from models.Garden import Garden
from flask import request

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

        if "location" not in j:
            abort(422, message="location not in json body")
        else:
            location = j["location"]

        if "location_name" not in j:
            abort(422, message="location_name not in json body")
        else:
            location_name = j["location_name"]

        if "description" not in j:
            abort(422, message="description not in json body")
        else:
            description = j["description"]


        if "garden_width" not in j:
            abort(422, message="garden_width not in json body")
        else:
            garden_width = j["garden_width"]

        if "garden_height" not in j:
            abort(422, message="garden_height not in json body")
        else:
            garden_height = j["garden_height"]

        garden_obj = Garden(
            name=name,
            username=username,
            description=description,
            location=location,
            location_name= location_name,
            garden_width=garden_width,
            garden_height=garden_height
        )


        d = garden_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

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