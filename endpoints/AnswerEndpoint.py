import json

from flask import request
from flask_restful import Resource, abort

from models.Answer import Answer

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
        pass
