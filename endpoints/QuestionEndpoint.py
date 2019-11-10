from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DoesNotExist
from flask_restful import Resource, abort, reqparse
import json
from models.Question import Question
from flask import request

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class QuestionEndpoint(Resource):
    def post(self):
        j = request.get_json()

        # need to ensure the required fields are in the json

        if "title" not in j:
            abort(422, message="title is not in json body")
        else:
            title = j["title"]

        if "author" not in j:
            abort(422, message="author not in json body")
        else:
            author = j["author"]

        if "description" not in j:
            abort(422, message="description not in json body")
        else:
            description = j["description"]

        question_obj = Question(
            title=title,
            author=author,
            description=description,
        )

        d = question_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('title', required=True, type=str, help='The title of the question')

        args = parser.parse_args()

        try:
            question = json.loads(Question.objects.get(title=args['title']).to_json())
        except Exception as e:
            print(e)
            abort(404, message="Question {} doesn't exist".format(args['title']))

        return question