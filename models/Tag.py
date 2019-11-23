"""
This model is for the tags

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField

class Tag(Document):
    name = StringField(required=True)
    blog_name = StringField(required=True)
