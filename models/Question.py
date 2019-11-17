"""
This model is for forum question

"""

from mongoengine import connect, Document, StringField, ListField, ReferenceField
from models.User import User

class Question(Document):
    question_title = StringField(required=True)
    author = StringField(unique_with="question_title")
    description = StringField(required=True)    