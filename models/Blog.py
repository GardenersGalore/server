"""
This model is for the blogs

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField

class Blog(Document):
    username = StringField(required=True)
    name = StringField(required=True)
    content = StringField(required=True)
