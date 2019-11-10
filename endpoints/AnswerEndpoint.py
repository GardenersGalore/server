from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DoesNotExist
from flask_restful import Resource, abort, reqparse
import json
from models.Question import Question
from models.Answer import Answer
from flask import request

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""

class AnswerEndpoint(Resource):
    def post(self):
        j = request.get_json()

        # need to ensure the required fields are in the json

        if "answer" not in j:
            abort(422, message="answer is not in json body")
        else:
            answer = j["answer"]

        if "author" not in j:
            abort(422, message="author not in json body")
        else:
            author = j["author"]

        if "question" not in j:
            abort(422, message="question not in json body")
        else:
            question = j["question"]

        answer_obj = Answer(
            answer=answer,
            author=author,
            question=question,
        )

        d = answer_obj.save()

        return json.loads(d.to_json())

    def put(self):
        # TODO
        pass

    def delete(self):
        # TODO
        pass

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('answer', required=True, type=str, help='The answer of the question')

        args = parser.parse_args()

        try:
            answer = json.loads(Answer.objects.get(answer=args['answer']).to_json())
        except Exception as e:
            print(e)
            abort(404, message="Answer {} doesn't exist".format(args['answer']))

        return question