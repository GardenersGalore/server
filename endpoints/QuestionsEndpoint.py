import json

from flask_restful import Resource, abort

from models.Answer import Answer
from models.Question import Question

"""
POST            Creates a new resource.
GET             Retrieves a resource.
PUT             Updates an existing resource.
DELETE          Deletes a resource.
"""


class QuestionsEndpoint(Resource):
    def get(self):
        try:
            questions = json.loads(Question.objects().to_json())
            for question in questions:
                answers = json.loads(Answer.objects(question_title=question['question_title']).to_json())
                question['answers'] = answers
        except Exception as e:
            print(e)
            abort(404, message="No questions available")

        return questions
