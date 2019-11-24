import json

from flask import request
from flask_restful import Resource, abort, reqparse

from models.Answer import Answer
from models.Question import Question

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

        if "question_title" not in j:
            abort(422, message="question_title is not in json body")
        else:
            question_title = j["question_title"]

        if "author" not in j:
            abort(422, message="author not in json body")
        else:
            author = j["author"]

        if "description" not in j:
            abort(422, message="description not in json body")
        else:
            description = j["description"]

        question_obj = Question(
            question_title=question_title,
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
        parser.add_argument('_id', type=str, help='unique question id')

        args = parser.parse_args()

        try:
            question = json.loads(Question.objects(pk=args['_id']).to_json())
            question = question[0]
            answers = json.loads(Answer.objects(question_title=question['question_title']).to_json())
            question['answers'] = answers

        except Exception as e:
            print(e)
            abort(404, message="Question Id {} doesn't exist".format(args['_id']))

        return question
