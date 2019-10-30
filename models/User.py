"""
This model is for the user

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, GeoPointField


class Garden(Document):
    name = StringField()
    username = StringField(unique_with="name")
    location = GeoPointField()
    width = IntField()
    height = IntField()