import json

from flask import jsonify
from flask_restful import Resource
from flask_restful import reqparse
from fuzzywuzzy import process

from models.Question import Question

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class QuestionSearchEndpoint(Resource):
    def get(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, help='Question search')
            args = parser.parse_args()
            questions = json.loads(Question.objects().to_json())
        except Exception as e:
            print(e)
            return {}

        titles = [x['question_title'] for x in questions]
        title_choices = process.extract(args['name'], titles)
        title_choices = [x for x in title_choices if x[1] > 50]
        title_list = []

        for x in title_choices:
            for y in questions:
                if y['question_title'] == x[0]:
                    title_list.append(y)

        return jsonify(title_list)
