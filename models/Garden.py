"""
This model is for the garden

"""

from mongoengine import connect, Document, StringField, IntField, StringField, StringField, ListField, DateField, PointField


class Garden(Document):
    name = StringField(required=True)
    username = StringField(required=True, unique_with="name")
    description = StringField()
    location = PointField()
    loaction_name = StringField()
    garden_width = IntField(required=True)
    garden_height = IntField(required=True)