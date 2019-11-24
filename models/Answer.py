"""
This model is for forum answer

"""

from mongoengine import Document, StringField


class Answer(Document):
    answer = StringField(required=True)
    author = StringField(required=True)
    question_title = StringField(required=True)
