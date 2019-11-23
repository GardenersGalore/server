"""
This model is for forum question

"""

from mongoengine import Document, StringField
class Question(Document):
    question_title = StringField(required=True)
    author = StringField(required=True)
    description = StringField(required=True)