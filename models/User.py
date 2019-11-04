"""
This model is for the user

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, GeoPointField


class User(Document):
    username = StringField(required=True, unique=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)
    phone_number = StringField()
    experience = StringField()
