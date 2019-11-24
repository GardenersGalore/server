"""
This model is for the garden

"""

from mongoengine import Document, IntField, StringField


class Garden(Document):
    name = StringField(required=True)
    username = StringField(required=True, unique_with="name")
    description = StringField()
    city_name = StringField()
    country_name = StringField()
    garden_width = IntField(required=True)
    garden_height = IntField(required=True)
    pictureURL = StringField()
