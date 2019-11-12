"""
This model is for forum question

"""

from mongoengine import connect, Document, StringField, ListField, ReferenceField
from models.User import User

class Question(Document):
    question_title = StringField(required=True)
    author = ReferenceField(User, unique_with="question_title")
    description = StringField(required=True)
    #answers = ListField(EmbeddedDocumentField(Answer))

    