"""
This model is for the user

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, GeoPointField


class User(Document):
    username = StringField(unique=True)
    email = StringField(unique=True)
    password = StringField()
    phone_number = StringField()
    experience = StringField()
