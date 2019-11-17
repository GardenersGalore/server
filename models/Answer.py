"""
This model is for forum answer

"""

from mongoengine import connect, Document, StringField, ReferenceField
from models.User import User
from models.Question import Question

class Answer(Document):
    answer = StringField(required=True)
    author = StringField(required=True)
    question_title = StringField(required=True)