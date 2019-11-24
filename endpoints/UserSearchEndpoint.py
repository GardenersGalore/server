import json

from flask import jsonify
from flask_restful import Resource
from flask_restful import reqparse
from fuzzywuzzy import process

from models.User import User

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class UserSearchEndpoint(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', type=str, help='Common Name of the user you want to search')
        args = parser.parse_args()

        try:
            user = json.loads(User.objects().to_json())

        except Exception as e:
            print(e)
            return {}

        user_names = [x['name'] for x in user]
        user_choices = process.extract(args['name'], user_names)
        user_choices = [x for x in user_choices if x[1] > 80]
        user_list = []

        for x in user_choices:
            for y in user:
                if y['name'] == x[0]:
                    user_list.append(y)

        return jsonify(user_list)
