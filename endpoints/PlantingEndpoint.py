from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DoesNotExist
from flask_restful import Resource, abort, reqparse
import json
from models.Planting import Planting
from models.Plant import Plant
from flask import request

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class PlantingEndpoint(Resource):
    def post(self):
        j = request.get_json()

        # need to ensure the required fields are in the json

        if "plant_name" not in j:
            abort(422, message="plant_name not in json body")
        else:
            plant_name = j["plant_name"]
            # verify that the plant with this name actually exists in db
            try:
                print(Plant.objects.get(name=plant_name))
            except DoesNotExist:
                abort(404, message="plant_name is not a name of a valid plant") 

        if "garden_name" not in j:
            abort(422, message="garden_name not in json body")
        else:
            garden_name = j["garden_name"]

        if "x_coord" not in j:
            abort(422, message="x_coordinate not in json body")
        else:
            x_coord = j["x_coord"]

        if "y_coord" not in j:
            abort(422, message="y_coord not in json body")
        else:
            y_coord = j["y_coord"]

        planting_obj = Planting(
            plant_name = plant_name,
            garden_name = garden_name,
            x_coord = x_coord,
            y_coord = y_coord
        )

        if "description" in j:
            planting_obj.description = j["description"]

        if "planted_from" in j:
            planting_obj.planted_from = j["planted_from"]

        if "harvest_count" in j:
            planting_obj.harvest_count = j["harvest_count"]

        
        d = planting_obj.save()


        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        parser = reqparse.RequestParser()
        parser.add_argument('garden_name', required=True , type=str, help='The name of the garden that this plant is in')
        parser.add_argument('x_coord', required=True , type=int, help='X Coordinates within the garden')
        parser.add_argument('y_coord', required=True , type=int, help='Y Coordinates within the garden')

        args = parser.parse_args()

        try: 
            planting = Planting.objects.get(garden_name=args['garden_name'],
                                                        y_coord=args['y_coord'],
                                                        x_coord=args['x_coord'])
            r = planting.delete()
        except Exception as e:
            print(e)
            abort(404, message="Planting in garden: {} doesn't exist".format(args['garden_name']))

        return r

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('garden_name', required=True , type=str, help='The name of the garden that this plant is in')
        parser.add_argument('x_coord', required=True , type=int, help='X Coordinates within the garden')
        parser.add_argument('y_coord', required=True , type=int, help='Y Coordinates within the garden')

        args = parser.parse_args()

        try:
            planting = json.loads(Planting.objects.get(garden_name=args['garden_name'],
                                                       y_coord=args['y_coord'],
                                                       x_coord=args['x_coord']).to_json())
        except Exception as e:
            print(e)
            abort(404, message="Planting in garden: {} doesn't exist".format(args['garden_name']))

        return planting