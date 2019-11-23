from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField
from flask_restful import Resource
from flask_restful import reqparse
import json
from models.Plant import Plant
from models.Planting import Planting
from models.Garden import Garden


"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class PlantInfoEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Common Name of the plant you want to search')
        args = parser.parse_args()



        try:
            plant = json.loads(Plant.objects.get(name=args['name']).to_json())
            plantings = json.loads(Planting.objects(plant_name=args['name']).to_json())

            seen_plantings = dict()
            # for planting in plantings:
            #     if planting['garden_name'] not in seen_plantings:
            #         print()
            #         seen_plantings[planting['garden_name']] = planting
            for planting in plantings:
                gname = planting['garden_name']
                if gname in seen_plantings:
                    if 'pictureURL' not in seen_plantings[gname] and 'pictureURL' in planting:
                        seen_plantings[gname]['pictureURL'] = planting['pictureURL']
                else:
                    seen_plantings[gname] = planting
                    try:
                        seen_plantings[gname]['garden'] = json.loads(Garden.objects.get(name=gname).to_json())
                    except:
                        del seen_plantings[gname]

            final_plantings = []
            for key, value in seen_plantings.items():
                final_plantings.append(value)

            plant['plantings'] = final_plantings

        except Exception as e:
            print(e)
            return {}

        return plant