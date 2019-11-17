from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DoesNotExist
from flask_restful import Resource, abort, reqparse
import json
from models.User import User
from flask import request

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class UserEndpoint(Resource):
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

        if "email" not in j:
            abort(422, message="email not in json body")
        else:
            email = j["email"]

        if "password" not in j:
            abort(422, message="password not in json body")
        else:
            password = j["password"]

        if "phone_number" not in j:
            abort(422, message="phone_number not in json body")
        else:
            phone_number = j["phone_number"]

        if "experience" not in j:
            abort(422, message="experience not in json body")
        else:
            experience = j["experience"]

        user_obj = User(
            name=name,
            username=username,
            email=email,
            password=password,
            phone_number=phone_number,
            experience=experience
        )

        d = user_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('username', required=True, type=str, help='The username of the User')

        args = parser.parse_args()

        try:
            user = json.loads(User.objects.get(username=args['username']).to_json())
        except Exception as e:
            print(e)
            abort(404, message="User doesnt exist: {} doesn't exist".format(args['username']))

        return user