"""
This model is for the garden

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, GeoPointField


class Garden(Document):
    name = StringField(required=True)
    username = StringField(required=True, unique_with="name")
    description = StringField()
    location = GeoPointField()
    loaction_name = StringField()
    garden_width = IntField(required=True)
    garden_height = IntField(required=True)