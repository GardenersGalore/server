"""
This model is for the user

"""

from mongoengine import Document, IntField, StringField, GeoPointField


class Garden(Document):
    name = StringField()
    username = StringField(unique_with="name")
    location = GeoPointField()
    width = IntField()
    height = IntField()
