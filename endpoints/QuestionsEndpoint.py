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

class QuestionsEndpoint(Resource):
    def get(self):
        try:
            questions = json.loads(Question.objects().to_json())
        except Exception as e:
            print(e)
            abort(404, message="No questions available")

        return questions