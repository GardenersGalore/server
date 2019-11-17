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

        if "question_title" not in j:
            abort(422, message="question_title not in json body")
        else:
            question_title = j["question_title"]

        answer_obj = Answer(
            answer=answer,
            author=author,
            question_title=question_title,
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
        parser.add_argument('question_title', required=True, type=str, help='The answer of the question')

        args = parser.parse_args()

        try:
            answer = json.loads(Answer.objects.get(question_title=args['question_title']).to_json())
        except Exception as e:
            print(e)
            abort(404, message="Answer to question {} doesn't exist".format(args['question_title']))

        return answer